# -*- coding: utf-8 -*-

class ApiErrors:
    def __init__(self):
        api_text = 'API Error: '
        self.errors_dict = {
            # Server default errors
            500: {
                "error": f"{api_text}Internal server error",
                "code": 500
            },
            404: {
                "error": f"{api_text}Not Found",
                "code": 404
            },
            405: {
                "error": f"{api_text}Method is not allowed(POST or GET)",
                "code": 405
            },

    def return_error(self, code, *args):
        return {
            'error': self.errors_dict[code]['error'] % args,
            'code': self.errors_dict[code]['code']
        }
