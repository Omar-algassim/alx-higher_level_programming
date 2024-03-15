#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    state = cur.execute("SELECT * FROM states")
    row = cur.fetchall()
    for i in row:
        print(i)
    
    cur.close()
    db.close()
    