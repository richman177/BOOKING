from django.urls import path
# from .models import Hotel
from .views import *

urlpatterns = [
    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='hotel_detail'),


    path('room/', RoomListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('room/<int:pk>/', RoomDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='movie_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='user_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='review_detail'),

    path('hotel_photos/', HotelPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_photos_list'),
    path('hotel_photos/<int:pk>/', HotelPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='hotel_photos_detail'),

    path('room_photos/', RoomPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_photos_list'),
    path('room_hoptos/<int:pk>/', RoomPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='room_photos_detail'),


]