from hytest import *
from lib.api.Student import *


class C16:
    name = '添加学生1 - tc002001'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的学生')
        sm.delete_student(self.addStudentid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加学生')
        response = sm.add_student('xiaobai','xiaohei',1,GSTORE['cid'][0],15230113199)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        self.addStudentid = res['id']
        STEP(3,'列出学生')
        response = sm.list_student()
        STEP(4,'检查学生添加成功')
        expected = {
            "username": "xiaobai",
            "classid": [GSTORE['cid'][0]], 
            "realname": "xiaohei",
            "id": self.addStudentid,
            "phonenumber": 15230113199
        }
        res = response.json()
        CHECK_POINT('检查id一致',res['retlist'][0]['id'] == self.addStudentid)
        CHECK_POINT('学生信息一致',expected == res['retlist'][0]) 


