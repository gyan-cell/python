import os
import platform
import subprocess

# print("Process ID:", os.getpid))
# print("Parent process ID:", os.getppid())
# print(os.getlogin())


# subprocess.run(["kitty", "--", "bash", "-c", "echo hello"], shell=True)

# openKitty = os.system("kitty")


# success = os.system("dir")


def open_terminal_and_run_command(command):
    # Determine the OS platform
    current_platform = platform.system().lower()

    if current_platform == "windows":
        # For Windows, use 'start' to open a new Command Prompt
        subprocess.run(["start", "cmd", "/K", command], shell=True)

    elif current_platform == "linux" or current_platform == "darwin":
        # For Linux or macOS, use 'gnome-terminal' (for Linux) or 'osascript' (for macOS)
        if current_platform == "linux":
            subprocess.run(["kitty", "--", "bash", "-c", command + "; exec bash"])
        elif current_platform == "darwin":
            # For macOS, use AppleScript to open the terminal and execute a command
            apple_script = f'tell application "Terminal" to do script "{command}"'
            subprocess.run(["osascript", "-e", apple_script])

    else:
        print("Unsupported OS")


# Example usage:
command_to_execute = "echo 'Hello, World!'"
open_terminal_and_run_command(command_to_execute)
