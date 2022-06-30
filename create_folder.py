import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_path: str):
        params = {"path": folder_path}
        create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(create_folder_url, headers=self.get_headers(), params=params)
        return response.status_code