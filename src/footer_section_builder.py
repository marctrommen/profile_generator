#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.PortfolioBuilder")


# -----------------------------------------------------------------------------
class FooterSectionBuilder():
    """Documentation TO BE DONE!"""    

    # -----------------------------------------------------------------------------
    def build(self, data: dict, templates: dict, datetime = str) -> str:
        """Build the footer section of the portfolio page out of the
        footer data structure.
        
        Uses the loaded HTML templates, loaded from files and puts in the 
        data from the data structure.
        
        The resulting HTML code is returned to the caller as text string.
        """
        logger.debug("build method started")

        if (data is None or templates is None or datetime == ""):
            raise ValueError("Invalid input parameters!")

        html_text = ""
        
        snippet_paramaters = dict(
            MAIL_ADDRESS=data["mail_address"],
            LINKEDIN_URL=data["linkedin_url"],
            POSTAL_ADDRESS=data["postal_address"],
            GOOGLE_MAPS_URL=data["google_maps_url"],
            GITHUB_URL=data["github_url"],
            GENERATED_DATETIME=datetime
        )

        html_text = templates["FOOTER_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text
