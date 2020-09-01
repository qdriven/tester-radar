
from github.Repository import Repository
from pydantic.main import BaseModel


class GithubRepoQuery(BaseModel):
    repo_url: str


class GithubRepo(BaseModel):
    title: str
    description: str
    stars: int
    url: str
    ## TODO: unstand array type and json
    labels: list


class RadarGithubRepo(BaseModel):
    name: str
    url: str
    stars: int
    topics: list
    desc: str
    forks: int
    languages: dict

    @staticmethod
    def from_gh_repo(gh_repo: Repository):
        return RadarGithubRepo(name=gh_repo.full_name,
                               url=gh_repo.html_url,
                               stars=gh_repo.stargazers_count,
                               desc=gh_repo.description, topics=gh_repo.get_topics(),
                               forks=gh_repo.forks_count,
                               languages=gh_repo.get_languages())
    #
    # def to_json(self):
    #     return json.dumps(self.__dict__)
    #
    # def to_dict(self):
    #     return self.__dict__
