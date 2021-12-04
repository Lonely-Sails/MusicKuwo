import requests

from MusicKuwo.Errors import RequestError

Headers = {
    'Referer': 'https://www.kuwo.cn/', 'csrf': 'HYZQI4KPK3P',
    'Cookie': '_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; '
              '_gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974;'
              ' Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P',
}


def RequestSend(Url, Params, Key='code'):
    Request = requests.get(Url, headers=Headers, params=Params)
    if Request.status_code != 200:
        raise RequestError(F'Request failed, error code {Request.status_code}.')
    RequestJson = Request.json()
    if 'code' in RequestJson.keys():
        if RequestJson[Key] != 200:
            raise RequestError(F'Request failed, error code {RequestJson[Key]}.')
    return RequestJson


def DetectType(ObjectName, Object, Type):
    if not isinstance(Object, Type):
        raise TypeError(F'The "{ObjectName}" parameter should be {Type} type, but the type is {type(Object)}.')
