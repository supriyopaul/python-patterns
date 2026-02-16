"""
Factory Pattern - Practice Problem 3 (Intermediate)
====================================================

Database Connector (Simulation)
-------------------------------

We need to simulate connecting to different databases (SQLite, MySQL)
based on a configuration string. We WON'T use real databases.

The "connection" object should just interpret query strings differently.

Requirements:
1.  Define a `Database` interface with `connect()` and `execute(query)`.
2.  Create `SQLiteDatabase` and `MySQLDatabase` classes.
    - `SQLiteConnection`'s execute() should print: "SQLite executing: [query]"
    - `MySQLConnection`'s execute() should print: "MySQL executing: [query]"
3.  Create a `DatabaseFactory` that takes a "connection_string" (url).
    - If url starts with "sqlite://", return SQLiteDatabase.
    - If url starts with "mysql://", return MySQLDatabase.
4.  Demonstrate connecting simulating a query execution.

Constraints & Tips:
- No `sqlite3` or `pymysql` imports! Just classes and print.
- Parse the string simply (e.g., string.startswith()).

Example Output:
---------------
Connecting to SQLite...
SQLite executing: SELECT * FROM users
"""
