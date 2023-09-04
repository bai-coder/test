from hytest import *
from lib.api.SClass import *
from lib.api.Teacher import *
from lib.api.Student import *
#force_tags = ['功能测试']


def suite_setup():
    INFO('添加3名学生')
    for i in range(3):
        sm.add_student(f'xueyu{i}',f'zhouxue{i}',i+1,GSTORE['cid'][i],f'1523011318{i}')
    res = sm.list_students()
    r = res.json()
    sidlist = []
    for i in range(3):
        sidlist.append(r['retlist'][i]['id'])
    GSTORE['sid'] = sidlist


def suite_teardown():
    INFO('清空学生')
    sm.delete_all_students()          
        