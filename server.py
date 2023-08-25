from flask_app import app
from flask_app.controllers import controller #replace rename_controller with your controller file name. Do not include .py
from flask_app.controllers import records
from flask_app.controllers import hospitals

if __name__=='__main__':
    app.run(debug=True, port=5000)