from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import psycopg2

app = Flask(__name__)

con = psycopg2.connect(database="rateup", user="postgres", password="", host="127.0.0.1", port="5432")
print("Database opened successfully")


templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('HomePage.html')

@app.route("/signUp", methods = ["GET", "POST"])
def signUp():
    name = request.args.get("name")
    email = request.args.get("email")
    password = request.args.get("password")
    if (name): 
        cur = con.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES(%s, %s, %s);", (name, email, password))
        con.commit()
        cur.close()
        return render_template("HomePage.html", name = name)
    return render_template("SignUp.html")

@app.route("/signIn", methods = ["GET", "POST"])
def signIn():
    email = request.args.get("email")
    password = request.args.get("password")
    if (email):
        cur = con.cursor()
        cur.execute("select name, email, password from users")
        users = cur.fetchall()
        print(users)
        for user in users:
            if user[1] == email and user[2] == password:
                cur.close()
                return redirect("/")
            else:
                print('error')
    return render_template("SignIn.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)