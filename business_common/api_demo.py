import requests
from common.custom_logs import info_log


class ApiDemo:
    @staticmethod
    def api_post(url, user_id, wps_sid, body):
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'cookie': "wps_sid={}".format(wps_sid)
        }

        info_log(f"request headers: {headers}")
        info_log(f"request body: {body}")
        response = requests.post(url=url, json=body, headers=headers, timeout=10)
        info_log(f"response code: {response.status_code}")
        info_log(f"response body: {response.json()}")
        return response

