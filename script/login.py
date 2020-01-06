import unittest, logging
from api.login_api import LoginApi
from utils import assert_common
import app


class Login(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login(self):
        response = self.login_api.login('13800000002', '123456')

        jsonData = response.json()

        logging.info("登陆成功接口返回的数据为： {}".format(jsonData))
        assert_common(self,
                      response,
                      200, True, 10000, "操作成功")

        token = jsonData.get("data")

        app.HEADERS['Authorization'] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.HEADERS))
