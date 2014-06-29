#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import config

try:
    con = mdb.connect(config.MYSQL['HOST'], config.MYSQL['USER'], config.MYSQL['PSWD'], config.MYSQL['DATABASE'])
    cur = con.cursor()

    #cur.execute("SELECT VERSION()")

    #ver = cur.fetchone()
    #print "Database version : %s " % ver

    cur.execute("CREATE TABLE task (id int(10), PRIMARY KEY(id))");



except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()

