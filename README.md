# Huawei E5576-856 Endpoint Auditor

A specialized Python utility designed to interact with, audit, and test API endpoints on Huawei E5576-856 and compatible Balong/Hilink mobile routers.

## Features
- **Session & CSRF Token Management**: Automatically handles `SesTokInfo` parsing, session cookies, and request verification tokens.
- **Endpoint Enumeration**: Quickly scans known namespaces (`developer`, `system`, `device`, etc.) to map out active versus permission-gated routes.
- **Custom Payload Fuzzing**: Test custom XML payloads against restricted endpoints to evaluate firmware behavior and error responses.

## Prerequisites
- Python 3.8 or higher installed on your system.
- Git installed for cloning the repository.
- Network connection to the router's local gateway (default: `http://192.168.8.1`).

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/CypherRSA/huawei-e5576-auditor.git](https://github.com/CypherRSA/huawei-e5576-auditor.git)
   cd huawei-e5576-auditor