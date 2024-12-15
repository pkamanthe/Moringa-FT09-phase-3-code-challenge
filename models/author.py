import sqlite3

class Author:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name
        if not id:
            self.create_author(name)
        
    def create_author(self, name):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        self._id = cursor.lastrowid
        self._name = name
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM articles WHERE author_id = ?
        ''', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT magazines.* FROM magazines
        JOIN articles ON articles.magazine_id = magazines.id
        WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines
