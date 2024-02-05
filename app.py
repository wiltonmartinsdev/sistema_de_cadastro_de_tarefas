from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []

task_id = 1

@app.route("/tasks", methods=["POST"])
def create_task():

    global task_id

    data = request.get_json()

    new_task = Task(Id=task_id, Title=data["Title"], Description=data.get("Description", ""))

    task_id += 1

    tasks.append(new_task)

    return jsonify({"Message": "Tarefa criada com Sucesso!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    list_tasks = [task.to_dict() for task in tasks]

    output ={
        "tasks": list_tasks,
        "total_tasks": len(list_tasks)
    }

    return jsonify(output)

@app.route("/tasks/<int:Id>", methods=["GET"])
def get_task(Id):
    for task in tasks:
        if task.Id == Id:
            return jsonify(task.to_dict())
        
    return jsonify({"Message": "Tarefa não encontrada!"})

@app.route("/tasks/<int:Id>", methods=["PUT"])
def update_task(Id):
    task = None

    for element in tasks:
        if element.Id == Id:
            task = element
            break

    if not task:
        return jsonify({"Message": "Tarefa não encontrada!"})
    
    data = request.get_json()

    task.Title = data["Title"]
    task.Description = data["Description"]
    task.Completed = data["Completed"]

    return jsonify({"Message": "Tarefa atualizada com Sucesso!"})

@app.route("/tasks/<int:Id>", methods=["DELETE"])
def delete_task(Id):
    task = None

    for element in tasks:
        if element.Id == Id:
            task = element
            break

    if not task:
        return jsonify({"Message": "Tarefa não encontra para exclusão!"})
    
    tasks.remove(task)

    return jsonify({"Message": "Tarefa excluída com Sucesso!"})




if __name__ == "__main__":
    app.run(debug=True)