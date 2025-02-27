import math

from moviepy import VideoFileClip


def createVideoSplitTasks(segment_length_in_seconds=120):
    source_video_file = "../../input/samplevideo.mp4"

    # get video length
    video = VideoFileClip(source_video_file)
    duration = math.ceil(video.duration)

    num_segments = math.ceil(duration / segment_length_in_seconds)

    for i in range(num_segments):
        start = i * segment_length_in_seconds
        end = min((i + 1) * segment_length_in_seconds, duration)

        print(f"Creating task for segment {i + 1}: {start} to {end} seconds")
        # TODO: write task to PubSub


if __name__ == "__main__":
    createVideoSplitTasks()
