from app.github.service.gh_service import get_github_repo_info


class TestGithubService:
    def test_get_github_repo_info(self):
       repo= get_github_repo_info("qdriven/tester-radar")
       print(repo)