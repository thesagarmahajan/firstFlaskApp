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
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        finally:
            print('Connection Opened Successfully')
        print(self.con)
        
    def insert(self, data):
        return jsonify(data)
    
    def list(self, parameters):
        self.cur.execute("SELECT *, to_char(created_on, 'YYYY-MM-DD') as created_on FROM all_products")
        itemsList = self.cur.fetchall()  
        print(itemsList)
        self.cur.close()
        self.con.close()
        return json.dumps(itemsList, indent=2)
    
    def update(self, data, parameters): #
        return "This is <h1>Update</h1> from <strong>CRUD</strong> Class"
    
    def delete(self, parameters):
        return "This is <h1>Delete</h1> from <strong>CRUD</strong> Class"
    