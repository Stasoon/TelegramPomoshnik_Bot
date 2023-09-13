from enum import Enum


class UsefulBotsCategory(Enum):
    CHATBOTS = 'chatbots'
    POSTING = 'posting'
    CLEANING = 'cleaning'
    PURCHASES = 'purchases'
    FEEDBACKS = 'feedbacks'


class SpecialistCategory(Enum):
    MANAGERS = 'managers'
    BUYERS = 'buyers'
    DESIGNERS = 'designers'
    CODERS = 'coders'
    GUARANTORS = 'guarantors'
    CONTENT_MAKERS = 'content_makers'
    CREATIVE = 'creative'
