#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.PortfolioBuilder")

# -----------------------------------------------------------------------------
class AboutSectionBuilder():
    """Documentation TO BE DONE!"""    

    # -----------------------------------------------------------------------------
    def build(self, data: dict, templates: dict) -> str:
        """Build the about section of the portfolio page out of the
        about data structure.
        
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
        html_items = []
        for group in self.data.keys():
            if group.startswith("group_"):
                html_items.append(self._build_group(item_id=group))
            elif group.startswith("slogan"):
                html_items.append(self._build_slogan(item_id=group))
            else:
                logger.warning("unknown group item:", group)

        snippet_paramaters = dict(
            CONTENT="\n".join(html_items)
        )
        
        html_text = self.templates["ABOUT_TEMPLATE"].format(**snippet_paramaters)

        return html_text
    

    # -----------------------------------------------------------------------------
    def _build_group(self, item_id: str) -> str:
        logger.debug("_build_group started")
        html_text = ""

        snippet_paramaters = dict(
            TITLE=self.data[item_id]["title"],
            DESCRIPTION=self._description_list(item_id = item_id)
        )

        html_text = self.templates["ABOUT_GROUP_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text


    # -----------------------------------------------------------------------------
    def _build_slogan(self, item_id: str) -> str:
        logger.debug("_build_slogan started")
        html_text = ""

        snippet_paramaters = dict(
            TITLE=self.data[item_id]["title"],
            DESCRIPTION=self._description_list(item_id = item_id)
        )

        html_text = self.templates["ABOUT_SLOGAN_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text


    # -----------------------------------------------------------------------------
    def _description_list(self, item_id: str) -> str:
        logger.debug("_description_list started")

        html_items = []
        for item in self.data[item_id]["description_list"]:
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
