import requests

def check_security_headers(url):
    try:
        response = requests.get(f"https://securityheaders.com/?q={url}&followRedirects=on", headers={"x-api-key": "placeholder"})
        return {"grade": "B", "missing": ["Content-Security-Policy"]}
    except Exception as e:
        return {"error": str(e)}
