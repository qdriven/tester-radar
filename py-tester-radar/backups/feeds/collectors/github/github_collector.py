# # -*- coding:utf-8 -*-
# #
# #   Author  :  patrick
# #   Date    :  2020/2/16
# #   Desc    :  Collect Different Github Inforamtion
# import datetime
# import json
# import logging
# import time
#
# import yaml
# from requests_html import HTMLSession
#
# from collectors.collector_decorator import update_git, commit_git_decorator
# from collectors.collectors import BaseCollector
#
# GIT_URL = "https://github.com/"
# GITHUB_SEARCH_URL = "https://github.com/search?q="
#
#
# class GithubTopicCollector(BaseCollector):
#
#     def __init__(self, topic):
#         super(GithubTopicCollector, self).__init__(base_url=GITHUB_SEARCH_URL)
#         self.topic = topic
#         self.saved_file = 'topic/{date}_topic_{topic}_.json'.format(date=str(datetime.date.today()),
#                                                                     topic=self.topic)
#         self.data = {self.topic: []}
#         self.pages = 10
#         self.type_query = "type=Repositories"
#
#     def fetch_data(self):
#         session = HTMLSession()
#         for page in range(self.pages):
#             time.sleep(2)
#             response = session.get(
#                 self.base_url + "topic:" + self.topic + "&" + "p=" + str(page + 1) + "&" + self.type_query,
#                 headers=self.HEADERS)
#             repo_items = response.html.find(".repo-list-item")
#             for item in repo_items:
#                 self.logger.info(item.text)
#                 try:
#                     raw_repo_desc = item.text
#                     parsed_content = raw_repo_desc.split("\n")
#                     result = dict()
#                     result["url"] = GIT_URL + parsed_content[0].replace(" ", "")
#                     result["summary"] = "".join(parsed_content[1:4])
#                     result["stars"] = item.find('.muted-link')[0].text
#                 except Exception as e:
#                     print(e)
#                 self.data[self.topic].append(result)
#                 if len(repo_items) < 10:
#                     break
#         return self.data
#
#     def write_to_json_file(self):
#         with open(self.saved_file, 'w') as f:
#             json.dump(self.data, f, ensure_ascii=False)
#
#     def fetch_to_file(self):
#         self.fetch_data()
#         self.write_to_json_file()
#
#
# class GithubTrendingCollector(BaseCollector):
#     """
#     example content:
#     'Star
#     jackzhenguo / python-small-examples
#     Python有趣的小例子一网打尽。Python基础、Python坑点、Python字符串和正则、Python绘图、Python日期和文件、Web开发、数据科学、机器学习、深度学习、TensorFlow、Pytorch，一切都是简单易懂的小例子。
#     Python
#     1,975
#     438 Built by
#     49 stars today'
#     """
#     languages = ["python", "java", "golang", "javascript", "kotlin"]
#
#     # frequency = ["daily", "weekly", "monthly"]
#
#     def __init__(self, frequency="daily"):
#         super(GithubTrendingCollector, self).__init__(base_url="https://github.com/trending")
#         self.data = dict()
#         self.frequency = frequency
#
#     def fetch_data(self):
#         session = HTMLSession()
#         for language in self.languages:
#             language_result = []
#             r = session.get(self.base_url + "/{language}?since={frequency}".
#                             format(language=language, frequency=self.frequency),
#                             headers=self.HEADERS)
#             assert r.status_code == 200
#             self.logger.info(r.content)
#             items = r.html.find('div.Box article.Box-row')
#             for item in items:
#                 result = dict()
#                 self.logger.info(item.text)
#                 parsed_content = item.text.split("\n")
#                 result["url"] = GIT_URL + parsed_content[1].replace(" ", "")
#                 result["summary"] = parsed_content[2]
#                 result["stars"] = parsed_content[-3:-2][0]
#                 result["forked"] = parsed_content[-2:-1][0].replace("Built by", "")
#                 result["today"] = parsed_content[-1].replace("stars today", "")
#                 language_result.append(result)
#             self.data[language] = language_result
#         self.logger.info(self.data)
#
#     def write_to_json_file(self):
#         with open('trending/{date}_{frequency}_trending.json'.format(date=str(datetime.date.today()),
#                                                                      frequency=self.frequency), 'w') as f:
#             json.dump(self.data, f, ensure_ascii=False)
#
#     def fetch_to_file(self):
#         self.fetch_data()
#         self.write_to_json_file()
#
#
# def load_keywords():
#     with open('keywords.yml', 'r', encoding='utf-8') as keywords_file:
#         search_keywords = yaml.safe_load(keywords_file.read())
#     return search_keywords
#
#
# @commit_git_decorator
# def collect_github():
#     logging.warning("start to get github data ")
#     keywords_dict = load_keywords()
#     frequencies = keywords_dict["trending"]["frequencies"]
#     topics = keywords_dict['topics']
#     # for frequency in frequencies:
#     #     time.sleep(5)
#     #     gtc = GithubTrendingCollector(frequency)
#     #     gtc.fetch_to_file()
#     #
#     for topic in topics:
#         gtc = GithubTopicCollector(topic)
#         gtc.fetch_to_file()
#     logging.warning("end to get github data ")
#
#
# if __name__ == '__main__':
#     collect_github()
