import sqlite3
import functools

query_cache = {}


def with_db_connection(func):
    """Decorator to handle opening and closing of database connection"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result

    return wrapper


def cache_query(func):
    """Decorator to cache query results based on the query string"""

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # extract query string (positional or keyword)
        query = None
        if args:
            # If first positional argument after conn is the query
            query = args[0] if len(args) > 0 else None
        if "query" in kwargs:
            query = kwargs["query"]

        if query in query_cache:
            print(f"Returning cached result for query: {query}")
            return query_cache[query]

        # Execute query if not cached
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print(f"Cached result for query: {query}")
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
