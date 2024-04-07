from pytest_mock import MockerFixture

from leetcode_make_tests.api import LeetCodeAPI
from leetcode_make_tests.models.api import LeetCodeAPIResponse


def test_get_problem_success(mocker: MockerFixture) -> None:
    """Test the successful exec of get_problem method."""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "consolePanelConfig": {
                "questionId": "123456",
                "questionFrontendId": "1",
                "questionTitle": "__TITLE__",
                "enableDebugger": True,
                "enableRunCode": True,
                "enableSubmit": True,
                "enableTestMode": False,
                "exampleTestcaseList": [
                    "__CASE_1__",
                    "__CASE_2__",
                    "__CASE_3__",
                    "__CASE_4__",
                ],
                "metaData": "__METADATA__",
            },
            "questionContent": {
                "content": "__CONTENT__",
                "mysqlSchemas": [],
                "dataSchemas": [],
            },
        },
    }
    mocker.patch("requests.post", return_value=mock_response)

    result = LeetCodeAPI.get_problem("__TITLE_SLUG__")

    assert result == LeetCodeAPIResponse(
        question_id=123456,
        title_slug="__TITLE_SLUG__",
        title="__TITLE__",
        description="__CONTENT__",
        test_cases=["__CASE_1__", "__CASE_2__", "__CASE_3__", "__CASE_4__"],
        metadata="__METADATA__",
    )


def test_get_problem_doesnt_exist(mocker: MockerFixture) -> None:
    """Test case for non-existent problem."""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {"consolePanelConfig": None, "questionContent": None},
    }
    mocker.patch("requests.post", return_value=mock_response)

    result = LeetCodeAPI.get_problem("adadadssasd")

    assert result is None
