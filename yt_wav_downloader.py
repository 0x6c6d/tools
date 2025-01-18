# pip install audioop-lts pytubefix pydub
# nodejs needs to be installed -> for generating a po token automatically (anti bot detection)

import os
from pytubefix import YouTube
from pydub import AudioSegment

def download_audio(url):
    try:
        download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        if not os.path.exists(download_folder):
            download_folder = os.path.dirname(os.path.abspath(__file__))

        # Download the audio from the YouTube URL
        print(f"Downloading audio to {download_folder}...")
        yt = YouTube(url, 'WEB')
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download(output_path=download_folder, filename="temp_audio.mp4")
        print(f"Downloaded audio to {audio_file}")

        # Convert the downloaded audio to .wav using pydub
        print("Converting audio to .wav format...")
        audio = AudioSegment.from_file(audio_file)
        wav_file_path = os.path.join(download_folder, "yt_audio.wav")
        audio.export(wav_file_path, format="wav")
        print(f"Conversion complete! Saved as {wav_file_path}")

        # Clean up the temporary file
        os.remove(audio_file)
        print("Temporary audio file removed.")

    except Exception as e:
        print(f"An error occurred: {e}")

url = input("Enter the YouTube video URL: ")
download_audio(url)
