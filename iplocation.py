req = top.api.AlibabaSecurityYundunXingtuIplocationTotalRequest(url, port)
req.set_app_info(top.appinfo(appkey, secret))

req.ips = "3.5.2.0,45.23.12.45,42.120.237.10"
try:
    resp = req.getResponse()
    print(resp)
except Exception, e:
    print(e)
