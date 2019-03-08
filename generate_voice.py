
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


# In[2]:


TEXT="""
, , ,

这一部分讲解的是人工晶体度数的计算和生物学测量,

在这一课里, 我会对人工晶体度数计算的基本概念做详细的介绍, 应该了解最基本的SRK公式, 知道改换A常数时, 应该如何改变晶体度数, 知道高度近视推荐选择哪些公式, 知道A超测量和IOL master测量的特点.

, , ,

从人工晶体发明的第一天起, 就面临一个问题, 到底要装多少屈光度的晶体到病人眼睛里? 实际上, 第一枚人工晶体, 也就是1949年11月29日, Ridely医生植入到伊丽莎白左眼里的那枚人工晶体, 度数就算错了, 术后病人有1800度近视和600度散光

, , ,

人眼的光学系统, 大致相当于由两个透镜和一个屏幕组合而成.

第一个透镜是角膜, 占了整个眼球屈光力的2/3左右, 大约40 D,

第二个透镜是晶状体, 占1/3的屈光力, 大约19 D,

一个屏幕就是视网膜, 在计算人工晶体度数的时候, 我们只关心视网膜上黄斑中心凹的位置.

如果需要计算出一束平行光经过角膜和晶状体如何聚焦到视网膜上, 那么只需要知道这两个透镜的位置、屈光力和屏幕的位置.

所以只需要知道:
角膜的屈光度, 晶状体的位置, 晶状体的屈光度, 和视网膜的位置.
就可以了.

, , ,

做完了白内障手术, 人工晶体就替代了晶状体, 那么一个人工晶体眼也是两个透镜一个屏幕, 透镜分别是角膜和人工晶体, 屏幕是视网膜.


刚才我们说了, 只需要知道:
角膜的屈光度,
人工晶体的位置, 人工晶体的屈光度,
和视网膜的位置.
就可以知道光是如何聚焦的.

要让一个人能够看清楚东西, 就是让一束平行光, 照射进入眼睛以后, 在视网膜上聚焦成一点.

所以角膜的屈光度, 人工晶体的位置, 人工晶体的屈光度, 和视网膜的位置. 里面如果只有一个未知数, 就可以求解出来.

, , ,

这就是一个理论公式, 看起来很复杂, 眼科医生不翻书也不会记得住的.

如果人工晶体的度数是未知数, 那么通过角膜的屈光度, 人工晶体的位置, 视网膜的位置就可以计算出一个准确数值来.

然而, 很不幸. 实际情况是我们遇到了两个未知数而不是一个.

在手术之前, 我们可以测量角膜曲率得到角膜的屈光度, 可以测量眼轴长, 得到视网膜的位置. 但是在手术之前, 我们不知道人工晶体的度数, 是需要求解的, 我们还不知道人工晶体的位置, 为什么呢?

因为天然晶体是更厚的, 厚度大概3-4毫米, 而人工晶体只有薄薄的一片, 可能不到1毫米, 这片人工晶体放入到囊袋里面, 可就不一定是原来天然晶体的位置了.

如何在手术前尽可能准确地估计出人工晶体的位置, 就是各种度数计算公式实际在做的事情.

, , ,

我们说各种度数计算公式实际上就是在估计人工晶体的位置, 也就是 Effective Lens Position, ELP.
最直接的想法, 就是先找个大家的平均值, 于是最最基础的SRK公式设定ELP=4毫米.

但这个公式用着用着发现有问题, 人工晶体并不是总在4mm的位置上.

那么改改吧, 眼轴越长, 人工晶体也应该越靠后, ELP应该越大吧, 于是有SRK two公式,

接下来发现角膜如果很凸的话, ELP可能更长, 于是把K值也纳入考虑, 这就是第三代公式.

再之后发现还有更多可能的参数, 比如角膜的直径也就是所谓白到白距离, 术前前房深度, 术前晶体厚度等等. 这是第四代公式.

今后还可能会有更多的公式, 比如我们可以把所有能够测量的参数都代入进去, 强行用机器学习拟合出一个机器学习公式.

, , ,

详细讲解一下SRK公式,

这是1980年 Sanders, Retzlaff 和 Kraff 发表的公式, 这3位医生研究了2500个病人的数据以后给出了这个非常简单的公式:
度数P 等于 A常数 减去 0.9 乘 角膜曲率K 减去 2.5 乘 眼轴长L.

虽然后世的眼科学家发明了很多很多公式, 但这是最为简单, 也可以直接手算的一个公式.

注意看这个公式, A常数前面没有乘系数, 或者说是乘了正1, 所以当角膜曲率K和眼轴长L都不变的时候, 如果A常数增加, 度数也随着增加, A常数增加多少, 计算出来的度数增加多少.

举个例子, 手术前原来选择了A常数=117.9的人工晶体20 D, 现在手术中发生变化, 需要重新选择A常数=118.4的人工晶体, 应该选多少?

A常数从117.9 增加到118.4, 增加了0.5, 所以人工晶体度数也应该增加0.5, 从20 D增加0.5 D,变成20.5 D.

记住, 是同向的增减.

SRK公式的改进版是SRK two公式, 也就是在计算时根据眼轴长来调整A常数. 其他是一样的.

, , ,

每种型号的人工晶体, 厂家都会给出一个A常数, 这是晶体设计制造好以后就确定了.

不同型号, 厂家给出的A常数可能是不同的, 影响A常数的因素很多. 比如人工晶体设计放置的位置不同, 前房型或者虹膜夹型的, 可能A常数就比较小.

还有其他可能的影响因素, 比如折射率, 光学部的形状, 襻是否有倾斜角度等等.

, , ,

下面浏览一下其他的公式, 这些公式都很复杂, 除了作者, 可能大多数眼科医生不查文献也写不出来这些公式.

Haigis公式里一下子就有好多参数, 还有 Hoffer Q, 以及后来的Holladay one和two公式, 这些公式都是内置在机器里面了, 直接选择就可以自动计算了.

, , ,

厂商在卖人工晶体的时候, 会在产品页上详细给出各个公式需要使用的常数,

A常数会给两个, 一个是用在A超测量的, 一个是用在IOL Master测量的, 不一定一致. 如果有其他的测量设备, 最好是由测量设备或者人工晶体的厂商给数据. 医生如果拿不到厂商数据, 而要做研究的话. 光学类的测量, 可以参考IOL master数据, 但可能要经过一些换算, 超声类的测量, 可以参考A超用的参数.

这张幻灯上说“各常数均可由A常数计算”是不对的. 其他常数如果能够由A常数算出来, 那么就只给出A常数好了.


, , ,


我们一开始就说到, 所有的公式其实都是在术前去猜术后人工晶体的位置, 仔细想的话, 是不可能猜准的, 因为IOL在囊袋内的位置, 角度, 形态, 撕囊口的大小, 囊袋纤维化的程度等等, 有大量术前无法测量的因素在起作用, 甚至医生的手术技巧也会有影响. 所以不可能用一个公式去适合所有的眼睛. 只能说某个公式算出来的误差比较小, 在可以接受的范围内.

对于大多数正常眼轴长度的病人, 大概眼轴长度在22到24.5毫米范围内, 所有的公式都还不错. 容易出差错的是在眼轴短的远视, 和眼轴太长的高度近视. 高度近视的病人可能相对多一些, 有研究说对于太长眼轴的眼球可能SRK/T公式准确一些, 但也是统计而言, 针对某个特定的病人可能还是会有比较大的误差.

这个要在术前跟病人充分沟通, 交代好, 有些可能就预留一些近视, 比如留出300度近视, 即使错出100度, 变成200度近视或者400度近视, 影响也不大. 人眼对近视的耐受还可以, 远处模糊一些, 近处还清楚, 反正现代人主要看电脑手机, 病人也能接受. 但是, 万万不可错到远视上去, 那样远近都看不清, 病人受不了.

, , ,


"""


