import psycopg2

con = psycopg2.connect(database="rateup", user="postgres", password="papalina", host="localhost", port="5432")
print("Database opened successfully")

cur = con.cursor()


cur.execute(''' CREATE TABLE users
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        EMAIL    VARCHAR, 
        PASSWORD VARCHAR, 
        RATING int);''')

cur.execute(''' CREATE TABLE movies
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        DIRECTOR    VARCHAR, 
        GENRE VARCHAR
        );''')

cur.execute(''' CREATE TABLE tvshows
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        DIRECTOR    VARCHAR, 
        GENRE VARCHAR
        );''')

cur.execute(''' CREATE TABLE popular
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        DIRECTOR    VARCHAR, 
        GENRE VARCHAR
        );''')

print("Table created successfully!")

con.commit()
con.close()