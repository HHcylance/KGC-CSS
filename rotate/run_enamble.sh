# CUDA_VISIBLE_DEVICES=0 \python ./codes/run.py \
# 		--cuda --init../rotate/models/RotatE_wn18rr_0 \
# 		--test_batch_size 16 \
# 		--star_info_path .../KGC/result/WN18RR_roberta-large-hy2 \
# 		--get_scores --get_model_dataset 

CUDA_VISIBLE_DEVICES=2 \python ./codes/run.py \
		--cuda --init ../models/RotatE_FB15k-237_0 \
		--test_batch_size 16 \
		--star_info_path .../KGC/result/FB15k-237_roberta-large-hy2 \
		--get_scores --get_model_dataset 
