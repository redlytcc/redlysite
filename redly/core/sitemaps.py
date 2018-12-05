from django.contrib.sitemaps import Sitemap
from .models import User
from django.contrib.auth import get_user_model

User=get_user_model()


class Useriten(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return User.objects.all()
