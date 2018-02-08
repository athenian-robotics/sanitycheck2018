import time


class StatusVault(object):

    def __init__(self):
        self.healthData = {}  # TODO make it contain no data but all the needed keys

    def addHTML(self):
        html1 = "{}".format(
            '''<!DOCTYPE html><html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><table><tr><th>Topic</th><th>Data</th><th>Time</th></tr>''')
        # Create the beginning HTML
        html2 = '' # create an empty string to store the table in
        for i in self.healthData.keys():  # for each key...
            html2 += '''<tr>
            <th>{0}</th>
            <th>{1}</th>
            <th>{2}</th>
            </tr>'''.format(i, self.healthData[i][0], str(time.time() - self.healthData[i][1]))  # make the table
            # TODO use the getValue instead of the self.healthData directly
        html3 = '''</table></body></html>'''  # Close it all
        return html1 + html2 + html3  # return the whole shebang

    def getValue(self, key):
        if key in self.healthData:  # if we've already got data...
            return self.healthData[key]  # give it up
        else:
            self.healthData[key] = "The default value; no value has been set yet."  # otherwise set a value
            return self.healthData[key]  # and return it

    def callback_test(self, data):  # TODO make one function that accepts arguments for topic
        self.healthData["test_system"] = [data.data, time.time()]

    def callback_test2(self, data):
        self.healthData["test_system2"] = [data.data, time.time()]