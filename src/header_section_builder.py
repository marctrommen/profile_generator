#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.PortfolioBuilder")


# -----------------------------------------------------------------------------
class HeaderSectionBuilder():
    """Documentation TO BE DONE!"""    

    # -----------------------------------------------------------------------------
    def build(self, data: dict, templates: dict) -> str:
        """Build the header section of the portfolio page out of the
        header data structure.
        
        Uses the loaded HTML templates, loaded from files and puts in the 
        data from the data structure.
        
        The resulting HTML code is returned to the caller as text string.
        """
        logger.debug("build method started")

        if (data is None or templates is None):
            raise ValueError("Invalid input parameters!")
        
        self.data = data
        self.templates = templates

        html_text = ""
        
        snippet_paramaters = dict(
            HEADER_LOGO=self.data["header_logo"],
            HEADER_LOGO_ALT=self.data["header_logo_alt"],
            HEADER_TITLE=self.data["header_title"],
            HEADER_SUBTITLE=self.data["header_subtitle"],
            HEADER_ITEM_LIST=self._description_list(),
            HEADER_CV_FILE=self.data["header_cv_file"]
        )

        html_text = self.templates["HEADER_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text


    # -----------------------------------------------------------------------------
    def _description_list(self) -> str:
        logger.debug("Build description list")

        if "header_description_list" not in self.data:
            return ""
        elif len(self.data["header_description_list"]) == 0:
            return ""
        
        html_items = []
        for item in self.data["header_description_list"]:
            snippet_parameters = dict(
                ITEM=item
            )
            html_text = self.templates["ITEM_TEMPLATE"].format(**snippet_parameters)
            html_items.append(html_text)

        if len(html_items) == 0:
            return ""
        
        snippet_parameters = dict(
            ITEM_LIST="\n".join(html_items)
        )

        return self.templates["ITEM_LIST_TEMPLATE"].format(**snippet_parameters)
