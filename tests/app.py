from flask import Flask
import sys, os

sys.path.append('../flaskblockly')
from flaskblockly import Blockly


app = Flask(__name__)
Blockly(app)
# Blockly(app, config={'endpoint': 'blockly', 'user_static_folder': 'user_static'})