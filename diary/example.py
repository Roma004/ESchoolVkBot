# -*- coding: utf-8 -*-
from diary_api import Diary
import datetime

api = Diary(login='',
            password='')

today = datetime.date.today()

if datetime.datetime.today().isoweekday() == 5:
    use_date = (today + datetime.timedelta(days=3)).strftime('%d.%m.%Y')
else:
    use_date = (today + datetime.timedelta(days=1)).strftime('%d.%m.%Y')

resp = api.send(from_date=use_date, to_date=use_date)

lessons = resp[str(api.childs[0][0])]['days'][0][1]['lessons']

lesson_wrapper = '''
%s
Учитель: %s
%s
Номер урока: %s
Урок начинается в: %s
Урок кончается в: %s
Домашние задание: %s
Тема урока: %s
'''

lessons_info = f'На {use_date}\n{"- " * 10}'
for lesson in lessons:
    lessons_info += lesson_wrapper % (
            lesson['discipline'],
            lesson['teacher'],
            lesson['room'],
            lesson['lesson'][1],
            lesson['lesson'][2],
            lesson['lesson'][3],
            lesson['homework'],
            lesson['subject']
        )

    lessons_info += '- ' * 10

print(lessons_info)
