#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration module for the application.
This module contains the global configuration for the application.
It sets up the project directories, template files, and other constants.
It also initializes the logging and locale settings.

As this file is just a template to store it in the repository, it needs to be copied and renamed to
"config.py" befor running the application!
"""

import os
import datetime
import locale

import logging
logger = logging.getLogger("myapp.configuration")

def configuration():
    """Global configuration of the application."""

    logger.debug("global configuration started")
    config = {}
    locale.setlocale(locale.LC_ALL, '')
    config['GENERATOR_STARTED'] = datetime.datetime.now()
    config['CURRENT_YEAR'] = config['GENERATOR_STARTED'].strftime('%Y')
    config['GENERATED_DATETIME'] = config['GENERATOR_STARTED'].strftime('%Y%m%d %H%M%S')
    config['GENERATED_DATETIME_HUMAN_READABLE'] = config['GENERATOR_STARTED'].strftime('%d.%m.%Y %H:%M:%S')

    aPath = os.path.realpath(__file__)
    aPath = os.path.dirname(aPath)
    aPath = os.path.normpath(aPath)
    aPath = os.path.join(aPath, "..")
    aPath = os.path.normpath(aPath)
    config["PROJECT_ROOT_DIR"] = aPath
    config["SRC_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "src" )
    config["DATA_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "data" )
    config["BUILD_OUT_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "_www" )
    config["BUILD_OUT_FILE"] = os.path.join( config["BUILD_OUT_DIR"], "portfolio.html" )
    config["TEMPLATES_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "html" )
    config["TEMPLATE_FILES"] = [
        ("main.html", "MAIN_TEMPLATE"),
        ("item.html", "ITEM_TEMPLATE"),
        ("item_list.html", "ITEM_LIST_TEMPLATE"),
        ("about_section.html", "ABOUT_TEMPLATE"),
        ("about_section_group.html", "ABOUT_GROUP_TEMPLATE"),
        ("about_section_slogan.html", "ABOUT_SLOGAN_TEMPLATE"),
        ("footer_section.html", "FOOTER_TEMPLATE"),
        ("header_section.html", "HEADER_TEMPLATE"),
        ("skills_section.html", "SKILLS_TEMPLATE"),
        ("skill_group.html", "SKILLS_GROUP_TEMPLATE"),
        ("skill_item.html", "SKILLS_GROUP_ITEM_TEMPLATE"),
        ("projects_section.html", "PROJECTS_TEMPLATE"),
        ("project_item.html", "PROJECT_ITEM_TEMPLATE"),
        ("project_item_branch.html", "PROJECT_ITEM_BRANCH_TEMPLATE"),
        ("project_item_company_client.html", "PROJECT_ITEM_COMPANY_CLIENT_TEMPLATE"),
        ("project_item_methods.html", "PROJECT_ITEM_METHODS_TEMPLATE"),
        ("project_item_roles.html", "PROJECT_ITEM_ROLES_TEMPLATE"),
        ("project_item_tasks.html", "PROJECT_ITEM_TASKS_TEMPLATE"),
        ("project_item_task.html", "PROJECT_ITEM_TASK_TEMPLATE"),
        ("project_item_time_range.html", "PROJECT_ITEM_TIME_RANGE_TEMPLATE"),
        ("project_item_tools.html", "PROJECT_ITEM_TOOLS_TEMPLATE"),
        ("referto_section.html", "REFERTO_TEMPLATE")
    ]

    # with the flag "HAS_REFERTO_SECTION" you can enable or disable the refer to section
    # If you want to use the "Top Projects" together with the "Refer To" section you have to set
    # this flag to "True".
    # The "Top Projects" section will be shown instead of the "All Projects" section.
    # The "Top Projects" section lists only the subset of Projects out of the all projects list, which is 
    # defined with the variable "TOP_PROJECTS_NAME_LIST".
    # In the refer to section you can then set a Link to the Webpage which contains the list of all projects.
    # If you set the "HAS_REFERTO_SECTION" to "False", then the All Project List will be shown and the 
    # Top Projects list will be ignored and not shown. The Refer To Link will not shown, too.
    config["HAS_REFERTO_SECTION"] = False
    config["REFERTO_SECTION_LINK"] = "https://link/to/full/profile.html"
    config["TOP_PROJECTS_NAME_LIST"] = ["profil_1"]

    config["ALL_PROJECTS_JSON_FILE"] = "all_project_list.json"
    config["SKILLS_JSON_FILE"] = "skills.json"
    config["ABOUT_JSON_FILE"] = "about.json"
    config["FOOTER_JSON_FILE"] = "footer.json"
    config["HEADER_JSON_FILE"] = "header.json"

    logger.debug("global configuration done")
    return config

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    raise RuntimeError("This is a configuration module and should not be run directly")