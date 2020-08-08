import itertools
import qualifier
import datetime
import gc

x = []

for i in range(0 , 5):
    
    article = qualifier.Article(
            title="a", author="b", content="c", publication_date=datetime.datetime.now()
            )
    print(article.id)