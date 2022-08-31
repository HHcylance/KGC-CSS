import json
from posixpath import split
import numpy as np
from numpy.core.fromnumeric import transpose
from numpy.lib.twodim_base import tri
import pandas as pd
import os
import collections
import pickle

from pandas.io.formats.format import return_docstring





def creat_data(path):
    path = os.path.join(path, 'data.json')
    lhs, rel, rhs = [], [], []
    database = []
    entities = set()
    with open(path, 'r', encoding='utf-8-sig') as data_json:
        data = json.load(data_json)
        node_n = data['nodes']
        relation = data['links']
        # print(node_n)
        # print(rel)
        for r in relation:
            if r['label'] == '合作':
                _rel = '1'
            elif r['label'] == '作者':
                _rel = '2'
            elif r['label'] == '刊登':
                _rel = '3'
            # print(_rel) 
            database.append(" ".join([r['source'], _rel, r['target']]))
            lhs.append(r['source'])
            rel.append(_rel)
            rhs.append(r['target'])    
            entities.add(r['source'])
            entities.add(r['target'])
    data = {
        "head":lhs,
        "relation":rel,
        "tail":rhs
    }
    data = pd.DataFrame(data)
    return entities, data
    
   

def typical_samling(data):
    # 如果使用相同的seed( )值，则每次生成的随机数都相同，numpy.random.seed(seed=2)
    np.random.rand()  
    # 用分组函数groupby()进行数据的分组，分组依据为'TYPE'这一属性
    gbr = data.groupby('relation')  
     # 获取分组后gbr的数据
    gbr.groups   
    # 所有数据中60%作为训练数据集，20%作为测试数据集
    train_rate = 0.6    
    # 全部数据中3种关系的元组数
    num_tup = []
    for rel in ['1', '2', '3']:
        count = data['relation'] == rel
        print(count)
        num_tup.append(count.sum())
    # print(num_tup)
    
    num_train_tup = np.array([(int)(round(i*train_rate)) for i in num_tup])   # round函数对数进行四舍五入处理
    num_test_tup = np.array([(int)(round(i*(1-train_rate)/2)) for i in num_tup])
    num_val_tup = num_tup - num_train_tup - num_test_tup
    print(num_train_tup)
    print(num_test_tup)
    print(num_val_tup)

    # 定义分层抽样的字典，格式为：组名：数据个数
    typicalNDict_train = {'1': num_train_tup[0], '2': num_train_tup[1], '3': num_train_tup[2]}  # 此处要根据不同的地物类型的总数设置抽样的数据
    typicalNDict_test = {'1': num_test_tup[0], '2': num_test_tup[1], '3': num_test_tup[2]}  # 此处要根据不同的地物类型的总数设置抽样的数据
    typicalNDict_val = {'1': num_val_tup[0], '2': num_val_tup[1], '3': num_val_tup[2]}

    # 函数定义
    def typicalsamling(group, typicalNDict):
        name = group.name
        n = typicalNDict[name]
        return group.sample(n=n)

    # 返回值：抽样后的训练数据框,此处抽取的是按照分层抽样的方法，抽取的60%的训练数据
    result_train = data.groupby('relation').apply(typicalsamling, typicalNDict_train)
    print(result_train.head())
    result_train.to_csv('train.csv', index=False)

    #返回值：抽样后的测试数据框,此处抽取的是按照分层抽样的方法，抽取的30%的测试数据，是随机抽取的数据，有可能与训练数据集有重复的数据
    result_val = data.groupby('relation').apply(typicalsamling, typicalNDict_val)
    print(result_val.head())
    result_val.to_csv('valid.csv', index=False)

    #返回值：抽样后的测试数据框，注意，此处是抽取完70%的训练数据之后，剩下的30%的数据，与训练集不会有重复的数据，该数据集带有分类的标签
    result_test = data.groupby('relation').apply(typicalsamling, typicalNDict_test)
    print(result_test.head())
    result_test.to_csv('test.csv', index=False)

    # #返回值：剩下的30%的数据，该数据集不带有分类的标签，专门用来验证的
    # result_test = result_test_label.iloc[:, :-1]      #去除result_test_label中的最后一列，也就是去除标签列
    # print(result_test.head())
    # result_test_label.to_csv('csv_data/sample_test.csv', index=False)

    print('训练数据集中每种样例的个数:\n', result_train['relation'].value_counts())
    print('验证数据集中每种样例的个数:\n', result_val['relation'].value_counts())
    print('测试数据集中每种样例的个数:\n', result_test['relation'].value_counts())


def check(triples, entities,data):
    count = 0
    # print(triples)
    trip_ent = set()
    for l in triples:
        rhs, rel, lhs = l.strip().split('\t')
        trip_ent.add(rhs)
        trip_ent.add(lhs)
    # print(trip_ent)
    if entities.issuperset(trip_ent):
        add_ent = set(entities).difference(set(trip_ent))
    triple_add = []
    for ent in add_ent:
        triple_add_idx = data[(data['head'] == ent) | (data['tail'] == ent)].index
        # print(triple_add_idx[1])
        if len(triple_add_idx) > 1:
            trip = data.loc[triple_add_idx[0]].values.tolist()
            trip_l = trip[0]+'\t'+trip[1]+'\t'+trip[2]+'\n'
            triple_add.append(trip_l)
            trip = data.loc[triple_add_idx[1]].values.tolist()
            trip_l = trip[0]+'\t'+trip[1]+'\t'+trip[2]+'\n'
            triple_add.append(trip_l)
        # else:
            trip = data.loc[triple_add_idx[0]].values.tolist()
            trip_l = trip[0]+'\t'+trip[1]+'\t'+trip[2]+'\n'
            triple_add.append(trip_l)
    # print(triple_add)
    # print(triples)
    triple_add.extend(triples)
    return triple_add


        
        


if __name__ == "__main__":
    path  = ''
    for spilt in ['train', 'test', 'valid']:
        file_name = spilt + '.csv'
        entities, data = creat_data(path)
        if not os.path.exists(os.path.join(path, file_name)):
            typical_samling(data)
        with open(file_name, 'r') as file:
            line = file.readlines()
            line = line[1:]
        triples = []
        for l in line:
            rhs, rel, lhs = l.split(',')
            triple = rhs + "\t" + rel + "\t" + lhs
            triples.append(triple)
        if spilt == 'train':
            triples = check(triples, entities, data)
        with open(spilt, 'w') as wr_file:
            wr_file.writelines(triples)
        os.remove(spilt +'.csv')
        


   