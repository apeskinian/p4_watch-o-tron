from django.db import models
from django.contrib.auth.models import User
import cloudinary.uploader
from cloudinary.models import CloudinaryField

class WatchList(models.Model):
    list_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.list_name

class WatchMovement(models.Model):
    movement_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.movement_name

class Watch(models.Model):
    # general watch details
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_owner')
    list_name = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='watch_list')
    movement_type = models.ForeignKey(WatchMovement, on_delete=models.CASCADE, related_name='watch_movement')
    make = models.CharField(max_length=100, null=False, blank=False)
    collection = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    movement_model = models.CharField(max_length=50, blank=True)
    image = CloudinaryField('image', default='placeholder', asset_folder='/wot_watches/')
    # complications
    complication_chronograph = models.BooleanField(default=False)
    complication_date = models.BooleanField(default=False)
    complication_day = models.BooleanField(default=False)
    complication_gmt = models.BooleanField(default=False)
    complication_world_timer = models.BooleanField(default=False)
    complication_moonphase = models.BooleanField(default=False)
    complication_power_reserve = models.BooleanField(default=False)
    complication_tourbillon = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.make} {self.collection} {self.model}'

    def delete(self, *args, **kwargs):
        # checking to see if the image is a placeholder and delete image if not
        if self.image != 'placeholder':
            public_id = self.image.public_id
            cloudinary.uploader.destroy(public_id)
        # proceed with normal deletion
        super().delete(*args, **kwargs)