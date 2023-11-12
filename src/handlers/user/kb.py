from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from src.misc.enums import UsefulBotsCategory, SpecialistCategory
from src.misc.callback_data import nav_buttons_callback, bots_nav_callback, specialists_nav_callback


class Keyboards:

    back_to_menu_reply_button = KeyboardButton('🔙 Назад в меню 🔙')

    @staticmethod
    def get_main_menu() -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        markup.add("💸 CPM тематик", "🙋Стоимость ПДП",
                   "📝 Термины в TG", "📙Полезные чаты",
                   "🤝 Специалисты по TG", "🔎 Каналы по поиску сотрудников",
                   "👷‍♂️ Биржи по продаже каналов", "🤖 Полезные боты")
        markup.row("📌 Полезные блоги")

        return markup

    @staticmethod
    def get_navigation_buttons(category: str, current_page_num: int) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                text='⬅', callback_data=nav_buttons_callback.new(
                    category=category, direction='prev', page_to_open=current_page_num - 1
                )
            ),
            InlineKeyboardButton(
                text='➡', callback_data=nav_buttons_callback.new(
                    category=category, direction='next', page_to_open=current_page_num + 1
                )
            )
        )
        return markup

    @staticmethod
    def get_useful_chats() -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            '💵 Покупка', '💶 Продажа',
            '🚨 Админские чаты'
        )
        markup.row(Keyboards.back_to_menu_reply_button)
        return markup

    @staticmethod
    def get_useful_bots_categories() -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=2)

        markup.add(
            InlineKeyboardButton(
                "💭 Для чата", callback_data=bots_nav_callback.new(category=UsefulBotsCategory.CHATBOTS.value)
            ),
            InlineKeyboardButton(
                "📢 Для постинга", callback_data=bots_nav_callback.new(category=UsefulBotsCategory.POSTING.value)
            ),
            InlineKeyboardButton(
                "🗑 Для чистки", callback_data=bots_nav_callback.new(category=UsefulBotsCategory.CLEANING.value)
            ),
            InlineKeyboardButton(
                "💸 Для закупа", callback_data=bots_nav_callback.new(category=UsefulBotsCategory.PURCHASES.value)
            ),
            InlineKeyboardButton(
                "🧑‍💻 Для обратной связи",
                callback_data=bots_nav_callback.new(category=UsefulBotsCategory.FEEDBACKS.value)
            ),
        )
        return markup

    @staticmethod
    def get_back_to_bot_categories() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup() \
            .add(InlineKeyboardButton(text="🔙 Назад 🔙", callback_data=bots_nav_callback.new(category='all')))

    @staticmethod
    def get_specialists() -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton('👥 Манаги',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.MANAGERS.value)),
            InlineKeyboardButton('👥 Закупщики',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.BUYERS.value)),
            InlineKeyboardButton('👥 Дизайнеры',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.DESIGNERS.value)),
            InlineKeyboardButton('👥 Кодеры',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.CODERS.value)),
            InlineKeyboardButton('👥 Гаранты',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.GUARANTORS.value)),
            InlineKeyboardButton('👥 Контентщики',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.CONTENT_MAKERS.value)),
            InlineKeyboardButton('👥 Креативщики',
                                 callback_data=specialists_nav_callback.new(category=SpecialistCategory.CREATIVE.value)),
        )
        return markup

    @staticmethod
    def get_back_to_specialists_categories() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup() \
            .add(InlineKeyboardButton(text="🔙 Назад 🔙", callback_data=specialists_nav_callback.new(category='all')))

