'''
Usage:
python test.py -cinf=True -cimg=True -d=data/1.json
'''
import helper.log_helper as logger

import argparse
import config

def test_crashinfo(**kwargs):
    log = logger.get(True, "Main")
    log.info("START hack winners 2019")

def test_crashinfo(**kwargs):
    log = logger.get(True, "Main")
    log.info("START hack winners 2019")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test utility for CrashSimulationAsimov')
    parser.add_argument('-cinf','--crashInfo', help='execute crashInfo test', required=False, default="False")
    parser.add_argument('-cimg','--crashImage', help='execute crashImage test', required=False, default="False")
    parser.add_argument('-d','--data', help='json file to use', required=True)
    args = vars(parser.parse_args())

    log = logger.get(True, "TestUtility")
    if args['crashInfo'] == "True":
        log.info("Executing crashInfo test with: " + args['data'])
    else:
        log.info("CrashInfo test not enabled...")

    if args['crashImage'] == "True":
        log.info("Executing crashImage test with: " + args['data'])
    else:
        log.info("crashImage test not enabled...")
