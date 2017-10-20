import requests

from sender_actions import SenderActions


class MessengerClient(object):
    def __init__(self, access_token):
        """
        :param access_token: the Messenger Platform access token
        :type access_token: str
        """
        self._access_token = access_token
        self._api_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={0}'.format(self._access_token)

    def send(self, to, obj):
        to_send = {
            'recipient': {
                'id': to
            },
            'message': obj.to_dict()
        }
        return self._send_raw(to_send)

    def mark_seen(self, to):
        """Marks last message as read.

        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        :param to: The recipient id, also known as PSID.
        """
        return self._send_sender_action(to, SenderActions.MARK_SEEN)

    def typing_on(self, to):
        """Turn typing indicators on. Typing indicators are automatically turned off after 20 seconds.

        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        :param to: The recipient id, also known as PSID.
        """
        return self._send_sender_action(to, SenderActions.TYPING_ON)

    def typing_off(self, to):
        """Turn typing indicators off.

        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        :param to: The recipient id, also known as PSID.
        """
        return self._send_sender_action(to, SenderActions.TYPING_OFF)

    def _send_sender_action(self, to, action):
        """Sends a sender action.

        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        :param to: The recipient id, also known as PSID.
        :param action: The type of the action to be sent.
        """
        obj = {
            'recipient': {
                'id': to
            },
            'sender_action': '{0}'.format(action.value)
        }
        return self._send_raw(obj)

    def _send_raw(self, obj):
        return requests.post(self._api_url, json=obj).json()
