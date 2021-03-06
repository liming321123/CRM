import unittest
import xlrd
import time
from HTMLTestRunner import HTMLTestRunner

def run_discover():
    discover = unittest.defaultTestLoader.discover(start_dir='../testcase',
                                                   pattern='test*.py')

    file_time = time.strftime("%Y%m%d%H%M",time.localtime())
    file_report = 'report'+file_time+'.html'
    with open(file_report,'wb+') as f:
        runner = HTMLTestRunner(stream=f,title="CRM测试报告",description="CRM测试详情")
        runner.run(discover)

def run_business():
    discover = unittest.defaultTestLoader.discover(start_dir='../testcase',
                                                   pattern='test_003*.py')

    file_time = time.strftime("%Y%m%d%H%M",time.localtime())
    file_report = 'report'+file_time+'.html'
    with open(file_report,'wb+') as f:
        runner = HTMLTestRunner(stream=f,title="CRM测试报告",description="CRM测试详情")
        runner.run(discover)

# run_discover()
run_business()