#!/usr/bin/env python
import rospy
from threading import Thread
from std_msgs.msg import String
import sys
from flask import Flask
from flask import Response
import logging
from dataVault import StatusVault
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(name)-10s %(funcName)-10s():%(lineno)i: %(levelname)-6s %(message)s')

dataVault = StatusVault()

PORT = 'port'
http = Flask(__name__)

@http.route('/throwup')
def throwup():
    text = "I AM FANCY"
    return Response(text, mimetype='text/plain')
    # throwup (badump-chhh) a simple server that says "I AM FANCY" in plaintext

@http.route('/statesimple')
def statesimple():
    global dataVault
    text = dataVault.getValue("test_system")
    return Response(text, mimetype='text/html')

def run_http(flask_server, host, port):
    flask_server.run(host=host, port=port)

if __name__ == '__main__':
    # http.run(debug=False, port=8080, host='0.0.0.0')
    Thread(target=run_http, kwargs={'flask_server': http, "host": "0.0.0.0", "port": 8080}).start()

    rospy.init_node('healthcheckbackend')
    rospy.Subscriber("test_system", String, dataVault.callback_test)

    # rospy.Subscriber("test_system", String, dataVault.callback_test)

    rospy.spin()