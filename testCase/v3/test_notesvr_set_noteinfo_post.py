import unittest
import time
import requests
from common.read_yml import ReadYaml
from business_common.api_demo import ApiDemo
from copy import deepcopy
from common.custom_logs import info_log, log_class_methods
from parameterized import parameterized

"""
数据驱动：把用户输入的信息和代码结构分离开  减少编码成本，提高编码效率
"""


@log_class_methods
class NotesvrSetNoteinfoPost(unittest.TestCase):
    env_config = ReadYaml().env_yaml("config.yml")
    host = env_config["host"]
    user_id = env_config["user_id"]
    wps_sid = env_config["wps_sid"]
    env_config = ReadYaml().api_yaml("v3/notesvr_set_noteinfo_post.yml")
    path = "/v3/notesvr/set/noteinfo"
    url = host + path
    base = {
        "noteId": "abc",
        "star": 0,
        "remindTime": 0,
        "remindType": 0
    }

    def testCase01_major(self):
        """上传/更新便签信息主体，主用例"""
        noteId = str(int(time.time() * 1000)) + "TestNote"
        body = deepcopy(self.base)
        body["noteId"] = noteId

        info_log("上传便签信息主体")
        response = ApiDemo().api_post(url=self.url, body=body, user_id=self.user_id, wps_sid=self.wps_sid)
        self.assertEqual(200, response.status_code)

    @parameterized.expand(env_config["must_key"])
    def testCase02_input_check(self, key):
        """上传/更新便签信息主体，所有字段的必填校验"""
        noteId = str(int(time.time() * 1000)) + "TestNote"
        body = deepcopy(self.base)
        body.pop(key)
        response = ApiDemo().api_post(url=self.url, body=body, user_id=self.user_id, wps_sid=self.wps_sid)
        self.assertEqual(500, response.status_code)
