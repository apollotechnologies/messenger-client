from enum import Enum


class Tags(Enum):
    """Enum of all the allowed tags.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/tags
    """
    SHIPPING_UPDATE = 'SHIPPING_UPDATE'
    RESERVATION_UPDATE = 'RESERVATION_UPDATE'
    ISSUE_RESOLUTION = 'ISSUE_RESOLUTION'
    APPOINTMENT_UPDATE = 'APPOINTMENT_UPDATE'
    GAME_EVENT = 'GAME_EVENT'
    TRANSPORTATION_UPDATE = 'TRANSPORTATION_UPDATE'
    FEATURE_FUNCTIONALITY_UPDATE = 'FEATURE_FUNCTIONALITY_UPDATE'
    TICKET_UPDATE = 'TICKET_UPDATE'
