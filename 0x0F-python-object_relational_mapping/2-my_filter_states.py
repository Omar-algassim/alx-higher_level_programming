#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    name = sys.argv[4]
    print ("SELECT * FROM states WHERE name = {} ORDER BY id".format(sys.argv[4]))
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(sys.argv[4]))
    state = cur.fetchall()
    for i in state:
        print(i)

    cur.close()
    db.close()
