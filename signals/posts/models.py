from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Now we need signals to handle what is going to take place when save method is executed on the "Post".

# In order to handle the receiving part, we need to define a function.

# The arguments that go into these receiving function are first the sender. Sender is actually the model that is signalling this to take place.

# "**kwargs" is the keyword arguments.

# def save_post(sender, instance, **kwargs):

def save_post(sender, instance, **kwargs):
    print("something")

def after_delete_post(sender, instance, **kwargs):
    print("you deleted something")

# "connect" is the method you pass to attach the receiver, sender.

pre_save.connect(save_post, sender=Post) # the first "something" is called at the beginning of the save method.

post_save.connect(save_post, sender=Post) # the second "something" is called at the end of the save method.

post_delete.connect(after_delete_post, sender=Post) 

# There is also another signal called "request finished" which basically listens when a request is finished.