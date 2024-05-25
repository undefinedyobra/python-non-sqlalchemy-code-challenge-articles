class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) in range(5, 51) and not hasattr(self, "_title"):
            self._title = title
        # else:
        #     raise ValueError("Title must be between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def articles(self):
        pass
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        pass
        return list({
            article.magazine for article in Article.all if article.author is self
        })

    def add_article(self, magazine, title):
        pass
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        pass
        categories = {article.magazine.category for article in Article.all if article.author is self}
        return list(categories) if categories else None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
        # else:
        #     raise ValueError("Names must be longer than 0 characters")


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all.append(self)

    def articles(self):
        pass
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        pass
        authors = {article.author for article in self.articles() if isinstance(article.author, Author)}
        return list(authors) if authors else None



    def article_titles(self):
        pass
        titles = [article.title for article in self.articles()]
        return titles if titles else None


    def contributing_authors(self):
        pass
        authors = [article.author for article in self.articles()]
        qualified_authors = [author for author in authors if authors.count(author) > 2]
        return qualified_authors if qualified_authors else None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(2, 17):
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category