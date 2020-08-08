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
import datetime #For dates
import typing

import re #For splitting strings
import collections #For sorting
import itertools #For sequential IDs
import random


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    unique_id = itertools.count(0) #Create an Iterable List of Objects

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        #Initialize variables
        self.id = next(self.unique_id) #Create the Unique ID

        #Define the Article's Attributes (based on the args)
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

        #Create the ISO Datetime String
        self.iso_datetime = self.publication_date.isoformat()


    def __repr__(self): #Repr Function to return a specific format
        '''
        Format:
        <Article title="Title" author='Author' publication_date='ISOTimeStamp'>
        '''

        return '<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.iso_datetime}\'>'.format(self=self) #Returns our text (using format())

    def __len__(self):  #Len function to return the length of content
        return len(self.content) 

    def short_introduction(self, n_characters): #Function to return a short introduction

        cut_string = self.content[:n_characters + 1] #Cut the original string based on our original number (n_characters)
        last_space = cut_string.rindex(' ') #Gets the index of the last space

        try: #Check to see if there is a line break
            last_line_break = cut_string.rindex('\n')
        except:
            last_line_break = 0

        #Checks whether the space is located further towards the end or if the line break is
        if last_space > last_line_break:
            last_char = last_space

        else:
            last_char = last_line_break


        return self.content[:last_char] #Cuts the content based on where the last space or linebreak was

    def most_common_words(self, num): #Function to return a dictionary of the most common words
        char_list = self.clear_list(self.content) #Splits the article content into list based on special characters that it finds
        return dict(collections.Counter(char_list).most_common(num)) #Returns a dictionary of the most common words

'''    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, new_value):
        self.content = new_value
        self.last_edited = datetime.datetime.now()'''


        

x = Article(
    title = "The emperor's new clothes",
    author = "Hans Christian Andersen",
    content = "'But he has nothing at all on!' at last cried out all the people.",
    publication_date = datetime.datetime(1837, random.randint(1, 12), random.randint(1, 7), 12, 15, 0)
)

y = Article(
    title = "The emperor's new clothes",
    author = "Hans Christian Andersen",
    content = "'But he has nothing at all on!' at last cried out all the people.",
    publication_date = datetime.datetime(1837, random.randint(1, 12), random.randint(1, 7), 12, 15, 0)
)




