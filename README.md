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

### V2.0

* Support for other translation agency services, e.g., proofreading, translation only etc. 

### V1.0

* Basic functionality. 
* A function to auto-detect programs location (where the user has upzipped it), so he or she does not need to set the "root_directory" parameter. The user can have an option to manually change the location of project folders. 

## Bugs and Issues

## Author

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
