# File Tray
Python program for project management. 

At start, the program will be focused on translation agencies, providing services as translation, revision, proofreading etc. Later on, it will provide options for the user to create his or her own folder structure. 

First push: 02.11.2018 \n
Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

[https://github.com/SebastjanLeskovar/file_tray](https://github.com/SebastjanLeskovar/file_tray)

## Getting Started

### Prerequisites

As of version V1.0, the following prerequisites are necessary to run this program:
- Python 3.x

Apart from the standard libraries 'os', 'sys', 'json' and 'datetime', the library 'docx' must be installed. Please install it using the following terminal command: 

```bash
pip install python-docx
```

### Installation

1. In GitHub, click the green button 'Clone or download' on the right, and 'Download ZIP'.

2. Extract the files from ZIP to any folder on your computer. 

### How to use

#### Config.json

Before using the program, please set a parameter in the 'config.json' file, located at the top-most level. Open and edit the file with any text editor or ide (Notepad will do). 

That parameter is "root_directory", please insert your root directory where you wish to store your project folders. You need to use double backslashes. 

If unsure, use the default setting: 
```bash
"root_directory": "C:\\corp_data",
```
This way, your projects will be stored in 'C:\\corp_data'. 

'project_number' will start at '1'. If and error occurs, please set this parameter to the number of the next project. E.g., if the last project's name is 'Project No 4', please set this number to '5'. 

#### Starting the program

After setting the configuration, use Command Prompt to navigate to the root of the unziped folder (e.g., cd ...\file_tray). Launch the program with the folowing command:

```bash
python file_tray.py
```

First, the program will ask the user to create a project folder. If the user agrees, he will be presented with two more options:

- To create subfolders.

If selected, the program will create subfolders as specified in 'config.json' file. The default services are for a translation agency, but can be easily adjusted in 'config.json' file to any specific needs. 

- To create a project log file. 

If selected, the program will create a log document in the project folder. This document will be used to store all important project information in one place. 

The folder structure will be created at the designated location. 

## Versioning

### V5.0

* Implementing tkinter GUI.

### V4.0

* Wizard at first launch to specify project manager's name and folder location.

### V3.5

* Option to create a project specifics file in .docx format.

#### V3.0

* Implementation of classes.

#### V2.5

* Adding support for a log file to record a list of all actions that this program has done. 

### V2.0

* Option to cancel project creation.

#### V1.5

* Support for other translation agency services, e.g., proofreading, translation only etc. 

### V1.0

* Basic functionality. 

## Bugs and Issues

1. (03.11.2018): If a project folder already exists at the location, the following error is raised:
```bash
Traceback (most recent call last):
  File "file_tray.py", line 68, in <module>
    create_project_folder_structure()
  File "file_tray.py", line 53, in create_project_folder_structure
    os.makedirs(os.path.join(config["root_directory"], project_folder_name))
  [...]
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\corp_data\\Project No 6'
```
Appearently, the check "if os.path.isdir(project_folder_name):" does not work. The issue might get fixed by setting the perameter "exist_ok" in os.makedirs(). 

SOLVED: added the following line:
```bash
"if os.path.exists(self.project_folder_location):". 
```

## Author

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
