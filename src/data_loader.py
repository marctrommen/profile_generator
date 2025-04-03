#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from copy import deepcopy

import logging
logger = logging.getLogger("myapp.DataLoader")


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
        self.data["JSON"]["ABOUT_DATA"] = {}
        self.data["JSON"]["HEADER_DATA"] = {}
        self.data["JSON"]["FOOTER_DATA"] = {}
        self.data["JSON"]["ALL_PROJECTS_DATA"] = {}
        self.data["JSON"]["TOP_PROJECTS_DATA"] = {}
        self.data["JSON"]["SKILLS_DATA"] = {}
        self.data["TEMPLATES"] = {}
        self._load_html_templates()
        self._load_about()
        self._load_header()
        self._load_footer()
        self._load_projects()
        self._load_skills()
        self._deepcopy_top_projects()


    # -----------------------------------------------------------------------------
    def _load_html_templates(self):
        logger.debug("Load HTML templates")

        for (file_name, template_name)  in self.data["CONFIG"]['TEMPLATE_FILES']:
            file_name = os.path.join(self.data["CONFIG"]["TEMPLATES_DIR"], file_name)
            with open(file_name, 'r') as fileObject:
                self.data["TEMPLATES"][template_name] = fileObject.read()


    # -----------------------------------------------------------------------------
    def _load_about(self):
        logger.debug("Load JSON of about data")
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], self.data["CONFIG"]["ABOUT_JSON_FILE"])
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data of about should not be empty!")
            self.data["JSON"]["ABOUT_DATA"] = json_data


    # -----------------------------------------------------------------------------
    def _load_header(self):
        logger.debug("Load JSON of header data")
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], self.data["CONFIG"]["HEADER_JSON_FILE"])
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data of header should not be empty!")
            self.data["JSON"]["HEADER_DATA"] = json_data


    # -----------------------------------------------------------------------------
    def _load_footer(self):
        logger.debug("Load JSON of footer data")
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], self.data["CONFIG"]["FOOTER_JSON_FILE"])
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data of footer should not be empty!")
            self.data["JSON"]["FOOTER_DATA"] = json_data


    # -----------------------------------------------------------------------------
    def _load_projects(self):
        logger.debug("Load JSON of all projects data")
        file_name = self.data["CONFIG"]["ALL_PROJECTS_JSON_FILE"]
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], file_name)
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data of projects should not be empty!")
            self.data["JSON"]["ALL_PROJECTS_DATA"] = json_data


    # -----------------------------------------------------------------------------
    def _deepcopy_top_projects(self):
        logger.debug("deepcopy JSON partially from all projects data")
        if "TOP_PROJECTS_NAME_LIST" in self.data["CONFIG"]:
            if len(self.data["CONFIG"]["TOP_PROJECTS_NAME_LIST"]) > 0:
                for top_project_name in self.data["CONFIG"]["TOP_PROJECTS_NAME_LIST"]:
                    self.data["JSON"]["TOP_PROJECTS_DATA"][top_project_name] = deepcopy(self.data["JSON"]["ALL_PROJECTS_DATA"][top_project_name])


    # -----------------------------------------------------------------------------
    def _load_skills(self):
        logger.debug("Load JSON of skills data")
        file_name = os.path.join(self.data["CONFIG"]["DATA_DIR"], self.data["CONFIG"]["SKILLS_JSON_FILE"])
        with open(file_name, 'r') as fileObject:
            json_data = json.load(fileObject)
            if not json_data:
                raise RuntimeError("JSON data of skills should not be empty!")
            self.data["JSON"]["SKILLS_DATA"] = json_data
