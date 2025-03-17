#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import init
import os
import shutil
import json

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
def _load_templates():
    print("Load HTML templates")
    for (file_name, template_name)  in data["CONFIG"]['TEMPLATE_FILES']:
        file_name = os.path.join(data["CONFIG"]["TEMPLATES_DIR"], file_name)
        with open(file_name, 'r') as fileObject:
            data[template_name] = fileObject.read()


# -----------------------------------------------------------------------------
def _load_projects(all_projects:bool):
    print("Load JSON of", ("all" if all_projects else "top"), "projects data")
    if all_projects:
        file_name = data["CONFIG"]["ALL_PROJECTS_JSON_FILE"]
    else:
        file_name = data["CONFIG"]["TOP_PROJECTS_JSON_FILE"]
    file_name = os.path.join(data["CONFIG"]["DATA_DIR"], file_name)
    with open(file_name, 'r') as fileObject:
        json_data = json.load(fileObject)
        if not json_data:
            raise RuntimeError("JSON data should not be empty!")
        if all_projects:
            data["ALL_PROJECTS_DATA"] = json_data
        else:
            data["TOP_PROJECTS_DATA"] = json_data


# -----------------------------------------------------------------------------
def _load_skills():
    print("Load JSON of skills data")
    file_name = os.path.join(data["CONFIG"]["DATA_DIR"], data["CONFIG"]["SKILLS_JSON_FILE"])
    with open(file_name, 'r') as fileObject:
        json_data = json.load(fileObject)
        if not json_data:
            raise RuntimeError("JSON data should not be empty!")
        data["SKILLS_DATA"] = json_data


# -----------------------------------------------------------------------------
def _handle_project_list(all_projects:bool):
    print("handle project list of", ("all" if all_projects else "top"), "projects data")
    if all_projects:
        project_list = data["ALL_PROJECTS_DATA"]
    else:
        project_list = data["TOP_PROJECTS_DATA"]

    for project_item in project_list:
        

# -----------------------------------------------------------------------------
def main():
    print("Main")
    _init()
    _clean()
    _load_templates()
    _load_projects(all_projects=True)
    _load_projects(all_projects=False)
    _load_skills()


# -----------------------------------------------------------------------------
# do the build process
if __name__ == '__main__':
    main()
