import os
import json


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
        
    for service in config["translation_project"]:
        os.makedirs(os.path.join(config["root_directory"], project_folder_name, service))

    with open("config.json", "w") as json_file:
        json.dump(config, json_file, indent=4)

create_project_folder_structure()
