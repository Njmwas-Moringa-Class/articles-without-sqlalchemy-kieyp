import unittest
import ipdb  # Import the ipdb module
from Article import Article
from Magazine import Magazine  # Assuming your Magazine class is in a file named 'magazine.py'

class TestMagazineClass(unittest.TestCase):

    def setUp(self):
        # Create instances for testing
        self.magazine1 = Magazine("Magazine1", "Tech")
        self.magazine2 = Magazine("Magazine2", "Science")

    def test_find_by_name(self):
        # Test finding a magazine by name
        ipdb.set_trace()  # Set a breakpoint using ipdb
        self.assertEqual(Magazine.find_by_name("Magazine1"), self.magazine1)
        self.assertEqual(Magazine.find_by_name("Magazine2"), self.magazine2)
        self.assertIsNone(Magazine.find_by_name("NonexistentMagazine"))

    def test_article_titles(self):
        # Test retrieving article titles for a magazine
        ipdb.set_trace()  # Set a breakpoint using ipdb
        self.assertEqual(Magazine.article_titles("Magazine1"), [])
        
        # Add a published article to Magazine1
        article1 = Article("Article1", "Author1")
        self.magazine1.published_articles.append(article1)
        self.assertEqual(Magazine.article_titles("Magazine1"), ["Article1"])

    # ... (similar breakpoints in other test methods)

if __name__ == '__main__':
    unittest.main()
