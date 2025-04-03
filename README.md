# Profile Page Generator

Generator written in Python to build up a static HTML webpage.
The webpage represents a profile page for job application purposes.

The data for the sections *skills* and *project list* of the webpage
is stored as JSON data files. These JSON data files are read from the
generator and transformed with standard Python string formatting
into the static HTML webpage.


## Get Started

Adjust configuration and data files to your local conditions. For that,
copy ...

```
project_root
├── data
│   ├── about_template.json            ──> about.json 
│   ├── all_project_list_template.json ──> all_project_list.json
│   ├── footer_template.json           ──> footer.json
│   ├── header_template.json           ──> header.json
│   └── skills_template.json           ──> skills.json
└── src
    └── config_template.py             ──> config.py 
```



## Credits

Thanks to [Hints on Profilepage Creation](https://www.youtube.com/watch?v=X9l2SooDlck) and [AI Background Remover](https://removal.ai/) for images.
