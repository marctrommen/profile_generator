#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import init
import os
import shutil
import json
from data_loader import DataLoader

# -----------------------------------------------------------------------------
# initialize main's data structure
data = {}

# -----------------------------------------------------------------------------
def _init():
    print("Initialize application")
    data["CONFIG"] = init()
    if not data["CONFIG"]:
        raise RuntimeError("config data should not be empty!")


# -----------------------------------------------------------------------------
def _clean():
    print("Cleaning build directory")
    shutil.rmtree(data["CONFIG"]["BUILD_OUT_DIR"], ignore_errors=True)
    os.makedirs(data["CONFIG"]["BUILD_OUT_DIR"])


# -----------------------------------------------------------------------------
def _load_data_from_files():
    print("Load data from files")
    loader = DataLoader()
    loader.load_data(data)

# -----------------------------------------------------------------------------
def _handle_project_list(all_projects:bool):
    print("handle project list of", ("all" if all_projects else "top"), "projects data")
    if all_projects:
        project_list = data["ALL_PROJECTS_DATA"]
    else:
        project_list = data["TOP_PROJECTS_DATA"]

    for project_item in project_list:
        html = _handle_project_item(item=project_item)

# -----------------------------------------------------------------------------
def _handle_project_item(item):
    print("handle project item")
    html = ""
    time_range = "{month_from:02d}/{year_from} - {month_to:02d}/{year_to}".format(
        month_from=item["project_start_month"], 
        year_from=item["project_start_year"], 
        month_to=item["project_end_month"], 
        year_to=item["project_end_year"]
    )

    snippet_parameters = dict(
        TIME_RANGE=time_range,

        project_name=item["project_name"],
        project_description=item["project_description"],
        project_link=item["project_link"],
        project_image=item["project_image"],
        project_technologies=item["project_technologies"],
        project_tasks=item["project_tasks"]
    )
    
    html = data["PROJECT_TASK_TEMPLATE"].format(**snippet_parameters)

    return html


# -----------------------------------------------------------------------------
def main():
    print("Main")
    _init()
    _clean()
    _load_data_from_files()


# -----------------------------------------------------------------------------
# do the build process
if __name__ == '__main__':
    main()
