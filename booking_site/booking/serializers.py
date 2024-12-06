from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars']



class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['hotel_image']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_photos = HotelPhotosSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars', 'hotel_photos', 'owner', 'description', 'address', 'hotel_video']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_price', 'type', 'hotel_room', 'all_inclusive']


class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['room_image']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotosSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['room_photos', 'room_number', 'hotel_room', 'room_price', 'type', 'all_inclusive', 'room_description']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
