"""
Factory Pattern - Practice Problem 3 (Intermediate)
====================================================

Database Connector (Simulation)
-------------------------------

We need to simulate connecting to different databases (SQLite, MySQL)
based on a configuration string. We WON'T use real databases.

The "connection" object should just interpret query strings differently.

Requirements:
1.  Implement a factory that parses a connection string (URL) and returns
    the appropriate database connection object.
    - e.g. "sqlite://..." -> SQLite Connection
    - e.g. "mysql://..." -> MySQL Connection
2.  The client code should treat all connections uniformly (e.g. `connect()`, `execute()`).
3.  Demonstrate connecting to both types and simulating a query execution.

Constraints & Tips:
- No `sqlite3` or `pymysql` imports! Just classes and print.
- Parse the string simply (e.g., string.startswith()).

Example Output:
---------------
Connecting to SQLite...
SQLite executing: SELECT * FROM users
"""
