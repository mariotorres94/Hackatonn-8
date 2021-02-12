from conection.conn import Conexion
from helpers.helper import handler_response
from flask import json

c = Conexion()

class Client:
    def read_all_clients(self,app):
        try:
            c.conn = Conexion()
            query = f'''
                SELECT * FROM cliente;
            '''
            result = c.conn.execute_query(query)
            result_json = []
            for i in result:
                client = {
                    'id_cliente': i[0],
                    'nombres': i[1], 
                    'apellido_pat': i[2],
                    'apellido_mat': i[3],
                    'direccion': i[4],
                    'celular': i[5]
                }
                result_json.append(client)
            return handler_response(app, 200, 'Data client', True, result_json)
        except Exception as err:
            return handler_response(app, 501, str(err))