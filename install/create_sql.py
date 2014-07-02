#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import config
import os 
import json


def open_json(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except:
        sys.stderr.write("ERROR: Could not open file %s in dir %s" % (filename, dirpath))
        exit(1)





try:
    con = mdb.connect(config.MYSQL['HOST'], config.MYSQL['USER'], config.MYSQL['PSWD'], config.MYSQL['DATABASE'], charset='utf8')
    cur = con.cursor()

    #cur.execute("SELECT VERSION()")

    #ver = cur.fetchone()
    #print "Database version : %s " % ver

    
    cur.execute("SET NAMES utf8;")

    cur.execute("DROP TABLE IF EXISTS task ")
    cur.execute("CREATE TABLE task (id int(10) auto_increment, file_name varchar(250), format varchar(50), id_document int(10), lang varchar(50), line_nb int(10),path varchar(250),  PRIMARY KEY(id)) DEFAULT CHARSET=utf8");

    res = cur.fetchone();

    tasks = open_json("rep.json")
    for task in tasks:

        try:
            query = "INSERT INTO task (file_name, format, id_document, lang, line_nb, path) VALUES (\"%s\", \"%s\", %s, \"%s\", %s, \"%s\")" \
                % (task['file_name'], task['format'], task['id'], task['lang'], task['line_nb'], task['path'])
            print query
        
            cur.execute(query);
            res = cur.fetchone()
        except:
            with open("error.txt", 'a') as myFile:
                myFile.write("%s\n"%task)

    cur.execute("SELECT COUNT(*) FROM task")
    res = cur.fetchone()
    print "il y a %d lignes\n" % res
                





except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

#finally:
#    if con:
#        print "Closing Connection \n"
#        con.close()
cur.execute("SELECT * FROM task")
rows = cur.fetchall()
for row in rows:
    print row

con.commit()
 
con.close()


con = mdb.connect(config.MYSQL['HOST'], config.MYSQL['USER'], config.MYSQL['PSWD'], config.MYSQL['DATABASE'], charset='utf8')
cur = con.cursor()
cur.execute("SELECT count(*) FROM task")
rows = cur.fetchall()
for row in rows:
    print row
 
con.close()



