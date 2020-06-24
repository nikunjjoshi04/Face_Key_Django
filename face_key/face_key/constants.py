import os
from django.conf import settings

TRAIN_IMAGES_PATH = os.path.join(os.path.join(settings.PROJECT_ROOT, 'static'), 'train_images/')