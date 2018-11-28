from django.db import models
from core.models import User
from django.contrib.auth import get_user_model
from functools import partial
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

User=get_user_model()

def make_filepath(field_name, instance, filename):
    new_filename = "%s.%s" % (User.objects.make_random_password(10),filename.split('.')[-1])
    return '/'.join([instance.__class__.__name__.lower(),field_name, new_filename])

class Chat(models.Model):
    nome=models.CharField(max_length=40)
    text=models.TextField(max_length=6000,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to=partial(make_filepath,'media'),blank=True)
    visible=models.IntegerField(default=1)
    def save(self):
        if self.img != '':
            i=Image.open(self.img)
            o=BytesIO()
            i=i.resize((400,300))
            i.save(o,format='PNG',quality=100)
            o.seek(0)
            self.img = InMemoryUploadedFile(o,'ImageField', "%s.png" %self.img.name.split('.')[0], 'image/png', sys.getsizeof(o), None)
            super(Chat,self).save()
        elif self.img == '' and (self.text == '' or self.text == 'null'):
            return
        else:
            super(Chat,self).save()
