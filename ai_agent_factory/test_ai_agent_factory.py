import unittest
from ai_agent_factory import AIAgentFactory

class TestAIAgentFactory(unittest.TestCase):
    def setUp(self):
        self.ai_agent_factory = AIAgentFactory()

    def test_create_agent(self):
        agent = self.ai_agent_factory.create_agent()
        self.assertIn(agent, self.ai_agent_factory.agents)

if __name__ == '__main__':
    unittest.main()