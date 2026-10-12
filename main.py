import argparse
from e5576_tool.core import E5576Auditor

COMMON_ENDPOINTS = [
    "developer/developermode-featureswitch",
    "app/atport-status",
    "device/config.xml",
    "device/basic_information",
    "device/device_feature_switch",
    "filemanager/upload",
    "system/deviceinfo",
    "webserver/SesTokInfo"
]

def main():
    parser = argparse.ArgumentParser(description="Huawei E5576-856 Endpoint Auditor & Payload Tester")
    parser.add_argument("--ip", default="192.168.8.1", help="Router IP address")
    parser.add_argument("--user", default="admin", help="Admin username")
    parser.add_argument("--password", required=True, help="Admin password")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Scan command
    subparsers.add_parser("scan", help="Scan common Huawei API endpoints")
    
    # Test payload command
    test_parser = subparsers.add_parser("test", help="Test a custom XML payload against an endpoint")
    test_parser.add_argument("--endpoint", required=True, help="API endpoint path (e.g. developer/developermode-featureswitch)")
    test_parser.add_argument("--data", required=True, help="Raw XML string payload")

    args = parser.parse_args()

    auditor = E5576Auditor(ip=args.ip)
    
    print("[*] Authenticating with router...")
    if not auditor.login(args.user, args.password):
        print("[-] Authentication failed. Exiting.")
        return

    if args.command == "scan":
        auditor.scan_endpoints(COMMON_ENDPOINTS)
    elif args.command == "test":
        auditor.test_payload(args.endpoint, args.data)

if __name__ == "__main__":
    main()