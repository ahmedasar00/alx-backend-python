import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print("Connection closed.")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False


if __name__ == "__main__":
    db_name = "../python-decorators-0x01/test_users.db"
    with DatabaseConnection(db_name) as cusor:
        cusor.execute("SELECT * FROM users")
        rows = cusor.fetchall()
        print("Query result:")
        for row in rows:
            print(rows)
