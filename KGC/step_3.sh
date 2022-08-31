# CUDA_VISIBLE_DEVICES=1,2,3,5 \
# python run_link_prediction.py \
#     --model_class roberta \
#     --weight_decay 0.01 \
#     --learning_rate 1e-5 \
#     --adam_betas 0.9,0.98 \
#     --adam_epsilon 1e-6 \
#     --max_grad_norm 0. \
#     --warmup_proportion 0.05 \
#     --do_train --do_eval \
#     --do_prediction \
#     --num_train_epochs 7 \
#     --dataset WN18RR \
#     --max_seq_length 128 \
#     --gradient_accumulation_steps 4 \
#     --train_batch_size 16 \
#     --eval_batch_size 128 \
#     --logging_steps 100 \
#     --eval_steps 4000 \
#     --save_steps 2000 \
#     --model_name_or_path roberta-large \
#     --output_dir ./result/WN18RR_roberta-large \
#     --num_worker 12 \
#     --seed 42 \
#     --cls_method cls \
#     --distance_metric hyperbolic \
#     --overwrite_output_dir

CUDA_VISIBLE_DEVICES=0 \
python run_link_prediction.py \
    --model_class roberta \
    --weight_decay 0.01 \
    --learning_rate 1e-5 \
    --adam_betas 0.9,0.98 \
    --adam_epsilon 1e-6 \
    --max_grad_norm 0. \
    --warmup_proportion 0.05 \
    --do_train --do_eval \
    --do_prediction \
    --num_train_epochs 7. \
    --dataset FB15k-237 \
    --max_seq_length 100 \
    --gradient_accumulation_steps 4 \
    --train_batch_size 16 \
    --eval_batch_size 128 \
    --logging_steps 100 \
    --eval_steps -1 \
    --save_steps 2000 \
    --model_name_or_path roberta-large \
    --output_dir ./result/FB15k-237_roberta-large \
    --num_worker 12 \
    --seed 42 \
    --fp16 \
    --cls_method cls \
    --distance_metric hyperbolic \