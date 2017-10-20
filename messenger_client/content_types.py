"""Types of raw (unstructured) content that can be sent to the users. For structured templates see templates"""
from abc import ABCMeta

from six import with_metaclass


class TextMessage(object):
    """Text message.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
    """
    def __init__(self, text):
        self._text = text

    def to_dict(self):
        """Returns a dict representation of the current object"""
        return {'text': self._text}


class Attachment(with_metaclass(ABCMeta)):
    """Base class for attachments."""
    _type = None

    def __init__(self, url):
        self._url = url

    def to_dict(self):
        """Returns a dict representation of the current object"""
        return {
            'attachment': {
                'type': self._type,
                'payload': {
                    'url': self._url
                }
            }
        }


class AudioAttachment(Attachment):
    """Audio attachment.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment
    """
    _type = 'audio'


class FileAttachment(Attachment):
    """File attachment.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment
    """
    _type = 'file'


class ImageAttachment(Attachment):
    """Image attachment.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
    """
    _type = 'image'


class VideoAttachment(Attachment):
    """Video attachment.

    https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment
    """
    _type = 'video'
