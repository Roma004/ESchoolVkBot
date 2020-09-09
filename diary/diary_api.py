# -*- coding: utf-8 -*-
import requests


class Diary(object):
    def __init__(self, login, password):
        super(Diary, self).__init__()
        params = {"login": login, "password": password}
        session = requests.Session()
        login_response = session.get(
            'https://e-school.ryazangov.ru/rest/login',
            params=params
        ).json()

        print('Try auth')
        print(login_response)
        self.session = session
        self.childs = login_response['childs']
        self.profile_id = login_response['profile_id']
        self.id = login_response['id']
        self.type = login_response['type']
        self.fio = login_response['fio']

    def send(self, **kwargs):
        """
        Use params: from_date and to_date
        """
        url = 'https://e-school.ryazangov.ru/rest/diary'

        response = {}
        try:
            for child in self.childs:
                new_kwargs = kwargs
                new_kwargs.update({"pupil_id": child[0]})
                response.update({
                    str(child[0]): self.session.get(
                        url,
                        params=new_kwargs
                    ).json()
                })
        except Exception as error:
            response = error

        return response
