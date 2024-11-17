# pip install moviepy
# > python video_audio_increaser.py -p ~/workspace/recordings/video.mkv -db 10

# tool for increasing the audio of a video file

import argparse
import os
from moviepy.editor import VideoFileClip
from datetime import datetime


def increase_volume(input_file, output_file, volume_db):
    video = VideoFileClip(input_file)
    volume_factor = 10 ** (volume_db / 20.0)

    video = video.volumex(volume_factor)
    video.write_videofile(output_file, codec="libx264", audio_codec="aac")


def main():
    parser = argparse.ArgumentParser(description="Increase the volume of a video.")
    parser.add_argument(
        "-p", "--path", required=True, help="Path to the input video file."
    )
    parser.add_argument(
        "-o", "--output", help="Optional path to save the output video file."
    )
    parser.add_argument(
        "-db",
        "--decibels",
        type=float,
        required=True,
        help="Volume increase in decibels.",
    )

    args = parser.parse_args()

    input_file = args.path
    output_file = args.output
    volume_db = args.decibels

    if not output_file:
        input_dir = os.path.dirname(input_file)
        input_filename = os.path.basename(input_file)
        base_name, ext = os.path.splitext(input_filename)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{base_name}_volume_{timestamp}{ext}"

        output_file = os.path.join(input_dir, output_filename)

    increase_volume(input_file, output_file, volume_db)


if __name__ == "__main__":
    main()
