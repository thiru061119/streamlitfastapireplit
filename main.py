from fastapi import FASTAPI
import psycopg2
from pydantic import BaseModel
import os
app=FASTAPI()
#host='mjxobygptnklpkdktkjf.supabase.co',
class User(BaseModel):
    name: str
    age: int
    #mjxobygptnklpkdktkjf
conn=psycopg2.connect(
                      host='mjxobygptnklpkdktkjf.supabase.co',
                      database='postgres'.
                      user='postgres',
                      password='IEq3UmvSo6sYfF5k',
                      port=5432)
cursor = conn.cursor()

@app.get("/test")
def root():
    return {"message": "FastAPI running on Replit"}

@app.post("/users")
#def create_user(name:str,age:int):
def create_user(user:User)
  cursor.execute(insert into users (name,age) values (%s, %s),(user.name,user.age))
  conn.commit
  return {'message':'User Saved'}
@app.get("/userdata")
def get_users():
  cursor.execute("select name,age from users")
  rows=cursor.fetchall()
  return [{'name': r[0], 'age': r[1]} for r in rows]
  


