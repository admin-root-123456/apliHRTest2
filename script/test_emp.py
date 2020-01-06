import logging
import unittest
from api.emp_api import EmpApi
from utils import assert_common
import app


class TestIHRMEmp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:

        cls.emp_api = EmpApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add_emp(self):
        response = self.emp_api.add_emp("无助xxx1v5", "10099098763")

        jsonData = response.json()

        logging.info("添加员工接口返回数据为：{}".format(jsonData))

        assert_common(self, response, 200, True, 10000, "操作成功")

        app.EMP_ID = jsonData.get("data").get("id")

    def test02_query_emp(self):
        """查询员工测试方法"""
        response = self.emp_api.query_emp()
        json_data = response.json()
        logging.info("查询员工接口返回的数据为：{}".format(json_data))

        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test03_modify_emp(self):
        """查询员工测试方法"""
        response = self.emp_api.modify_emp('汤姆猫')
        jsonData = response.json()
        logging.info("修改员工接口返回的数据为：{}".format(jsonData))

        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")
    def test04_delete_emp(self):
        """查询员工测试方法"""
        response = self.emp_api.delete_emp()
        jsonData = response.json()
        logging.info("删除员工接口返回的数据为：{}".format(jsonData))

        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")