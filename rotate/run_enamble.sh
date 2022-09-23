CUDA_VISIBLE_DEVICES=3 \python ./codes/run.py \
		--cuda --init ../rotate/models/RotatE_wn18rr_0 \
		--test_batch_size 16 \
		--star_info_path  PATH\
		--get_scores --get_model_dataset 

# CUDA_VISIBLE_DEVICES=2 \python ./codes/run.py \
# 		--cuda --init ../models/RotatE_FB15k-237_0 \
# 		--test_batch_size 16 \
# 		--star_info_path  PATH\
# 		--get_scores --get_model_dataset 
