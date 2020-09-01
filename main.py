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
from starlette.middleware.cors import CORSMiddleware

from app.endpoints.api import api_router

app = FastAPI(
    title="test-radar", openapi_url=f"/openapi.json"
)

app.include_router(api_router, prefix="/radar")
