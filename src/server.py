# -*- coding: utf-8 -*-
"""Server for the Raspi Webapp
Examples:
- get json with curl -> curl -X POST http://0.0.0.0:2828/api/v1/getCrashInfo
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

app = Sanic()
app.name = "CrashSimulationAsimov"
log = logger.get(True, "Server")

# SIGINT handler (when pressing Ctrl+C)

def signal_int_handler(sig, frame):
    print("Ctrl+C Pressed. Exit...")
    sys.exit(0)

# Routes
# POST request 1 - returns JSON {"impactAngle": degrees, "offsetMaximumForce": millisecond}
@app.route('/api/v1/getCrashInfo', methods=['POST',])
async def crash_info(request):
    ''' crash info parses the crash record and returns a JSON object '''
    log.info("Handling '/api/v1/getCrashInfo'")
    return json({'impactAngle': 90, 'offsetMaximumForce': 3})

# POST request 2 - returns a rendered crash image (PNG)
@app.route('/api/v1/getCrashImage', methods=['POST',])
async def crash_image(request):
    ''' crash image parses the crash record and returns a JSON object '''
    log.info("Handling '/api/v1/getCrashImage'")
    return await file('images/lena.png')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_int_handler)
    ##app.add_task(task(app))
    app.run(host=config.host, port=config.port)
