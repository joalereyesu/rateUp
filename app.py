from os import error
from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import psycopg2




app = Flask(__name__)

con = psycopg2.connect(database="rateup", user="postgres", password="papalina", host="127.0.0.1", port="5432")
print("Database opened successfully")


templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

def getUserInfo(username):
    cur = con.cursor()
    cur.execute("select id, name, email, password from users")
    users = cur.fetchall()
    for user in users:
            print(user[0])
            if user[1] == username:
                cur.close()
                return user


@app.route("/signUp", methods = ["GET", "POST"])
def signUp():
    username = request.args.get("name")
    email = request.args.get("email")
    password = request.args.get("password")
    if (username): 
        cur = con.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES(%s, %s, %s);", (username, email, password))
        con.commit()
        cur.close()
        return redirect(url_for('home', username=username))
    return render_template("SignUp.html")

@app.route("/signIn", methods = ["GET", "POST"])
def signIn():
    username = request.args.get("username")
    password = request.args.get("password")
    if (username):
        cur = con.cursor()
        cur.execute("select name, email, password from users")
        users = cur.fetchall()
        print(users)
        print(users[0])
        for user in users:
            if user[0] == username and user[2] == password:
                cur.close()
                return redirect(url_for('home', username=user[0]))
            else:
                return page_not_found(401)
    return render_template("SignIn.html")

@app.route("/homepage/<username>", methods = ["GET", "POST"])
def home(username):
    return render_template('MovieHP.html', username = username)

@app.route("/deleteUser/<name>", methods = ["GET", "DELETE"])
def deleteUser(name):
    cur = con.cursor()
    userInfo = getUserInfo(name)
    print(userInfo)
    if userInfo[1] == name:
        user_id = userInfo[0]
        cur.execute("DELETE from users where id = %s;", (user_id,))
        con.commit()
        return redirect(url_for("signUp"))

@app.route("/deleteMovie/<name>", methods = ["DELETE"])
def deleteMovie(name):
    cur = con.cursor()
    cur.execute("select id, name from movies")
    movies = cur.fetchall()
    for movie in movies:
            if movie[1] == name:
                movie_id = movie[0]
                cur.execute("DELETE from movies where id = %s;", (movie_id,))
                con.commit()
                cur.close()
                print("Success!")

@app.route("/movies/<username>", methods = ["GET"])
def movies(username):
    return render_template("Movies.html", username=username)

@app.route("/tvshows/<username>", methods = ["GET"])
def tvshows(username):
    return render_template("tvShows.html", username = username)

@app.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username):
    user = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")
    newInfo = [user, email, password]
    print(newInfo)
    if (user and email and password):
        return redirect(url_for("editProfile", username = username, user = user, email = email, password = password))
    return render_template("profile.html", username = username)

@app.route("/editProfile/<username>/<user>/<email>/<password>")
def editProfile (username, user, email, password):
    userInfo = getUserInfo(username)
    print(userInfo)
    cur = con.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s", (user, email, password, userInfo[0]))
    con.commit()
    return redirect(url_for("signIn"))

@app.route("/insert", methods = ["GET", "POST"])
def insert():
    name = "The Eternals"
    director = ""
    cur = con.cursor()
    cur.execute("INSERT INTO popular (name, director, genre) VALUES(%s, %s, %s);", (username, email, password))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_found.html'), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True)
