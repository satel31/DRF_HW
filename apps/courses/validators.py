from rest_framework import serializers


class VideoLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue is not None:
            if tmpvalue[12:23] != 'youtube.com':
                raise serializers.ValidationError('You can add only youtube videos')
