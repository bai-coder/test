from selenium import webdriver
import time
from cfg.cfg import g_api_server

class TeacherOp:

    def teacherLogin(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.driver.get(f'{g_api_server}/teacher/login/login.html')

        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    def getHomePageInfo(self):
        self.driver.find_element_by_css_selector("a[href='#/home']>li").click()

        time.sleep(2)

        eles = self.driver.find_elements_by_css_selector('#home_div .ng-binding')

        return [ele.text for ele in eles]


teachWebOp = TeacherOp()

if __name__ == '__main__':
    teachWebOp.teacherLogin('wangdonghua','888888')
    info = teachWebOp.getHomePageInfo()
    print(info)