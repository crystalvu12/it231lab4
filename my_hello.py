from datetime import datetime
import sqlite3

def hello_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    #mydtetme = datetime.now().ctime()
    
    #content='''<p>The time is now {} Surprise!'''.format(mydtetme)
    conn = sqlite3.connect("/home/cabox/workspace/dataparts/chinook.db")
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres")
 
    rows = cur.fetchall()
 
    rout=('''<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    margin: auto;
    table-layout:auto;
}
td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>
<table>
<caption><h2>Music Genres</h2></caption>
  <tr>
    <th>ID</th>
    <th>Name</th>
  </tr>''')
    
    for row in rows:
        # rowout='''<p>row {} name {}</p><br />'''.format(row[0],row[1])
        
        rowout='''<tr><td> {} </td><td> {} </td></tr>'''.format(row[0],row[1])
        
        rout = rout + rowout
        # rout.append(bytes(row,'UTF-8') ) 
    
    htmlclose=('''</table>
</body>
</html>''')
    
    rout = rout + htmlclose
    
    # print(rout)
    
    # The returned object is going to be printed
    # return [b"Hello World"]
    
    return[bytes(rout, 'UTF-8')]
