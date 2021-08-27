from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
#
# """"Create your models here."""
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(uploud_to='profile_pic', default='user.png')
#
#     def save(self, *args, **kwargs):
#         return super().save(*args, **kwargs)
#
#         img = Image.open(self.image.path)
#
#         if img.width > 300 and img.height > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
