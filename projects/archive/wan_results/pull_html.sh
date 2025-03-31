#!/bin/bash

# Create the subfolder if it doesn't exist

# Download each index.html file and rename them using the folder name


wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/high_res_baseline_720p_ts5/index.html" \
     -O "wanbaseline_high_res_720p_81f_ts5.html"
wget "https://huggingface.co/datasets/YunjinZhang/video_results_tmp/resolve/main/long_baseline_161f/index.html" \
     -O "wanbaseline_long_480p_161f_ts3.html"
