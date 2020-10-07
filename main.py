#
# from fastapi import FastAPI
#
# from app.schemas.gh_schemas import RadarGithubRepo
# from app.service import gh_service
#
# app = FastAPI()
#
#
# @app.get("/github", response_model=RadarGithubRepo)
# def get_github_repo_status(repo_name: str):
#     return gh_service.get_github_repo_info(repo_name)


from fastapi import FastAPI

from app.github.endpoints import gh_api_router
from app.maven.maven_endpoints import maven_router

app = FastAPI(
    title="test-radar", openapi_url=f"/openapi.json"
)

app.include_router(gh_api_router, prefix="/radar")
app.include_router(maven_router,prefix="/maven")
