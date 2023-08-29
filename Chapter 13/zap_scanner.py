# zap_scanner.py

"""
Description:
    Use ZAP API to perform scans on the target systems


Author:
    Nishant Krishna

Created:
    31 July, 2023
"""

import requests

class ZapScanner:
    def get_active_scan_status(self):
        params = {'apikey': '4qot4rnp1vi7f6qaa10080528a'}
        response = requests.get(f'http://localhost:8080/JSON/ascan/action/scan/', params=params)

        if (response.status_code == 200):
            json_response = response.json()
            zap_scan_id = str(json_response["scan"])
            print('ZAP scan ID: ', zap_scan_id)
        else:
            print(f'No scans running. Status code: {str(response.status_code)}')

    def get_alert_summary(self):
        params = {'apikey': '4qot4rnp1vi7f6qaa10080528a'}
        response = requests.get(f'http://localhost:8080/JSON/alert/view/alertsSummary/', params=params)

        if (response.status_code == 200):
            json_response = response.json()
            print(json_response["alertsSummary"])
        else:
            print(f'No scan summary available. Status code: {str(response.status_code)}')


if __name__ == "__main__":
    scanner = ZapScanner()
    scanner.get_active_scan_status()
    scanner.get_alert_summary()
