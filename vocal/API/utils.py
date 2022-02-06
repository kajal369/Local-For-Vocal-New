import json
from API import config

def makeup_url(url):
    str1 = 'http://'
    server_ip = config.SERVER_IP_ADDRESS
    url1 = str1 + server_ip +'/MeraMandir/' + url
    return url1


def makeupphp_url(url):
    str1 = 'http://'
    server_ip = config.SERVER_IP_ADDRESS
    url1 = str1 + server_ip +'/MeraMandir/' + url
    return url1

def getotp_url(mobileno=None,otp=None):
    url = 'http://2factor.in/API/V1/840dc120-65b2-11ec-b710-0200cd936042/SMS/'+mobileno+'/'+otp+'/ABCDEF'
    return url




