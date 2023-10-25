from employees_controller import employees_controller
from flask import Flask,render_template #,request,redirect
from models import db,EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///a.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(employees_controller)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host='localhost', port=5000)
