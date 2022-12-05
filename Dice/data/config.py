import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('API_TOKEN'))
# bot admin
admins = [

]

IP = str(os.getenv('ip'))
POSTGRESUSER = str(os.getenv('PostgresUser'))
POSTGRESPASSWORD = str(os.getenv('PostgresPassword'))
DATABASE = str(os.getenv('DataBase'))

POSTGRES_URI = f'postregsql://{POSTGRESUSER}:{POSTGRESPASSWORD}@{IP}/{DATABASE}'
