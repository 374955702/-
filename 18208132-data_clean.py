import pandas as pd
import re
import warnings
warnings.filterwarnings('ignore')
f=open('DATAt.csv','r',errors='ignore',encoding='gbk')
data=pd.read_csv(f)
stop = open('stop_words.txt', 'r+', encoding='utf-8')
stopword = stop.read().split("\n")
def find_word(content):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    return re.sub(pattern, '', content)
def data_check():
    print('数据大小:', data.shape)
    # 去空
    print('isnull:',data.isnull().any())
    data.dropna(subset=['评论内容'],inplace=True)
    print('评论内容去空后大小', data.shape)
    # 去重
    print(data.duplicated().value_counts())
    data.drop_duplicates(subset=None, keep='first',inplace=True)
    # data.to_csv('cc.csv',index=False)
    print('去重后大小', data.shape)
def clean():
    print('处理数据')
    c_data=data
    # 去除无评论用户
    c_data=c_data[~c_data['评论内容'].str.contains('此用户')]
    c_data = c_data[~c_data['评论内容'].str.contains('买家没有填写评价内容')]
    # 去除评论信息小于4个字符的无意义评论
    c_data=c_data[data['评论内容'].str.len()>=4]
    print('去除无用评论后',c_data.shape)
    # 去除特殊符号
    c_data['评论内容']=c_data['评论内容'].apply(lambda x:find_word(x))
    print(c_data['评论内容'].head(30))
def main():
    data_check()

main()