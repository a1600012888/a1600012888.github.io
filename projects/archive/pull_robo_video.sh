mkdir -p robo_videos_phase_2

# for folder in droid ego4d epic_kitchens language_table pandas something
for folder in bridge driod
do
  wget "https://huggingface.co/datasets/YunjinZhang/robo_videos_phase_2/resolve/main/${folder}/index.html" \
       -O "robo_videos_phase_2/${folder}.html"
done

