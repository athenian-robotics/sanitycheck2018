import time

class StatusVault(object):
    def __init__(self):
        self.healthData = {}
        with open("topics.txt") as f:
            self.topics = f.read().split(",")  # get the list of topics from topics.txt
        for topic in self.topics:
            self.set_default(topic)
    def addHTML(self):
        html1 = "{}".format(
            '''<!DOCTYPE html><html><head><style>table {font-family: avenir, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><h1>YOU CAN PUBLISH ANY DATATYPE. HAPPY, ADIT?</h1><table><tr><th>Topic</th><th>Data</th><th>Time</th></tr>''')
        # Create the beginning HTML
        html2 = ''  # create an empty string to store the table in
        for i in sorted(self.healthData.keys()):  # for each key...
            html2 += '''<tr>
            <th>{0}</th>
            <th>{1}</th>
            <th>{2}</th>
            </tr>'''.format(i, self.getValue(i)[0], str(round((time.time() - self.getValue(i)[1])*1000))+ " ms")  # make the table
        html3 = '''</table></body></html>'''  # Close it all
        return html1 + html2 + html3  # return the whole thingy

    def getValue(self, key):
        if key in self.healthData:  # if we've already got data...
            return self.healthData[key]  # return it
        else:
            self.healthData[key] = ["The default value; no value has been set yet.", time.time()]  # otherwise set a value
            return self.healthData[key]  # and return it

    def set_default(self, key):  # set the default data
        self.healthData[key] = ["The default value; no value has been set yet.", time.time()]

    def callback(self, data, system):
        self.healthData[system] = [str(data.data), time.time()]

    def write(self, topic):
        with open("topics.txt") as f:
            tmp = f.read().split(",")  # get the list of topics from topics.txt
            if topic in tmp:
                return "Topic " + topic + " is already in database. Restart server to view changes."
        with open("topics.txt", "a") as f:
            self.topics = f.write(",/" + topic)  # write topic to end
            return "Topic /" + topic + " added successfully."
