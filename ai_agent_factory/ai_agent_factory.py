from ai_agent import AIAgent

class AIAgentFactory:
    def __init__(self):
        self.agents = []

    def create_agent(self):
        agent = AIAgent()
        self.agents.append(agent)
        return agent