
# coding: utf-8

# # 使用mac自带的TTS引擎为PPT配音
# 

# In[1]:


import sys, os , subprocess
from pptx import Presentation
from  AppKit import NSSpeechSynthesizer
import Foundation
from pptx.util import Inches


# ## 读取ppt中每页的注释

# In[2]:


def get_notes_text(ppt_filename):
    prs = Presentation(ppt_filename)
    notes_dict={}
    for index, slide in enumerate(prs.slides):
        notes_slide = slide.notes_slide
        text = notes_slide.notes_text_frame.text
        notes_dict[index]=text
    return notes_dict


# ## 将每页注释用tts转换成音频文件

# In[3]:


def save_tts(TEXT, filename):
    nssp = NSSpeechSynthesizer
    ve = nssp.alloc().init()
    ve.setRate_(200)
    url = Foundation.NSURL.fileURLWithPath_(filename)
    ve.startSpeakingString_toURL_(TEXT,url)
    return filename


# In[4]:


def save_notes_voice(notes_dict):
    voice_file_dict={}
    
    for index, text in notes_dict.items():
        voice_filename= "temp_tts_{:3d}.aiff".format(index)
        voice_file_dict[index]=save_tts(text,voice_filename )
    return voice_file_dict


# ## 将每个音频文件插入到ppt页面中

# In[5]:


def insert_voice(voice_file_dict, ppt_filename, output_filename):
    prs = Presentation(ppt_filename)
    left = top = Inches(0.0)
    width = height = Inches(1.0)

    for index, slide in enumerate(prs.slides):
        notes_slide = slide.notes_slide
        shapes = slide.shapes
        movie = shapes.add_movie(voice_file_dict[index], 
                                 left , top , width , height, 
                                 poster_frame_image=None, 
                                 mime_type='video/unknown')

#     ppt_path=os.path.dirname(ppt_filename)
    prs.save(output_filename)


# ## 清理掉临时文件

# In[6]:


def clean_temp(voice_file_dict):
    for index, filename in voice_file_dict.items():
        os.remove(filename)
    


# # 包装

# In[7]:


def main(ppt_filename, output_filename):
    notes_dict=get_notes_text(ppt_filename)
    voice_file_dict=save_notes_voice(notes_dict)
    insert_voice(voice_file_dict, ppt_filename, output_filename)
    clean_temp(voice_file_dict)


# In[8]:


# clean_temp(voice_file_dict)


# In[ ]:


if __name__=="__main__":
    if len(sys.argv)>=3 :
        ppt_filename=sys.argv[1]
        output_filename=sys.argv[2]
    elif len(sys.argv)==2 :
        ppt_filename=sys.argv[1]
        ppt_path=os.path.dirname(ppt_filename)
        output_filename=os.path.join(ppt_path, "output.pptx")
    else:
        print("Error, I need input filename")
    main(ppt_filename, output_filename)

