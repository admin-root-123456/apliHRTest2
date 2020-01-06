import time
import unittest
import app
from script.login import Login
from script.test_emp import TestIHRMEmp
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))

report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb',encoding='utf-8') as f:
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="V1.0.0")

    runner.run(suite)
