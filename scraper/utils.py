import urllib.request
from urllib.request import urlopen
from header import header
BASE_URL = "http://lalafo.kg"
def get_html(url):
    request = urllib.request.Request(url=url,headers=header)
    html = urlopen(request)
    return html