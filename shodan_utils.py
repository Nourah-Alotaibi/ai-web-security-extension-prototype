import os
import shodan

def get_shodan_info(domain_or_ip):
    key = os.environ.get("SHODAN_API_KEY")
    if not key:
        return {"error": "Set SHODAN_API_KEY to enable this optional integration."}
    try:
        api = shodan.Shodan(key)
        result = api.host(domain_or_ip)
        return {
            "ip": result["ip_str"], "hostnames": result.get("hostnames"),
            "ports": result.get("ports"), "org": result.get("org"),
            "os": result.get("os"), "vulns": result.get("vulns", [])
        }
    except Exception as error:
        return {"error": str(error)}
