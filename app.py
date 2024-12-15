from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input for the author, magazine, and article
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert new author, magazine, and article into the database
    try:
        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid  # Use this to fetch the id of the newly created magazine

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                       (article_title, article_content, author_id, magazine_id))

        # Commit the changes to the database
        conn.commit()

    except Exception as e:
        print(f"Error while inserting records: {e}")
        conn.rollback()
    
    # Fetch inserted data from the database
    try:
        # Query all magazines
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        # Query all authors
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        # Query all articles
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

    except Exception as e:
        print(f"Error while fetching records: {e}")

    finally:
        conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

if __name__ == "__main__":
    main()
