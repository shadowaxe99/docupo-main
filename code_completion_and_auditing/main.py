import os

# Define the commands to be executed
commands = [
    'git clone https://github.com/username/repo1',
    'git clone https://github.com/username/repo2',
    'git clone https://github.com/username/repo3',
    # Add more git clone commands for additional repositories
    'python3 code_auditors/main.py'
]

# Execute the commands
for command in commands:
    os.system(command)