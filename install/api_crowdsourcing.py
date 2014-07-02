# -*- coding:utf-8 -*-

from flask import Flask,request
import MySQLdb as mdb
import config






app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

@app.route('/api/random_task')
def print_random_task():
    try:
        con = mdb.connect(config.MYSQL['HOST'], config.MYSQL['USER'], config.MYSQL['PSWD'], config.MYSQL['DATABASE'], charset='utf8')
        cur = con.cursor()
        cur.execute("SELECT id, id_document, file_name, path FROM task order by rand() LIMIT 0,1")
        res = cur.fetchone()

        txt_file = "../data/Responses/%d.txt" % res[1]
        #txt_file = "../data/Responses/%d.txt" % res['id_document']
        file = open(txt_file, 'r') 
        return file.read()

    except mdb.Error, e:
        return "Error %d: %s" % (e.args[0],e.args[1])


if __name__ == '__main__':
    app.run(host=config.FLASK['DOMAIN'],port=config.FLASK['PORT'],debug=True)
