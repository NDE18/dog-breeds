# dogbreed/__init__.py
from flask import Flask


app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecret"

from dogbreed.core.views import core

app.register_blueprint(core)