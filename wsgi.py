from flask import Blueprint
from app.master.view import blu
from app import app

app.register_blueprint(blu)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
