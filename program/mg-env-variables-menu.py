import os
import platform
import subprocess
import csv
import winreg


def show_env_variables():
    """Show all environment variables with their names and values from the registry."""
    print("\nCurrent Environment Variables (from registry):\n")
    env_vars = get_env_variables_from_registry()
    for key, value in env_vars.items():
        print(f"{key}: {value}")
    print("\n")

    # Option to save to CSV file in the "output" directory
    save_to_csv = input("Do you want to save the variables to a CSV file? (y/n): ").strip().lower()
    if save_to_csv == 'y':
        save_env_to_csv(env_vars)


def save_env_to_csv(env_vars):
    """Save environment variables to a CSV file in the 'output' directory."""
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'env_variables.csv')

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Value'])  # CSV header
        for key, value in env_vars.items():
            writer.writerow([key, value])

    print(f"\nEnvironment variables have been saved to {output_file}\n")


def add_env_variable():
    """Add new environment variables."""
    input_option = input("Do you want to add variables from a CSV file? (y/n): ").strip().lower()

    if input_option == 'y':
        add_variables_from_csv()
    else:
        key = input("Enter the name of the environment variable: ").strip()
        value = input("Enter the value of the environment variable: ").strip()
        _persist_env_variable(key, value)


def add_variables_from_csv():
    """Add multiple environment variables from a CSV file in the 'input' directory."""
    input_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    input_file = os.path.join(input_dir, 'to_add.csv')

    if not os.path.exists(input_file):
        print(f"File '{input_file}' not found. Please ensure the file exists in the 'input' directory.")
        return

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if len(row) != 2:
                print(f"Invalid format in row: {row}")
                continue
            key, value = row
            _persist_env_variable(key.strip(), value.strip())


def delete_env_variable():
    """Delete environment variables."""
    input_option = input("Do you want to delete variables from a CSV file? (y/n): ").strip().lower()

    if input_option == 'y':
        delete_variables_from_csv()
    else:
        key = input("Enter the name of the environment variable to delete: ").strip()
        _remove_env_variable(key)


def delete_variables_from_csv():
    """Delete multiple environment variables from a CSV file in the 'input' directory."""
    input_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    input_file = os.path.join(input_dir, 'to_delete.csv')

    if not os.path.exists(input_file):
        print(f"File '{input_file}' not found. Please ensure the file exists in the 'input' directory.")
        return

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if len(row) != 2:
                print(f"Invalid format in row: {row}")
                continue
            key, _ = row  # Only need the key to delete
            _remove_env_variable(key.strip())


def _persist_env_variable(key, value):
    """Persist environment variable permanently in Windows."""
    # Construct the command string with proper escaping for special characters like & and ^.
    command = f'setx {key} "{value}"'

    # Execute the command as a string (not a list) to properly handle special characters.
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f"Permanently added '{key}' with value '{value}' to Windows environment variables.")
        print("Note: The variable will be visible in new sessions, but we will reload from the registry now.")
    else:
        print(f"Failed to add '{key}' with value '{value}' to environment variables. Error: {result.stderr.decode()}")


def _remove_env_variable(key):
    """Remove environment variable permanently."""
    result = subprocess.run(f'reg delete "HKCU\\Environment" /F /V {key}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Removed '{key}' from Windows environment variables.")
        print("Note: The variable will be removed in new sessions, but we will reload from the registry now.")
    else:
        print(f"Failed to delete '{key}'. It may not exist or may be a system variable.")


def get_env_variables_from_registry():
    """Get environment variables directly from the Windows registry."""
    env_vars = {}
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_READ)
        i = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(reg_key, i)
                env_vars[name] = value
                i += 1
            except OSError:
                break
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"Error reading environment variables from registry: {e}")
    
    return env_vars


def main():
    if platform.system() != 'Windows':
        print("This script is designed to work only on Windows.")
        return

    while True:
        print("\nSelect an option:")
        print("1. Show all environment variables")
        print("2. Add a new environment variable permanently")
        print("3. Delete an environment variable permanently")
        print("4. Exit")

        choice = input("\nEnter your choice (1/2/3/4): ").strip()

        if choice == '1':
            show_env_variables()
        elif choice == '2':
            add_env_variable()
        elif choice == '3':
            delete_env_variable()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
