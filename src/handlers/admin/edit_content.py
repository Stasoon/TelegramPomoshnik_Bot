from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from config import Config
from src.misc.admin_states import ContentEditingStates
from src.utils import Json, read_txt_file
from src.utils.txt_data import rewrite_txt_file

editing_callback_data = CallbackData("edit_content", "option", "category")


class Messages:
    @staticmethod
    async def get_current_content(option: str, category: str = None) -> str:
        match option:
            case 'spec':
                return await Json(Config.JsonFilePath.SPECIALISTS).get_data(key=category)
            case 'bots':
                return await Json(Config.JsonFilePath.USEFUL_BOTS).get_data(key=category)
            case 'chats':
                return await Json(Config.JsonFilePath.USEFUL_CHATS).get_data(key=category)
            case 'blogs':
                return await read_txt_file(Config.TxtFilePath.BLOGS)


class Keyboards:
    reply_button_for_admin_menu = KeyboardButton('📝 Изменить контент 📝')

    @staticmethod
    def get_back_button():
        return InlineKeyboardMarkup().add(InlineKeyboardButton(text='❌ Отменить', callback_data='back_to_edit_options'))

    @staticmethod
    def get_options_to_edit() -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=2)

        markup.add(InlineKeyboardButton("* Специалисты по TG *", callback_data="*")).row().add(
            InlineKeyboardButton("👥 Манаги",
                                 callback_data=editing_callback_data.new(option='spec', category='managers')),
            InlineKeyboardButton("👥 Закупщики",
                                 callback_data=editing_callback_data.new(option='spec', category='buyers')),
            InlineKeyboardButton("👥 Дизайнеры",
                                 callback_data=editing_callback_data.new(option='spec', category='designers')),
            InlineKeyboardButton("👥 Кодеры", callback_data=editing_callback_data.new(option='spec', category='coders')),
            InlineKeyboardButton("👥 Гаранты",
                                 callback_data=editing_callback_data.new(option='spec', category='guarantors')),
            InlineKeyboardButton("👥 Контентщики",
                                 callback_data=editing_callback_data.new(option='spec', category='content_makers')),
            InlineKeyboardButton("👥 Креативщики",
                                 callback_data=editing_callback_data.new(option='spec', category='creative')),
        )

        markup.add(InlineKeyboardButton("* Полезные боты *", callback_data="*")).row().add(
            InlineKeyboardButton("💭 Для чатов",
                                 callback_data=editing_callback_data.new(option='bots', category='chatbots')),
            InlineKeyboardButton("📢 Для постинга",
                                 callback_data=editing_callback_data.new(option='bots', category='posting')),
            InlineKeyboardButton("🗑 Для чистки",
                                 callback_data=editing_callback_data.new(option='bots', category='cleaning')),
            InlineKeyboardButton("💸 Для закупа",
                                 callback_data=editing_callback_data.new(option='bots', category='purchases')),
            InlineKeyboardButton("🧑‍💻 Для обратной связи",
                                 callback_data=editing_callback_data.new(option='bots', category='feedbacks')),
        )

        markup.add(InlineKeyboardButton("* Чаты *", callback_data="*")).row().add(
            InlineKeyboardButton("🚨 Админские чаты",
                                 callback_data=editing_callback_data.new(option='chats', category='admin')),
        )

        markup.add(InlineKeyboardButton("* Полезные блоги *", callback_data="*")).row().add(
            InlineKeyboardButton("📌 Полезные блоги",
                                 callback_data=editing_callback_data.new(option='blogs', category=''))
        )

        return markup


class Handlers:
    @staticmethod
    async def __handle_edit_content_button(message: Message):
        await message.answer('✏ Выберите, какой раздел хотите изменить:', reply_markup=Keyboards.get_options_to_edit())

    @staticmethod
    async def __handle_back_to_edit_options(callback: CallbackQuery, state: FSMContext):
        await state.finish()
        await callback.message.edit_text(
            '❌ Изменение отменено. \n\n✏ Выберите, какой раздел хотите изменить:',
            reply_markup=Keyboards.get_options_to_edit()
        )

    @staticmethod
    async def __handle_edit_specialists(callback: CallbackQuery, callback_data: dict, state: FSMContext):
        await callback.message.edit_text(f'Текущий текст:')

        category = callback_data.get('category')
        option = callback_data.get('option')
        current_data = await Messages.get_current_content(option=option, category=category)
        await callback.message.answer(current_data)

        await callback.message.answer('Введите новое содержание:', reply_markup=Keyboards.get_back_button())

        await state.update_data(category=category, option=option)
        await state.set_state(ContentEditingStates.Specialists.enter_content.state)

    @staticmethod
    async def __handle_new_content_message(message: Message, state: FSMContext):
        data = await state.get_data()
        category = data.get('category')
        option = data.get('option')
        message_text = message.html_text

        match option:
            case 'spec':
                await Json(Config.JsonFilePath.SPECIALISTS).update_data(key=category, value=message_text)
            case 'bots':
                await Json(Config.JsonFilePath.USEFUL_BOTS).update_data(key=category, value=message_text)
            case 'chats':
                await Json(Config.JsonFilePath.USEFUL_CHATS).update_data(key=category, value=message_text)
            case 'blogs':
                await rewrite_txt_file(Config.TxtFilePath.BLOGS, new_text=message_text)

        await message.answer('✅ Данные обновлены')
        await state.finish()

    @classmethod
    def register_export_users_handlers(cls, dp: Dispatcher):
        dp.register_message_handler(cls.__handle_edit_content_button, is_admin=True,
                                    text=Keyboards.reply_button_for_admin_menu.text)

        dp.register_callback_query_handler(cls.__handle_back_to_edit_options,
                                           text='back_to_edit_options', state='*')

        dp.register_callback_query_handler(cls.__handle_edit_specialists,
                                           editing_callback_data.filter(), state=None)

        dp.register_message_handler(cls.__handle_new_content_message,
                                    state=ContentEditingStates.Specialists.enter_content)
