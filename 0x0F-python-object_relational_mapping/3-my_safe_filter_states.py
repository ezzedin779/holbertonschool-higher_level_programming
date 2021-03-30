#!/usr/bin/python3
""" Gets all states with starting N from hbtn_0e_0_usa
Usage: ./1-filter_states.py <username> <password> <Database> """
import sys
import MySQLdb


if __name__ == "__main__":
    s = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    q = s.cursor()
    q.execute("SELECT * FROM `states`")
    for state in q.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
