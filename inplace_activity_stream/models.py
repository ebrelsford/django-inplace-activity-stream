from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField

from actstream.actions import action_handler
from actstream.models import Action

from .signals import action


def place_action_handler(verb, **kwargs):
    """
    Add default actor if none exists, else use the action handler provided by
    django-activity-stream.
    """
    actor = kwargs.get('sender', None)
    if not actor:
        kwargs['sender'] = User.objects.get(pk=settings.ACTIVITY_STREAM_DEFAULT_ACTOR_PK)
    return action_handler(verb, **kwargs)


# Use our action handler instead
action.disconnect(dispatch_uid='actstream.models')
action.connect(place_action_handler, dispatch_uid='activity_stream.models')

# Make Action.place available
PointField(blank=True, null=True).contribute_to_class(Action, 'place')
