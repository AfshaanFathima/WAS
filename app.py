from flask import Flask,request,jsonify

app=Flask(__name__)

todos=[
    {
        "id":1,
        "title":"Afshaan"
    }
]

@app.route("/todos",methods=['GET'])
def getmeth():
    return jsonify(todos)

@app.route("/todos",methods=['POST'])
def postmeth():
    new=request.json
    todos.append(new)
    return jsonify({"Message":"Post done!!"})

@app.route("/todos/<int:t_id>",methods=['PUT'])
def putmeth(t_id):
    for todo in todos:
        if todo["id"]==t_id:
            todo["title"]=request.json["title"]
            return jsonify({"Message":"Put done!!"})
    return jsonify({"Message":"Invalid"})

@app.route("/todos/<int:t_id>",methods=['DELETE'])
def delmeth(t_id):
    global todos
    for todo in todos:
        if todo["id"]==t_id:
            todos.remove(todo)
            return jsonify({"Message":"Deletion done!!"})
    return jsonify({"Message":"Invalid"})

if __name__=="__main__":
    app.run(debug=True)
