from MusicKuwo import SearchMusic


class MusicDownload(object):
    Name = None
    Path = None
    Musics = None

    def __init__(self):
        self.Name = input('请输入你要下载的歌曲名称：')
        self.Path = input('请输入你要下载的歌曲的储存位置：')
        print()
        self.Search()
        print()
        self.Download()

    def Search(self):
        Number = 0
        self.Musics = SearchMusic(self.Name)
        for Music in self.Musics:
            Number += 1
            print(F'{Number:0>2} 名称：{Music.Name} 歌手：{Music.Artist.Name}')

    def Download(self):
        Number = input('请输入你要下载的歌曲编号：')
        if self.Musics[int(Number) - 1].Download(self.Path):
            print('下载歌曲成功！')
            return None
        print('下载歌曲失败！')


if __name__ == '__main__':
    MusicDownload()
