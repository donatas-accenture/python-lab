from flask import Flask, request

app = Flask(__name__)
print(app)

@app.get("/")
def home_page():
    return "Hello user"

@app.get("/users")
def users_page():
    return {
        "response": ["John", "Mark", "Steve"]
    }

@app.post("/users/register")
def users_register():
    data = request.get_json()
    surname = data.get("Surname1", "The key not found")
    print(data)
    return {
        "response": surname,
        "status": 307
    }, 307

app.run(use_reloader=True)