import datetime

class Logging():

    def get_timestamp(self):
        self.timestamp = datetime.datetime.now().replace(microsecond=0)
        self.timestamp.strftime('%Y/%m/%d %H:%M:%S')
        return str(self.timestamp) + " - "

    def write_to_log(self, text):
        self.log = open('Log.txt', 'a')
        self.log.write(self.get_timestamp())
        self.log.write(text)
        self.log.write("\n")
        self.log.close()
