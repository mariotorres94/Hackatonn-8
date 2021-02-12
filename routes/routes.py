from flask import Flask, render_template, request, redirect, url_for
from conection.conn import Conexion
from helpers.helper import handler_response
from classes.clientes import Client

c = Conexion()

cli = Client()

app = Flask(__name__)

def routes(app):
    @app.route('/')
    def home():
        return render_template('menu_cajero.html')

    @app.route('/crear_cliente', methods=['GET','POST'])
    def crear_cliente():
        if request.method == 'POST':
            nombres = request.form['nombres']
            apellido_pat = request.form['apellido_pat']
            apellido_mat = request.form['apellido_mat']
            direccion = request.form['direccion']
            celular = request.form['celular']
            
            c.conn = Conexion()
            c.cursor = c.conn.cursor
            c.cursor.execute("INSERT INTO cliente(nombres,apellido_pat,apellido_mat,direccion,celular) VALUES(%s,%s,%s,%s,%s)",(nombres,apellido_pat,apellido_mat,direccion,celular))
            c.conn.commit()
            
            return redirect(url_for('crear_cliente'))

        return render_template('registro_cliente.html')

    @app.route('/edit/<id_cliente>')
    def edit_client(id_cliente):
        c.conn = Conexion()
        c.cursor = c.conn.cursor
        c.cursor.execute('SELECT * FROM cliente WHERE id_cliente = {0}'.format(id_cliente))
        data = c.cursor.fetchall()       

        return render_template('edit_client.html', client=data[0])

    @app.route('/update/<id_cliente>', methods=['POST'])
    def update_client(id_cliente):
        c.conn = Conexion()
        if request.method == 'POST':

            nombres = request.form['nombres']
            apellido_pat = request.form['apellido_pat']
            apellido_mat = request.form['apellido_mat']
            direccion = request.form['direccion']
            celular = request.form['celular']
            c.cursor = c.conn.cursor
            c.cursor.execute("""
                UPDATE cliente 
                SET nombres=%s,
                    apellido_pat=%s,
                    apellido_mat=%s,
                    direccion=%s,
                    celular=%s
                WHERE id_cliente=%s
            """, (nombres,apellido_pat,apellido_mat,direccion,celular,id_cliente))
            c.conn.commit()
            return redirect(url_for('read_all_clients'))

    @app.route('/delete/<string:id_cliente>')
    def delete_client(id_cliente):
        c.cursor = c.conn.cursor
        c.cursor.execute("DELETE FROM cliente WHERE id_cliente={0}".format(id_cliente))
        c.conn.commit()

        return redirect(url_for('home'))

    @app.route('/read_all_clients', methods=['GET'])
    def read_all_clients():
        c.conn = Conexion()
        c.cursor.execute("SELECT * FROM cliente")
        clientes = c.cursor.fetchall()

        return render_template("todos_los_clientes.html", cliente=clientes)

    @app.route('/read_a_client', methods=['GET','POST'])
    def read_a_client():
        c.conn = Conexion()
        c.cursor.execute("SELECT * FROM cliente WHERE id_cliente=3;")
        cliente = c.cursor.fetchone()

        return render_template("leer_cliente.html", cliente=cliente)