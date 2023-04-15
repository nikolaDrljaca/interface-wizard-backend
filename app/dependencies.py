import motor.motor_asyncio as motor
from dotenv import load_dotenv
from os import getenv


load_dotenv()


db_username = getenv('DB_USER')
db_password = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')


async def get_db():
    connection_string = f'mongodb://{db_username}:{db_password}@{db_host}:{db_port}'
    client = motor.AsyncIOMotorClient(connection_string)
    try:
        yield client.interface_wizard
    finally:
        client.close()


def get_db_sync():
    connection_string = f'mongodb://{db_username}:{db_password}@{db_host}:{db_port}'
    client = motor.AsyncIOMotorClient(connection_string)
    return client
