from random import randint

import requests


def RequestJson(Url: str, Params: dict) -> dict:
    HeadersToken = str(randint(1000000000, 9999999999))
    Headers = {'Referer': 'https://www.kuwo.cn/', 'Cookie': F'kw_token={HeadersToken}', 'csrf': HeadersToken}
    Response = requests.get(Url, headers=Headers, params=Params)
    if Response.status_code == 200:
        ResponseJson = Response.json()
        if ResponseJson.get('status') == 200 or ResponseJson.get('code') == 200:
            return ResponseJson.get('data')


def DownloadFile(Url: str, Path: str, ChuckSize: int = 2500) -> bool:
    Response = requests.get(Url)
    if Response.status_code == 200:
        with open(Path, mode='wb') as File:
            for Data in Response.iter_content(ChuckSize):
                File.write(Data)
            return True
