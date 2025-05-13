import yt_dlp
import whisper
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def extract_clips(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict['formats'][0]['url']
    return [{'url': video_url, 'start': 10, 'end': 20, 'subtitles': 'This is a sample subtitle'}]

def burn_subtitles(video_path, text, start, end):
    clip = VideoFileClip(video_path).subclip(start, end)
    subtitle = TextClip(
        text, fontsize=60, font='Arial-Bold', color='white', stroke_color='black', stroke_width=2, size=clip.size, method='caption'
    ).set_position(('center', 'bottom')).set_duration(end - start)
    final = CompositeVideoClip([clip, subtitle])
    final.write_videofile(f"output/{os.path.basename(video_path)}", codec="libx264", audio_codec="aac")
