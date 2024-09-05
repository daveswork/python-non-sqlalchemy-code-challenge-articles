class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, "title"):
            self._title = new_title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0  and not hasattr(self, 'name'):
            self._name = new_name

    def articles(self):
        return [ article for article in Article.all if article.author is self ]

    def magazines(self):
        return list(set([ article.magazine for article in self.articles() ]))

    def add_article(self, magazine, title):
        return Article(
            author=self,
            magazine=magazine,
            title=title
        )

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        else:
            return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2<= len(new_name) <= 16):
            self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        return [ article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        my_articles = self.articles()
        ranking_authors = {}
        more_than_two = []

        for article in my_articles:
            if article.author in ranking_authors:
                ranking_authors[article.author] += 1
            else:
                ranking_authors[article.author] = 1
        for author in ranking_authors:
            if ranking_authors[author] > 2:
                more_than_two.append(author)
        
        if len(more_than_two) > 0:
            return more_than_two
        else:
            return None
        
    @classmethod
    def top_publisher(cls):
        if len(cls.all) == 0:
            return None
        maxed_magazine = None
        maxed_count = 0
        for magazine in cls.all:
            if len(magazine.articles()) > maxed_count:
                maxed_count = len(magazine.articles())
                maxed_magazine = magazine
        return maxed_magazine