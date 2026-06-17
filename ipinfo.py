import urllib.request
import json
import sys

def get_ip_info(ip=""):
    url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))

        print("\n" + "=" * 40)
        print("        IP INFORMATION")
        print("=" * 40)
        print(f"  IP        : {data.get('ip', 'N/A')}")
        print(f"  Hostname  : {data.get('hostname', 'N/A')}")
        print(f"  City      : {data.get('city', 'N/A')}")
        print(f"  Region    : {data.get('region', 'N/A')}")
        print(f"  Country   : {data.get('country', 'N/A')}")
        print(f"  Location  : {data.get('loc', 'N/A')}")
        print(f"  ISP/Org   : {data.get('org', 'N/A')}")
        print(f"  Timezone  : {data.get('timezone', 'N/A')}")
        print("=" * 40 + "\n")

    except Exception as e:
        print(f"Failed to fetch IP info: {e}")

if __name__ == "__main__":
    ip = sys.argv[1] if len(sys.argv) > 1 else ""
    get_ip_info(ip)
