from sqlalchemy import Column, String, BigInteger, sql

from utils.dp_api.db_lmao import TimedBaseModel


class User(TimedBaseModel):
    __tablename__='users'
    user_id = Column(BigInteger,primary_key=True)
    name =Column(String(200),primary_key=True)
    update_name=Column(String(50),primary_key=True)

    query: sql.select