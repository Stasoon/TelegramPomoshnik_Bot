from config import Config
from src.utils import Json, read_txt_file


class Messages:
    # Статья со ссылками на фотографии: https://telegra.ph/Ishodniki-dlya-bota-pomoshchnika-Telegramm-09-11

    @staticmethod
    async def get_welcome_text(user_name: str = 'незнакомец') -> str:
        text = await read_txt_file(Config.TxtFilePath.WELCOME_POST)
        return text.format(user=user_name)

    @staticmethod
    def get_welcome_photo() -> str:
        return "https://telegra.ph/file/e56de1595ec404577f9fb.png"

    @staticmethod
    def get_main_menu():
        return '💫 Что вы хотите узнать?'

    # Термины телеграм
    @staticmethod
    async def get_telegram_term(number: int, separator: str = '///') -> str:
        header = '📝 Термины в TG'
        terms = (await read_txt_file(Config.TxtFilePath.TERMS)).split(separator)

        # номер уменьшается/увеличивается при нажатии кнопки, поэтому
        index = abs(number) % len(terms)
        index *= -1 if number < 0 else 1  # если число отрицательное, идём с конца кортежа
        return f'{header} \n\n{terms[index].strip()}'

    # CPM тематика
    @staticmethod
    async def get_cpm_thematics_photo() -> str:
        return (await read_txt_file(path=Config.TxtFilePath.CPM)).strip()

    # Полезные чаты
    @staticmethod
    def get_choose_useful_chat_thematics() -> str:
        return '💎 Выберите категорию, которая вас интересует:'

    @staticmethod
    async def get_purchases_chats(page_num: int = 0, separator: str = '///') -> str:
        storage = Json(Config.JsonFilePath.USEFUL_CHATS)
        parts = (await storage.get_data('purchases')).split(separator)
        index = abs(page_num) % len(parts)
        index *= -1 if page_num < 0 else 1
        return parts[index]

    @staticmethod
    def get_purchases_chats_photo() -> str:
        return 'https://telegra.ph/file/2dd57b9486aeb432c4a72.png'

    @staticmethod
    async def get_sales_chats(page_num: int = 0, separator: str = '///') -> str:
        storage = Json(Config.JsonFilePath.USEFUL_CHATS)
        parts = (await storage.get_data('sell')).split(separator)
        index = abs(page_num) % len(parts)
        index *= -1 if page_num < 0 else 1
        return parts[index]

    @staticmethod
    def get_sales_chats_photo() -> str:
        return 'https://telegra.ph/file/6aeffc0ab942a5975a328.png'

    @staticmethod
    async def get_admin_chats() -> str:
        storage = Json(Config.JsonFilePath.USEFUL_CHATS)
        return await storage.get_data('admin')

    # Цены за ПДП
    @staticmethod
    async def get_subscriber_costs() -> str:
        return await read_txt_file(Config.TxtFilePath.SUBSCRIBER_COST)

    # Полезные боты
    @staticmethod
    def get_choose_useful_bot_type() -> str:
        return '🤖 Какой бот вам нужен?'

    @staticmethod
    async def get_bot_category_description(useful_bot_type: str):
        storage = Json(Config.JsonFilePath.USEFUL_BOTS)
        return await storage.get_data(key=useful_bot_type)

    # Специалисты
    @staticmethod
    def get_specialists() -> str:
        return '🛠 Какие специалисты вас интересуют?'

    @staticmethod
    async def get_specialist_category_description(specialist_category: str):
        storage = Json(Config.JsonFilePath.SPECIALISTS)
        return await storage.get_data(key=specialist_category)

    # Биржи
    @staticmethod
    async def get_stock_markets() -> str:
        return await read_txt_file(Config.TxtFilePath.STOCK_MARKET)

    # Поиск сотрудников
    @staticmethod
    async def get_employee_search_chats() -> str:
        return await read_txt_file(path=Config.TxtFilePath.EMPLOYEES_SEARCH)

    # Блоги
    @staticmethod
    async def get_useful_blogs() -> str:
        return await read_txt_file(Config.TxtFilePath.BLOGS)

