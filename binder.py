import subprocess

def open_app(app_path):
    subprocess.Popen(app_path)

# get the path for the application
app_to_open = input("enter the path of the application you want to open: ")

# get the trigger code for the application
trigger_input = input(f"enter the input to trigger opening '{app_to_open}': ")

# prompt the user to run the application
if input(f"Press '{trigger_input}' to run '{app_to_open}'") == trigger_input:
    open_app(app_to_open)