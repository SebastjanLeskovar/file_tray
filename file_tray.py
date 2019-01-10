import os
import sys
import json
from src import folder_structure, log_document, log_tracking


log = log_tracking.Logging()
structure = folder_structure.FolderStructure()
log_document = log_document.LogDocument()

    
class UI():
    '''Basic UI of the program.'''
    
    def create_project(self):
        '''Create project folder, subfolders and log document.'''

        print("==== Welcome to program File Tray. ====")
        log.write_to_log("Program File Tray started.")

        while True:     # Check whether the user wants to create a new project folder.
            input_1 = input("Should I create a new project? Type in 'yes' to create a new project or 'no' to cancel. ")

            if input_1 in ("yes", "y", "1"): 
                log.write_to_log("The user entered '%s'." % input_1)
                structure.create_project_folder()
                break
            
            elif input_1 in ('no', 'n', '2'):
                print("Project creation was cancelled.")
                log.write_to_log("The user cancelled the creation of project folder.")
                break

            else:
                print("Wrong input.")
                log.write_to_log("Wrong input. The user entered %s." % input_1)
                continue
        
        if structure.project_folder_created == True:
            while True:     # Check which subfolders the user wants to create.
                input_2 = input("Which subfolders would you like to create?\n1. Translation only\n2. Translation with revision\n3. Proofreading\n4. Cancel creating subfolders\nPlease enter 1, 2, 3 or 4: ")

                if input_2 in ("1", "2", "3"):
                    with open("config.json", "r") as json_file:
                        config = json.load(json_file)

                        self.service_selection = config["service_selection"][input_2]
                        log.write_to_log("User selected service '%s'." % self.service_selection)
                    
                        structure.create_subfolders(self.service_selection)
                        print("The subfolders for service '%s' were created." % self.service_selection)
                    break

                elif input_2 == "4":
                    print("No subfolders will be created.")
                    log.write_to_log("The user decided not to create subfolders.")
                    break
                
                else:
                    print("Wrong input.")
                    log.write_to_log("Wrong input: user entered %s." % input_2)
                    continue

            while True:    # Check whether the user wants to create the log document.
                input_3 = input("Would you like to create a Log file for the project?\nPlease enter 'yes' or 'no': ")
                if input_3.lower() in ("yes", "y", "1"):
                    log_document.create_log_document()
                    break

                elif input_3.lower() in ("no", "n", "2"):
                    log.write_to_log("The user did not decide to create a log document.")
                    break
                
                else:
                    print("Wrong input.")
                    log.write_to_log("Wrong input: the user entered %s." % input_3)

            structure.counter()
            log.write_to_log("'project_number' in 'config.json' was increased by 1.")

            print("Program completed creating your project.")
        
        log.write_to_log("Program closed.")

# if '__name__' == '__main__':
#     try:
auto_start = UI()
auto_start.create_project()  # Automatically start the program.
    # except KeyboardInterrupt:
        # print("The program was closed by user.")
