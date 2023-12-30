from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config.config import get_configs
from beanie import init_beanie
from src.models.user import User
from fastapi import FastAPI, Request

async def init_mongo(app: FastAPI):
    configs = get_configs()
    client = AsyncIOMotorClient(configs.mongo_host)
    app.mongo_client = client
    app.mongo = app.mongo_client[configs.mongo_db]

async def close_mongo(app:FastAPI):
    app.mongo_client.close()


async def getDB(request:Request)-> AsyncIOMotorDatabase:
    return request.app.mongo