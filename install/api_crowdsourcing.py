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

        org_file = "%s%s" %(res[3], res[2])
        #org_file = org_file.encode('utf-8')

        txt_file = "../data/Responses/%d.txt" % res[1]
        file = open(txt_file, 'r') 
        txt =  file.read()
        txt = txt.replace("\n", "<br/>")

        result = "<div>%s</div><div>%s</div>" %(org_file, txt.decode('iso8859_15'))
        #result = "<div>%s</div>" % txt.decode('utf-8')

        return result

    except mdb.Error, e:
        return "Error %d: %s" % (e.args[0],e.args[1])


if __name__ == '__main__':
    app.run(host=config.FLASK['DOMAIN'],port=config.FLASK['PORT'],debug=True)
