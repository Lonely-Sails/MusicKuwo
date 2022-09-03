from MusicKuwo.Objects import Music, Artist
from MusicKuwo.Uitls import RequestJson


def SearchHints(Word: str = None) -> list[str, ...]:
    Result = []
    RequestParams = {'httpsStatus': 1, 'key': Word if Word else ''}
    ResponseJson = RequestJson('https://www.kuwo.cn/api/www/search/searchKey', RequestParams)
    if ResponseJson:
        for HintString in ResponseJson:
            Result.append(HintString.strip('RELWORD=').split('\r\n')[0])
        return Result


def SearchMusic(Word: str, PageNumber: int = 30, Page: int = 1) -> list[Music, ...]:
    Result = []
    RequestParams = {'httpsStatus': 1, 'key': Word, 'rn': PageNumber, 'pn': Page}
    ResponseJson = RequestJson('https://www.kuwo.cn/api/www/search/searchMusicBykeyWord', RequestParams)
    if ResponseJson:
        ResponseJson = ResponseJson.get('list')
        for MusicInfo in ResponseJson:
            Result.append(Music(**MusicInfo))
        return Result


def SearchArtist(Word: str, PageNumber: int = 10, Page: int = 1) -> list[Artist, ...]:
    Result = []
    RequestParams = {'httpsStatus': 1, 'key': Word, 'rn': PageNumber, 'pn': Page}
    ResponseJson = RequestJson('https://kuwo.cn/api/www/search/searchArtistBykeyWord', RequestParams)
    if ResponseJson:
        ResponseJson = ResponseJson.get('list')
        for MusicInfo in ResponseJson:
            Result.append(Artist(**MusicInfo))
        return Result


if __name__ == '__main__':
    Musics = SearchMusic('小城夏天', 1, 1)
    for MusicOne in Musics:
        print(MusicOne)
