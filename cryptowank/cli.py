import argparse
import time
import yaml
import subprocess

from .utils import parse_rules
from . import exchanges

def parse_args():
    parser = argparse.ArgumentParser(description='Cryptowank! Alerts for crypto prices')
    parser.add_argument('-c', '--config', 
        required=True,
        help='Config file, refer to help to see this structure.')
    args = parser.parse_args()
    return args


def run_command(command):
    subprocess.call(command)

def poloniex_thread(config):
    try:
        settings = config['poloniex']
    except KeyError:
        return

    while True:
        rules = parse_rules(settings.get('rules', []))
        exchange = exchanges.poloniex.API()
        ticker = exchange.ticker()
        for rule in rules:
            market_obj = ticker[rule['market']]
            if rule['operator'](market_obj['last'], rule['target']):
                print("DING DING DING!")
                print("{} hit {}".format(rule['market'], rule['target']))
                run_command(config['config']['command'])
        
        time.sleep(config['config']['timeout'])


import threading

def main():
    args = parse_args()
    
    with open(args.config, 'r') as f:
        obj = yaml.load(f.read())

    threads = []

    polo = threading.Thread(target=poloniex_thread,
                     name="poloniex-thread", args=(obj, ),
                     )
    threads.append(polo)
    
    for th in threads:
        th.start()
    
    while True:
        time.sleep(1)
