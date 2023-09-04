from hytest import *
from lib.api.SClass import *
from lib.api.Teacher import *

#force_tags = ['功能测试']


def suite_setup():
    INFO('创建3个班级')
    for i in range(3):
        scm.add_class(i+1,f'小天才{i+1}班',20)
    res = scm.list_class()
    r = res.json()
    cidlist = []
    for i in range(3):
        cidlist.append(r['retlist'][i]['id'])
    GSTORE['cid'] = cidlist
def suite_teardown():
    INFO('清空班级')
    scm.delete_all_classes()          
        