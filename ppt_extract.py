
# coding: utf-8

# 读取ppt, 将ppt中的注释文字提取出来

# In[11]:


from pptx import Presentation
import pandas as pd


# In[2]:


if __name__=="__main__":
    ppt_filename="data/test.pptx"


# In[22]:


def get_notes_text(ppt_filename):
    prs = Presentation(ppt_filename)
    dict={}
    for index, slide in enumerate(prs.slides):
        notes_slide = slide.notes_slide
        text = notes_slide.notes_text_frame.text
        dict[index]=text
    return dict


# 将每个注释转换成语音

# In[19]:


from generate_voice import tts


# In[27]:


def get_notes_voice(notes_dict):
    voice_dict={}
    for index, text in notes_dict.items():
        voice_dict[index]=tts(text)
    return voice_dict


# 将语音分别保存为音频mp3

# In[ ]:


if __name__=="__main__":

    notes_dict=get_notes_text(ppt_filename)
    voice_dict=get_notes_voice(notes_dict)


# In[33]:


def save_notes_voice(voice_dict):
    temp_file_dict={}
    for index, voice_data in voice_dict.items():
        temp_filename="data/temp_{:03d}.mp3".format(index)
        with open(temp_filename, 'wb') as outfile:
            outfile.write(voice_data)
        temp_file_dict[index]=temp_filename
    return temp_file_dict


# 将音频mp3插入到每张幻灯片中, 
# 
# 咦, 似乎卡关了. 没有找到如何将mp3插入到幻灯中的方法
