import time


class StatusVault(object):

    def __init__(self):
        self.healthData = {}

    def addHTML(self):
        bad = False
        html1 = "{}".format(
            '''<!DOCTYPE html><html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><table><tr><th>Topic</th><th>Data</th><th>Time</th></tr>''')
        html2 = ''
        for i in self.healthData.keys():
            html2 += '''<tr>
            <th>{0}</th>
            <th>{1}</th>
            <th>{2}</th>
            </tr>'''.format(i, self.healthData[i][0], str(time.time() - self.healthData[i][1]))
        html4 = '<img src="file:~/home/arc852/catkin_ws/src/healthcheck/src/sanitycheck2018/python/assets/DefiniteBetterGuillemot-size_restricted.gif">'
        html3 = '''</table></body></html>'''
        return html1 + html2 + html3 + html4

    def getValue(self, key):
        if key in self.healthData:
            return self.healthData[key]
        else:
            self.healthData[key] = "The default value; no value has been set yet."
            return self.healthData[key]

    def callback_test(self, data):
        self.healthData["test_system"] = [data.data, time.time()]

    def callback_test2(self, data):
        self.healthData["test_system2"] = [data.data, time.time()]
