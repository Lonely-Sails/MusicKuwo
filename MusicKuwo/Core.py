from MusicKuwo.Music import *


def Search(Key, Page=1, Number=30):
    DetectType('Key', Key, str)
    DetectType('Page', Page, int)
    DetectType('Number', Number, int)
    SearchMusic = GroupMusic()
    Params = {'key': Key, 'pn': Page, 'rn': Number}
    SearchJson = RequestSend('https://www.kuwo.cn/api/www/search/searchMusicBykeyWord', Params)
    for SearchInfo in SearchJson['data']['list']:
        SearchMusic.Append(Music(SearchInfo))
    return SearchMusic


def SearchPrompt(Key):
    DetectType('Key', Key, str)
    Prompts = []
    Params = {'key': Key}
    PromptJson = RequestSend('https://www.kuwo.cn/api/www/search/searchKey', Params)
    for Prompt in PromptJson['data']:
        Prompts.append((Prompt.split('\r\n')[0])[8:])
    return Prompts


def DownloadFile(Path, Url):
    DetectType('Url', Url, str)
    DetectType('Path', Path, str)
    with open(Path, mode='wb') as File:
        Request = requests.get(Url)
        if Request.status_code != 200:
            raise RequestError(F'Request failed, error code {Request.status_code}.')
        for RequestData in Request.iter_content():
            File.write(RequestData)


def DownloadMusic(Path, Code):
    DetectType('Code', Code, int)
    Params = {'mid': Code}
    UrlJson = RequestSend('https://www.kuwo.cn/api/v1/www/music/playUrl', Params)
    DownloadFile(Path, UrlJson['data']['url'])
