from html import unescape

from MusicKuwo.Uitls import RequestJson, DownloadFile


class Music(object):
    Code = None
    Name = None
    Artist = None
    CoverImage = None
    TimeMinutes = None
    ReleaseDate = None

    def __repr__(self):
        return F'<MusicKuwo.MusicObject \'{self.Name}\'>'

    def __init__(self, Code: int = None, **KwArgs):
        if not KwArgs and Code:
            Params = {'mid': Code}
            KwArgs = RequestJson('https://www.kuwo.cn/api/www/music/musicInfo', Params)
        self.Code = KwArgs.get('rid')
        self.CoverImage = KwArgs.get('pic')
        self.ReleaseDate = KwArgs.get('releaseDate')
        self.TimeMinutes = KwArgs.get('songTimeMinutes')
        self.Name = unescape(KwArgs.get('name'))
        self.Artist = Artist(**KwArgs)

    def loadOther(self, Code: int = None):
        pass

    def Download(self, Path: str):
        Params = {'mid': self.Code}
        ResponseJson = RequestJson('https://www.kuwo.cn/api/v1/www/music/playUrl', Params)
        if ResponseJson:
            return DownloadFile(ResponseJson.get('url'), Path)

    def DownloadLyrics(self, Path: str, Encoding: str = 'Gbk'):
        Params = {'musicId': self.Code}
        ResponseJson = RequestJson('https://m.kuwo.cn/newh5/singles/songinfoandlrc', Params)
        if ResponseJson:
            with open(Path, encoding=Encoding, mode='w') as File:
                for LyricInfo in ResponseJson.get('lrclist'):
                    Time = float(LyricInfo.get('time'))
                    Content = LyricInfo.get('lineLyric')
                    File.write(F'[{(Time // 60)}:{round((Time % 60), 2)}]{Content}\n')
                return True


class Artist(object):
    Code = None
    Name = None
    Tall = None
    Info = None
    Image = None
    Gender = None
    Weight = None
    Country = None
    Language = None
    MvNumber = None
    Birthday = None
    Birthplace = None
    FansNumber = None
    MusicNumber = None
    AlbumNumber = None
    EnglishName = None
    Constellation = None

    def __repr__(self):
        return F'<MusicKuwo.ArtistObject \'{self.Name}\'>'

    def __init__(self, Code: int = None, **KwArgs):
        self.Name = KwArgs.get('artist')
        self.Code = KwArgs.get('artistid')
        if not self.Code:
            self.Code = KwArgs.get('id')
            self.Name = KwArgs.get('name')
            self.Country = KwArgs.get('country')
            self.MusicNumber = KwArgs.get('musicNum')
        elif not KwArgs and Code:
            self.LoadOther(Code)

    def LoadOther(self, Code: int = None):
        Params = {'artistid': Code if Code else self.Code}
        ResponseJson = RequestJson('https://kuwo.cn/api/www/artist/artist', Params)
        if ResponseJson:
            self.Code = ResponseJson.get('id')
            self.Tall = ResponseJson.get('tall')
            self.Image = ResponseJson.get('pic')
            self.Gender = ResponseJson.get('gener')
            self.Weight = ResponseJson.get('weight')
            self.Country = ResponseJson.get('country')
            self.MvNumber = ResponseJson.get('mvNum')
            self.Language = ResponseJson.get('language')
            self.Birthday = ResponseJson.get('birthday')
            self.Birthplace = ResponseJson.get('birthplace')
            self.FansNumber = ResponseJson.get('artistFans')
            self.MusicNumber = ResponseJson.get('musicNum')
            self.AlbumNumber = ResponseJson.get('albumNum')
            self.Constellation = ResponseJson.get('constellation')
            self.Info = unescape(ResponseJson.get('info')).split('<br/>')
            self.Name = unescape(ResponseJson.get('name'))
            self.EnglishName = unescape(ResponseJson.get('aartist'))
            return True


if __name__ == '__main__':
    ChenYiXun = Artist(336)
    print(ChenYiXun.MusicNumber)
