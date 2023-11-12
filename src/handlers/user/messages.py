import aiogram.utils.markdown as text_formatting

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
    def get_telegram_term(number: int) -> str:
        header = '📝 Термины в TG'
        terms = (
            '<b>ЦА:</b> целевая аудитория. ЦА называют группу людей, у которых есть потребность в продукте и '
            'возможность его купить. \n'
            'Членов такой группы объединяют по возрасту, полу, месту проживания, профессии, личным предпочтениям '
            'и другим признакам. \n\n'
            '<b>ЖЦА:</b> женская целевая аудитория. \n'
            '<b>МЦА:</b> мужская целевая аудитория.'
            ,
            '<b>ER:</b> Уровень вовлеченности аудитории (в процентах) = кол-во просмотров 1 поста \n'
            'Кол-во подписчиков * 100. \n\n'
            '<b>СРМ:</b> цена за 1 000 просмотров поста. \n\n'
            '<b>Стата:</b> статистика канала. Можно запросить через бота: @telemetrmebot или @TGStat_Bot.'
            ,
            '<b>К:</b> Буквой "К" принято обозначать тысячу. \n'
            'Например: - 1к- 1000 \n'
            '12K-12 000 \n'
            '1KK - 1 000 000 \n'
            '12KK-12 000 000 \n\n'
            '<b>ПДП:</b> подписчики. Если спросят, сколько пдп за неделю, надо посмотреть, сколько подписчиков '
            'пришло за запрошенный период.'
            ,
            '<b>Скрытое продолжение:</b> это функция, с помощью которой можно опубликовать текст, доступный только '
            'для подписчика канала. \n'
            'Т.е. для того, чтобы узнать ответ или продолжение, подписчику нужно подписаться на канал. \n\n'
            '<b>Креатив:</b> рекламный пост для покупки рекламы на другом канале. \n\n'
            ,
            '<b>Байт пост:</b> Пост со скрытым продолжением, где для просмотра ответа надо подписаться.'
            'В данном случае делается с кнопкой. Чтобы прочитать продолжение, надо подписаться. \n\n'
            '<b>Кликбейт:</b> рекламный пост для привлечения максимального количества людей, играющий на интересе '
            'человека получить полную информацию, узнать ответ на вопрос. \n\n'
            '<b>Прямой пост:</b> Когда нет скрытой информации и подписчика призывают подписаться на канал, '
            'раскрывая его преимущества. \n'
            'К примеру, предлагают подписаться и получать актуальные предложения о скидках и бонусах.'
            ,
            '<b>Ответка:</b> ответ на рекламный пост фразой и или ссылкой на рекламируемый канал. \n'
            'Пример: этот пост удалится через 1 час, успейте посмотреть. \n\n'
            '<b>Закреп:</b> закрепление поста в верхней части экрана канала или группы, которое сопровождается '
            'уведомлением и звуковым сигналом для всех подписчиков (даже с отключенными уведомлениями). \n\n'
            '<b>Реакции:</b> кнопки с эмодзи под постами в каналах для оценки содержимого поста. \n\n'
            '<b>ТОП:</b> последний пост опубликованный в канале (держать в ТОП - не публиковать новые посты).'
            ,
            '<b>Оплата фикс:</b> оплата перед размещением, за фиксированную стоимость \n\n'
            '<b>Оплата по факту охвата:</b> после 24 часов, после публикации, исходя из набранного охвата '
            'рекламного поста. \n\n'
            '<b>Закуп:</b> покупка рекламы. \n\n'
            '<b>ВП:</b> взаимный пиар. Может быть с доплатой и без. Доплата требуется, если охваты разные.'
            ,
            '<b>Частный или закрытый канал:</b> это канал, на который надо сначала подписаться, чтобы смотреть '
            'ПОСТЫ. \n\n'
            '<b>Публичный или открытый канал:</b> его можно смотреть посты без подписки. \n\n'
            '<b>Проклаладка:</b> публичный канал в котором выложена приватная ссылка.'
            ,
            '<b>2фа</b> – двухэтапная аутентификация. \n\n'
            '<b>Ботовод</b> – человек, накручивающий подписчиков на канал и/или просмотры на посты. \n\n'
            '<b>Инвайтить</b> – массовое приглашение людей в чат. \n\n'
            '<b>Юзербот</b> – запрограммированный аккаунт.'
            ,
            '<b>Ответка</b> – ответ на рекламный пост фразой и/или ссылкой на рекламируемый канал. \n\n'
            '<b>Отложка</b> – автоматическая публикация поста в определенное время и дату. \n\n'
            '<b>Подборка</b> – список из 3-8 каналов по схожей тематике. \n\n'
            '<b>Риенвест</b> – вложение части заработанных денег обратно в продвижении канала (фул риенвест - '
            'вложение всех заработанных денег)'
        )
        # номер уменьшается/увеличивается при нажатии кнопки, поэтому
        index = abs(number) % len(terms)
        index *= -1 if number < 0 else 1  # если число отрицательное, идём с конца кортежа
        return f'{header} \n\n{terms[index]}'

    # CPM тематика
    @staticmethod
    def get_cpm_thematics_photo() -> str:
        return 'https://telegra.ph/file/222a63af66bada0a95454.png'

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
    def get_employee_search_chats() -> str:
        return ("<a href='https://t.me/birjatrudaleo'>Биржа труда | Chatileo</a> \n"
                "<a href='https://t.me/job_t'>TJop | Биржа труда </a> \n"
                "<a href='https://t.me/tg_chat1'>Работа и Вакансии</a> \n"
                "<a href='https://t.me/+fMT5B0JQlbkwZTky'>Вакансии инста/тг</a> \n"
                "<a href='https://t.me/obyavleniya_ad'>Админские Объявления</a> \n"
                "<a href='https://t.me/vakansii_telega'>Вакансии в tg</a>")

    # Блоги
    @staticmethod
    async def get_useful_blogs() -> str:
        return await read_txt_file(Config.TxtFilePath.BLOGS)

