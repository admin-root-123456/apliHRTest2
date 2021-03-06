import requests
import app


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"

        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-12-02",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2019-12-15T16:00:00.000Z"
        }

        response = requests.post(self.emp_url, json=data, headers=self.headers)

        return response

    def query_emp(self):
        url = self.emp_url +"/"+app.EMP_ID
        return requests.get(url,headers=self.headers)

    def modify_emp(self,username):
        url = self.emp_url +"/"+ app.EMP_ID
        data={
            "username":username
        }
        return requests.put(url,json=data,headers=self.headers)
    def delete_emp(self):
        url = self.emp_url +"/"+ app.EMP_ID
        return requests.put(url,headers=self.headers)
