from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from src.database.user import create_user
from src.utils import send_typing_action, throttle
from src.misc import terms_nav_callback, bots_nav_callback, specialists_nav_callback
from .messages import Messages
from .kb import Keyboards


# region Handlers

@throttle()
async def handle_start_command(message: Message) -> None:
    await send_typing_action(message)

    # создаём пользователя
    create_user(
        telegram_id=message.from_id,
        name=message.from_user.username or message.from_user.full_name,
        reflink=message.get_full_command()[1]
    )

    # отправляем приветственное сообщение
    await message.answer_photo(
        caption=Messages.get_welcome_text(message.from_user.first_name),
        photo=Messages.get_welcome_photo(),
        reply_markup=Keyboards.get_main_menu()
    )


async def handle_back_to_menu_button(message: Message):
    await message.answer(
        text=Messages.get_main_menu(),
        reply_markup=Keyboards.get_main_menu()
    )


# Термины
@throttle(1.3)
async def handle_telegram_terms_button(message: Message):
    await send_typing_action(message)

    text = Messages.get_telegram_term(0)
    reply_markup = Keyboards.get_terms_navigation(0)
    await message.answer(text=text, reply_markup=reply_markup)


@throttle(1.3)
async def handle_telegram_terms_navigation_callback(callback: CallbackQuery, callback_data: dict):
    current_term_number = int(callback_data.get('current_term_number'))
    next_term_number = current_term_number + (1 if callback_data.get('direction') == 'next' else -1)

    text = Messages.get_telegram_term(next_term_number)
    reply_markup = Keyboards.get_terms_navigation(next_term_number)
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


# CPM
@throttle()
async def handle_cpm_thematics_button(message: Message):
    await send_typing_action(message)

    await send_typing_action(message)
    await message.answer_photo(photo=Messages.get_cpm_thematics_photo())


# Полезные чаты
@throttle()
async def handle_useful_chats_button(message: Message):
    await message.answer(text=Messages.get_choose_useful_chat_thematics(), reply_markup=Keyboards.get_useful_chats())


@throttle()
async def handle_purchases_button(message: Message):  # покупка
    await send_typing_action(message)
    await message.answer_photo(
        caption=await Messages.get_purchases_chats(), photo=Messages.get_purchases_chats_photo()
    )


@throttle()
async def handle_sales_chats_button(message: Message):  # продажа
    await send_typing_action(message)
    await message.answer_photo(
        caption=await Messages.get_sales_chats(), photo=Messages.get_sales_chats_photo()
    )


@throttle()
async def handle_admin_chats_button(message: Message):  # администраторские
    await send_typing_action(message)
    await message.answer(text=await Messages.get_admin_chats(), disable_web_page_preview=True)


# Стоимость ПДП
@throttle()
async def handle_subscriber_cost_button(message: Message):
    await send_typing_action(message)
    await message.answer(text=await Messages.get_subscriber_costs())


# Полезные боты
@throttle()
async def handle_useful_bots_button(message: Message):
    await send_typing_action(message)
    await message.answer(
        text=Messages.get_choose_useful_bot_type(),
        reply_markup=Keyboards.get_useful_bots_categories()
    )


async def handle_back_to_bot_categories_callbacks(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Messages.get_choose_useful_bot_type(),
        reply_markup=Keyboards.get_useful_bots_categories()
    )


async def handle_useful_bots_navigation_callbacks(callback: CallbackQuery, callback_data: dict):
    category_name = callback_data.get('category')
    text = await Messages.get_bot_category_description(category_name)

    await callback.message.edit_text(
        text=text, reply_markup=Keyboards.get_back_to_bot_categories()
    )


# Специалисты телеграм
async def handle_telegram_specialists_button(message: Message):
    await send_typing_action(message)
    await message.answer(text=Messages.get_specialists(), reply_markup=Keyboards.get_specialists())


async def handle_back_to_specialist_categories_callbacks(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Messages.get_specialists(), reply_markup=Keyboards.get_specialists(),
        disable_web_page_preview=True
    )


async def handle_specialists_navigation_callbacks(callback: CallbackQuery, callback_data: dict):
    # принцип работы такой: в .json файлах лежат тексты по ключам,
    category_name = callback_data.get('category')
    text = await Messages.get_specialist_category_description(category_name)

    await callback.message.edit_text(
        text=text, reply_markup=Keyboards.get_back_to_specialists_categories(),
        disable_web_page_preview=True
    )


# Биржи по продаже
@throttle(rate=1.3)
async def handle_stock_markets_button(message: Message):
    await send_typing_action(message)
    await message.answer(text=await Messages.get_stock_markets(), disable_web_page_preview=True)


# Поиск сотрудников
@throttle(rate=1.3)
async def handle_employee_search_chats_button(message: Message):
    await send_typing_action(message)
    await message.answer(text=Messages.get_employee_search_chats(), disable_web_page_preview=True)


# Полезные блоги
@throttle(rate=1.3)
async def handle_useful_blogs_button(message: Message):
    await send_typing_action(message)
    await message.answer(text=await Messages.get_useful_blogs(), disable_web_page_preview=True)


# endregion

def register_user_handlers(dp: Dispatcher) -> None:
    # обработчик команды /start
    dp.register_message_handler(handle_start_command, commands=['start'])

    # обработка кнопки Назад в меню
    dp.register_message_handler(handle_back_to_menu_button, lambda message: '🔙 Назад в меню 🔙' in message.text)

    # Термины
    dp.register_message_handler(handle_telegram_terms_button, lambda message: 'термины' in message.text.lower())
    dp.register_callback_query_handler(handle_telegram_terms_navigation_callback, terms_nav_callback.filter())

    # CPM тематик
    dp.register_message_handler(handle_cpm_thematics_button, lambda message: 'cpm тематик' in message.text.lower())

    # Стоимость ПДП
    dp.register_message_handler(handle_subscriber_cost_button, lambda message: 'стоимость пдп' in message.text.lower())

    # Полезные чаты
    dp.register_message_handler(handle_useful_chats_button, lambda message: 'полезные чаты' in message.text.lower())
    dp.register_message_handler(handle_purchases_button, lambda message: 'покупка' in message.text.lower())
    dp.register_message_handler(handle_sales_chats_button, lambda message: 'продажа' in message.text.lower())
    dp.register_message_handler(handle_admin_chats_button, lambda message: 'админские чаты' in message.text.lower())

    # Полезные боты
    dp.register_message_handler(handle_useful_bots_button, lambda message: 'полезные боты' in message.text.lower())
    dp.register_callback_query_handler(handle_back_to_bot_categories_callbacks,
                                       bots_nav_callback.filter(category='all'))
    dp.register_callback_query_handler(handle_useful_bots_navigation_callbacks, bots_nav_callback.filter())

    # Специалисты по тг
    dp.register_message_handler(handle_telegram_specialists_button,
                                lambda message: 'специалисты по' in message.text.lower())
    dp.register_callback_query_handler(handle_back_to_specialist_categories_callbacks,
                                       specialists_nav_callback.filter(category='all'))
    dp.register_callback_query_handler(handle_specialists_navigation_callbacks, specialists_nav_callback.filter())

    # Биржи
    dp.register_message_handler(handle_stock_markets_button, lambda message: 'биржи по продаже' in message.text.lower())

    # Поиск сотрудников
    dp.register_message_handler(handle_employee_search_chats_button,
                                lambda message: 'каналы по поиску сотрудников' in message.text.lower())

    # Полезные блоги
    dp.register_message_handler(handle_useful_blogs_button, lambda message: 'полезные блоги' in message.text.lower())
