import json
import os
from src import log_tracking, project_information

log = log_tracking.Logging()
pr_info = project_information.ProjectInfo()

# Create folder structure (project folder and subfolders)
class FolderStructure():

    project_folder_created = False

    def counter(self):
        '''Increase 'project_number' value in 'config.json by 1.'''

        with open("config.json", "r") as json_file:
            config = json.load(json_file)
      
        project_number = config["project_number"]
        project_number += 1
        config["project_number"] = project_number
        
        with open("config.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

    def create_project_folder(self):
        '''Create project folder. Check first, if the folder exists.'''
        
        pr_info.get_project_info()

        if os.path.exists(pr_info.project_folder_location):
            print("Project folder '%s' already exists at location '%s'. Please check the location and update the 'project_number' value in file 'config.json' accordingly, probably insert the next project number." % (pr_info.project_folder_name, pr_info.project_folder_location))
            log.write_to_log("Project folder '%s' was found at location '%s' and was not created." % (pr_info.project_folder_name, pr_info.project_folder_location))
            
        else:
            os.makedirs(pr_info.project_folder_location)
            print("Project folder '%s' was created at location '%s'." % (pr_info.project_folder_name, pr_info.project_folder_location))
            self.project_folder_created = True
            
            log.write_to_log("Project folder '%s' was created at location '%s'." % (pr_info.project_folder_name, pr_info.project_folder_location))

                   
    def create_subfolders(self, service_selection):
        '''Create subfolders in the project folder.'''

        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            for service in config["service"][service_selection]:
                os.makedirs(os.path.join(pr_info.project_folder_location, service))
                log.write_to_log("Subfolder '%s' was created at location '%s'." % (service, pr_info.project_folder_location))
