import json


with open('datasets/data/WN18RR/train', 'r') as train:
    entities = set()
    for line in train:
        rhs, re, lhs = line.strip().split('\t')
        entities.add(rhs)
        entities.add(lhs)
print(len(entities))
ent = set()
# with open('data.json', 'r', encoding='utf-8-sig') as data_json:
#     data = json.load(data_json)
#     node_n = data['nodes']
#     relation = data['links']
#     # print(node_n)
#     # print(rel)
#     for r in relation:
#         if r['label'] == '合作':
#             _rel = '1'
#         elif r['label'] == '作者':
#             _rel = '2'
#         elif r['label'] == '刊登':
#             _rel = '3'
#         # print(_rel) 
#         # database.append(" ".join([r['source'], _rel, r['target']]))
#         # lhs.append(r['source'])
#         # rel.append(_rel)
#         # rhs.append(r['target'])    
#         ent.add(r['source'])
#         ent.add(r['target'])
# if ent == entities:
#      print('ok')
import os 
import pickle as pkl
import numpy as np
split = 'train'
data = {}
file_path = 'datasets/data/WN18RR/'+split + ".pickle"
with open(file_path, "rb") as in_file:
    data[split] = pkl.load(in_file)
filters_file = open( "datasets/data/WN18RR/to_skip.pickle", "rb")
to_skip = pkl.load(filters_file)
# print(to_skip)
filters_file.close()
#该实体数是训练集上的实体数
# print(data['train'][1][0])
ent_idx = set()
for l in data['train']:
    ent_idx.add(l[0])
    ent_idx.add(l[2])

# print(len(ent_idx))

max_axis = np.max(data["train"], axis=0)
a = np.max(data["train"], axis=1)
n_entities = int(max(max_axis[0], max_axis[2]) + 1)
print('over')