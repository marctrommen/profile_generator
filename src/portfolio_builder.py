#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.PortfolioBuilder")

from projects_section_builder import ProjectsSectionBuilder
from skills_section_builder import SkillsSectionBuilder


class PortfolioBuilder:
    """
    Build the portfolio from the data structure.
    Uses the 'data' as data structure from the config file to build the portfolio.
    """


    # -----------------------------------------------------------------------------
    def build(self, data:dict, 
              projects_section_builder:ProjectsSectionBuilder, 
              skills_section_builder:SkillsSectionBuilder):
        """
        Public Method as entry point to build the portfolio from the data structure.
        Internally the main page, about section, skills section, top projects section, 
        all projects section, project task and skill item are built in this sequence.
        """
        logger.debug("Build portfolio")
        if (data == None or 
            projects_section_builder == None or 
            skills_section_builder == None):
            raise ValueError("Invalid input parameters!")
        
        self.data = data
        self.data["HTML"] = {}
        self.projects_section_builder = projects_section_builder
        self.skills_section_builder = skills_section_builder

        self._build_projects_sections()
        self._build_skills_section()
        self._build_main_page()


    # -----------------------------------------------------------------------------
    def _build_projects_sections(self):
        logger.debug("Build projects sections")

        has_top_projects = False
        if "TOP_PROJECTS_DATA" in self.data["JSON"]:
            project_list = self.data["JSON"]["TOP_PROJECTS_DATA"]
            html_text = ""
            if len(project_list) > 0:
                html_text = self.projects_section_builder.build(
                    projects=project_list, 
                    templates=self.data["TEMPLATES"], 
                    heading="Meine Top 3 Projekte"
                )

                if html_text != "":
                    has_top_projects = True
                    self.data["HTML"]["TOP_PROJECTS_SECTION"] = html_text
        
        if not has_top_projects:
            raise Exception("Top projects data is empty")

        has_all_projects = False
        if "ALL_PROJECTS_DATA" in self.data["JSON"]:
            project_list = self.data["JSON"]["ALL_PROJECTS_DATA"]
            html_text = ""
            if len(project_list) > 0:
                html_text = self.projects_section_builder.build(
                    projects=project_list, 
                    templates=self.data["TEMPLATES"], 
                    heading="Meine Projekte"
                )

                if html_text != "":
                    has_all_projects = True
                    self.data["HTML"]["ALL_PROJECTS_SECTION"] = html_text
            
        if not has_all_projects:
            raise Exception("Top projects data is empty")
    

    # -----------------------------------------------------------------------------
    def _build_skills_section(self):
        logger.debug("Build skills section")

        has_skills = False
        if "TOP_PROJECTS_DATA" in self.data["JSON"]:
            skill_groups = self.data["JSON"]["SKILLS_DATA"]
            html_text = ""
            if len(skill_groups.keys()) > 0:
                html_text = self.skills_section_builder.build(
                    skill_groups=skill_groups, 
                    templates=self.data["TEMPLATES"]
                )

                if html_text != "":
                    has_skills = True
                    self.data["HTML"]["SKILLS_SECTION"] = html_text
        
        if not has_skills:
            raise Exception("Skills data is empty")


    # -----------------------------------------------------------------------------
    def _build_main_page(self):
        logger.debug("Build main page")

        if not "TOP_PROJECTS_SECTION" in self.data["HTML"]:
            raise Exception("Top projects section is missing")
        
        if not "ALL_PROJECTS_SECTION" in self.data["HTML"]:
            raise Exception("All projects section is missing")
        
        if not "SKILLS_SECTION" in self.data["HTML"]:
            raise Exception("Skills section is missing")
        
        if not "ABOUT_TEMPLATE" in self.data["TEMPLATES"]:
            raise Exception("About section is missing")
        
        snippet_paramaters = dict(
            ABOUT_SECTION=self.data["TEMPLATES"]["ABOUT_TEMPLATE"],
            SKILLS_SECTION=self.data["HTML"]["SKILLS_SECTION"],
            TOP_PROJECTS_SECTION=self.data["HTML"]["TOP_PROJECTS_SECTION"],
            ALL_PROJECTS_SECTION=self.data["HTML"]["ALL_PROJECTS_SECTION"]
        )

        self.data["HTML"]["PORTFOLIO"] = self.data["TEMPLATES"]["MAIN_TEMPLATE"].format(**snippet_paramaters)
