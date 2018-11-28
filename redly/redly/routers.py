from rest_framework import routers
from core.viewsets import CadUser
from redweb.viewsets import ChatSend

router = routers.DefaultRouter()

router.register(r'create', CadUser)
router.register(r'chatSend', ChatSend)
