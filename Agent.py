import torch
import random
import numpy as np
from Game import Snake
from Const import *
from collections import deque
from model import Linear_QNet, QTrainer
from Plot import plot


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.discount_rate = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game):
        return game.create_state()

    def remember(self, state, action, reward, next_state, game_over):
        self.memory.append((state, action, reward, next_state, game_over))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, game_overs = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, game_overs)

    def train_short_memory(self, state, action, reward, next_state, game_over):
        self.trainer.train_step(state, action, reward, next_state, game_over)

    def get_action(self, state):
        self.epsilon = 80 - self.n_games
        new_action = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            new_action[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            new_action[move] = 1
        return new_action

    def process_one_step(self, game, data):
        state_old = self.get_state(game)

        action = self.get_action(state_old)
        is_game_over, score, reward = game.make_step(action)
        new_state = self.get_state(game)

        self.train_short_memory(state_old, action, reward, new_state, is_game_over)

        self.remember(state_old, action, reward, new_state, is_game_over)

        if is_game_over:
            game.start_newgame()
            self.n_games += 1
            if data.record < score:
                data.record = score
                self.model.save()
            # self.train_long_memory()
            print(f'Game: {self.n_games} Score: {score} Record: {data.record}')
            data.plot_scores.append(score)
            data.total_score += score
            data.plot_values.append(data.total_score / self.n_games)
            plot(data.plot_scores, data.plot_values)


class AgentDataHolder:
    def __init__(self):
        self.plot_scores = []
        self.plot_values = []
        self.total_score = 0
        self.record = 0


