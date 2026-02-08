from fastapi import FASTAPI
import psycopg2
app=FASTAPI()
conn=psycopg2.connect(host='https://mjxobygptnklpkdktkjf.supabase.co',
                      database='streamlit-fastapi-demo'.
                      user='postgres',
                      password='IEq3UmvSo6sYfF5k',
                      port=5432)
cursor = conn.cursor()
@app.post("/users")
def create_user(name:str,age:int):
  cursor.execute(insert into users (name,age) values (%s, %s),(name,age))
  conn.commit
  return {'message':'User Saved'}
@app.get("/userdata")
def get_users():
  cursor.execute("select name,age from users")
  rows=cursor.fetchall()
  return [{'name": r[0], 'age": r[1]} for r in rows]
  


