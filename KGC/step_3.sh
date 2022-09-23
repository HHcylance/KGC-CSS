CUDA_VISIBLE_DEVICES=0 python run_get_ensemble_data.py \
    --dataset WN18RR \
    --model_class roberta \
    --model_name_or_path ./result/WN18RR_roberta-large \
    --output_dir ./result/WN18RR_roberta-large \
    --seed 42 \
    --fp16 
