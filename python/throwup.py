#!/usr/bin/env python
import rospy
from threading import Thread
from std_msgs.msg import String
import rostopic
import sys
from flask import Flask
from flask import Response
import logging
from dataVault import StatusVault
import roslib

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='%(asctime)s %(name)-10s %(funcName)-10s():%(lineno)i: %(levelname)-6s %(message)s')

dataVault = StatusVault()  # make a new StatusVault called dataVault.

PORT = 'port'
http = Flask(__name__)


@http.route('/throwup')
def throwup():
    text = "I AM FANCY"
    return Response(text, mimetype='text/plain')
    # throwup (badump-chhh) a simple server that says "I AM FANCY" in plaintext, so you can make sure server is up


@http.route('/overview')
def overview():
    global dataVault  # use the proper dataVault
    text = dataVault.addHTML()  # get the HTML
    return Response(text, mimetype='text/html')  # return the HTML


@http.route('/add/<topic>')
def add(topic):
    global dataVault  # use the proper dataVault
    text = dataVault.write(topic)
    return Response(text, mimetype='text/html')  # return the HTML


@http.route('/list')
def list():
    text_src = rospy.get_published_topics(namespace='/')
    text = ""
    for i in range(len(text_src)):
        print(text_src[i][0])
        if text_src[i][1] == "std_msgs/String":
            text += text_src[i][0] + "<br>"
    return Response(text, mimetype='text/html')  # return the HTML


def run_http(flask_server, host, port):
    flask_server.run(host=host, port=port)


if __name__ == '__main__':
    # http.run(debug=False, port=8080, host='0.0.0.0')
    Thread(target=run_http, kwargs={'flask_server': http, "host": "0.0.0.0", "port": 8080}).start()
    # Start a server in a new thread
    rospy.init_node('healthcheckbackend')
    for topic in dataVault.topics:
        data_type = rostopic.get_topic_type(topic, blocking=False)[0]
        if data_type:
            data_class = roslib.message.get_message_class(data_type)
            rospy.Subscriber(topic, data_class, dataVault.callback, topic)
    rospy.spin()  # don't die all over yourself
