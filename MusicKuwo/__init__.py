"""
Copyright (c) 2021 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '0.1.1'
__title__ = 'MusicKuwo'
__author__ = 'Xiaocaicai'
__author_email__ = 'xiaocaicai_email@sina.com'
__description__ = 'Kuwo music Python API package.'
__url__ = 'https://github.com/xiaocaicai-github/MusicKuwo/'
__all__ = ['RequestError', 'DownloadFile', 'SearchPrompt', 'Search']

from sys import version

from MusicKuwo.Errors import *

PythonVersion = version[0:5]
if PythonVersion[0] != '3':
    raise PythonVersionError(
        F'Your Python version is {PythonVersion}, but this module only applies to Python3 versions.')

from MusicKuwo.Core import DownloadFile, SearchPrompt, Search
