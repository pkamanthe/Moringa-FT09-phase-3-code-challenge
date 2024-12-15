import sqlite3  # Add this import at the top of the file

class Article:
    def __init__(self, title, content, author, magazine):
        """
        Initialize an article.

        :param title: The title of the article.
        :param content: The content of the article.
        :param author: The Author object associated with the article.
        :param magazine: The Magazine object associated with the article.
        """
        self._title = title
        self._content = content
        self._author = author  # Store the Author object
        self._magazine = magazine  # Store the Magazine object
        self.create_article()

    def create_article(self):
        """
        Insert the article into the database.
        """
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        # Use author's and magazine's ids from the passed objects
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                       (self._title, self._content, self._author.id, self._magazine.id))
        conn.commit()
        self._id = cursor.lastrowid  # Get the last inserted ID
        conn.close()
