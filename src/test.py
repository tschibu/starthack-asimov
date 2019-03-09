'''
Usage:
- run server (python server.py)
- run test (python test.py -cinf=True -cimg=True -d=data/1.json)
'''
import helper.log_helper as logger

import requests
import argparse
import config

def test_crashinfo(json_file):
    __post_request(__get_url('/api/v1/getCrashInfo'), json_file)

def test_crashimage(json_file):
    __post_request(__get_url('/api/v1/getCrashImage'), json_file)

def __post_request(url, json_file):
    resp = requests.post(url, data=open(json_file, 'rb'))
    return resp

def __get_url(endpoint):
    return 'http://'+config.host+':'+str(config.port)+endpoint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test utility for CrashSimulationAsimov')
    parser.add_argument('-cinf','--crashInfo', help='execute crashInfo test', required=False, default="False")
    parser.add_argument('-cimg','--crashImage', help='execute crashImage test', required=False, default="False")
    parser.add_argument('-d','--data', help='json file to use', required=True)
    args = vars(parser.parse_args())

    log = logger.get(True, "TestUtility")
    if args['crashInfo'] == "True":
        log.info("Executing crashInfo test with: " + args['data'])
        test_crashinfo(args['data'])
    else:
        log.info("CrashInfo test not enabled...")

    if args['crashImage'] == "True":
        log.info("Executing crashImage test with: " + args['data'])
        test_crashimage(args['data'])
    else:
        log.info("crashImage test not enabled...")
