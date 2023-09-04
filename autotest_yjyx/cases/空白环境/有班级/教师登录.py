from hytest import *
from lib.api.Teacher import *
from lib.webui.TeacherOP import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class C19:
    name = '老师登录1 - tc005001'
   
    def setup(self):
        pass
    
    def teardown(self):
        INFO('清除添加的教师')
        tm.delete_teacher(self.addTeacherid)
    
    def teststeps(self):
        # 测试步骤如下
        STEP(1,'添加教师')
        response = tm.add_teacher('baijinhang','白金航',1,str(GSTORE['cid'][0]),15230113188,'jcysdf@123.com',130481199604050999)
        res = response.json()
        self.addTeacherid = res['id']

        STEP(2,'用教师账号登录系统')
        teachWebOp.teacherLogin('baijinhang',888888)

        STEP(3,'检查首页信息')
        homePageInfo = teachWebOp.getHomePageInfo()
        expected = ['白月学院00002', '白金航', '初中数学', '0', '0', '0']
        CHECK_POINT('检查首页信息', homePageInfo==expected)

        STEP(4,'点击班级学生菜单')
        ac = ActionChains(teachWebOp.driver)
        ac.move_to_element(teachWebOp.driver.find_element(By.CSS_SELECTOR,'#topbar > div > div > ul > li:nth-child(9) > a'))
        teachWebOp.driver.find_element(By.CSS_SELECTOR,'span.menu-title').click()

        STEP(5,'检查班级学生人数为0')
        eles = teachWebOp.driver.find_elements(By.CSS_SELECTOR,'i.fa-user')
        
