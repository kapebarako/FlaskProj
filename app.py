from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/employees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initializing database
db = SQLAlchemy(app)

#db Model
class employees_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    address = db.Column(db.String(150), nullable = False)
    mobile = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    sss = db.Column(db.Integer, nullable = False)
    pagibig = db.Column(db.Integer, nullable = False)
    philhealth = db.Column(db.Integer, nullable = False)
    hired = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(150), nullable = False)
    remarks = db.Column(db.String(250), nullable = False)

    def __init__(self, id, name, address, mobile, email, sss, pagibig, philhealth, hired, status, remarks):
        self.id = id
        self.name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.sss = sss
        self.pagibig = pagibig
        self.philhealth = philhealth
        self.hired = hired
        self.status = status
        self.remarks = remarks

@app.route("/")
def index():
    all_data = employees_data.query.all()
    return render_template("index.html", employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        mobile = request.form['mobile']
        email = request.form['email']
        sss = request.form['sss']
        pagibig = request.form['pagibig']
        philhealth = request.form['philhealth']
        hired = request.form['hired']
        status = request.form['status']
        remarks = request.form['remarks']

        my_data = employees_data(id, name, address, mobile, email, sss, pagibig, philhealth, hired, status, remarks)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")
        return redirect(url_for('index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = employees_data.query.get(request.form.get('id'))

        my_data.id = request.form['id']
        my_data.name = request.form['name']
        my_data.address = request.form['address']
        my_data.mobile = request.form['mobile']
        my_data.email = request.form['email']
        my_data.sss = request.form['sss']
        my_data.pagibig = request.form['pagibig']
        my_data.philhealth = request.form['philhealth']
        my_data.hired = request.form['hired']
        my_data.status = request.form['status']
        my_data.remarks = request.form['remarks']

        db.session.commit()

        flash("Employee Updated Successfully")
        return redirect(url_for('index'))

if __name__== "__main__":
    app.run(debug=True)