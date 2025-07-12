from collections import defaultdict 
from django.db import models 
from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField 
from django.core.validators import MinValueValidator, MaxValueValidator 


 
class UserProfile(AbstractUser): 
    STATUS_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
    )
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(15), 
                                                       MaxValueValidator(110)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG') 
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default = 'client')

    def __str__(self):
        return f'{self.first_name}' 


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=60)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='owner')
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(6)], verbose_name='Рейтинг')
    hotel_video = models.FileField(upload_to='hotel_vid/', null=True, blank=True)



    def __str__(self):
        return f'{self.hotel_name} , {self.country} , {self.city}'

    def get_average_rating(self):
        ratings = self.review.all()
        if ratings.exists():
            return (round(sum(rating.stars for rating in ratings) / ratings.count(), 1))
        return 0

class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_photos', on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/')


    def __str__(self):
        return f'{self.hotel_image}'




class Room(models.Model):
    room_number = models.IntegerField()
    hotel_room = models.ForeignKey(Hotel, related_name='hotel_room', on_delete=models.CASCADE)
    ROOM_CHOICES = (
        ('free', 'free'),
        ('booked', 'booked'),
        ('busy', 'busy'),
    )
    room_status = models.CharField(choices=ROOM_CHOICES, max_length=30)
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=32)
    room_price = models.PositiveIntegerField()
    room_description = models.TextField()
    all_inclusive = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.hotel_room},{self.room_number},{self.type}'



class RoomPhotos(models.Model):
    room_photos = models.ForeignKey(Room, related_name='room_photos',on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')


    def __str__(self):
        return f'{self.room_image}, {self.room_photos}'



class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user')
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE, related_name='comments')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,11)], verbose_name="Рейтинг", null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'

class Room(models.Model):
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=[
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('out_of_service', 'Out of Service')])

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[
        ('booked', 'Booked'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    canceled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
