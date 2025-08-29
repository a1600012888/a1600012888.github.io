import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def download_videos_and_update_html(html_file_path):
    """
    Parses an HTML file to find video sources, downloads the videos,
    and updates the HTML to point to the local files.

    Args:
        html_file_path (str): The path to the HTML file.
    """
    # Create a folder to store the downloaded videos and the updated HTML
    output_folder = "downloaded_videos"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and parse the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all video tags
    video_tags = soup.find_all('video')

    if not video_tags:
        print("No video tags found in the HTML file.")
        return

    for video_tag in video_tags:
        source_tag = video_tag.find('source')
        if source_tag and source_tag.get('src'):
            video_url = source_tag['src']

            # Get the filename from the URL
            parsed_url = urlparse(video_url)
            video_filename = os.path.basename(parsed_url.path)
            local_video_path = os.path.join(output_folder, video_filename)

            # Download the video
            try:
                print(f"Downloading {video_url}...")
                response = requests.get(video_url, stream=True)
                response.raise_for_status()  # Raise an exception for bad status codes

                with open(local_video_path, 'wb') as video_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        video_file.write(chunk)
                print(f"Successfully downloaded to {local_video_path}")

                # Update the src attribute in the HTML
                source_tag['src'] = video_filename

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {video_url}: {e}")

    # Save the updated HTML content
    updated_html_filename = "updated_" + os.path.basename(html_file_path)
    updated_html_path = os.path.join(output_folder, updated_html_filename)
    with open(updated_html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"\nSuccessfully created updated HTML file: {updated_html_path}")

if __name__ == '__main__':
    # The name of your original HTML file
    input_html_file = 'model_1_userstudy_idx_0_100.html'

    if os.path.exists(input_html_file):
        download_videos_and_update_html(input_html_file)
    else:
        print(f"Error: The file '{input_html_file}' was not found in the current directory.")
