
# coding: utf-8

# In[1]:


from  AppKit import NSSpeechSynthesizer
import sys
import Foundation
import os
import subprocess


# In[2]:


if __name__ == "__main__":
    OUTPUT_FILE = "data/tts_test.aiff"    # 输出音频的保存路径，请根据自己的情况替换
    txt_file="data/test.txt"
    with open(txt_file, "r") as txt_file:  
        TEXT = txt_file.read()


# In[3]:


def tts(TEXT):
    nssp = NSSpeechSynthesizer
    ve = nssp.alloc().init()
    ve.setRate_(200)
    return ve

def save_tts(TEXT, filename):
    url = Foundation.NSURL.fileURLWithPath_(filename)
    tts(TEXT).startSpeakingString_toURL_(TEXT,url)
    return filename

# def save_short_tts(TEXT, filename):
#     url = Foundation.NSURL.fileURLWithPath_(filename)
#     tts(TEXT).startSpeakingString_toURL_(TEXT,url)
#     return filename
    

# def save_tts(TEXT, filename):
#     max_length=5000
    
#     split_TEXT_list=[TEXT[i:i+max_length] for i in range(0, len(TEXT), max_length)]
#     fname_list=[]
#     for index, t in enumerate(split_TEXT_list):
#         split_fname="tts_temp_{:03d}.aiff".format(index)
#         save_short_tts(t, split_fname)
#         fname_list.append(split_fname)
        
#     #ffmpeg -i "concat:input1.ts|input2.ts|input3.ts" -c copy output.ts
#     with open("tts_tmp_list.txt", "w") as f:
#         for v in fname_list:
#             f.write("file "+"'{}'\n".format(v)) # 注意ffmpeg在从txt里调用文件名时, 似乎是用了相对路径  
#     subprocess.call(["ffmpeg", "-f", "concat",
#                      "-i", "tts_tmp_list.txt",
#                      "-c", "copy",
#                      filename])
    
# #     for f in fname_list:
# #         os.remove(f)
# #     os.remove("tts_tmp_list.txt")
    
#     return filename


# In[4]:


if __name__=="__main__":
    save_tts(TEXT, OUTPUT_FILE)


# In[5]:


# ! ffmpeg -f concat -i tts_tmp_list.txt -c copy data/tts_test.aiff

