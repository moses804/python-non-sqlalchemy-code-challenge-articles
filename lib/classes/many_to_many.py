class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
            
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        # Ignore assignment to maintain immutability
        pass

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        # Ignore assignment to maintain immutability
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories)) if categories else None

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
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            # If invalid, don't change the value
            return
        self._name = value
        
    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            # If invalid, don't change the value
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
            
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None