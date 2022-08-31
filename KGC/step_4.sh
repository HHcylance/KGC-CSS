CUDA_VISIBLE_DEVICES=2 python ./ensemble/run.py \
--do_train --do_eval --do_prediction --seen_feature \
--mode tail \
--learning_rate 1e-3 \
--feature_method mix \
--neg_times 5 \
--num_train_epochs 3 \
--hinge_loss_margin 0.6 \
--train_batch_size 32 \
--test_batch_size 64 \
--logging_steps 100 \
--save_steps 2000 \
--eval_steps -1 \
--warmup_proportion 0 \
--output_dir ./StAR/result/WN18RR_roberta-large_ensemble  \
--dataset_dir ./StAR_KGC-master/StAR/result/WN18RR_roberta-large \
--context_score_path ./StAR/result/WN18RR_roberta-large \
--translation_score_path ../rotate/models/RotatE_wn18rr_0  \
--seed 42 