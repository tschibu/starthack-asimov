# -*- coding: utf-8 -*-
"""Server for the Raspi Webapp
Examples:
- get json with curl -> curl -X POST http://0.0.0.0:2828/api/v1/getCrashInfo -d data/1.json
- get image with curl -> curl -X POST http://0.0.0.0:2828/api/v1/getCrashImage -o received_img.png
"""
import sys
sys.path.append('..')
import os
import signal
import time

from sanic import Sanic
from sanic.response import json
from sanic.response import file

import helper.log_helper as logger
import config
from drawer import Drawer
from data_parser import DataParser

app = Sanic()
app.name = "CrashSimulationAsimov"
log = logger.get(True, "Server")

# SIGINT handler (when pressing Ctrl+C)
def signal_int_handler(sig, frame):
    print("Ctrl+C Pressed. Exit...")
    sys.exit(0)

# Routes
# GET - index.html
@app.route('/', methods=['GET'],)
async def index(request):
    return await file(os.path.join(os.path.dirname(__file__), 'frontend/index.html'))

# GET - favicon.ico
@app.route('/favicon.ico', methods=['GET'],)
async def favicon(request):
    return await file(os.path.join(os.path.dirname(__file__), 'frontend/favicon.ico'))


# POST request 1 - returns JSON {"impactAngle": degrees, "offsetMaximumForce": millisecond}
@app.route('/api/v1/getCrashInfo', methods=['POST',])
async def crash_info(request):
    ''' crash info parses the crash record and returns a JSON object '''
    log.info("Handling '/api/v1/getCrashInfo'")
    angle, max_force_offset, _, _ = DataParser().parse_input_data(request.body.decode('utf8'))
    return json({'impactAngle': angle, 'offsetMaximumForce': max_force_offset})

# POST request 2 - returns a rendered crash image (PNG)
@app.route('/api/v1/getCrashImage', methods=['POST',])
async def crash_image(request):
    ''' crash image parses the crash record and returns a JSON object '''
    log.info("Handling '/api/v1/getCrashImage'")
    d = Drawer(1300, 550, 60, 180, 6110)
    return await file(d.get_image())

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_int_handler)
    ##app.add_task(task(app))
    app.static('/frontend', './frontend')
    app.run(host=config.host, port=config.port)
