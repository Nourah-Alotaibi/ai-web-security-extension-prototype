import requests
import time

def run_zap_scan(target_url):
    try:
        scan = requests.get(f"http://localhost:8080/JSON/ascan/action/scan/?url={target_url}")
        scan_id = scan.json().get("scan")

        while True:
            progress = requests.get("http://localhost:8080/JSON/ascan/view/status/").json()
            if progress["status"] == "100":
                break
            time.sleep(2)

        alerts = requests.get("http://localhost:8080/JSON/core/view/alerts/?baseurl=" + target_url).json()
        return alerts["alerts"]
    except Exception as e:
        return [{"name": "ZAP error", "description": str(e)}]
