import keyboard
import subprocess

def open_app(app_path):
    try:
        subprocess.Popen(app_path, shell=True)
        print(f"app opened: {app_path}")
    except FileNotFoundError:
        print(f"nvalid app path - {app_path}")

def main():
    print("Welcome to the Binder!")

    hotkeys = []

    while True:
        app_path = input("enter the path of the app (or type 'exit' to finish adding): ")

        if app_path.lower() == 'exit':
            break

        hotkey = input("enter the hotkey combination (for example ctrl+alt+a): ")
        hotkeys.append((hotkey, app_path))

    for hotkey, app_path in hotkeys:
        try:
            keyboard.add_hotkey(hotkey, open_app, args=(app_path,))
            print(f"binding set : Hotkey - {hotkey}, App Path - {app_path}")
        except KeyboardInterrupt:
            print("exiting...")

    print("Press esc to exit.")
    keyboard.wait("esc")

if __name__ == "__main__":
    main()
