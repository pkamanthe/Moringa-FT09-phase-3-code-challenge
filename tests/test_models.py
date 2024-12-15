import sqlite3
import unittest
from models.author import Author
from models.magazine import Magazine
from models.article import Article

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.conn = sqlite3.connect(":memory:")
        cursor = cls.conn.cursor()

     
        cursor.execute("""
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(id)
        )
        """)
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_author_creation(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES ('Jane Smith')")
        self.conn.commit()
        cursor.execute("SELECT * FROM authors WHERE name = 'Jane Smith'")
        author = cursor.fetchone()
        self.assertIsNotNone(author)  

    def test_magazine_creation(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO magazines (title, category) VALUES ('Health Monthly', 'Health')")
        self.conn.commit()
        cursor.execute("SELECT * FROM magazines WHERE title = 'Health Monthly'")
        magazine = cursor.fetchone()
        self.assertIsNotNone(magazine) 

    def test_article_creation(self):
        cursor = self.conn.cursor()

        
        cursor.execute("INSERT INTO authors (id, name) VALUES (1, 'John Doe')")
        cursor.execute("INSERT INTO magazines (id, title, category) VALUES (1, 'Tech Weekly', 'Technology')")
        self.conn.commit()

        
        cursor.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES ('Test Title', 'Test Content', 1, 1)
        """)
        self.conn.commit()

       
        cursor.execute("SELECT * FROM articles WHERE title = 'Test Title'")
        article_data = cursor.fetchone()
        self.assertIsNotNone(article_data) 
