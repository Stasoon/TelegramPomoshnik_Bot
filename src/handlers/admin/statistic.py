from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from src.database import user
from src.misc.admin_states import StatsGetting
from src.database.user import get_users_total_count, get_users_by_hours


statistic_callback_data = CallbackData('statistic', 'value')


class Keyboards:
    reply_button_for_admin_menu = KeyboardButton('📊 Статистика 📊')

    menu_markup = InlineKeyboardMarkup(row_width=2)\
        .add(
        InlineKeyboardButton(text='Месяц', callback_data=statistic_callback_data.new('month')),
        InlineKeyboardButton(text='Неделя', callback_data=statistic_callback_data.new('week')),
        InlineKeyboardButton(text='Сутки', callback_data=statistic_callback_data.new('day')),
        InlineKeyboardButton(text='Час', callback_data=statistic_callback_data.new('hour')),
        InlineKeyboardButton(text='⌨ Другое количество', callback_data=statistic_callback_data.new('other')),
    )

    back_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton('🔙 Назад', callback_data=statistic_callback_data.new('back'))
    )


class Messages:
    @staticmethod
    def get_menu():
        return f'🌐 Пользователей онлайн: {user.get_online_users_count()} \n' \
               f'👥 Всего пользователей: {user.get_users_total_count()} \n\n' \
               f'📊 Выберите, за какой промежуток времени просмотреть статистику:'

    @staticmethod
    def get_count_per_hours(time_word: str, hours: int):
        return f'За {time_word} ботом пользовались: \n<b>{get_users_by_hours(hours)} юзера(ов)</b>'


class Handlers:
    @staticmethod
    async def __handle_admin_statistic_button(message: Message):
        await message.answer(Messages.get_menu(), reply_markup=Keyboards.menu_markup)

    @staticmethod
    async def __handle_show_stats_callback(callback: CallbackQuery, state: FSMContext, callback_data: statistic_callback_data):
        value = callback_data.get('value')
        message = callback.message

        match value:
            case 'back':
                await message.edit_text(Messages.get_menu(), reply_markup=Keyboards.menu_markup)
                await state.finish()
            case 'all_time':
                await message.edit_text(
                    text=f'Всего пользовалось ботом: <b>{get_users_total_count()} юзеров</b>',
                    reply_markup=Keyboards.back_markup
                )
            case 'month':
                await message.edit_text(
                    text=Messages.get_count_per_hours('месяц', 30 * 24), reply_markup=Keyboards.back_markup
                )
            case 'week':
                await message.edit_text(
                    text=Messages.get_count_per_hours('неделю', 7 * 24), reply_markup=Keyboards.back_markup
                )
            case 'day':
                await message.edit_text(
                    text=Messages.get_count_per_hours('сутки', 24), reply_markup=Keyboards.back_markup
                )
            case 'hour':
                await message.edit_text(
                    text=Messages.get_count_per_hours('час', 1), reply_markup=Keyboards.back_markup
                )
            case 'other':
                await message.edit_text(
                    text='🔘 Введите количество часов, за которое хотите получить статистику: ',
                    reply_markup=Keyboards.back_markup
                )
                await state.set_state(StatsGetting.wait_for_hours_count)

    @staticmethod
    async def __handle_get_hours_message(message: Message, state: FSMContext):
        if not message.text.isdigit():
            await message.answer('❗Вы ввели не число. Попробуйте снова:', reply_markup=Keyboards.back_markup)
            return

        users_count = get_users_by_hours(int(message.text))
        await message.answer(f'За <b>{message.text} часа(ов)</b> ботом воспользовались <b>{users_count} юзеров</b>',
                             reply_markup=Keyboards.back_markup)
        await state.finish()

    @classmethod
    def register_admin_statistic_handlers(cls, dp: Dispatcher):
        dp.register_message_handler(
            cls.__handle_admin_statistic_button, is_admin=True,
            text=Keyboards.reply_button_for_admin_menu.text
        )

        dp.register_callback_query_handler(
            cls.__handle_show_stats_callback, statistic_callback_data.filter(), state='*'
        )

        dp.register_message_handler(
            cls.__handle_get_hours_message,
            is_admin=True, state=StatsGetting.wait_for_hours_count
        )





