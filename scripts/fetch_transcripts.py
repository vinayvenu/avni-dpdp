#!/usr/bin/env python3
"""Fetch YouTube transcripts and save them as text files in the video/ directory."""

import os
import re
from youtube_transcript_api import YouTubeTranscriptApi

VIDEOS_FILE = os.path.join(os.path.dirname(__file__), "..", "videos")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "video")


def extract_video_id(url):
    match = re.search(r"[?&]v=([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None


def fetch_transcript(video_id):
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    lines = []
    for entry in transcript:
        start = entry.start
        minutes = int(start // 60)
        seconds = int(start % 60)
        lines.append(f"[{minutes:02d}:{seconds:02d}] {entry.text}")
    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(VIDEOS_FILE) as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        video_id = extract_video_id(url)
        if not video_id:
            print(f"Skipping invalid URL: {url}")
            continue

        out_path = os.path.join(OUTPUT_DIR, f"{video_id}.txt")
        if os.path.exists(out_path):
            print(f"Already exists, skipping: {video_id}")
            continue

        print(f"Fetching transcript for {video_id} ({url}) ...")
        try:
            transcript = fetch_transcript(video_id)
            with open(out_path, "w") as f:
                f.write(f"Source: {url}\n\n")
                f.write(transcript)
                f.write("\n")
            print(f"  Saved to {out_path}")
        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
