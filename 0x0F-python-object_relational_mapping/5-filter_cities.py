#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    name = sys.argv[4]
    cur.execute("SELECT cities.name FROM\
                cities JOIN states ON states.id=cities.state_id WHERE \
                    states.name = '{}'".format(name))
    state = cur.fetchall()
    count = 0
    for i in state:
        count += 1
        print(i[0], end="")
        if count < len(state):
            print(", ", end="")
    print("")
    cur.close()
    db.close()