# In[3]:


OUTPUT_FILE = "output.mp3"    # 输出音频的保存路径，请根据自己的情况替换
TEXT=TEXT.replace("\n","¡")


# In[4]:


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


# In[5]:


def xunfei_tts(TEXT, Param, api, max_length=400):
    
#     Param_b64str= construct_base64_str(Param)    

    split_TEXT_list=[''.join(x) for x in zip(*[list(TEXT[z::max_length]) for z in range(max_length)])]
    data=b''
    
    for t in split_TEXT_list:
        # 发送HTTP POST请求
        req = urllib.request.Request(
            api["url"], 
            data=construct_urlencode_utf8(t), 
            headers=construct_header(api, construct_base64_str(Param)))
        
        response = urllib.request.urlopen(req)
        data+=response.read()
        
    return data

def tts(TEXT):
    # 读取API url, API key, APP ID
    with open('API_setup.txt') as json_file:  
        api = json.load(json_file)
    # 构造输出音频配置参数
    Param = {
        "auf": "audio/L16;rate=16000",    #音频采样率
        "aue": "lame",    #音频编码，raw(生成wav)或lame(生成mp3)
        "voice_name": "xiaoyan",
        "speed": "50",    #语速[0,100]
        "volume": "77",    #音量[0,100]
        "pitch": "50",    #音高[0,100]
        "engine_type": "aisound"    #引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
    }
    return xunfei_tts(TEXT, Param,api,max_length=400)


# In[6]:


data=tts(TEXT)


# In[7]:


out_file = open(OUTPUT_FILE, 'wb')
out_file.write(data)
out_file.close()
print('输出文件: ' + OUTPUT_FILE)

# # 读取结果

# if(response.headers['Content-Type'] == "audio/mpeg"):
#     out_file = open(OUTPUT_FILE, 'wb')
#     data = response.read() # a 'bytes' object
#     new_data=data+data+data+data
#     out_file.write(new_data)
#     out_file.close()
#     print('输出文件: ' + OUTPUT_FILE)
# else:
#     print(response.read().decode('utf8'))

