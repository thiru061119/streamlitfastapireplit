from fastapi import FastAPI
#import psycopg2
from pydantic import BaseModel
import os
from supabase import create_client, Client

url ='https://mjxobygptnklpkdktkjf.supabase.co'   #url: str = os.environ.get("SUPABASE_URL")
key='sb_publishable_IVQGvbPJE8dbRjB6ERNodg_K2WDuTpI'   # key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app=FastAPI()
#host='mjxobygptnklpkdktkjf.supabase.co',
class User(BaseModel):
    name: str
    age: int
    #mjxobygptnklpkdktkjf
#conn=psycopg2.connect(host='db.mjxobygptnklpkdktkjf.supabase.co',database='postgres',user='postgres',password='IEq3UmvSo6sYfF5k',port=5432,sslmode="require")
#cursor = conn.cursor()

@app.get("/test")
def root():
    return {"message": "FastAPI running on Replit"}

@app.post("/users")
#def create_user(name:str,age:int):
def create_user(user:User):
  response = (supabase.table("users").insert({"name": user.name, "age": user.age}).execute())  
#  cursor.execute('insert into users (name,age) values (%s, %s)',(user.name,user.age))
#  conn.commit
  return {'message':'User Saved'}
@app.get("/userdata")
def get_users():
  #cursor.execute("select name,age from users")
  response = (supabase.table("users").select("*").execute())  
  #return [response.json()]
  return [response]
  


