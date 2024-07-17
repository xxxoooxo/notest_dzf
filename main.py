import unittest
import os
from BeautifulReport import BeautifulReport
import datetime

"""切换环境"""
# 使用哪个环境打开哪个环境
# 测试环境
# Environ = "/env_config/Offline/"
# 线上环境
Environ = "/env_config/Online/"


DIR = os.path.dirname(os.path.abspath(__file__))  # 获取当前执行文件所在目录的绝对路径


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', log_path=DIR)


if __name__ == "__main__":

    # discover方法执行测试套件
    start_time = datetime.datetime.now()
    print("start time : {}".format(datetime.datetime.now()))
    case_level = "all"  # smoke 冒烟用例，all 全量用例
    if case_level == "smoke":
        pattern = "test_smoke*.py"
    else:
        pattern = "test_*.py"

    testsuite = unittest.defaultTestLoader.discover(
        start_dir=DIR + '/testCase',
        pattern=pattern
    )
    run(testsuite)
    end_time = datetime.datetime.now()
    print("end time : {}".format(end_time))
    print("use time : {}".format(end_time-start_time))

