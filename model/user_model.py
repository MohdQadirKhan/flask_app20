
from unicodedata import name
import mysql.connector 
import json 

class user_model():
    def __init__(self):
             
     
     try:
        self.con=mysql.connector.connect(host="localhost", user="root", password="Access179",database="aman")
        
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        print("connection successfull")
     except:
        print("some error")
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM info")
        result = self.cur.fetchall()
        print(result)
        if len(result)>0:
            return json.dumps(result) 
        else:
            return "no data found"
    def user_addone_model(self,data): 
        print(data)   
        self.cur.execute(f"INSERT INTO info(id,name,phone,clg) values({data['id']},'{data['name']}',{data['phone']},'{data['clg']}')")
        return "user created successfully"
    def user_update_model(self,data):    
        self.cur.execute(f"UPDATE info SET name='{data['name']}', phone={data['phone']} , clg='{data['clg']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
         return "user update successfully" 
        else:
            return "Nothing update"
    def user_delete_model(self,id):    
        self.cur.execute(f"DELETE FROM info WHERE id=={id}")
        if self.cur.rowcount>0:
         return "user delete successfully" 
        else:
            return "Nothing update"    