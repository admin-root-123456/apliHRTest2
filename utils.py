import app

import json


def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


def read_login_data():
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)

        p_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append((mobile, password, http_code, success, code, message))
    print(p_list)
    return p_list


if __name__ == '__main__':
    read_login_data()
