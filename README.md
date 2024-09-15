# Environment Variables Manager for Windows

This Python script allows you to **view**, **add**, and **delete** environment variables permanently on **Windows**. It also supports **batch processing** of environment variables through CSV files. The script interacts with the Windows **registry** to handle environment variables, ensuring changes are reflected permanently.

---

## Features
- **View Environment Variables**: Lists all user environment variables stored in the Windows registry.
- **Add Environment Variables**: Add new environment variables either manually via the CLI or through a CSV file.
- **Delete Environment Variables**: Delete environment variables either manually via the CLI or through a CSV file.
- **CSV Support**: Batch add or delete variables by providing CSV files.
- **Export Environment Variables to CSV**: Save the current environment variables to a CSV file for easy reference.

---

## Requirements
- **Operating System**: Windows
- **Python Version**: Python 3.x
- **Libraries**:
  - `winreg` (built-in for Windows registry access)
  - `subprocess` (built-in for executing system commands)
  - `os` (built-in for file handling)
  - `csv` (built-in for CSV file handling)

---

## Directory Structure
	/your_project/
	    /program/    # This script resides here
	    /input/      # Place to_add.csv and to_delete.csv here
	    /output/     # The script saves env_variables.csv here when exporting variables
---

## Usage Instructions

1. **Download or Clone the Script**:
   - Ensure the script resides in the `/program/` directory as shown in the directory structure.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the `program` directory where the script is located:
     ```bash
     cd /path/to/program
     ```
   - Run the script:
     ```bash
     python env_manager.py
     ```

3. **Main Menu**:
   - After running the script, you'll be presented with the following options:
     ```
     Select an option:
     1. Show all environment variables
     2. Add a new environment variable permanently
     3. Delete an environment variable permanently
     4. Exit
     ```

### Option 1: **Show Environment Variables**
- Lists all environment variables stored in the Windows registry.
- Optionally, you can export these variables to a CSV file by following the prompt. The file will be saved in the `/output/` directory as `env_variables.csv`.

### Option 2: **Add New Environment Variable**
- You can add new variables in two ways:
  - **Manual Entry**: The script will ask for the variable name and value, and then permanently add it to the Windows environment.
  - **From a CSV File**: Place a CSV file named `to_add.csv` in the `/input/` directory. The file should contain rows in the format `name;value`. Example:
    ```csv
    VAR1;Value1
    VAR2;Value2
    ```
  - The script will read and add all variables in the CSV file.

### Option 3: **Delete Environment Variable**
- You can delete variables in two ways:
  - **Manual Entry**: The script will ask for the variable name and permanently remove it from the Windows environment.
  - **From a CSV File**: Place a CSV file named `to_delete.csv` in the `/input/` directory. The file should contain rows with just the variable name. The format is `name;value` but only the name is required. Example:
    ```csv
    VAR1;
    VAR2;
    ```

### Option 4: **Exit the Program**
- Safely exit the script.

---

## CSV File Format

### **to_add.csv** (For adding variables):
- The file should contain rows with the format `name;value`. Example:
  ```csv
  VAR1;Value1
  VAR2;Value2

### **to_delete.csv** (For deleting variables):
- The file should contain rows with the format `name;`. Only the name field is necessary. Example:
  ```csv
  VAR1;
  VAR2;
  
---

## Important Notes

1. **Permanent Changes**:
   - Environment variables added or deleted using this script are **permanent** and are stored in the Windows registry.
   - Changes will apply immediately to new sessions, but you may need to restart your terminal to see them in the current session.

2. **Batch Processing**:
   - Ensure CSV files (`to_add.csv` and `to_delete.csv`) are placed in the `/input/` directory before running the script.

3. **Error Handling**:
   - The script handles errors, such as missing CSV files or invalid formats, and will inform you if something goes wrong during variable addition or deletion.

---

## License

MIT License

Copyright (c) 2024 Miguel Gomes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
