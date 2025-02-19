import os
import subprocess

while True:
    choice = input("Do you want to list a directory (ls) or view a file (cat)? [ls/cat]: ").strip().lower()

    if choice == "ls":
        path = input("Type the directory path to display: ").strip()
        if os.path.isdir(path):
            print(subprocess.run(["ls", "-l", path], capture_output=True, text=True).stdout)
        else:
            print("Error: Invalid directory path.")
        break  # Exit loop after listing directory

    elif choice == "cat":
        file = input("Type the file path to see the content: ").strip()
        if os.path.isfile(file):
            print(subprocess.run(["cat", file], capture_output=True, text=True).stdout)
        else:
            print("Error: File not found.")
        break  # Exit loop after showing file content

    else:
        print("Invalid option. Please type 'ls' or 'cat'.")
