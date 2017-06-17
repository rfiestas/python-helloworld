#!/usr/bin/env python
from flask import Flask
import logging

PORT_NUMBER = 8080
LOG_NAME = 'helloworld.log'
VERSION = '1.0'

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! (V%s)" % (VERSION)

if __name__ == '__main__':
	logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG)
	app.run(host='0.0.0.0', port=PORT_NUMBER, debug=True)
