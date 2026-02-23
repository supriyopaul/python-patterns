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

from typing import Protocol

class DBConnector(Protocol):
    
    def connect(self):
        pass
    
    def execute(self, connection, sql_string:str):
        pass


def parse_connection_url(url):
    sql_type = url.split("://")[0]
    host_port = url.split("://")[1]
    host = host_port.split(':')[0]
    port = host_port.split(':')[1]
    return (sql_type.lower(), host.lower(), port.lower())

class SQLiteConnector():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_connected = False
    
    def connect(self):
        if self.host and self.port:
            print("Connecting to SQLite at {host}:{port}".format(host=self.host, port=self.port))
            self.is_connected = True
    
    def execute(self, sql_string:str):
        if not self.is_connected:
            self.connect()
        print("SQLite executing sql: {sql_string}".format(sql_string=sql_string))


class MySQLConnector():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_connected = False
    
    def connect(self):
        if self.host and self.port:
            print("Connecting to MySQL at {host}:{port}".format(host=self.host, port=self.port))
            self.is_connected = True
    
    def execute(self, sql_string:str):
        if not self.is_connected:
            self.connect()
        print("MySQL executing sql: {sql_string}".format(sql_string=sql_string))

def get_db_connector(url:str):
    connection_info = parse_connection_url(url)
    db_type = connection_info[0]
    host = connection_info[1]
    port = connection_info[2]

    if db_type == "sqlite":
        return SQLiteConnector(host=host, port=port)
    elif db_type == "mysql":
        return MySQLConnector(host=host, port=port)
    else:
        raise ValueError("Invalid SQL type: {db_type}".format(db_type=db_type))

if __name__ == '__main__':
    url1 = 'sqlite://localhost:5132'
    url2 = 'mysql://remote-server:3306'
    sqlite_connection = get_db_connector(url1)
    mysql_connection = get_db_connector(url2)

    sqlite_connection.execute("Select * from users limit 10;")
    mysql_connection.execute("Select * from customers limit 5;")
