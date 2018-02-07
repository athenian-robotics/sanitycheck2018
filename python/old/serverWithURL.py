from old.generateHTML import *
import sys
from flask import Flask
from flask import Response
import logging
from getState import *
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(name)-10s %(funcName)-10s():%(lineno)i'
                                                                  ': %(levelname)-6s %(message)s')

PORT = 'port'
http = Flask(__name__)
settupGetState("test_system", Bool)


@http.route('/html-health')
def html_hello():
    text = makehtml(getStateSimple("test_system", Bool))
    return Response(text, mimetype='text/html')


if __name__ == '__main__':
    http.run(debug=False, port=8080, host='0.0.0.0')