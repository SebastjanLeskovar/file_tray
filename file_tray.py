import os
import json


service_selection = None

def ask_for_service():
    print("Welcome to program File Tray.")
    options = "1. Translation only\n2. Translation with revision\n3. Proofreading\nPlease enter 1, 2 or 3: "
    
    global service_selection
    
    number_input = input("What is the service of this project? \n" + options)

    # print("Point 1: ", number_input)

    while number_input not in ["1", "2", "3"]:
        number_input = input("Wrong input. The options are: \n" + options)
        
    if number_input == "1":
        service_selection = "translation"
    elif number_input == "2":
        service_selection = "translation_and_revision"
    elif number_input == "3":
        service_selection = "proofreading"

def create_project_folder_structure():

    with open("config.json", "r") as json_file:
        config = json.load(json_file)
    
    project_folder_name = "Project No " + str(config["project_number"])

    if os.path.isdir(project_folder_name):
        print("The folder '%s' already exists at that location. Please check the project folders and change the 'project_number' value in Config accordingly. " % project_folder_name)
    else:
        os.makedirs(os.path.join(config["root_directory"], project_folder_name))
        print("The project folder '%s' has been created." % project_folder_name)

        config["project_number"] += 1
        
        for service in config["service"][service_selection]:
            os.makedirs(os.path.join(config["root_directory"], project_folder_name, service))

    with open("config.json", "w") as json_file:
        json.dump(config, json_file, indent=4)

ask_for_service()

# print("Point 1: ", service_selection)

create_project_folder_structure()
