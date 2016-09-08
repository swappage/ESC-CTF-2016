#!/usr/bin/python

from flask import *
import json
import MySQLdb

with open ("config/dbconfig.json") as f:
        connect_params = json.load(f)

connect_params["db"] = "blog"

app = Flask(__name__)

MYSQL_SPECIAL_CHARS = [
        ("\\", "\\\\"),
        ("\0", "\\0"),
        ("\n", "\\n"),
        ("\r", "\\r"),
        ("'", "\\'"),
        ('"', '\\"'),
        ("\x1a", "\\Z"),
]

def mysql_escape(s):
        for find, replace in  MYSQL_SPECIAL_CHARS:
                s = s.replace(find, replace)
        return s

Response.charset = "shift-jis"
connect_params["charset"] = "sjis"

@app.route('/')
@app.route('/index')
def index():
        recipes = []
        db = MySQLdb.connect(**connect_params)
        cur = db.cursor()
        cur.execute("SELECT * FROM recipes")
        for row in cur.fetchall():
                dictionary = {}
                dictionary.update({'title' : row[1]})
                dictionary.update({'image' : row[2]})
                dictionary.update({'body' : row[3]})
                recipes.append(dictionary)
        return render_template("index.html", recipes=recipes)

@app.route('/recipe/<name>', methods = ["GET", "POST"])
def recipe(name):
        if request.method == "POST":
                name = request.form['name']
        recipe = []
        db = MySQLdb.connect(**connect_params)
        cur = db.cursor()
        escaped = mysql_escape(name)
        #print name
        #print escaped
        try:
                statement = 'SELECT * FROM recipes where name ="%s"' % escaped
                #print statement
                cur.execute(statement)
        except MySQLdb.Error, e:
                return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])

        row = cur.fetchone()
        dictionary = {}
        try:
                dictionary.update({'title' : row[1]})
                dictionary.update({'image' : row[2]})
                dictionary.update({'body' : row[3]})
                recipe.append(dictionary)
        except:
                pass

        return render_template("recipe.html", recipe=recipe)

if __name__ == '__main__':
        app.run(debug=False,host='0.0.0.0')
