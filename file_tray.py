import os
import json
import sys
import datetime

service_selection = None

def get_timestamp():
    timestamp = datetime.datetime.now().replace(microsecond=0)
    timestamp.strftime('%Y/%m/%d %H:%M:%S')
    return str(timestamp) + " - "

def write_to_log(text):
    log = open('Log.txt', 'a')
    log.write(get_timestamp())
    log.write(text)
    log.write("\n")
    log.close()

def ask_for_service():
    write_to_log("Program File Tray started.")
    print("Welcome to program File Tray.")
    
    options = "1. Translation only\n2. Translation with revision\n3. Proofreading\n4. Cancel\nPlease enter 1, 2, 3 or 4: "
        
    number_input = input("What is the service of this project? \n" + options)

    while number_input not in ("1", "2", "3", "4"):
        number_input = (input("Wrong input. The options are: \n" + options))
        
    global service_selection
    
    if number_input == "1":
        service_selection = "translation"
    elif number_input == "2":
        service_selection = "translation_and_revision"
    elif number_input == "3":
        service_selection = "proofreading"
    elif number_input == "4":
        print("The program is terminated.")
        write_to_log("The program was terminated with sys.exit().")
        sys.exit()

def create_project_folder_structure():

    with open("config.json", "r") as json_file:
        config = json.load(json_file)
    
    project_folder_name = "Project No " + str(config["project_number"])
    project_folder_location = os.path.join(config["root_directory"], project_folder_name)

    if not os.path.exists(project_folder_location):
    
        os.makedirs(project_folder_location)
        print("The project folder '%s' was created." % project_folder_name)
        write_to_log("The project folder '%s' was created." % project_folder_name)

        config["project_number"] += 1
    
        for service in config["service"][service_selection]:
            os.makedirs(os.path.join(config["root_directory"], project_folder_name, service))
        
        print("The folders for service '%s' were created." % service_selection)
        write_to_log("The folders for service %s were created in project folder '%s'." % (service_selection, project_folder_name))

        with open("config.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

    else:
        print("The folder '%s' already exists at that location. Please check the project folders and change the 'project_number' value in Config accordingly. " % project_folder_name)
        write_to_log("The folder '%s' was found at the location. The project folder was not created." % project_folder_name)
    

ask_for_service()

create_project_folder_structure()
