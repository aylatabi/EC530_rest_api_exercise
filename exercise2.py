from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {}
notes = {}
next_id = 1

# CREATE an account
@app.post("/users")
def create_user(username: str):
    global next_id
    # check if username already exists
    for user in users.values():
        if user["username"] == username:
            raise HTTPException(status_code=409, detail="Username already exists")
    
    user = {
        "id": next_id,
        "username": username
    }
    users[next_id] = user
    notes[next_id] = []
    next_id += 1
    return user

# GET an account by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# ADD a note
@app.post("/users/{user_id}/notes")
def add_note(user_id: int, text: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    notes[user_id].append(text)
    return {"message": "Note added", "note": text}

# GET all notes
@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "notes": notes[user_id]}