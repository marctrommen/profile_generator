#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.Application")

import os
import shutil
from data_loader import DataLoader
from portfolio_builder import PortfolioBuilder
from skills_section_builder import SkillsSectionBuilder
from projects_section_builder import ProjectsSectionBuilder

class Application:
    """
    Application class to run the build process.
    """

    # -----------------------------------------------------------------------------
    def __init__(self, 
                 configuration: dict, 
                 data_loader: DataLoader, 
                 portfolio_builder: PortfolioBuilder, 
                 projects_section_builder: ProjectsSectionBuilder,
                 skills_section_builder: SkillsSectionBuilder):
        if (configuration == None or
            data_loader == None or
            portfolio_builder == None or
            projects_section_builder == None or
            skills_section_builder == None):
            raise ValueError("Invalid input parameters!")
        
        self.data = {}
        self.data["CONFIG"] = configuration
        self.data_loader = data_loader
        self.portfolio_builder = portfolio_builder
        self.projects_section_builder = projects_section_builder
        self.skills_section_builder = skills_section_builder


    # -----------------------------------------------------------------------------
    def run(self):
        logger.debug("run application")
        self._clean_and_copy_static_files()
        self._load_data_from_files()
        self._build_portfolio_page()
        self._save_portfolio_page()


    # -----------------------------------------------------------------------------
    def _clean_and_copy_static_files(self):
        logger.debug("Cleaning build directory")
        shutil.rmtree(self.data["CONFIG"]["BUILD_OUT_DIR"], ignore_errors=True)
        os.makedirs(self.data["CONFIG"]["BUILD_OUT_DIR"])

        # copy page.css file if any exists
        filepath = os.path.join(self.data["CONFIG"]['TEMPLATES_DIR'], 'style.css')
        if os.path.exists(filepath):
            shutil.copy(filepath, self.data["CONFIG"]["BUILD_OUT_DIR"])

        # copy image file if any exists
        filepath = os.path.join(self.data["CONFIG"]['TEMPLATES_DIR'], 'marcus_wo_background.png')
        if os.path.exists(filepath):
            shutil.copy(filepath, self.data["CONFIG"]["BUILD_OUT_DIR"])


    # -----------------------------------------------------------------------------
    def _load_data_from_files(self):
        logger.debug("Load data from files")
        self.data_loader.load_data(data = self.data)


    # -----------------------------------------------------------------------------
    def _build_portfolio_page(self):
        logger.debug("Build portfolio page")
        self.portfolio_builder.build(data=self.data,
                                     projects_section_builder=self.projects_section_builder,
                                     skills_section_builder=self.skills_section_builder)
        if not "HTML" in self.data:
            raise RuntimeError("No HTML generated for portfolio page")

        
    # -----------------------------------------------------------------------------
    def _save_portfolio_page(self):
        logger.debug("Save portfolio page")
        has_file_written = False    
        if "HTML" in self.data:
            if "PORTFOLIO" in self.data["HTML"]:
                file_name = os.path.join(self.data["CONFIG"]["BUILD_OUT_DIR"], "portfolio.html")
                with open(file_name, 'w') as fileObject:
                    fileObject.write(self.data["HTML"]["PORTFOLIO"])
                    has_file_written = True
        if not has_file_written:
            raise RuntimeError("Portfolio page not written to file!")
