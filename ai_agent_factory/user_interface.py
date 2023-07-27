from ai_agent_factory import AIAgentFactory

factory = AIAgentFactory()

# Add tasks
factory.task_manager.create_task('Task1')
factory.task_manager.create_task('Task2')
factory.task_manager.create_task('Task3')
factory.task_manager.create_task('Task4')
factory.task_manager.create_task('Task5')

# Assign tasks to agents
factory.assign_tasks()

# Print agent tasks
for agent in factory.ai_agents:
    print(f'Agent {agent.id} is assigned task: {agent.task}')