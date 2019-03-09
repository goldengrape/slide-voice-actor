
# coding: utf-8

# 测试讯飞语音

# 导入基本库

# In[1]:


import base64
import json
import time
import hashlib
import urllib.request
import urllib.parse
import json


# 设定输出音频的位置和输入文本文件的位置

# In[2]:


if __name__ == "__main__":
    OUTPUT_FILE = "data/output.mp3"    # 输出音频的保存路径，请根据自己的情况替换
    txt_file="data/test.txt"
    with open(txt_file, "r") as txt_file:  
        TEXT = txt_file.read()


# 按照讯飞的要求, 分别配置设置的字符串, http请求的head和body

# In[3]:


def construct_base64_str(Param):
    # 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
    Param_str = json.dumps(Param)    #得到明文字符串
    Param_utf8 = Param_str.encode('utf8')    #得到utf8编码(bytes类型)
    Param_b64 = base64.b64encode(Param_utf8)    #得到base64编码(bytes类型)
    Param_b64str = Param_b64.decode('utf8')    #得到base64字符串
    return Param_b64str

def construct_header(api, Param_b64str):
    # 构造HTTP请求的头部
    time_now = str(int(time.time()))
    checksum = (api["key"] + time_now + Param_b64str).encode('utf8')
    checksum_md5 = hashlib.md5(checksum).hexdigest()
    header = {
        "X-Appid": api["id"],
        "X-CurTime": time_now,
        "X-Param": Param_b64str,
        "X-CheckSum": checksum_md5
    }
    return header

def construct_urlencode_utf8(t):
    # 构造HTTP请求Body
    body = {
        "text": t
    }
    body_urlencode = urllib.parse.urlencode(body)
    body_utf8 = body_urlencode.encode('utf8')
    return body_utf8


# 将长的txt

# In[4]:


def xunfei_tts(TEXT, Param, api, max_length=300):
    data=b''
    split_TEXT_list=[TEXT[i:i+max_length] for i in range(0, len(TEXT), max_length)]
    for t in split_TEXT_list:
        # 发送HTTP POST请求
        req = urllib.request.Request(
            api["url"], 
            data=construct_urlencode_utf8(t), 
            headers=construct_header(api, construct_base64_str(Param)))
        response = urllib.request.urlopen(req)
        data+=response.read()
#         time.sleep(5)
    return data

def tts(TEXT):
    # 读取API url, API key, APP ID
    with open('API_setup.txt') as json_file:  
        api = json.load(json_file)
    # 构造输出音频配置参数
    Param = {
        "auf": "audio/L16;rate=16000",    #音频采样率
        "aue": "lame",    #音频编码，raw(生成wav)或lame(生成mp3)
        "voice_name": "aisjiuxu",
        "speed": "50",    #语速[0,100]
        "volume": "77",    #音量[0,100]
        "pitch": "30",    #音高[0,100]
        "engine_type": "aisound"    #引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
    }
    return xunfei_tts(TEXT, Param,api,max_length=300)


# In[5]:


if __name__ == "__main__":
    data=tts(TEXT)
    out_file = open(OUTPUT_FILE, 'wb')
    out_file.write(data)
    out_file.close()
    print('输出文件: ' + OUTPUT_FILE)


# In[ ]:




