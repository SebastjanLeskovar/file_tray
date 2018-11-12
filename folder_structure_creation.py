import json
import os
import logging

log = logging.Logging()

class folder_structure_creation():

    # Open config.json and get values 'root_directory' and 'project_number'
    def get_data_from_config(self):
        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            self.root_directory = config["root_directory"]
            self.project_number = str(config["project_number"])
    
    # Return 'project_folder_name' and 'project_folder_location'.
    def project_folder_name_and_location(self):
        self.project_folder_name = "Project No " + str(self.project_number)
        self.project_folder_location = os.path.join(self.root_directory, self.project_folder_name)

    # Increase 'project_number' value in 'config.json by 1.
    def counter(self):

        with open("config.json", "r") as json_file:
            config = json.load(json_file)
      
        project_number = config["project_number"]
        project_number += 1
        config["project_number"] = project_number
        
        with open("config.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

    # Create project folder. Check first, if the folder exists. 
    def create_project_folder(self):
        
        # TODO: 'file-tray.py' naj preveri, ali je return value od create_project_folder() True ali False in glede na to zažene funkcijo create_subfolders(). 
        # project_folder_created = None
        if os.path.exists(self.project_folder_location):
            print("Project folder '%s' already exists at location '%s'. Please check the location and update the 'project_number' value in Config accordingly." % (self.project_folder_name, self.project_folder_location))
            log.write_to_log("Project folder '%s' was found at location '%s' and was not created." % (self.project_folder_name, self.project_folder_location))
            # project_folder_created = False
            
        else:
            os.makedirs(self.project_folder_location)
            print("Project folder '%s' was created at location '%s'." % (self.project_folder_name, self.project_folder_location))
            # project_folder_created = True
            log.write_to_log("Project folder '%s' was created at location '%s'." % (self.project_folder_name, self.project_folder_location))
            
            self.counter()
            log.write_to_log("'project_number' in 'config.json' was increased by 1.")
                        
    # Create subfolders for that project. 
    def create_subfolders(self, service_selection):

        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            for service in config["service"][service_selection]:
                os.makedirs(os.path.join(self.project_folder_location, service))
                log.write_to_log("Subfolder '%s' was created at location '%s'." % (service, self.project_folder_location))