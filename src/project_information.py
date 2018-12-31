import os
import json

class project_info:
    '''Open config.json and get values 'root_directory' and 'project_number.'''

    def get_project_info(self):
        with open("config.json", "r") as json_file:
            config = json.load(json_file)

            self.root_directory = config["root_directory"]
            self.project_number = str(config["project_number"])
    
            self.project_folder_name = "Project No " + str(self.project_number)
            self.project_folder_location = os.path.join(self.root_directory, self.project_folder_name)
            
            self.log_name = self.project_folder_name + '.docx'
            self.log_name_and_location = os.path.join(self.project_folder_location, self.log_name)

