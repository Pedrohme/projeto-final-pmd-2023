import os
from dotenv import load_dotenv
from fastapi import FastAPI
import motor.motor_asyncio

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI"])
db = client[os.environ["MONGO_DATABASE"]]
app = FastAPI()


@app.get("/")
async def root():
    docs = await db.chat.find_one()
    return docs