from hytest import *
from lib.api.Student import *


class C17:
    name = '添加学生2 - tc002002'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的学生')
        sm.delete_student(self.addStudentid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加学生')
        response = sm.add_student('Heihei','zhouxue',1,GSTORE['cid'][1],15230113100)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        self.addStudentid = res['id']
        STEP(3,'列出学生')
        response = sm.list_student()
        STEP(4,'检查学生添加成功')
        expected = {
            "username": "Heihei",
            "classid": [GSTORE['cid'][1]], 
            "realname": "zhouxue",
            "phonenumber": 15230113100,
            "id": self.addStudentid
        }
        res = response.json()
        CHECK_POINT('学生信息已被添加',expected in res['retlist'])

class C18:
    name = '删除学生1 - tc002081'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('还原删除学生信息')
        response = sm.add_student('xueyu1','zhouxue1',2,GSTORE['cid'][1],'15230113181')
        res = response.json()
        for one in res['retlist']:
            if one['username'] == 'wangdonghua1':
                GSTORE['tid'][1] = one['id']
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'删除学生信息')
        response = sm.delete_student(GSTORE['sid'][1])
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        STEP(3,'列出学生列表')
        response = sm.list_student()
        STEP(4,'检查学生删除成功')
        res = response.json()
        for one in res['retlist']:
            CHECK_POINT('检查没有已经删除的学生',one['id'] != GSTORE['tid'][1])