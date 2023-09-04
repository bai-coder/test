from hytest import *
from lib.api.Teacher import *


class C10:
    name = '添加教师2 - tc001002'
   
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
        CHECK_POINT('教师信息已被添加',expected in res['retlist'])

class C11:
    name = '添加教师3 - tc001003'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'列出添加教师前的列表')
        oldResponse = tm.list_teacher()
        STEP(2,'添加教师')
        response = tm.add_teacher('wangdonghua0', '王东华01', 11, GSTORE['cid'][1],'12345678908','sdfds@sdff.com','1233213213127')
        STEP(3,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 1)
        CHECK_POINT('reason检查',res['reason'] == "登录名wangdonghua0已经存在")
        STEP(3,'列出添加教师后的列表')
        newResponse = tm.list_teacher()
        STEP(4,'检查没有添加教师')
        CHECK_POINT('教师信息没有被添加',oldResponse == newResponse)

class C12:
    name = '修改教师1 - tc001051'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'修改教师信息')
        response = tm.modify_teacher(199)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 1)
        CHECK_POINT('reason检查',res['reason'] == "id 为`199`的老师不存在")
        
class C13:
    name = '修改教师2 - tc001052'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('还原修改教师信息')
        response = tm.modify_teacher(GSTORE['tid'][0],realname='王东华0',classlist=f"{GSTORE['cid'][0]}")
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'修改教师信息')
        response = tm.modify_teacher(GSTORE['tid'][0],realname='王东华',classlist=f"{GSTORE['cid'][0]},{GSTORE['cid'][1]}")
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        STEP(3,'列出教师列表')
        response = tm.list_teacher()
        STEP(4,'检查教师修改成功')
        expected = {
            "username": "wangdonghua0",
            "teachclasslist": [GSTORE['cid'][0],[GSTORE['cid'][1]]], 
            "realname": "王东华",
            "id": GSTORE['tid'][0],
            "phonenumber": 12345678900,
            "email": 'sdfds@sdf0.com',
            "idcardnumber": 1233213213120
        }
        res = response.json()
        CHECK_POINT('教师信息已被修改',expected in res['retlist'])
    
class C14:
    name = '删除教师1 - tc001081'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'删除教师信息')
        response = tm.delete_teacher(199)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 404)
        CHECK_POINT('reason检查',res['reason'] == "id 为`199`的老师不存在")

class C15:
    name = '删除教师2 - tc001082'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('还原删除教师信息')
        response = tm.add_teacher('wangdonghua1', '王东华1', 12, GSTORE['cid'][1],'12345678901','sdfds@sdf1.com','1233213213121')
        res = response.json()
        for one in res['retlist']:
            if one['username'] == 'wangdonghua1':
                GSTORE['tid'][1] = one['id']
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'删除教师信息')
        response = tm.delete_teacher(GSTORE['tid'][1])
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        STEP(3,'列出教师列表')
        response = tm.list_teacher()
        STEP(4,'检查教师删除成功')
        res = response.json()
        for one in res['retlist']:
            CHECK_POINT('检查没有已经删除的教师',one['id'] != GSTORE['tid'][1])