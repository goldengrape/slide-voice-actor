
# coding: utf-8

# # 使用mac自带的TTS引擎为PPT配音
# 

# In[8]:


import sys, os
from pptx import Presentation


# ## 读取ppt中每页的注释

# In[7]:


# if __name__=="__main__":
#     ppt_filename=sys.argv[1]
ppt_filename = "data/test.pptx"


# In[6]:


ppt_path=os.path.dirname(ppt_filename)


# In[ ]:


def get_notes_text(ppt_filename):
    prs = Presentation(ppt_filename)
    dict={}
    for index, slide in enumerate(prs.slides):
        notes_slide = slide.notes_slide
        text = notes_slide.notes_text_frame.text
        dict[index]=text
    return dict

