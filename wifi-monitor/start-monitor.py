#!/usr/bin/python3

import logging
import sniffer
import file_recorder

def create_logger():
    logger = logging.getLogger('wifi-monitor')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s]: %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger

def main():
    logger = create_logger()
    logger.info('Starting program')

    recorder = file_recorder.File_Recorder()

    monitor = sniffer.Sniffer(recorder)
    monitor.start()

    logger.info('Exiting program')

if (__name__ == '__main__'):
    main()
