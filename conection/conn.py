import os
from psycopg2 import connect
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Conexion:
    def __init__(self):
        self.conn = connect(database=os.getenv('DB_NAME'),user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),host=os.getenv('DB_HOST'),
                    port=os.getenv('DB_PORT'))
        self.cursor = self.conn.cursor()

    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor

    def close_connection(self):
        return self.conn.close()

    def commit(self):
        self.conn.commit()
        return True
    
    def rollback(self):
        self.conn.rollback()
        return True