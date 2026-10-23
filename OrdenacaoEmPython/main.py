from flask import Flask
from Controller.controller import main_blueprint

app = Flask(__name__)
#registra as rotas defindas no controller
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)