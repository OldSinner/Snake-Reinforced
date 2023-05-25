from Game import Snake
from Agent import AgentDataHolder, Agent


def train():
    data = AgentDataHolder()
    agent = Agent()
    game = Snake()
    while True:
        agent.process_one_step(game, data)

if __name__ == '__main__':
    train()
