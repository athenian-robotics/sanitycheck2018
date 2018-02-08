import time


class StatusVault(object):
    def __init__(self):
        self.healthData = {}
        with open("/home/arc852/catkin_ws/src/healthcheck/src/sanitycheck2018/python/topics.txt") as f:
            self.topics = f.read().split(",")  # get the list of topics from topics.txt
        for topic in self.topics:
            self.set_deafult(topic)
    def addHTML(self):
        html1 = "{}".format(
            '''<!DOCTYPE html><html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><h1>IF YOU DON'T SEE ANYTHING CHECK THAT YOU'RE PUBLISHING A STRING</h1><table><tr><th>Topic</th><th>Data</th><th>Time</th></tr>''')
        # Create the beginning HTML
        html2 = ''  # create an empty string to store the table in
        for i in self.healthData.keys():  # for each key...
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
    def set_deafult(self,key):
        self.healthData[key] = ["The default value; no value has been set yet.", time.time()]
    def callback(self, data, system):
        self.healthData[system] = [data.data, time.time()]