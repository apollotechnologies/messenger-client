from abc import ABCMeta
from enum import Enum

from six import with_metaclass


class WebviewHeight(Enum):
    COMPACT = 'compact'
    FULL = 'full'
    TALL = 'tall'


class Button(with_metaclass(ABCMeta)):
    """Base class for buttons."""
    pass


class URLButton(Button):
    """URL Button

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button
    """
    _type = 'web_url'

    def __init__(self, title, url, webview_height_ratio=WebviewHeight.FULL,
                 messenger_extensions=None, fallback_url=None, webview_share_button=None):
        self._title = title
        self._url = url
        self._webview_height_ratio = webview_height_ratio
        self._messenger_extensions = messenger_extensions
        self._fallback_url = fallback_url
        self._webview_share_button = webview_share_button


class PostbackButton(Button):
    """Postback button.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/postback-button
    """
    _type = 'postback'

    def __init__(self, title, payload):
        self._title = title
        self._payload = payload


class CallButton(Button):
    """Call button.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/call-button
    """
    _type = 'phone_number'

    def __init__(self, title, payload):
        self._title = title
        self._payload = payload


class ShareButton(Button):
    """Share button.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/share-button
    """
    _type = 'element_share'


class LogInButton(Button):
    """Log in button.

    https://developers.facebook.com/docs/messenger-platform/account-linking/link-account
    """
    _type = 'account_link'

    def __init__(self, url):
        self._url = url


class LogOutButton(Button):
    """Log out button.

    https://developers.facebook.com/docs/messenger-platform/account-linking/unlink-account
    """
    _type = 'account_unlink'
