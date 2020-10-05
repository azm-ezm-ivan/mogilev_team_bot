import logging
from properties import config

nameLevel = {
    'CRITICAL': 50,
    'FATAL': 50,
    'ERROR': 40,
    'WARN': 30,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0,
}


def init_logger():
    logging.basicConfig(filename=config.logging_file, level=config.logging_level, format=config.logging_pattern)
    return logging

