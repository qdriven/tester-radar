from pydantic.main import BaseModel


class GithubRepoQuery(BaseModel):
    repo_url:str

class GithubRepo(BaseModel):
    title: str
    description: str
    stars: int
    url: str
    ## TODO: unstand array type and json
    labels: list
