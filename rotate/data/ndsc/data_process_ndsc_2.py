import os

relation_dict = []
relations = ['1','2','3']
for i in range(3):
    relation_dict.append(str(i) + '\t' + relations[i]+'\n')
# print(relation_dict)
with open('relations.dict', 'w') as relations:
    relations.writelines(relation_dict)


splits = ["train", "valid", "test"]
for split in splits:
    dataset_file = os.path.join(split)
    with open(dataset_file, 'r') as file:
        dataset = file.readlines()
    with open(dataset_file+'.txt', 'w') as new_file:
        new_file.writelines(dataset)
node_list = []
for node in range(3543):
    node_dict = str(node)+'\t'+str(node)+'\n'
    # print(node_dict)
    node_list.append(node_dict)
with open('entities.dict', 'w') as entities:
    entities.writelines(node_list)
