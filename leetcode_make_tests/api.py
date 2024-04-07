"""LeetCode GraphQL API client."""

import requests

from leetcode_make_tests.models.api import LeetCodeAPIResponse

GRAPHQL_PROBLEM_QUERY = """\
query ProblemQuery($titleSlug: String!) {
  consolePanelConfig: question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    enableDebugger
    enableRunCode
    enableSubmit
    enableTestMode
    exampleTestcaseList
    metaData
  }
  questionContent: question(titleSlug: $titleSlug) {
    content
    mysqlSchemas
    dataSchemas
  }
}
"""


class LeetCodeAPI:
    """A client for interacting with the LeetCode API."""

    @staticmethod
    def get_problem(title_slug: str) -> LeetCodeAPIResponse | None:
        """Get information about problem.

        Args
        ----
            title_slug: text ID of the LeetCode problem.

        Returns
        -------
            LeetCodeAPIResponse
        """
        r = requests.post(
            "https://leetcode.com/graphql",
            json={
                "query": GRAPHQL_PROBLEM_QUERY,
                "variables": {"titleSlug": title_slug},
            },
            timeout=10,
        ).json()["data"]

        console_panel_config = r["consolePanelConfig"]
        question_content = r["questionContent"]

        if console_panel_config is None or question_content is None:
            return None

        return LeetCodeAPIResponse(
            question_id=int(console_panel_config["questionId"]),
            title_slug=title_slug,
            title=console_panel_config["questionTitle"],
            description=question_content["content"],
            test_cases=console_panel_config["exampleTestcaseList"],
            metadata=console_panel_config["metaData"],
        )
