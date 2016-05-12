from django.conf.urls import url

from .views import PlaceActivityFeed, PlaceActivityListView


urlpatterns = [

    url(r'^feeds/all/$',
        PlaceActivityFeed(),
        name='activitystream_feed',
    ),

    url(r'^',
        PlaceActivityListView.as_view(),
        name='activitystream_activity_list'
    ),

]
