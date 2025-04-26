#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.PortfolioBuilder")


# -----------------------------------------------------------------------------
class ProjectsSectionBuilder():
    """Documentation TO BE DONE!"""    

    # -----------------------------------------------------------------------------
    def build(self, projects: dict, templates: dict, heading: str) -> str:
        """Build the project list section of the portfolio page out of the
        projects data structure.
        
        Uses the loaded HTML templates, loaded from files and puts in the 
        data from the data structure.
        
        The resulting HTML code is returned to the caller as text string.
        """
        logger.debug("build method started")

        if (projects is None or templates is None or heading == ""):
            raise ValueError("Invalid input parameters!")
        
        self.projects = projects
        self.templates = templates
        self.heading = heading

        html_items = []
        project_counter = 0
        for project in self.projects.keys():
            project_counter += 1
            html_items.append(self._build_project(project=project, 
                                            project_counter=project_counter))
        
        snippet_paramaters = dict(
            PROJECT_LIST_HEADING=self.heading,
            PROJECT_ITEM_LIST="\n".join(html_items)
        )

        html_text = self.templates["PROJECTS_TEMPLATE"].format(**snippet_paramaters)
        return html_text


    # -----------------------------------------------------------------------------
    def _build_project(self, project: str, project_counter: int) -> str:
        logger.debug("_build_project started")
        html_text = ""
        
        snippet_paramaters = dict(
            PROJECT_COUNTER=project_counter,
            PROJECT_NAME=self.projects[project]["project_name"],
            PROJECT_DESCRIPTION=self.projects[project]["project_description"],
            PROJECT_LABLE=self._lable(project=project),
            TIME_RANGE=self._time_range(project=project),
            PROJECT_COMPANY_CLIENT=self._company_client(project=project),
            PROJECT_BRANCH=self._branch(project=project),
            PROJECT_ROLES=self._roles_list(project=project),
            PROJECT_TASKS=self._tasks_list(project=project),
            PROJECT_TOOLS=self._tools_list(project=project),
            PROJECT_METHODS=self._methods_list(project=project)
        )

        html_text = self.templates["PROJECT_ITEM_TEMPLATE"].format(**snippet_paramaters)
        
        return html_text


    # -----------------------------------------------------------------------------
    def _lable(self, project: str) -> str:
        logger.debug("Build lable")
        html_text = ""

        if "project_lable" in self.projects[project]:
            snippet_parameters = dict(
                PROJECT_LABLE=self.projects[project]["project_lable"]
            )
            
            html_text = self.templates["PROJECT_ITEM_PROJECT_LABLE_TEMPLATE"].format(**snippet_parameters)

        return html_text


    # -----------------------------------------------------------------------------
    def _time_range(self, project: str) -> str:
        logger.debug("Build time range")
        time_range = ""

        if ("project_start_month" in self.projects[project]
            and "project_start_year" in self.projects[project]
            and "project_end_month" in self.projects[project]
            and "project_end_year" in self.projects[project]):
            time_range = "{month_from:02d}/{year_from} - {month_to:02d}/{year_to}".format(
                month_from=self.projects[project]["project_start_month"], 
                year_from=self.projects[project]["project_start_year"], 
                month_to=self.projects[project]["project_end_month"], 
                year_to=self.projects[project]["project_end_year"]
            )
        else:
            return ""

        snippet_parameters = dict(
            TIME_RANGE=time_range
        )
        
        html_text = self.templates["PROJECT_ITEM_TIME_RANGE_TEMPLATE"].format(**snippet_parameters)

        return html_text
    

    # -----------------------------------------------------------------------------
    def _project_description(self, project: str) -> str:
        logger.debug("Build project description")

        if "project_description" not in self.projects[project]:
            return ""
        
        return self.projects[project]["project_description"]
    

    # -----------------------------------------------------------------------------
    def _company_client(self, project: str) -> str:
        logger.debug("Build company client")

        if "project_company_client" not in self.projects[project]:
            return ""

        snippet_parameters = dict(
            PROJECT_COMPANY_CLIENT=self.projects[project]["project_company_client"]
        )

        return self.templates["PROJECT_ITEM_COMPANY_CLIENT_TEMPLATE"].format(**snippet_parameters)
    

    # -----------------------------------------------------------------------------
    def _branch(self, project: dict) -> str:
        logger.debug("Build branch")

        if "project_branch" not in self.projects[project]:
            return ""

        snippet_parameters = dict(
            PROJECT_BRANCH=self.projects[project]["project_branch"]
        )

        return self.templates["PROJECT_ITEM_BRANCH_TEMPLATE"].format(**snippet_parameters)


    # -----------------------------------------------------------------------------
    def _roles_list(self, project: dict) -> str:
        logger.debug("Build roles list")

        if "project_roles" not in self.projects[project]:
            return ""
        elif len(self.projects[project]["project_roles"]) == 0:
            return ""
        
        snippet_parameters = dict(
            PROJECT_ROLES=", ".join(self.projects[project]["project_roles"])
        )

        return self.templates["PROJECT_ITEM_ROLES_TEMPLATE"].format(**snippet_parameters)


    # -----------------------------------------------------------------------------
    def _tasks_list(self, project: dict) -> str:
        logger.debug("Build tasks list")

        if "project_tasks" not in self.projects[project]:
            return ""
        elif len(self.projects[project]["project_tasks"]) == 0:
            return ""
        
        html_items = []
        for task in self.projects[project]["project_tasks"]:
            snippet_parameters = dict(
                PROJECT_TASK=task
            )
            html_text = self.templates["PROJECT_ITEM_TASK_TEMPLATE"].format(**snippet_parameters)
            html_items.append(html_text)

        if len(html_items) == 0:
            return ""
        
        snippet_parameters = dict(
            PROJECT_TASKS="\n".join(html_items)
        )

        return self.templates["PROJECT_ITEM_TASKS_TEMPLATE"].format(**snippet_parameters)


    # -----------------------------------------------------------------------------
    def _tools_list(self, project: dict) -> str:
        logger.debug("Build tools list")

        if "project_tools" not in self.projects[project]:
            return ""
        elif len(self.projects[project]["project_tools"]) == 0:
            return ""
        
        snippet_parameters = dict(
            PROJECT_TOOLS=", ".join(self.projects[project]["project_tools"])
        )

        return self.templates["PROJECT_ITEM_TOOLS_TEMPLATE"].format(**snippet_parameters)


    # -----------------------------------------------------------------------------
    def _methods_list(self, project: dict) -> str:
        logger.debug("Build methods list")

        if "project_methods" not in self.projects[project]:
            return ""
        elif len(self.projects[project]["project_methods"]) == 0:
            return ""
        
        snippet_parameters = dict(
            PROJECT_METHODS=", ".join(self.projects[project]["project_methods"])
        )

        return self.templates["PROJECT_ITEM_METHODS_TEMPLATE"].format(**snippet_parameters)
