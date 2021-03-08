# HTTP-tester-tool
Is s simple multi tread tool for creating a flood of HTTP GET requests. Initially was created for testing WordPress installation on Azure VMs

Powered by "concurrent.futures" and "ThreadPoolExecutor" particularly.

## How to use

```javascript
http-test.py testUrl numberOfRequests max_workers getRequestTimeout
```
##Parameters

- testUrl: host name, like "https://www.google.com/"
- numberOfRequests: total number of request
- max_workers: max parallel tasks (thread)
- getRequestTimeout: timeout for each request


#Using in Windows
For simplicity, can be used with the http-test.exe that was created with "pyinstaller"
