import os
import sys
import json
import logging
import folder_structure_creation

service_selection = None

log = logging.Logging()
creation = folder_structure_creation.folder_structure_creation()


class terminal():

    def start_message(self):
        print("Welcome to program File Tray.")
        log.write_to_log("Program File Tray started.")

    def create_project(self):
        
        self.start_message()

        while True:
            input_1 = input("Should I create a new project? Type in 'yes' to create a new project or 'no' to cancel. ")

            if input_1.lower() not in ("yes", "y", "1", "no", "n", "2"):
                print("Wrong input.")
                log.write_to_log("Wrong input. User entered %s." % input_1)
                continue
            else:
                break
        
        if (input_1 == "yes") or (input_1 == "y") or (input_1 == "1"):
            log.write_to_log("The user entered '%s'." % input_1)
            creation.get_data_from_config()
            creation.project_folder_name_and_location()
            creation.create_project_folder()
            terminal.create_subfolders()

        else:
            print("The program was cancelled.")
            log.write_to_log("The program was terminated with sys.exit().")
            sys.exit()
       
    def create_subfolders(self):
        
        while True:
            input_2 = input("What is the service of this project?\n1. Translation only\n2. Translation with revision\n3. Proofreading\n4. Cancel creating subfolders\nPlease enter 1, 2, 3 or 4: ")

            if input_2 == "4":
                print("The program was closed.")
                log.write_to_log("The program was terminated with sys.exit().")
                sys.exit()
            elif input_2 not in ("1", "2", "3"):
                print("Wrong input.")
                log.write_to_log("Wrong input: user entered %s." % input_2)
                continue
            else:
                break

        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            service_selection = config["service_selection"][input_2]
            log.write_to_log("User selected service '%s'." % service_selection)
            creation.create_subfolders(service_selection)
            print("The subfolders for service '%s' were created. Program closed." % service_selection)
            log.write_to_log("Program closed.")

# Instantiation. 
terminal = terminal()

terminal.create_project()
