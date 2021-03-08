# HTTP-tester-tool
Is s simple multi tread tool for creating a flood of HTTP GET requests. Initially was created for testing WordPress installation on Azure VMs

Powered by "concurrent.futures" and "ThreadPoolExecutor" particularly.

## How to use

```javascript
http-test.py testUrl numberOfRequests max_workers getRequestTimeout
```
## Parameters

- testUrl: host name, like "https://www.google.com/"
- numberOfRequests: total number of request
- max_workers: max parallel tasks (thread)
- getRequestTimeout: timeout for each request


# Using in Windows
For simplicity, can be used with the http-test.exe that was created with "pyinstaller"

Usage example is the same as with py-file:
```javascript
http-test.exe testUrl numberOfRequests max_workers getRequestTimeout
```

Also can be used with windows bat-files, to create semi auto tests:
```javascript
http-test.exe https://www.google.com/ 5000 10 10 %*
echo Waiting For Three 3 minutes... 
TIMEOUT /T 180 /NOBREAK

http-test.exe https://www.google.com/ 5000 20 10 %*
echo Waiting For Three 3 minutes... 
TIMEOUT /T 180 /NOBREAK

http-test.exe https://www.google.com/ 5000 30 10 %*
echo Waiting For Three 3 minutes... 
TIMEOUT /T 180 /NOBREAK
```
