import asyncio

from data import config
from utils.dp_api.db_lmao import db
from utils.dp_api import quick_commands as commands


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'negr','geterosexyal')

    users = await commands.select_all_users()

    count =await commands.count_users()

    user=await commands.select_user()

    await commands.select_user(1)


loop=asyncio.get_event_loop()
loop.run_until_complete()
