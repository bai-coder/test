from hytest import *
from lib.api.Teacher import *
#force_tags = ['功能测试']


def suite_setup():
    INFO('添加3位老师')
    for i in range(3):
        tm.add_teacher(f'wangdonghua{i}', f'王东华{i}', i+11, GSTORE['cid'][i],f'1234567890{i}',f'sdfds@sdf{i}.com',f'123321321312{i}')
    res = tm.list_teacher()
    r = res.json()
    tidlist = []
    for i in range(3):
        tidlist.append(r['retlist'][i]['id'])
    GSTORE['tid'] = tidlist

def suite_teardown():
    INFO('清空老师')
    tm.delete_all_teacheres()     
        