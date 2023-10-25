import sys
import os

# Get the parent directory
parent_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from . import employees_controller
from flask import render_template,request,redirect,abort
from models import db,EmployeeModel

controller_root='/employees'
#@employees_controller.route("/test", methods=['GET'])
#def hello():
#  return 'hello world'

@employees_controller.route(controller_root+'/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('add.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect(controller_root)

@employees_controller.route(controller_root)
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template('list.html',employees = employees, controller_root = controller_root)
 
 
@employees_controller.route(controller_root+'/<int:id>')
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('show.html', employee = employee)
    return f"Employee with id ={id} Doesn't exist"
 
 
@employees_controller.route(controller_root+'/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
            db.session.add(employee)
            db.session.commit()
            return redirect(f(controller_root+'/{id}'))
        return f"Employee with id = {id} Doesn't exist"
 
    return render_template('update.html', employee = employee)


@employees_controller.route(controller_root+'/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect(controller_root)
        abort(404)
    return render_template('delete.html')
