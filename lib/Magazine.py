# magazine.py

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.additional_info = {}
        self.published_articles = []
        self.__class__.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls.all_magazines

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all_magazines if magazine.name == name), None)

    @classmethod
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title for article in magazine.published_articles]
        else:
            return []

    def contributing_authors(self):
        authors_count = {}
        for article in self.published_articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    def update_info(self, key, value):
        self.additional_info[key] = value

    def contributors(self):
        return list(set(article.author for article in self.published_articles))

    def __str__(self):
        return f"Magazine: {self._name}, Category: {self._category}, Additional Info: {self.additional_info}"
