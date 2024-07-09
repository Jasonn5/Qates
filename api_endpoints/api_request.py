import requests

class EspoCRMRequest:
    @staticmethod
    def get_with_url(url):
        response = requests.get(url)
        return response

    @staticmethod
    def get_with_url_headers(url, headers):
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def get_with_url_headers_params(url, params, headers):
        response = requests.get(url, params=params, headers=headers)
        return response

    @staticmethod
    def post(url, headers, payload):
        response = requests.post(url, headers=headers, data=payload)
        return response


    @staticmethod
    def delete(url, headers):
        response = requests.delete(url, headers=headers)
        return response

    @staticmethod
    def post_json(url, headers, payload):
        response = requests.post(url, headers=headers, json=payload)
        return response

    @staticmethod
    def post_without_headers(url, payload):
        response = requests.post(url, json=payload)
        return response