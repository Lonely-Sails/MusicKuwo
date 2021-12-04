from urllib.parse import unquote

from MusicKuwo.Tools import *


class CommentAnswer:
    def __init__(self, InfoJson):
        self.Time = InfoJson['time']
        self.Content = InfoJson['msg']
        self.UserName = unquote(InfoJson['u_name'])
        self.ContentParser()

    def ContentParser(self):
        ParserComparison = {'[微笑]': '🙂', '[使坏]': '😁', '[大哭]': '😭', '[高兴]': '😃', '[猪头]': '🐷', '[大爱]': '😍',
                            '[尴尬]': '🤔', '[星星]': '✨'}
        for ParserKey in ParserComparison.keys():
            if ParserKey in self.Content:
                self.Content = self.Content.replace(ParserKey, ParserComparison[ParserKey])


class Comment(CommentAnswer):
    def __init__(self, InfoJson):
        CommentAnswer.__init__(self, InfoJson)
        self.CommentAnswer = None
        self.UserImage = InfoJson['u_pic']
        if 'reply' in InfoJson.keys():
            self.CommentAnswer = CommentAnswer(InfoJson['reply'])


class GroupComment:
    def __init__(self):
        self.Group = []

    def __iter__(self):
        return iter(self.Group)

    def Append(self, Item):
        DetectType('Item', Item, Comment)
        self.Group.append(Item)
