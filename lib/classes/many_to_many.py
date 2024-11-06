class Article:
    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("title must be a string")
        elif len(value_to_validate) not in range(5, 50):
            raise ValueError("title must be a string between 5 and 50 characters.")
        elif hasattr(self, "_title"):
            raise AttributeError("name cannot be initialized")
        self._title = value_to_validate
        


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("name is not a string")
        elif not len(value_to_validate):
            raise ValueError("Name must be a non-empty string.")
        elif hasattr(self, "_name"):
            raise AttributeError("Name is immutable and cannot be changed.")
        self._name = value_to_validate

    def articles(self):
        return[article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        #! recieves a magazine instance, and a title as arguments
        #! creates and returns a new Article instance and associates it with author, magazine provided
        return Article(self, magazine, title)

    def topic_areas(self):
        #! retunrs a unique list with categories of the magazines the author and returns non if the author has no articles
        return list({magazine.category for magazine in self.magazines()}) if self.articles() else None

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("name must be a string")
        elif len(value_to_validate) not in range(2,16):
            raise ValueError("name must be between 2 and 17 characters, inclusive")
        self._name = value_to_validate

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("category is not a string")
        elif not len(value_to_validate):
            raise ValueError("category must be longer than 0 characters")
        self._category = value_to_validate

    def articles(self):
        return [article for article in Article.all if article.magazine is self]


    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None

    def contributing_authors(self):
         # Returns authors with more than 2 articles in this magazine
        author = {}
        for article in self.articles():
            author[article.author] = author.get(article.author, 0) + 1
        return [author for author, count in author.items() if count > 2] or None  # Returns None if no authors meet the criteria
