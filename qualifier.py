"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re
import collections

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        #Initialize variables
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

        self.iso_datetime = self.publication_date.isoformat()

    def clear_list(self, string):
        string = re.split(',|_|-|!| |\'|\n', string.lower())

        for char in string.copy():
            if char == '':
                string.remove(char)

            elif '.' in char:
                string[string.index(char)] = char.replace('.', '')

        return string


    def __repr__(self):
        '''
        Format:
        <Article title="Title" author='Author' publication_date='ISOTimeStamp'>
        '''

        return '<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.iso_datetime}\'>'.format(self=self)

    def __len__(self):  
        return len(self.content)

    def short_introduction(self, n_characters):
        cut_string = self.content[:n_characters + 1]
        last_space = cut_string.rindex(' ')

        try:
            last_line_break = cut_string.rindex('\n')
        except:
            last_line_break = 0

        if last_space > last_line_break:
            last_char = last_space

        else:
            last_char = last_line_break


        return self.content[:last_char]

    def most_common_words(self, num):
        char_list = self.clear_list(self.content)
        return dict(collections.Counter(char_list).most_common(num))


