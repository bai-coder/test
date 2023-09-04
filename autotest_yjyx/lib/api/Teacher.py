import requests,json
from cfg import *
from pprint import pprint

class Teacher:

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        body = response.content.decode('utf8')
        print(body)

        try:
            jsonBody = response.json()
            print(f'\n\n---- 消息体json ----\n'  )
            pprint(jsonBody)
        except:
            print('消息体不是json格式！！')

        print('-------- HTTP response * end -------\n\n')

    def list_teacher(self,subjectid=None):

        params = {
            'vcode': g_vcode,
            'action': 'search_with_pagenation'
        }

        if subjectid != None:
            params['subjectid'] = subjectid

        res = requests.get(
            g_api_url_teacher,
            params= params
        )

        self._printResponse(res)

        return res

    def add_teacher(self,username, realname, subjectid, classlist,
                    phonenumber, email, idcardnumber
                    ):
        '''

        :param username:
        :param realname:
        :param subjectid:
        :param classlist:  格式为 id1,id2,id3
        :param phonenumber:
        :param email:
        :param idcardnumber:
        :return:
        '''

        # 处理参数classlist  : '23,  24 '
        idList= classlist.split(',')
        classlist2 = [{'id':int(cid.strip())} for cid in idList]
        
        payload  = {
            'vcode'  : g_vcode,
            'action' : 'add',
            'username'  : username,
            'realname'   : realname,
            'subjectid'  : subjectid,
            'classlist'  : json.dumps(classlist2),
            'phonenumber'  : phonenumber,
            'email'  : email,
            'idcardnumber'  : idcardnumber,
        }

        res = requests.post(
            g_api_url_teacher,
            data= payload
        )

        self._printResponse(res)

        return res

    def modify_teacher(self,teacherid,realname=None, subjectid=None, classlist=None,
                    phonenumber=None, email=None, idcardnumber=None):
        
        # 处理参数classlist  : '23,  24 '
        if ',' in classlist:
            idList= classlist.split(',')
            classlist2 = [{'id':int(cid.strip())} for cid in idList]
        else:
            classlist3 = {}
            classlist3['id'] = int(classlist)
            classlist2.append(classlist3)

        payload = {
            'vcode' : g_vcode,
            'action' : 'modify',
            'realname'   : realname,
            'subjectid'  : subjectid,
            'classlist'  : json.dumps(classlist2),
            'phonenumber'  : phonenumber,
            'email'  : email,
            'idcardnumber'  : idcardnumber,
        }
        res = requests.put(
            g_api_url_teacher + f'/{teacherid}',
            data= payload
        )

        self._printResponse(res)
        return res
     
    def delete_teacher(self,teacherid):

        payload  = {
            'vcode'  : g_vcode,
        }
        url = f'{g_api_url_teacher}/{teacherid}'
        res = requests.delete(url,data = payload)

        self._printResponse(res)

        return res

    def delete_all_teacheres(self):
        res = self.list_teacher()
        retObj = res.json()
        for one in retObj['retlist']:
            self.delete_teacher(one['id'])

tm = Teacher()

if __name__ == '__main__':
    tm.add_teacher('wangdonghua', '王东华', 1, '20236','12345678901','sdfds@sdf.com','1233213213123')
    tm.list_teacher()