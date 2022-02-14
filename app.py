# coding: utf-8
import MySQLdb
from flask import Flask


app = Flask(__name__)

@app.route("/test")
def test1():
    conn = MySQLdb.connect(user='ns2pole',passwd='ns2pole0306',host='mysql717.db.sakura.ne.jp', db='ns2pole_data_base')
    cursor = conn.cursor()
    sql = "insert into name_age_list values('5', 'test3', '10')"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return "2211"

if __name__ == "__main__":
    app.run(debug=True)
