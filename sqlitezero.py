#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3
from sqlite3 import Error
 
from wsgiref.simple_server import make_server

from chinook_sql import sql_read_app
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_playlists(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM playlists")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_artists(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM artists")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = "chinook.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all playlists")
        select_playlists(conn)
 
        print("2. Query all artists")
        select_artists(conn)
 
 
if __name__ == '__main__':
    main()
    
    
'''
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"Hello World"]
'''
with make_server('', 3000, sql_read_app) as httpd:
    print("Serving on port 3000...")

    # Serve until process is killed
    httpd.serve_forever()
    
