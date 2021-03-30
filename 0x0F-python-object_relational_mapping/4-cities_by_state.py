#!/usr/bin/python3
""" Gets all states with starting N from hbtn_0e_0_usa
Usage: ./1-filter_states.py <username> <password> <Database> """
import sys
import MySQLdb


if __name__ == "__main__":
    s = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    q = s.cursor()
    q.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                FROM `cities` INNER JOIN `states` \
                ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    for city in q.fetchall():
        print(city)
