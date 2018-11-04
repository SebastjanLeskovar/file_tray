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

Please check the 'requirements.txt' file for an up-to-date list of prerequisites.

### Installation

1. Click the green button 'Clone or download' on the right, and 'Download ZIP'.

2. Extract the ZIP file to your computer. It should be extracted to the top-level (root) folder where you store all your data. That is usually a seperate partition (D:) or a folder on a partition (D:\corp). 

### How to use

Before using the program, please set a parameter in the 'config.json' file, located at the top-most level. Open and edit it with any text editor or ide (Notepad will do). 

That parameter is "root_directory", you have to insert your root directory where the project folders will be stored. 

If unsure, use the default setting: 
```bash
"root_directory": "C:\\corp_data",
```
This way, your projects will be stored in 'C:\\corp_data'. 

'project_number' will start at '1'. If and error occurs, please set this parameter to the number of the next project. E.g., if the last project's name is 'Project No 4', please set this number to '5'. 

After setting the configuration, use Command Prompt to navigate to the root of the unziped folder (e.g., cd ...\file_tray). Launch the program with the folowing command:

```bash
python file_tray.py
```

The folder structure will be created at the designated location. 

## Versioning

### V4.0

* Implementing tkinter GUI
* Implementing classes

### V3.0

* Adding creation of a project log file in .docx format.

#### V2.5

* Adding support for a log file to record a list of all actions that this program has done. 

### V2.0

* Option to cancel project creation.

#### V1.5

* Support for other translation agency services, e.g., proofreading, translation only etc. 

### V1.0

* Basic functionality. 

## Bugs and Issues

1. (03.11.2018): If a project folder already axists at the location, the following error is raised:
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

## Author

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
