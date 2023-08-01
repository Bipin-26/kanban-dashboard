from flask import Flask, Response, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import json
app = Flask(__name__)

app.config['JSON_SORT_KEYS']=False
app.config['MONGO_DBNAME'] = 'KanbanDB'
app.config['MONGO_URI'] = 'mongodb+srv://super5:KNmLJNpkI4k3Bm07@cluster0.ns7vyxt.mongodb.net/KanbanDB?retryWrites=true&w=majority'
mongo = PyMongo(app)
userCollection = mongo.db.users

@app.errorhandler(Exception)
def server_error(err):
    return Response(response={err})

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

@app.route('/admin/employeeList', methods=['GET'])
def get_employee_list():
    try:
        docs = list(userCollection.find())
        for item in docs:
            item['_id'] = str(item['_id'])
        if len(docs) == 0:
            return Response(response="No Records Found")
        else:
            return Response(response=json.dumps(docs), status=200, mimetype='application/json')
    except Exception as err:
        return server_error(err)

@app.route('/admin/addEmployee', methods=['POST'])
def add_employee_to_list():
    try:
        employee = {
            'empID':request.form['empID'],
            'empName':request.form['empName'],
            'empDesignation':request.form['empDesignation'],
            'reportingManager':request.form['reportingManager']
        }
        insert_query = userCollection.insert_one(employee)
        if(insert_query.inserted_id):
            return Response(response=json.dumps({"message":"Employee added successfully", "id":f"{insert_query.inserted_id}"}),status=200, mimetype="application/json")
        else:
            return Response(response=json.dumps({"message":"Cannot insert employee details"}), status=500, mimetype="application/json")
    except Exception as err:
        return server_error(err)

if __name__ == '__main__':
    app.run(debug=True)