import sys
import datetime
from django.core.management.base import BaseCommand

from accounts.models import CustomUser
from detection.models import UserDates


class Command(BaseCommand):
    help = 'Get Data From Ml'

    def handle(self, *args, **options):
        self.stdout.write('Getting Data...')
        FILE = '/data_' + str(datetime.datetime.now().date()) + '.txt'
        lst = []
        try:
            f = open("static/files/" + FILE, "r+")
        except Exception as e:
            try:
                f = open("/home/nikunj/Projects/Face_Key_Django/face_key/static/files/" + FILE, "r+")
            except Exception as e:
                pass
        for obj in f:
            lst = list(
                map(
                    str, obj.rstrip().replace("'", "").replace(" ", "").replace("{", "").replace("}", "").split(',')
                )
            )
        f.close()
        lst_id = [int(x.split('_')[1]) for x in lst]
        for id in lst_id:
            obj = CustomUser.objects.get(id=id)
            if not obj.user.all().filter(date=datetime.datetime.now().date()).filter(attend=True).exists():
                UserDates.objects.create(
                    user=obj,
                    date=datetime.datetime.now().date(),
                    attend=True
                )
        self.stdout.write('Done...!')
