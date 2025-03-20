#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import yaml

def setup_logging(config_path="src/logging_config.yaml"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)

# configure Logging by importing this modul
setup_logging()
logger = logging.getLogger("myapp")
logger.info("Logging is configured.")