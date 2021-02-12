from flask import Flask
from conection.conn import Conexion
from routes.routes import routes

c = Conexion()

app = Flask(__name__)

routes(app)

if __name__ == '__main__':
    app.run()