import yt_dlp
import csv

channel_url = "https://www.youtube.com/@EnglishByClips/videos"

ydl_opts = {
    'quiet': True,
    'extract_flat': True,
}

videos = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(channel_url, download=False)
    if 'entries' in result:
        for video in result['entries']:
            videos.append((video['title'], video['url']))

# Save to CSV
with open('youtube_videos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'URL'])
    writer.writerows(videos)

print(f"✅ Saved {len(videos)} videos to CSV.")



# from pytube import YouTube, Channel
# import csv

# channel_url = "https://www.youtube.com/@EnglishByClips/videos"

# # Get the channel object
# channel = Channel(channel_url)

# # Fetch all video URLs
# video_urls = channel.video_urls

# # Extract titles and URLs
# videos = []
# for url in video_urls:
#     try:
#         yt = YouTube(url)
#         videos.append((yt.title, url))
#     except Exception as e:
#         print(f"Error fetching {url}: {e}")

# # Save to CSV
# with open('youtube_videos.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Title', 'URL'])
#     writer.writerows(videos)

# print(f"✅ Saved {len(videos)} videos to 'youtube_videos.csv'")