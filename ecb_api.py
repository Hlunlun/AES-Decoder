import requests
import binascii
import string
import json
import time
import random

# 发送 HTTP 请求
url = 'http://tool.chacuo.net/cryptaes'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '93',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '__yjs_duid=1_427af19a582f9c010f34856d1d5254e31696663246264; Hm_lvt_4183351950d6f3ac05fb254f4eec5518=1696663248; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1697725049,1697785413,1697857080,1697880356; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1697957564',
    'Host': 'tool.chacuo.net',
    'Origin': 'http://tool.chacuo.net',
    'Referer': 'http://tool.chacuo.net/cryptaes',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

cipher = "2NHkjlDyk82JBke5q8CnMQZ1iiHID8QEst+/Ld6lWFMP5omXXh/1LnmrYKOD04idKfzfL+6C96391/iN7+X0eg=="



# 要重复运算的次数
symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','+','\\','|','}',']','[','{','"','\'',':',';','/','?','.','>','<',',',' ']
for i in range(10):
    symbols.append(str(i))
symbols = symbols + list(string.ascii_lowercase) + list(string.ascii_uppercase)
size = len(symbols)
# random.shuffle(symbols)

f1 = open('results_api.txt', 'w',encoding='utf-8')

index = 0

i=0
j=0
for i in range(size):
    for j in range(size):
        for m in range(size):
            for n in range(size):
                f1.write(str(index)+'\n') 
                key = "$\""+symbols[i]+"vXl"+symbols[j]+"K"+symbols[m]+"\\/{9Fp"+symbols[n]   
                data = {
                    'data': cipher,
                    'type': 'aes',
                    'arg': 'm=ecb_pad=zero_block=128_p='+key+'_o=0_s=utf-8_t=1',
                }
                response = requests.post(url, headers=headers, data=data)
                
                if response.status_code == 200:                   
                    response_data = json.loads(response.text)
                    plaintext = response_data.get("data", [])[0]                    
                    if len(plaintext) > 0 :                           
                        f1.write('\n---------------------------------------\n key: '+str(key)+'\n') 
                        f1.write('plaintext: '+plaintext+'\n')     
                index = index+1

                time.sleep(40)
                
                        
