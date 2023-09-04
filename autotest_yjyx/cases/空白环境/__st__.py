from hytest import INFO
from lib.api.SClass import *
from lib.api.Teacher import *

#force_tags = ['功能测试']


def suite_setup():
    INFO('清空所有班级数据')
    scm.delete_all_classes()
    INFO('清空所有教师数据')
    tm.delete_all_teacheres()
    INFO('清空所有学生数据')
    #sm.delete_all_students()

def suite_teardown():
    INFO('暂无任务')
    pass          
        