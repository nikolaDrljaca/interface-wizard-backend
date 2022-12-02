import motor.motor_asyncio as motor

# Later switch to environment variables
db_username = 'test'
db_password = 'test1234'
db_host = 'localhost'
db_port = '27017'

async def get_db():
    connection_string = f'mongodb://{db_username}:{db_password}@{db_host}:{db_port}'
    client = motor.AsyncIOMotorClient(connection_string)
    try:
        yield client.interface_wizard
    finally:
        client.close()
