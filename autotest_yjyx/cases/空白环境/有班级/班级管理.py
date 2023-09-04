from hytest import *
from lib.api.SClass import *
from pprint import pprint


class C2:
    name = '添加班级2 - tc000002'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的班级')
        scm.delete_class(self.addClassid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加班级')
        response = scm.add_class(2,'无双小学院',20)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        self.addClassid = res['id']
        self.addInviteCode = res['invitecode']
        STEP(3,'列出班级')
        response = scm.list_class()
        STEP(4,'检查返回数据中包含新添加的班级')
        res = response.json()
        addClassData = {
                "name": "无双小学院",
                "grade__name": "八年级",
                "invitecode": self.addInviteCode,
                "studentlimit": 20,
                "studentnumber": 0,
                "id": self.addClassid,                    
                "teacherlist": []
        }
        CHECK_POINT('检查数据',addClassData in res['retlist'])

class C3:
    name = '添加班级3 - tc000003'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加前列出班级')
        oldResponse = scm.list_class()
        STEP(2,'添加班级')
        response = scm.add_class(1,'小天才1班',20)
        STEP(3,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 1)
        CHECK_POINT('reason检查',res['reason'] == "duplicated class name")
        STEP(4,'添加后列出班级')
        newResponse = scm.list_class()
        STEP(4,'检查返回数据中不包含新添加的班级')
        oldRes = oldResponse.json()
        newRes = newResponse.json()
        CHECK_POINT('检查添加前后的班级列表一致',oldRes == newRes)

class C4:
    name = '修改班级1 - tc000051'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('还原班级信息')
        scm.modify_class(GSTORE['cid'][0],'小天才1班',20)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'修改班级')
        response = scm.modify_class(GSTORE['cid'][0],'大天才1班',20)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        STEP(3,'列出班级')
        response = scm.list_class()
        res = response.json()
        STEP(4,'检查班级信息已被修改')
        for one in res['retlist']:
            if one['id'] == GSTORE['cid'][0]:
                CHECK_POINT('检查班级名修改为新的班级名',one['name'] == '大天才1班')

class C5:
    name = '修改班级2 - tc000052'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'列出修改前班级')
        oldResponse = scm.list_class()
        res = oldResponse.json()
        for one in res['retlist']:
            if one['id'] == GSTORE['cid'][0]:
                oldData = one
        STEP(2,'修改班级')
        response = scm.modify_class(GSTORE['cid'][0],'小天才2班',20)
        STEP(3,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 1)
        CHECK_POINT('reason检查',res['reason'] == "duplicated class name")
        STEP(4,'列出修改后班级')
        newResponse = scm.list_class()
        res = newResponse.json()
        STEP(5,'检查班级信息')
        for one in res['retlist']:
            if one['id'] == GSTORE['cid'][0]:
                CHECK_POINT('检查班级信息没有被修改',one == oldData)

class C6:
    name = '修改班级3 - tc000053'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'修改班级')
        response = scm.modify_class(5,'小天才2班',20)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 404)
        CHECK_POINT('reason检查',res['reason'] == "id 为5的班级不存在")

class C7:
    name = '删除班级1 - tc000081'
   
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'删除班级')
        response = scm.delete_class(10)
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 404)
        CHECK_POINT('reason检查',res['reason'] == "id 为10的班级不存在")

class C8:
    name = '删除班级2 - tc000082'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('添加删除的班级')
        response = scm.add_class(2,'小天才2班',20)
        res = response.json()
        for one in res['retlist']:
            if one['name'] == '小天才2班':
                GSTORE['cid'][1] = one['id']
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'删除班级')
        response = scm.delete_class(GSTORE['cid'][1])
        STEP(2,'检查响应消息')
        res = response.json()
        CHECK_POINT('retcode检查',res['retcode'] == 0)
        STEP(3,'列出班级')
        response = scm.list_class()
        STEP(4,'检查删除班级已不在班级列表中')
        res = response.json()
        for one in res['retlist']:
            CHECK_POINT('检查没有已经删除的班级',one['id'] != GSTORE['cid'][1])
        

