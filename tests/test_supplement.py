# import json
# from pprint import pprint
#
# from extractors.supplement import to_json, yml_to_json, yml_to_dict
# from deepdiff import DeepDiff, Delta
# from imgix import UrlBuilder
#
#
# class TestSupplementUtil():
#     def test_to_json(self):
#         val = dict()
#         val['test'] = "value"
#         val['key'] = {"sub_key": "sub_value"}
#         result = to_json(val)
#         expected = """{"key": {"sub_key1": "sub_value"}, "test": "value"}"""
#         result = DeepDiff(result, expected, view='tree')
#         print(result)
#         for k, v in Delta(diff=result).to_dict().items():
#             print(k, v)
#         print(Delta(result))
#         assert len(result) == 0
#
#     def test_to_json_diff(self):
#         val = dict()
#         val['test'] = "value"
#         val['key'] = {"sub_key1": "sub_value"}
#         result = to_json(val)
#         expected = """{"key": {"sub_key": "sub_value"}, "test": "value"}"""
#
#         ## new value/old value
#         pprint(result, indent=2)
#         assert len(result) == 0
#
#     def test_yaml_to_json(self):
#         result = yml_to_dict("testing-sources.yml")
#         sites = result["sites"]
#         temp_dict = {
#             "logo": "/assets/images/icon/logo.png",
#             "name": "Karate",
#             "desc": "Test Automation Made Simple.",
#             "url": "https://github.com/intuit/karate"
#         }
#
#         total_result = []
#         for item in sites:
#             name = item.replace("http:","").replace("https://","").replace("www.","").replace("github.com/","")
#             site_name = name.split(".")[0]
#             total_result.append(
#                 {
#                     "logo": "/assets/images/icon/logo.png",
#                     "name": site_name,
#                     "desc": site_name,
#                     "url": item
#                 }
#             )
#         print(to_json(total_result))
#         with open('navigation-tools.json', 'w') as f:
#             json.dump(total_result,f)
#
#     # def test_imgx(self):
#     #     ub = UrlBuilder("github.com", include_library_param=False)
#     #     result = ub.create_url("bridge.png", {'w': 100, 'h': 100})
#     #     print(result)
#
#
# ## pytest-icdiff
# ## $ pip install dictdiffer
# ## www.obeythetestinggoat.com
# # from faker import Faker
# #
# # fake = Faker()
# # dict_1 = fake.pydict(nb_elements=10)
# # dict_2 = dict_1.copy()
# # dict_2[list(dict_1.keys())[1]] = "Test 1"
# # dict_2[list(dict_1.keys())[2]] = "Test 2"
# # dict_2[list(dict_1.keys())[3]] = "Test 3"
# # dict_2[list(dict_1.keys())[5]] = "Test 4"
# # dict_2[list(dict_1.keys())[6]] = "Test 5"
# #
# #
# # def test_diff():
# #     assert dict_1 == dict_2
from backups.feeds.extractors.supplement import load_json_file, write_to_json_file


def test_load_json_file():
    result = load_json_file("sample_repo.json")
    assert result["url"] is not None


def test_load_json_file_not_exist():
    result = load_json_file("./starred_repo_1.json")
    assert len(result) > 0


def test_write_dict_to_json_file():
    result = load_json_file("sample_repo.json")
    write_to_json_file(result, 'dump_dict.json')
