from pathlib import Path

# 対象動画の絶対PATHを指定
VIDEO_PATH = Path('/home/gesogeso/ビデオ/sample/sample.mp4')


def get_trimed_video_path():
    return Path(str(VIDEO_PATH).replace('.mp4', '_trimed.mp4'))


def get_each_frame_tsv():
    parent_dir = '/'.join(str(VIDEO_PATH).split('/')[:-1])
    return Path(parent_dir) / 'each_frame.tsv'


def get_milestone_tsv():
    parent_dir = '/'.join(str(VIDEO_PATH).split('/')[:-1])
    return Path(parent_dir) / 'milestone.tsv'