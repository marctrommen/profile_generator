#!/usr/bin/env python
# -*- coding: utf-8 -*-

from projects_section_builder import ProjectsSectionBuilder
from skills_section_builder import SkillsSectionBuilder
from header_section_builder import HeaderSectionBuilder
from about_section_builder import AboutSectionBuilder
from footer_section_builder import FooterSectionBuilder


import logging
logger = logging.getLogger("myapp.PortfolioBuilder")


# -----------------------------------------------------------------------------
class PortfolioBuilder:
    """
    Build the portfolio from the data structure.
    Uses the 'data' as data structure from the config file to build the portfolio.
    """


    # -----------------------------------------------------------------------------
    def build(self, data:dict,
              header_section_builder:HeaderSectionBuilder,
              about_section_builder:AboutSectionBuilder,
              projects_section_builder:ProjectsSectionBuilder, 
              skills_section_builder:SkillsSectionBuilder,
              footer_section_builder:FooterSectionBuilder):
        """
        Public Method as entry point to build the portfolio from the data structure.
        Internally the main page, about section, skills section, top projects section, 
        all projects section, project task and skill item are built in this sequence.
        """
        logger.debug("Build portfolio")
        if (data is None or 
            header_section_builder is None or
            about_section_builder is None or
            projects_section_builder is None or 
            skills_section_builder is None or
            footer_section_builder is None):
            raise ValueError("Invalid input parameters!")
        
        self.data = data
        self.data["HTML"] = {}
        self.header_section_builder = header_section_builder
        self.about_section_builder = about_section_builder
        self.projects_section_builder = projects_section_builder
        self.skills_section_builder = skills_section_builder
        self.footer_section_builder = footer_section_builder

        self._build_header_section()
        self._build_about_section()
        self._build_footer_section()
        self._build_projects_sections()
        self._build_skills_section()
        self._build_main_page()


    # -----------------------------------------------------------------------------
    def _build_header_section(self):
        logger.debug("Build header section")

        if "HEADER_DATA" in self.data["JSON"]:
            html_text = self.header_section_builder.build(
                    data=self.data["JSON"]["HEADER_DATA"], 
                    templates=self.data["TEMPLATES"]
            )
            self.data["HTML"]["HEADER_SECTION"] = html_text
        

    # -----------------------------------------------------------------------------
    def _build_about_section(self):
        logger.debug("Build about section")

        if "ABOUT_DATA" in self.data["JSON"]:
            html_text = self.about_section_builder.build(
                    data=self.data["JSON"]["ABOUT_DATA"], 
                    templates=self.data["TEMPLATES"]
            )
            self.data["HTML"]["ABOUT_SECTION"] = html_text
        

    # -----------------------------------------------------------------------------
    def _build_footer_section(self):
        logger.debug("Build footer section")

        if "FOOTER_DATA" in self.data["JSON"]:
            html_text = self.footer_section_builder.build(
                    data=self.data["JSON"]["FOOTER_DATA"], 
                    templates=self.data["TEMPLATES"],
                    datetime=self.data["CONFIG"]["GENERATED_DATETIME_HUMAN_READABLE"]
            )
            self.data["HTML"]["FOOTER_SECTION"] = html_text
        

    # -----------------------------------------------------------------------------
    def _build_projects_sections(self):
        logger.debug("Build projects sections")

        self.data["HTML"]["TOP_PROJECTS_SECTION"] = ""
        self.data["HTML"]["ALL_PROJECTS_SECTION"] = ""
        self.data["HTML"]["REFERTO_SECTION"] = ""

        if self.data["CONFIG"]["HAS_REFERTO_SECTION"]:
            if "TOP_PROJECTS_DATA" in self.data["JSON"]:
                project_list = self.data["JSON"]["TOP_PROJECTS_DATA"]
                html_text = ""
                if len(project_list) > 0:
                    html_text = self.projects_section_builder.build(
                        projects=project_list, 
                        templates=self.data["TEMPLATES"], 
                        heading="Meine Top Projekte",
                        prologue_text=self.data["CONFIG"]["TOP_PROJECTS_PROLOGUE_TEXT"]
                    )

            self.data["HTML"]["TOP_PROJECTS_SECTION"] = html_text

            self._build_referto_section()
        else:
            if "ALL_PROJECTS_DATA" in self.data["JSON"]:
                project_list = self.data["JSON"]["ALL_PROJECTS_DATA"]
                html_text = ""
                if len(project_list) > 0:
                    html_text = self.projects_section_builder.build(
                        projects=project_list, 
                        templates=self.data["TEMPLATES"], 
                        heading="Meine Projekte",
                        prologue_text=self.data["CONFIG"]["ALL_PROJECTS_PROLOGUE_TEXT"]
                    )
                self.data["HTML"]["ALL_PROJECTS_SECTION"] = html_text
            

    # -----------------------------------------------------------------------------
    def _build_referto_section(self):
        logger.debug("Build referto section")

        snippet_paramaters = dict(
            REFERTO_SECTION_LINK=self.data["CONFIG"]["REFERTO_SECTION_LINK"]
        )

        self.data["HTML"]["REFERTO_SECTION"] = self.data["TEMPLATES"]["REFERTO_TEMPLATE"].format(**snippet_paramaters)
        


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
                    prologue_text=self.data["CONFIG"]["SKILLS_PROLOGUE_TEXT"],
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

        if "HEADER_SECTION" not in self.data["HTML"]:
            raise Exception("Header section is missing")
        
        #if "TOP_PROJECTS_SECTION" not in self.data["HTML"]:
        #    raise Exception("Top projects section is missing")
        
        #if "ALL_PROJECTS_SECTION" not in self.data["HTML"]:
        #    raise Exception("All projects section is missing")
        
        if "SKILLS_SECTION" not in self.data["HTML"]:
            raise Exception("Skills section is missing")
        
        if "ABOUT_SECTION" not in self.data["HTML"]:
            raise Exception("About section is missing")
        
        if "FOOTER_SECTION" not in self.data["HTML"]:
            raise Exception("Footer section is missing")

        snippet_paramaters = dict(
            META_TITLE=self.data["JSON"]["HEADER_DATA"]["meta_title"],
            META_DESCRIPTION=self.data["JSON"]["HEADER_DATA"]["meta_description"],
            META_KEYWORDS=self.data["JSON"]["HEADER_DATA"]["meta_keywords"],
            META_AUTHOR=self.data["JSON"]["HEADER_DATA"]["meta_author"],
            HEADER_SECTION=self.data["HTML"]["HEADER_SECTION"],
            ABOUT_SECTION=self.data["HTML"]["ABOUT_SECTION"],
            SKILLS_SECTION=self.data["HTML"]["SKILLS_SECTION"],
            TOP_PROJECTS_SECTION=self.data["HTML"]["TOP_PROJECTS_SECTION"],
            ALL_PROJECTS_SECTION=self.data["HTML"]["ALL_PROJECTS_SECTION"],
            REFERTO_SECTION=self.data["HTML"]["REFERTO_SECTION"],
            FOOTER_SECTION=self.data["HTML"]["FOOTER_SECTION"]
        )

        self.data["HTML"]["PORTFOLIO"] = self.data["TEMPLATES"]["MAIN_TEMPLATE"].format(**snippet_paramaters)
