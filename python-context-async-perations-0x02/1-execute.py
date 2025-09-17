import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, parms=None):
        self.db_name = db_name
        self.query = query
        self.parms = parms or ()
        self.connection = None
        self.cursor = None
        self.resuts = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.parms)
        self.resuts = self.cursor.fetchall()
        return self.resuts

    def __exit__(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
        return False


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age> ?"
    parms = (25,)
    with ExecuteQuery(
        "../python-decorators-0x01/test_users.db", query, parms
    ) as results:
        print("Query result:")
        for row in results:
            print(row)
