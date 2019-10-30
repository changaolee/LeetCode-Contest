import os
import sys
import json
import requests
import html2text


class LeetCode(object):
    CONTEST_URL = "https://leetcode-cn.com/contest/api/info/{}"
    PROBLEM_URL = "https://leetcode-cn.com/contest/{}/problems/{}"
    PROBLEM_DATA_URL = "https://leetcode-cn.com/graphql"

    _contest_name = None
    _contest_directory_name = None

    def __init__(self, contest_type, number):
        self._contest_name, self._contest_directory_name = self._get_contest_name(contest_type, number)

    def save(self, problems):
        """ 题目存入文件 """
        os.makedirs(self._contest_directory_name, exist_ok=True)
        for i, problem in enumerate(problems):
            with open("{}/【{}】{}.md".format(
                    self._contest_directory_name, chr(ord('A') + i), problem["title"]), "w"
            ) as file:
                file.write(problem["content"])
                print("saved {}.".format(problem["title"]))

    def get_problems(self):
        """ 获取题目列表数据 """
        slugs = self._get_problem_slugs()

        result = []
        for slug in slugs:
            result.append(self._get_problem_detail(slug))

        return result

    def _get_problem_detail(self, slug):
        """ 获取题目详情 """
        params = {
            "operationName": "questionData",
            "variables": {
                "titleSlug": slug
            },
            "query": """
                query questionData($titleSlug: String!) {
                    question(titleSlug: $titleSlug) {
                        questionFrontendId
                        translatedTitle
                        translatedContent
                        difficulty
                    }
                }
            """
        }

        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Referer': self.PROBLEM_URL.format(self._contest_name, slug)
        }

        resp = requests.post(
            self.PROBLEM_DATA_URL,
            data=json.dumps(params),
            headers=headers,
            timeout=10
        ).json()

        data = resp["data"]["question"]
        content = resp["data"]["question"]["translatedContent"]
        title = data["translatedTitle"]
        id_title = "{}. {}".format(data["questionFrontendId"], title)

        problem_detail = {
            "id": data["questionFrontendId"],
            "title": title,
            "content": self._format_content(id_title, content, slug)
        }

        return problem_detail

    def _get_problem_slugs(self):
        """ 获取题目标题 slug 列表 """
        data = requests.get(self.CONTEST_URL.format(self._contest_name)).json()

        slugs = []
        for question in data["questions"]:
            slugs.append(question["title_slug"])
        return slugs

    @staticmethod
    def _get_contest_name(contest_type, number):
        """ 获取比赛名称 """
        if contest_type == "weekly":
            contest = "weekly-contest-{}".format(number)
            contest_directory = "Weekly-Contest-{}".format(number)
        elif contest_type == "biweekly":
            contest = "biweekly-contest-{}".format(number)
            contest_directory = "Biweekly-Contest-{}".format(number)
        else:
            raise ValueError("error contest type !!!")

        return contest, contest_directory

    def _format_content(self, title, content, slug):
        for text in ["输入", "输出", "解释"]:
            content = content.replace("<strong>{}：</strong>".format(text), "{}：".format(text))
        content = html2text.html2text(content)

        lines = [
            "> *题目原链接：[{}]({})*".format(title, self.PROBLEM_URL.format(self._contest_name, slug)),
            "### 题目",
            content,
            "### 解析",
            "### 代码"
        ]
        return "\n\n".join(lines)


def main(argv):
    leetcode = LeetCode(argv[0], argv[1])
    problems = leetcode.get_problems()
    leetcode.save(problems)


if __name__ == "__main__":
    if len(sys.argv[1:]) == 2:
        main(sys.argv[1:])
    else:
        print("Usage: init_contest.py <weekly/biweekly> <number>")
