from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

BASE_URL = "https://api.fda.gov/food/event.json"

users = {}
notes = {}
next_id = 1

# CREATE an account
@app.post("/users")
def create_user(username: str):
    global next_id
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

# SEARCH FDA and save results as notes
@app.post("/users/{user_id}/search")
def search_and_save(user_id: int, industry: str, limit: int = 5):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    payload = {
        "search": f"products.industry_name:{industry}",
        "limit": limit
    }
    r = requests.get(BASE_URL, params=payload)
    
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail="FDA API error")
    
    data = r.json()
    
    if "results" not in data:
        raise HTTPException(status_code=404, detail="No results found")
    
    saved = []
    for result in data["results"]:
        reactions = result.get("reactions", [])
        products = [p.get("name_brand", "Unknown") for p in result.get("products", [])]
        
        note = f"Industry: {industry} | Products: {', '.join(products)} | Reactions: {', '.join(reactions)}"
        notes[user_id].append(note)
        saved.append(note)
    
    return {"message": f"Saved {len(saved)} notes", "notes": saved}