import motor.motor_asyncio
import requests
from info import DATABASE_URI, DATABASE_NAME

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.bots

    def new_bot(self, id, name, user_name, b_token, owner):
        return dict(
            bot_id = id,
            name = name,
            u_name = user_name,
            token = b_token,
            owner_id = owner,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
        )
    async def add_bot(self, id, name, user_name, b_token, owner):
        bot = self.new_bot(id, name, user_name, b_token, owner)
        await self.col.insert_one(bot)
        
    async def is_bot_exist(self, token):
        bot = await self.col.find_one({'token':str(token)})
        return bool(bot)
    
    async def total_bots_count(self):
        count = await self.col.count_documents({})
        return count
    
    async def get_all_bots(self):
        return self.col.find({})
    
    ##%&62722*₹+:₹+₹:₹-₹73#
    
    async def delete_bot(self, bot_id):
        await self.col.delete_many({'bot_id': int(bot_id)})

    
    async def delete_all_bots(self):
        await self.col.drop()
    
    
    async def get_all_bots_token(self):
        bots = await self.col.find({'token'})
        bot = await get_all_bots()
        bot_tokens =  [bot['token'] async for bots in bot]
        
db = Database(DATABASE_URI, DATABASE_NAME)
