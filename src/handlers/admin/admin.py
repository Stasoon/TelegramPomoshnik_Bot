from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from . import statistic
from . import mailing
from . import edit_content
from . import refferal_links
from . import export_users
from . import admins_management


admin_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1) \
    .add(
    edit_content.Keyboards.reply_button_for_admin_menu,
    statistic.Keyboards.reply_button_for_admin_menu,
    mailing.Keyboards.reply_button_for_admin_menu,
    refferal_links.Keyboards.reply_button_for_admin_menu,
    admins_management.Keyboards.reply_button_for_admin_menu,
    export_users.Keyboards.reply_button_for_admin_menu
)


async def handle_admin_command(message: types.Message, state: FSMContext):
    await state.finish()
    await send_admin_menu(message)


async def send_admin_menu(message: types.Message):
    await message.answer('💼 Меню администратора: ', reply_markup=admin_kb)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_admin_command, is_admin=True, commands=['admin'], state='*')

    statistic.Handlers.register_admin_statistic_handlers(dp)
    mailing.Handlers.register_mailing_handlers(dp)
    edit_content.Handlers.register_export_users_handlers(dp)
    refferal_links.Handlers.register_reflinks_handlers(dp)
    admins_management.Handlers.register_admin_management_handlers(dp)
    export_users.Handlers.register_export_users_handlers(dp)
