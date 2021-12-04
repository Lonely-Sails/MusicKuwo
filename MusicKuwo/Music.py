from json import dump, load

from MusicKuwo.Comment import *


class Music:
    def __init__(self, InfoJson=None):
        if InfoJson:
            self.Code = InfoJson['rid']
            self.AlbumImage = InfoJson['albumpic']
            self.Name = InfoJson['name'].replace('&nbsp;', ' ')
            self.Artist = InfoJson['artist'].replace('&nbsp;', ' ')
            self.AlbumName = InfoJson['album'].replace('&nbsp;', ' ')

    def Comment(self, Page, Number=20, Hot=False):
        DetectType('Hot', Hot, bool)
        DetectType('Page', Page, int)
        DetectType('Number', Number, int)
        if Hot:
            Type = 'get_comment'
        else:
            Type = 'get_res_comment'
        Comments = GroupComment()
        Params = {'page': Page, 'type': Type, 'rows': Number, 'sid': self.Code, 'f': 'web', 'uid': '0', 'digest': '15',
                  'prod': 'newWeb'}
        CommentJson = RequestSend('https://www.kuwo.cn/comment', Params)
        for CommentInfo in CommentJson['rows']:
            Comments.Append(Comment(CommentInfo))
        return Comments

    def DownloadLyrics(self, Path, Encoding='GBK'):
        DetectType('Path', Path, str)
        DetectType('Encoding', Encoding, str)
        Params = {'musicId': self.Code}
        LyricsJson = RequestSend('https://m.kuwo.cn/newh5/singles/songinfoandlrc', Params)
        with open(Path, mode='w', encoding=Encoding) as File:
            for LyricInfo in LyricsJson['data']['lrclist']:
                LyricContent = LyricInfo['lineLyric']
                LyricTime = round(float(LyricInfo['time']), 2)
                LyricSecond = (LyricTime % 60)
                LyricMinute = (LyricTime // 60)
                File.write(F'[{LyricMinute}:{LyricSecond}]{LyricContent}\n')


class MusicDetailed(Music):
    def __init__(self, Code):
        Music.__init__(self)
        DetectType('Code', Code, int)
        Params = {'mid': Code}
        InfoJson = RequestSend('https://www.kuwo.cn/api/www/music/musicInfo', Params)
        self.Code = InfoJson['data']['rid']
        self.Date = InfoJson['data']['releaseDate']
        self.AlbumImage = InfoJson['data']['albumpic']
        self.Time = InfoJson['data']['songTimeMinutes']
        self.Name = InfoJson['data']['name'].replace('&nbsp;', ' ')
        self.Artist = InfoJson['data']['artist'].replace('&nbsp;', ' ')
        self.AlbumName = InfoJson['data']['album'].replace('&nbsp;', ' ')
        self.AlbumInfo = InfoJson['data']['albuminfo'].replace('&nbsp;', ' ')


class GroupMusic:
    def __init__(self):
        self.Group = []

    def __iter__(self):
        return iter(self.Group)

    def Append(self, Item):
        if not (isinstance(Item, MusicDetailed) or isinstance(Item, Music)):
            raise TypeError(
                F'The "Item" parameter should be MusicDetailed or Music type, but the type is {type(Item)}.')
        self.Group.append(Item)

    def SaveFile(self, Path, Encoding='GBK'):
        DetectType('Path', Path, str)
        DetectType('Encoding', Encoding, str)
        WriteJson = []
        with open(Path, mode='w', encoding=Encoding) as File:
            for Item in self.Group:
                WriteJson.append(Item.Code)
            dump(WriteJson, File)

    @staticmethod
    def ReadFile(Path, Encoding='GBK'):
        DetectType('Path', Path, str)
        DetectType('Encoding', Encoding, str)
        Group = GroupMusic()
        with open(Path, mode='r', encoding=Encoding) as File:
            ReadJson = load(File)
            for Code in ReadJson:
                Group.Append(MusicDetailed(Code))
            return Group
