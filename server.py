import psycopg2

con = psycopg2.connect(database="rateup", user="postgres", password="", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()


cur.execute(''' CREATE TABLE users
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        EMAIL    VARCHAR, 
        PASSWORD VARCHAR);''')

cur.execute(''' CREATE TABLE movies
        (ID SERIAL PRIMARY KEY,
        NAME     VARCHAR, 
        DIRECTOR    VARCHAR, 
        GENRE VARCHAR
        );
''')
print("Table created successfully!")

con.commit()
con.close()