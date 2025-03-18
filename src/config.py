#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import locale

# start configuration here

def init():
    config = {}
    locale.setlocale(locale.LC_ALL, '')
    config['GENERATOR_STARTED'] = datetime.datetime.now()
    config['CURRENT_YEAR'] = config['GENERATOR_STARTED'].strftime('%Y')
    config['GENERATED_DATETIME'] = config['GENERATOR_STARTED'].strftime('%Y%m%d %H%M%S')
    config['GENERATED_DATETIME_HUMAN_READABLE'] = config['GENERATOR_STARTED'].strftime('%d.%m.%Y %H:%M:%S')

    aPath = os.path.realpath(__file__)
    aPath = os.path.dirname(aPath)
    configPath = os.path.normpath(aPath)
    aPath = os.path.join(aPath, "..")
    aPath = os.path.normpath(aPath)
    config["PROJECT_ROOT_DIR"] = aPath
    config["SRC_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "src" )
    config["DATA_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "data" )
    config["BUILD_OUT_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "_www" )
    config["TEMPLATES_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "html" )
    config["TEMPLATE_FILES"] = [
        ("main.html", "MAIN_TEMPLATE"),
        ("about_section.html", "ABOUT_TEMPLATE"),
        ("skills_section.html", "SKILLS_TEMPLATE"),
        ("top_projects_section.html", "TOP_PROJECTS_TEMPLATE"),
        ("all_projects_section.html", "ALL_PROJECTS_TEMPLATE"),
        ("project_task.html", "PROJECT_TASK_TEMPLATE"),
        #("", "")
    ]
    config["ALL_PROJECTS_JSON_FILE"] = "all_project_list.json"
    config["TOP_PROJECTS_JSON_FILE"] = "top_project_list.json"
    config["SKILLS_JSON_FILE"] = "skills.json"

    return config

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    raise Exception("This is a configuration module and should not be run directly")