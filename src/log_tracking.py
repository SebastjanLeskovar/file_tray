import datetime

class Logging():
    '''Class for creating log entries.'''

    def get_timestamp(self):
        '''Create a time and date stamp when the log was created.'''
        timestamp = datetime.datetime.now().replace(microsecond=0)
        timestamp.strftime('%d/%m/%Y %H:%M:%S')
        return str(timestamp) + " - "

    def write_to_log(self, text):
        '''Write the chosen text to file 'log.txt', located in the root directory.'''

        log = open('Log.txt', 'a')
        log.write(self.get_timestamp())
        log.write(text)
        log.write("\n")
        log.close()
