from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)
        # Muodosta Project-olio datasta
        return Project(
        data["tool"]["poetry"]["name"],
        data["tool"]["poetry"]["description"],
        list(data["tool"]["poetry"]["dependencies"].keys()),
        list(data["tool"]["poetry"]["dependencies"].keys())
    )