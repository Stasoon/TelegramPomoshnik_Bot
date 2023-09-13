from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from src.misc.enums import UsefulBotsCategory, SpecialistCategory
from src.misc.callback_data import terms_nav_callback, bots_nav_callback, specialists_nav_callback


class Keyboards:

    back_to_menu_reply_button = KeyboardButton('🔙 Назад в меню 🔙')

    # check_sub_button = InlineKeyboardButton('❓ Проверить ❓', callback_data='checksubscription')
    #
    # @classmethod
    # def get_not_subbed_markup(cls, channels_to_sub_data) -> InlineKeyboardMarkup | None:
    #     if len(channels_to_sub_data) == 0:
    #         return None
    #
    #     channels_markup = InlineKeyboardMarkup(row_width=1)
    #     [
    #         channels_markup.add(InlineKeyboardButton(channel_data.get('title'), url=channel_data.get('url')))
    #         for channel_data in channels_to_sub_data
    #     ]
    #     channels_markup.add(cls.check_sub_button)
    #     return channels_markup

    @staticmethod
    def get_main_menu() -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        markup.add("📝 Термины в TG", "💸 CPM тематик",
                   "📙Полезные чаты", "🙋Стоимость ПДП",
                   "🤖 Полезные боты", "🤝 Специалисты по TG",
                   "🔎 Каналы по поиску сотрудников", "👷‍♂️ Биржи по продаже каналов")
        markup.row("📌 Полезные блоги")

        return markup

    @staticmethod
    def get_terms_navigation(current_term_number: int) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                text='⬅', callback_data=terms_nav_callback.new(direction='prev', current_term_number=current_term_number)
            ),
            InlineKeyboardButton(
                text='➡', callback_data=terms_nav_callback.new(direction='next', current_term_number=current_term_number)
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
