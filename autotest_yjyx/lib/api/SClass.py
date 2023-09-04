import requests
from cfg.cfg import *
from pprint import pprint

class SClass:

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

    def list_class(self,gradeid=None):

        params = {
            'vcode': g_vcode,
            'action': 'list_classes_by_schoolgrade'
        }

        if gradeid != None:
            params['gradeid'] = gradeid

        res = requests.get(
            g_api_url_class,
            params= params
        )

        self._printResponse(res)

        return res

    def add_class(self,gradeid,name,studentlimit):

        payload  = {
            'vcode'  : g_vcode,
            'action' : 'add',
            'grade'  : gradeid,
            'name'   : name,
            'studentlimit'  : studentlimit,
        }

        res = requests.post(
            g_api_url_class,
            data= payload
        )

        self._printResponse(res)

        return res

    def modify_class(self,classid,name,studentlimit):

        payload = {
            'vcode' : g_vcode,
            'action' : 'modify',
            'name' : name,
            'studentlimit' : studentlimit
        }
        res = requests.put(
            g_api_url_student + f'/{classid}',
            data= payload
        )
        self._printResponse(res)
        
        return res
    
    def delete_class(self,classid):

        payload  = {
            'vcode'  : g_vcode,
        }
        url = f'{g_api_url_class}/{classid}'
        res = requests.delete(url,data = payload)

        self._printResponse(res)

        return res

    def delete_all_classes(self):
        res = self.list_class()
        retObj = res.json()
        for one in retObj['retlist']:
            self.delete_class(one['id'])

scm = SClass()

if __name__ == '__main__':
    scm.add_class(1,'白月黑羽2班', 55)
    scm.list_class()
