#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import logging.handlers

from termcolor import cprint



class ColorLogger(object):
    """
    Write log messages to console (with any colors and
    backgrounds) and to file (optional).
    """

    def __init__(self, logger_name=None, log_file_name=None):
        super(ColorLogger, self).__init__()

        self.logger = None

        if logger_name and log_file_name:
            self.logger_name = logger_name
            self.log_file_name = log_file_name

            self.logging_formatter = logging.Formatter(
                '[%(asctime)s][%(levelname)s] %(message)s',
                '%Y.%m.%d %H:%M:%S',
            )

            handler = get_rotation_handler(log_file_name)
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False
            self.logger.addHandler(handler)

    def get_rotation_handler(log_file_name):
        rotating_handler = logging.handlers.RotatingFileHandler(
            log_file_name,
            maxBytes=3145728,   # 3Mb
            backupCount=5
        )
        rotating_handler.setFormatter(self.logging_formatter)

        return rotating_handler

    def write(self, message, color=None, background=None, attrs=[]):
        cprint(message, color, background, attrs=attrs)    # write to console
        if self.logger:
            self.logger.debug(message)                     # write to file


