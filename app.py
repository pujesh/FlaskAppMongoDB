from flask import Flask 
from routes import routes_bp
# import configclass

app = Flask(__name__) 
app.config.from_pyfile('config.cfg')
# app.config.from_object('configclass.DevelopmentConfig')

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run() 
