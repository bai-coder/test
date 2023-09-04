from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from cfg.cfg import g_api_server

class TeacherOp:

    def teacherLogin(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.driver.get(f'{g_api_server}/teacher/login/login.html')

        self.driver.find_element(By.ID,'username').send_keys(username)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.ID,'submit').click()

    def getHomePageInfo(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[href='#/home']>li").click()

        time.sleep(2)

        eles = self.driver.find_elements(By.CSS_SELECTOR,'#home_div .ng-binding')

        return [ele.text for ele in eles]


teachWebOp = TeacherOp()

if __name__ == '__main__':
    teachWebOp.teacherLogin('wangdonghua','888888')
    info = teachWebOp.getHomePageInfo()
    print(info)