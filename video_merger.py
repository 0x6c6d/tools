# pip install moviepy
# > python video_merger.py -f ~/workspace/recordings

# tool for merging all the videos inside a directory together
# the merging sequence of the videos is based on the file naming
# e.g. is the first part a.mp4 and the second part b.mp4

import argparse
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips


def merge_videos(input_folder, output_file=None):
    video_files = sorted(
        [
            f
            for f in os.listdir(input_folder)
            if f.lower().endswith((".mp4", ".mkv", ".avi", ".mov"))
        ]
    )

    if not video_files:
        print("No video files found in the specified folder.")
        return

    video_paths = [os.path.join(input_folder, f) for f in video_files]
    print("Merging the files in this sequence:")
    for video in video_paths:
        print(f"  - {video}")

    clips = [VideoFileClip(video) for video in video_paths]
    final_clip = concatenate_videoclips(clips, method="compose")

    if output_file is None:
        output_file = os.path.join(input_folder, "merged_video.mp4")

    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    print(f"Merged video saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Merge videos from a folder into one video."
    )
    parser.add_argument(
        "-f",
        "--folder",
        required=True,
        help="Path to the folder containing video files.",
    )
    parser.add_argument(
        "-o", "--output", help="Optional path to save the merged video."
    )

    args = parser.parse_args()
    merge_videos(args.folder, args.output)


if __name__ == "__main__":
    main()
