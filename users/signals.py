from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User 
from .models import Profile

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print("Profile Signal trigger!!")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def deletingUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender = User)
post_delete.connect(deletingUser, sender = Profile)