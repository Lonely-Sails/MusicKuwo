# MusicKuwo

酷我音乐的 Python 接口。  
可使用 `Pip install MusicKuwo` 来安装本模块。

***

## 功能

1. 搜索音乐和歌手；
2. 下载音乐以及对应的歌词；
3. 其他功能。

***

## 使用

本模块有内置示例，可直接使用。  
基于 MusicKuwo
模块的简易歌曲下载器：[示例源代码](https://github.com/XiaocaicaiGithub/MusicKuwo/tree/main/MusicKuwo/Domes/MusicDownload.py)

```python
from MusicKuwo.Domes import MusicDownload

if __name__ == '__main__':
    MusicDownload()
```

***

## 文档

使用 `import MusicKuwo` 来引入此模块。  
**注：此文档为 1.0.0 版本，与旧版并不兼容。**

### MusicKuwo.Core.SearchHints

函数构造：`SearchHints( Word: str ) -> list[str, ...]`  
此函数获取搜索提示词。

* 参数 `Word` 为传入词语的提示词，此参数可为空。

返回值为列表，列表里的元素均为字符串，获取失败返回 `None` 值。

### MusicKuwo.Core.SearchMusic

函数构造：`SearchMusic( Word: str, PageNumber: int, Page: int ) -> list[Music, ...]`   
此函数获取搜索音乐的结果。

* 参数 `Word` 为搜索音乐的名称，此参数不能为空。
* 参数 `PageNumber` 为搜索的每页数量，默认值为 30 。
* 参数 `Page` 为页面页数值，默认值为 1 。

返回值为列表，列表里的元素均为本模块的 `MusicKuwo.Objects.Music` 对象，列表长度取决于参数 `PageNumber` 。获取失败返回 `None`。

### MusicKuwo.Core.SearchArtist

函数构造：`SearchArtist( Word: str, PageNumber: int, Page: int ) -> list[Artist, ...]`   
此函数获取搜索歌手的结果。

* 参数 `Word` 为搜歌手的名字，此参数不能为空。
* 参数 `PageNumber` 为搜索的每页数量，默认值为 10 。
* 参数 `Page` 为页面页数值，默认值为 1 。

反回值为列表，列表里的元素均为本模块的 `MusicKuwo.Objects.Artist` 对象，列表长度取决于参数 `PageNumber` 。获取失败返回 `None`。

### MusicKuwo.Uitls.DownloadFile

函数构造：`DownloadFile( Url: str, Path: str, ChuckSize: int ) -> bool`  
此函数从网络上下载文件到本地。

* 参数 `Url` 为要下载的内容链接，此参数不能为空。
* 参数 `Path` 为你要下载的文件路径，不可为空。
* 参数 `ChuckSize` 为一次写入到文件里的字节区块大小，默认值为 2500 。

返回结果为 `True` 或者 `None` ，其中 `True` 代表下载成功，而 `None` 则代表下载失败。你可以很方便的用代码判断文件下载是否成功：

```python
from MusicKuwo.Uitls import DownloadFile

DownloadFlag = DownloadFile('https://h5static.kuwo.cn/www/kw-www/img/logo.7bf8751.png', './KuwoIcon.png')
if DownloadFlag:
    print('下载成功！')
else:
    print('下载失败！')
```

此代码将下载一个酷我音乐的标徽在本地，如下载成功将会打印 `下载成功！` 在控制台，反之则打印 `下载失败！` 。

### MusicKuwo.Objects.Music

#### Download

函数构造：`Download( self, Path: str )`  
此函数下载歌曲到本地。

* 参数 `Path` 为歌曲下载到本地的路径。

返回值和 `KuwoMusic.Uitls.DownloadFile` 的返回值同理。

#### DownloadLyrics

函数构造：`DownloadLyrics( self, Path: str, Encoding: str )`  
此函数把歌词文件下载到本地。

* 参数 `Path` 为歌词下载到本地的路径。
* 参数 `Encoding` 为下载的歌词文件的编码，默认为 `Gbk` 编码。

返回值和 `KuwoMusic.Uitls.DownloadFile` 的返回值同理。

### MusicKuwo.Objects.Artist

#### 初始函数

函数构造：`__init__( self, Code: int )`

* 参数 `Code` 为歌手编码，编码请参考文档最后，可为空。

#### LoadMore

函数构造：`LoadMore( self, Code: int )`  
此函数来加载更多的歌手信息，如所属国家和生日等。

* 参数 `Code` 为歌手编码，编码请参考文档最后，可为空，一般不填。

返回值为 `True` 或 `None`，返回 `True` 时代表加载成功，反之加载失败。

***

## 编码

编码为酷我音乐给歌手或歌曲等等的 `Id` ，在此模块统称为 `Code` 。  
编码为数值，如歌曲《 海市蜃楼 》的网址为 [https://kuwo.cn/play_detail/201737980](https://kuwo.cn/play_detail/201737980) 则此歌曲的 `Code`
就为 `201737980`；  
歌手三叔说的网址为 [https://kuwo.cn/singer_detail/4477027](https://kuwo.cn/singer_detail/4477027)，则 `Code`
为 `4477027` 。  
有些对象的 `Code` 无法通过网址获取，如评论等。  
在实际应用中很少用到，了解和不了解并没有太大区别。
