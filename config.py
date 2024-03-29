import os
from typing import Final
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Config:
    TOKEN: Final = os.getenv('BOT_TOKEN', 'define me')
    ADMIN_IDS: Final = tuple(int(i) for i in str(os.getenv('BOT_ADMIN_IDS')).split(','))

    class JsonFilePath:
        __directory_path = 'content'
        USEFUL_BOTS: Final = f'{__directory_path}/useful_bots.json'
        USEFUL_CHATS: Final = f'{__directory_path}/useful_chats.json'
        SPECIALISTS: Final = f'{__directory_path}/specialists.json'

    class TxtFilePath:
        __directory_path = 'content'
        WELCOME_POST: Final = f'{__directory_path}/welcome_post.txt'
        SUBSCRIBER_COST: Final = f'{__directory_path}/subscriber_cost.txt'
        STOCK_MARKET: Final = f'{__directory_path}/stock_markets.txt'
        BLOGS: Final = f'{__directory_path}/useful_blogs.txt'
        TERMS: Final = f'{__directory_path}/terms.txt'
        EMPLOYEES_SEARCH = f'{__directory_path}/employes_search.txt'
        CPM = f'{__directory_path}/cpm_photo_file_id.txt'

    DEBUG: Final = bool(os.getenv('DEBUG'))
