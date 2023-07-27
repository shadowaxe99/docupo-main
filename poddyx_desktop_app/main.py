import os

# Define the commands to be executed
commands = [
    'git clone https://github.com/shadowaxe99/poddyx',
    'pip install -r poddyx/requirements.txt',
    'python3 poddyx/cli.py'
]

# Execute the commands
for command in commands:
    os.system(command)