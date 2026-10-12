# Huawei E5576-856 Endpoint Auditor

A specialized Python utility designed to interact with, audit, and test API endpoints on Huawei E5576-856 and compatible Balong/Hilink mobile routers.

## Features
- **Session & CSRF Token Management**: Automatically handles `SesTokInfo` parsing and cookie management.
- **Endpoint Enumeration**: Quickly scans known namespaces (`developer`, `system`, `device`, etc.) to map out active vs. permission-gated routes.
- **Custom Payload Fuzzing**: Test custom XML payloads against restricted endpoints to evaluate firmware behavior and error responses.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/huawei-e5576-auditor.git](https://github.com/YOUR_USERNAME/huawei-e5576-auditor.git)
   cd huawei-e5576-auditor