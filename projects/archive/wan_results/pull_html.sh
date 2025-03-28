#!/bin/bash

# Create the subfolder if it doesn't exist

# Download each index.html file and rename them using the folder name

wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/wandb_1.3b_t2v_shift_5.0/index.html" \
     -O "wandb_1.3b_t2v_shift_5.0.html"

wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/output_videos_wan_1.4B_baseline_ts3/index.html" \
     -O "output_videos_wan_1.4B_baseline_ts3.html"

wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/wandb_14b_timeshift_5.0/index.html" \
     -O "wandb_14b_timeshift_5.0.html"

wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/wandb_1.4b_ft_7kiters/index.html" \
     -O "wandb_1.4b_ft_7kiters.html"
