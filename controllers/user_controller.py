from db.client import db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user(username: str):
    return await db.users.find_one({"username": username})

async def verify_user(username: str, password: str):
    user = await get_user(username)
    if user and pwd_context.verify(password, user["password"]):
        return user
    return None

async def create_user(username: str, password: str):
    hashed_pwd = pwd_context.hash(password)
    user_data = {"username": username, "password": hashed_pwd}
    await db.users.insert_one(user_data)
    return user_data
