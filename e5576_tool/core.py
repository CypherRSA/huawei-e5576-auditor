import requests
import xml.etree.ElementTree as ET
from colorama import init, Fore, Style

init(autoreset=True)

class E5576Auditor:
    def __init__(self, ip="192.168.8.1"):
        self.base_url = f"http://{ip}/api"
        self.session = requests.Session()
        self.tok_head = None
        self.session_id = None

    def get_tokens(self):
        """Fetch session cookies and CSRF request verification tokens."""
        try:
            r = self.session.get(f"{self.base_url}/webserver/SesTokInfo", timeout=5)
            if r.status_code == 200:
                root = ET.fromstring(r.text)
                self.tok_head = root.find('TokInfo').text
                self.session_id = root.find('SesInfo').text
                
                self.session.headers.update({
                    '__RequestVerificationToken': self.tok_head,
                    'Cookie': self.session_id,
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Referer': f"http://{ip}/html/home.html" if 'ip' in locals() else "http://192.168.8.1/html/home.html"
                })
                print(f"{Fore.GREEN}[+] Tokens acquired successfully.")
                return True
        except Exception as e:
            print(f"{Fore.RED}[-] Token acquisition failed: {e}")
        return False

    def login(self, username, password):
        """Authenticate with the router admin account."""
        if not self.get_tokens():
            return False
            
        # Huawei login typically requires base64 or specific XML structures depending on firmware version
        # Here we perform a standard token-backed login sequence
        login_url = f"{self.base_url}/user/login"
        
        # Basic XML payload for login
        payload = f"""<?xml version="1.0" encoding="UTF-8"?>
        <request>
            <Username>{username}</Username>
            <Password>{password}</Password>
            <CurrentPool></CurrentPool>
        </request>"""
        
        try:
            r = self.session.post(login_url, data=payload, timeout=5)
            if "<response>OK</response>" in r.text:
                print(f"{Fore.GREEN}[+] Successfully logged in as '{username}'.")
                # Refresh tokens post-login
                self.get_tokens()
                return True
            else:
                print(f"{Fore.YELLOW}[!] Login response: {r.text.strip()}")
        except Exception as e:
            print(f"{Fore.RED}[-] Login error: {e}")
        return False

    def scan_endpoints(self, endpoints):
        """Audit a list of endpoints and report status codes / error codes."""
        print(f"\n{Fore.CYAN}{'ENDPOINT':<40} | {'STATUS':<8} | {'RESPONSE'}")
        print("-" * 80)
        
        for ep in endpoints:
            url = f"{self.base_url}/{ep}"
            try:
                r = self.session.get(url, timeout=3)
                resp_snippet = r.text.strip().replace('\n', ' ')[:40]
                status_color = Fore.GREEN if r.status_code == 200 else Fore.YELLOW
                print(f"{ep:<40} | {status_color}{r.status_code:<8}{Style.RESET_ALL} | {resp_snippet}")
            except Exception as e:
                print(f"{ep:<40} | {Fore.RED}{'ERROR':<8}{Style.RESET_ALL} | {str(e)}")

    def test_payload(self, endpoint, xml_payload):
        """Send a custom POST payload to a target endpoint."""
        url = f"{self.base_url}/{endpoint}"
        print(f"{Fore.CYAN}[*] Sending POST payload to {endpoint}...")
        try:
            r = self.session.post(url, data=xml_payload, timeout=5)
            print(f"{Fore.GREEN}[+] HTTP Status: {r.status_code}")
            print(f"{Fore.WHITE}[+] Response Body:\n{r.text.strip()}")
        except Exception as e:
            print(f"{Fore.RED}[-] Request failed: {e}")