import datetime
import typing
import re
import collections
import itertools

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
        self._content = content

        #Create the ISO Datetime String
        self.iso_datetime = self.publication_date.isoformat()
        self.last_edited = None

        self.compare_datetime = self.publication_date.timestamp()

    
    def clear_list(self, string): #Function to split list into string and remove any special characters
        string = re.split(',|_|-|!| |\'|\n', string.lower()) #Split the string based on any special characters

        for char in string.copy(): #Iterate over a copy of the string (so that you can remove items)
            if char == '': #We cannot check for empty strings in the split function
                string.remove(char) #If it is an empty string, remove it from the original list

            elif '.' in char: #'.' (period) would not work with re.split, so I need to check it individually
                string[string.index(char)] = char.replace('.', '') #remove the '.'
        'I did not use enumerate() because I removing items from one list and iterating over a copy of another list'
        return string #Return our new list


    def __repr__(self): #Repr Function to return a specific format
        '''
        Format:
        <Article title="Title" author='Author' publication_date='ISOTimeStamp'>
        '''

        return '<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.iso_datetime}\'>'.format(self=self) #Returns our text (using format())

    def __len__(self):  #Len function to return the length of content
        return len(self._content) 

    def short_introduction(self, n_characters): #Function to return a short introduction

        cut_string = self._content[:n_characters + 1] #Cut the original string based on our original number (n_characters)
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


        return self._content[:last_char] #Cuts the content based on where the last space or linebreak was

    def most_common_words(self, num): #Function to return a dictionary of the most common words
        char_list = self.clear_list(self._content) #Splits the article content into list based on special characters that it finds
        return dict(collections.Counter(char_list).most_common(num)) #Returns a dictionary of the most common words


    @property
    def content(self):
      return self._content

    @content.setter
    def content(self, new_content):
      self._content = new_content
      self.last_edited = datetime.datetime.now()

    def __eq__(self, other_article):
      if self.compare_datetime == other_article.compare_datetime:
        return True

      else:
        return False

    def __gt__(self, other_article):
      if self.compare_datetime > other_article.compare_datetime:
        return True

      else:
        return False



        






      

      
