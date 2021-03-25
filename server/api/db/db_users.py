from .db_utils import get, put, get_return_row_count
from datetime import datetime

def create_user(username, password):
    put("""
        INSERT INTO
            Users (Username, Password)
        VALUES (?, ?)""", (username, password))

def get_all_users():
    users = get("""
        SELECT 
            Id,
            Username
        FROM 
            Users""")

    return users

def get_user_by_id(user_id):    
    users = get("""
        SELECT
            Id, 
            Username
        FROM 
            Users 
        WHERE Id = (?)""", [user_id])

    return users

def get_user_by_username(username):
    users = get("""
        SELECT
            Id,
            Username
        FROM 
            Users 
        WHERE 
            Username = (?)""", [username])

    return users

def get_user_password(user_id):
    result = get("""
        SELECT 
            Password AS password
        FROM 
            Users 
        WHERE 
            Id = (?)""", [user_id])
    password = result[0]["password"]
    return password

def update_user(user_id, data):
    if data.get("username"):
        put("""
            UPDATE 
                Users 
            SET 
                Username = (?) 
            WHERE 
                Id = (?)""", [data["username"], user_id])
    
    if data.get("password"):
        put("""
            UPDATE 
                Users 
            SET 
                Password = (?) 
            WHERE 
                Id = (?)""", [data["password"], user_id])

def delete_user(user_id):
    put("""
        DELETE FROM 
            Users 
        WHERE 
            Id = (?)""", [user_id])

def user_exists(user_id):
    count = get_return_row_count("""
    SELECT 
        *
    FROM
        Users
    WHERE
        Id = (?)""", [user_id])

    return count
