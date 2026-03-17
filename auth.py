import json
import os
from pathlib import Path
import hashlib

USERS_FILE = "users.json"

def hash_password(password: str) -> str:
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users() -> dict:
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users: dict):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def register_user(username: str, password: str, email: str) -> tuple[bool, str]:
    """Register a new user. Returns (success, message)"""
    users = load_users()
    
    if username in users:
        return False, "Username already exists"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    users[username] = {
        "password": hash_password(password),
        "email": email
    }
    save_users(users)
    return True, "Registration successful!"

def login_user(username: str, password: str) -> tuple[bool, str]:
    """Login a user. Returns (success, message)"""
    users = load_users()
    
    if username not in users:
        return False, "Invalid username or password"
    
    if users[username]["password"] != hash_password(password):
        return False, "Invalid username or password"
    
    return True, "Login successful!"

def user_exists(username: str) -> bool:
    """Check if user exists"""
    users = load_users()
    return username in users
