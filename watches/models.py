from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url


class WatchList(models.Model):
    class Meta:
        ordering = ['list_order', 'friendly_name']

    list_name = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    friendly_name = models.CharField(
        max_length=100, unique=True, verbose_name=' name'
    )
    list_order = models.IntegerField(default=1000)

    def __str__(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        # creating url friendly name from user entered friendly_name
        self.list_name = slugify(self.friendly_name)
        super().save(*args, **kwargs)


class WatchMovement(models.Model):
    movement_name = models.CharField(
        max_length=100, unique=True, verbose_name=' name'
    )

    def __str__(self):
        return self.movement_name


class Watch(models.Model):
    class Meta:
        verbose_name_plural = 'Watches'

    # general watch details
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watch_owner'
    )
    list_name = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name='watch_list'
    )
    movement_type = models.ForeignKey(
        WatchMovement, on_delete=models.CASCADE, related_name='watch_movement'
    )
    make = models.CharField(max_length=100, null=False, blank=False)
    collection = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    movement_model = models.CharField(max_length=50, blank=True)
    image = CloudinaryField(
        'image', default='placeholder', asset_folder='/wot_watches/'
    )
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
        parts = [self.make]
        if self.collection:
            parts.append(self.collection)
        if self.model:
            parts.append(self.model)
        return " ".join(parts)

    def delete(self, *args, **kwargs):
        # checking to see if the image is a placeholder and delete image if not
        if self.image != 'placeholder':
            public_id = self.image.public_id
            cloudinary.uploader.destroy(public_id)
        # proceed with normal deletion
        super().delete(*args, **kwargs)

    def get_optimized_image_url(self):
        return cloudinary_url(
            self.image.public_id,
            secure=True,
            fetch_format="auto",
            quality="auto:eco",
            width=400,
            height=400,
            crop="fill"
        )[0]
