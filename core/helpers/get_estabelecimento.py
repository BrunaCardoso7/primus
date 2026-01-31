from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def get_estabelecimento(self):
    return User.objects.get(id=settings.FEEDBACK_OWNER_ID)
