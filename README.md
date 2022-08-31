# Knowledge Completion Method of Combining Structural Information with Semantic Information
## 1. Thanks
The repository is partially based on [huggingface transformers](https://github.com/huggingface/transformers), [KG-BERT](https://github.com/yao8839836/kg-bert), [RotatE](https://github.com/DeepGraphLearning/KnowledgeGraphEmbedding) and [StAR](https://github.com/wangbo9719/StAR_KGC). 

## 2. Installing requirement packages
- conda create -n StAR python=3.6 
- source activate StAR
- pip install numpy torch tensorboardX tqdm boto3 requests regex sacremoses sentencepiece matplotlib

## 3. Dataset
- WN18RR, FB15k-237 

## 4. Training and Test
- you need to change the path to your own
- get the results of the graph embedding model in ./rotate
- run run_enmable.sh in ./rotate
- then run the step_2 to step_4 in order.





