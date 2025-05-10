#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.SkillsSectionBuilder")


# -----------------------------------------------------------------------------
class SkillsSectionBuilder:
    """Documentation TO BE DONE!"""

    # -----------------------------------------------------------------------------
    def build(self, skill_groups: dict, prologue_text: str, templates: dict):
        """Build the skills list section of the portfolio page out of the
        skills data structure.
        
        Uses the loaded HTML templates, loaded from files and puts in the 
        data from the data structure.
        
        The resulting HTML code is returned to the caller as text string.
        """
        logger.debug("build method started")

        if (skill_groups is None or prologue_text == "" or templates is None):
            raise ValueError("Invalid input parameters!")
        
        self.skill_groups = skill_groups
        self.templates = templates
        self.prologue_text = prologue_text

        html_items = []
        for skill_group in self.skill_groups.keys():
            html_items.append(self._build_skill_group(skill_group))

        if len(html_items) == 0:
            return ""

        snippet_paramaters = dict(
            SKILLS_GROUP_LIST="\n".join(html_items),
            SKILLS_PROLOGUE_TEXT=self.prologue_text
        )

        html_text = self.templates["SKILLS_TEMPLATE"].format(**snippet_paramaters)

        return html_text


    # -----------------------------------------------------------------------------
    def _build_skill_group(self, skill_group : str):
        logger.debug("_build_skill_group()")
        html_items = []
        
        for skill in self.skill_groups[skill_group].keys():
            skill_value = self.skill_groups[skill_group][skill]
            if skill_value == 1:
                template_name = "SKILLS_GROUP_ITEM_ONE_DOT_TEMPLATE"
            elif skill_value == 2:
                template_name = "SKILLS_GROUP_ITEM_TWO_DOTS_TEMPLATE"
            elif skill_value == 3:
                template_name = "SKILLS_GROUP_ITEM_THREE_DOTS_TEMPLATE"
            else:
                raise ValueError("Invalid skill value!")
            
            snippet_parameters = dict(
                SKILL_NAME=skill
            )
            
            html_items.append(self.templates[template_name].format(**snippet_parameters))

        if len(html_items) == 0:
            return ""
        
        snippet_paramaters = dict(
            SKILL_GROUPNAME=skill_group,
            SKILL_ITEM_LIST="\n".join(html_items)
        )

        html_text = self.templates["SKILLS_GROUP_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text
    