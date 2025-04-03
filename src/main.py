#!/usr/bin/env python
# -*- coding: utf-8 -*-


import config
from data_loader import DataLoader
from portfolio_builder import PortfolioBuilder
from skills_section_builder import SkillsSectionBuilder
from projects_section_builder import ProjectsSectionBuilder
from header_section_builder import HeaderSectionBuilder
from about_section_builder import AboutSectionBuilder
from footer_section_builder import FooterSectionBuilder
from app import Application

import logging
from logging_config import setup_logging
setup_logging()

logger = logging.getLogger("myapp")


# -----------------------------------------------------------------------------
def main() -> None:
    """Main function to run the application.
    """
    configuration = config.configuration()
    data_loader = DataLoader()
    portfolio_builder = PortfolioBuilder()
    header_section_builder = HeaderSectionBuilder()
    about_section_builder = AboutSectionBuilder()
    footer_section_builder = FooterSectionBuilder()
    skills_section_builder = SkillsSectionBuilder()
    projects_section_builder = ProjectsSectionBuilder()
    application = Application(configuration = configuration, 
                              data_loader = data_loader, 
                              portfolio_builder = portfolio_builder, 
                              header_section_builder = header_section_builder,
                              about_section_builder = about_section_builder,
                              footer_section_builder = footer_section_builder,
                              projects_section_builder = projects_section_builder, 
                              skills_section_builder = skills_section_builder)
    application.run()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    logger.info("Application started.")
    main()
    logger.info("Application finished")
