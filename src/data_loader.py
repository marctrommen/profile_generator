#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.DataLoader")

import os
import json

class DataLoader:
    """
    Load data from files.
    Uses the 'data' as data structure from the config file to load the data from files 
    and stores it into the data structure.

    Uses following fields from 'data':

        CONFIG:
            TEMPLATES_DIR: str
            TEMPLATE_FILES: list of tuples (str, str)
            DATA_DIR: str
            ALL_PROJECTS_JSON_FILE: str
            TOP_PROJECTS_JSON_FILE: str
            SKILLS_JSON_FILE: str
    
    Adds data into following fields from 'data':

        ALL_PROJECTS_DATA: dict
        TOP_PROJECTS_DATA: dict
        SKILLS_DATA: dict
        TEMPLATES: dict
        ["TEMPLATES"]<TEMPLATE_NAME>*: str
    """


    # -----------------------------------------------------------------------------
    def load_data(self, data):
        """
        Public Method as entry point to load data from files and store it into the 
        data structure.
        Internally HTML templates, projects data and skills data are loaded 
        in this sequence.
        """
        logger.debug("Load data")
        self.data = data
        self.data["JSON"] = {}
        self.data["JSON"]["ALL_PROJECTS_DATA"] = {}
        self.data["JSON"]["TOP_PROJECTS_DATA"] = {}
        self.data["JSON"]["SKILLS_DATA"] = {}
        self.data["TEMPLATES"] = {}
        self._load_html_templates()
        self._load_projects(all_projects=True)
        self._load_projects(all_projects=False)
        self._load_skills()


    # -----------------------------------------------------------------------------
    def _load_html_templates(self):
        logger.debug("Load HTML templates")

        for (file_name, template_name)  in self.data["CONFIG"]['TEMPLATE_FILES']:
            file_name = os.path.join(self.data["CONFIG"]["TEMPLATES_DIR"], file_name)
            with open(file_name, 'r') as fileObject:
                self.data["TEMPLATES"][template_name] = fileObject.read()


    # -----------------------------------------------------------------------------
    def _load_projects(self, all_projects:bool):
        logger.debug("Load JSON of", ("all" if all_projects else "top"), "projects data")
        if all_projects:
            file_name = self.data["CONFIG"]["ALL_PROJECTS_JSON_FILE"]
        else:
            file_name = self.data["CONFIG"]["TOP_PROJECTS_JSON_FILE"]
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], file_name)
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data should not be empty!")
            if all_projects:
                self.data["JSON"]["ALL_PROJECTS_DATA"] = json_data
            else:
                self.data["JSON"]["TOP_PROJECTS_DATA"] = json_data


    # -----------------------------------------------------------------------------
    def _load_skills(self):
        logger.debug("Load JSON of skills data")
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], self.data["CONFIG"]["SKILLS_JSON_FILE"])
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data should not be empty!")
            self.data["JSON"]["SKILLS_DATA"] = json_data
