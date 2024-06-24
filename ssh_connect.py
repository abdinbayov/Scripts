#!/usr/bin/env python3

import csv
import subprocess
import sys
"CSV file should consist of name,url,username"
# Define the constant username to be used for all SSH connections
CONSTANT_USERNAME = "mee"

def load_controllers(filename):
    """
    Reads the CSV file and loads the controller details into a dictionary.
    The CSV file is expected to have columns: 'name' and 'url'.
    """
    controllers = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            controllers[row['name']] = row['url']
    return controllers

def main():
    """
    Main function that handles command-line arguments and performs the SSH connection.
    """
    if len(sys.argv) != 2:
        print("Usage: ssh_connect.py <controller_name>")
        sys.exit(1)

    controller_name = sys.argv[1]
    controllers = load_controllers('controllers.csv')

    if controller_name not in controllers:
        print(f"Controller '{controller_name}' not found.")
        sys.exit(1)

    url = controllers[controller_name]

    print(f"Connecting to {controller_name} ({url}) as {CONSTANT_USERNAME}...")
    ssh_command = f"ssh {CONSTANT_USERNAME}@{url}"
    subprocess.run(ssh_command, shell=True)

if __name__ == "__main__":
    main()




