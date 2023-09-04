from hytest import *
from lib.api.SClass import *
from pprint import pprint
import requests


class C1:
    name = '添加班级1 - tc000001'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的班级')
        scm.delete_class(self.addClassid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加班级')
        response = scm.add_class(1,'无双学院',30)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        self.addClassid = res['id']
        self.addInviteCode = res['invitecode']
        STEP(3,'列出班级')
        response = scm.list_class()
        STEP(4,'检查返回数据与添加班级一致')
        res = response.json()
        expected = {
            "gradeid": 1,
            "retlist": [
                {
                    "name": "无双学院",
                    "grade__name": "七年级",
                    "invitecode": self.addInviteCode,
                    "studentlimit": 30,
                    "studentnumber": 0,
                    "id": self.addClassid,
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('检查数据',expected == res)

