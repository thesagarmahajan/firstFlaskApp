from flask import jsonify
import psycopg2
import json
from psycopg2.extras import RealDictCursor

class crud:
    def __init__(self):
        print("This is CRUD Class Constructor")
        
        try:
            self.con = psycopg2.connect(dbname='mahajan_jewellers', user='postgres', host='localhost', password='123123', port=5432)
            self.cur = self.con.cursor(cursor_factory=RealDictCursor)
            print('Connection Opened Successfully')
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        print(self.con)
        
    def insert(self, data):
        try:
            self.cur.execute("INSERT INTO all_products(item_name, purchase_cost, selling_cost) VALUES (%s, %s, %s)",  (data['item_name'], int(data['purchase_cost']), int(data['selling_cost'])))
            self.con.commit()
            self.con.close()
            return "SUCCESS"
        except:            
            return "ERROR"
    
    def list(self, parameters):
        try:
            self.cur.execute("SELECT *, to_char(created_on, 'YYYY-MM-DD') as created_on FROM all_products")
            itemsList = self.cur.fetchall()  
            print(itemsList)
            self.con.commit()
            self.con.close()
            return json.dumps(itemsList, indent=2)
        except:
            return "ERROR"
    
    def update(self, data, parameters):
        updateQryStart = "UPDATE all_products SET "
        setSubString = ""
        updateQryEnd = " WHERE id="+parameters
        for k in data:
            setSubString += k+"='"+data[k]+"', "
        qry = updateQryStart+setSubString[:-2]+updateQryEnd
        
        try:
            self.cur.execute(qry)
            self.con.commit()
            self.con.close()
            if self.cur.rowcount==0:
                return "NothingToUpdate"
            else:
                return "UPDATED"
        except:
            return "ERROR"
    
    def delete(self, parameters):
        try:
            self.cur.execute("DELETE FROM all_products WHERE id=%s", (parameters))
            self.con.commit()
            self.con.close()
            return "DELETED"
        except psycopg2.DatabaseError as e:
            print(e)
            return "This is <h1>Delete</h1> from <strong>CRUD</strong> Class"
    