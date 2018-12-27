import os
import sys
import json
from src import doc, folder_structure, log_writing


service_selection = None


log = log_writing.Logging()
structure = folder_structure.folder_structure()
doc = doc.Doc()


class ui():

    def create_project(self):
        
        print("==== Welcome to program File Tray. ====")
        log.write_to_log("Program File Tray started.")

        while True:
            self.input_1 = input("Should I create a new project? Type in 'yes' to create a new project or 'no' to cancel. ")

            if self.input_1.lower() not in ("yes", "y", "1", "no", "n", "2"):
                print("Wrong input.")
                log.write_to_log("Wrong input. User entered %s." % self.input_1)
                continue
            else:
                break
        
        if (self.input_1 == "yes") or (self.input_1 == "y") or (self.input_1 == "1"):
            log.write_to_log("The user entered '%s'." % self.input_1)
            structure.get_project_info()
            structure.create_project_folder()
        
        # TODO: Currently, create_subfolders() always starts automatically, even if the project folder exists and a new one was not created. create_project() should check if the project folder was created and start create_subfolders() only if it was. 
        # Create a function in folder_structure to return True or False whether the project folder was created or not. 
            self.create_subfolders()

        else:
            print("The program was cancelled.")
            log.write_to_log("The program was terminated with sys.exit().")
            sys.exit()
       
    def create_subfolders(self):
        
        while True:
            self.input_2 = input("What is the service of this project?\n1. Translation only\n2. Translation with revision\n3. Proofreading\n4. Cancel creating subfolders\nPlease enter 1, 2, 3 or 4: ")

            if self.input_2 == "4":
                print("The program was closed.")
                log.write_to_log("The program was terminated with sys.exit().")
                sys.exit()
            elif self.input_2 not in ("1", "2", "3"):
                print("Wrong input.")
                log.write_to_log("Wrong input: user entered %s." % self.input_2)
                continue
            else:
                break

        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            self.service_selection = config["service_selection"][self.input_2]
            log.write_to_log("User selected service '%s'." % self.service_selection)
            structure.create_subfolders(self.service_selection)
            print("The subfolders for service '%s' were created. Program closed." % self.service_selection)
            log.write_to_log("Program closed.")

    def create_doc(self):
        doc.create_doc("C:\corp_data\Project No 2")

# Instantiation. 
start = ui()

start.create_project()