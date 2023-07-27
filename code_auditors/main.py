import os

# Define the commands to be executed
commands = [
    'grep -r issue /Users/michaelgruen/Desktop/untitled\ folder\ 3/poddyx_desktop_app',
    'grep -r bug /Users/michaelgruen/Desktop/untitled\ folder\ 3/poddyx_desktop_app'
]

# Execute the commands
for command in commands:
    os.system(command)