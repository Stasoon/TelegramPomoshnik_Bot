from aiogram.utils.callback_data import CallbackData


terms_nav_callback = CallbackData('terms_navigation', 'direction', 'current_term_number')

bots_nav_callback = CallbackData('bots_navigation', 'category')

specialists_nav_callback = CallbackData('specialists_navigation', 'category')
