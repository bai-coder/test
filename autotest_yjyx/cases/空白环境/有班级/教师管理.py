from hytest import *
from lib.api.Teacher import *


class C9:
    name = '添加教师1 - tc001001'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的教师')
        tm.delete_teacher(self.addTeacherid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加教师')
        response = tm.add_teacher('Baibai','xiaobaibai',1,GSTORE['cid'][0],15230113188,'jcysdf@123.com',130481199604050999)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        self.addTeacherid = res['id']
        STEP(3,'列出教师')
        response = tm.list_teacher()
        STEP(4,'检查教师添加成功')
        expected = {
            "username": "Baibai",
            "teachclasslist": [GSTORE['cid'][0]], 
            "realname": "xiaobaibai",
            "id": self.addTeacherid,
            "phonenumber": 15230113188,
            "email": 'jcysdf@123.com',
            "idcardnumber": 130481199604050999
        }
        res = response.json()
        CHECK_POINT('检查id一致',res['retlist'][0]['id'] == self.addTeacherid)
        CHECK_POINT('教师信息一致',expected == res['retlist'][0]) 

