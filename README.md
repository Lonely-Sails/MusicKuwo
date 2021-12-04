# MusicKuwo
酷我音乐的 Python API 库。

`Pip install MusicKuwo`
##功能
> 1.搜索歌曲。
>
> 2.音乐搜索提示。
> 
> 4.下载音乐。
> 
> 5.下载音乐歌词。
> 
> 6.从网页下载二进制文件。
> 
> 7.获取音乐评论。

##文档
> ## Search
> `Search(Key, Page=1, Number=30) -> GroupMusic[Music, ……]`
> 
> 搜索音乐。
> 
> > `Key -> str`
> > 
> > 搜索音乐的关键字。
> 
> > `Page -> int`
> >
> > 搜索音乐的页数。
> 
> > `Number -> int`
> > 
> > 搜索音乐每页的个数。

> ## SearchPrompt
> `SearchPrompt(Key) -> List[str, ……]`
> 
> 音乐搜索的提示。
> 
> > `Key -> str`
> >
> > 获取音乐搜索提示的关键字。

> ## DownloadFile
>`DownloadFile(Path, Url) -> None`
> 
> 从链接下载文件。
> 
> > `Path -> str`
> >
> > 下载文件的保存位置。
> 
> > `Url -> str`
> > 
> > 要下载的链接。

> ## DownloadMusic
>`DownloadMusic(Path, Code) -> None`
> 
> 下载音乐。
> 
> > `Path -> str`
> >
> > 下载文件的保存位置。
> 
> > `Code -> str`
> > 
> > 下载音乐的 Code。

