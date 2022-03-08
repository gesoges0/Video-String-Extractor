import cv2
import numpy as np
import csv
from PIL import Image
import pyocr
from base import get_each_frame_tsv, get_trimed_video_path


def cv2pillow(image):
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image


if __name__ == '__main__':

    # 動画読み取りの準備
    trimed_video_path = get_trimed_video_path()
    cap_file: cv2.VideoCapture = cv2.VideoCapture(str(trimed_video_path))
    tools = pyocr.get_available_tools()
    tool = tools[0]

    # 基礎情報
    fps = cap_file.get(cv2.CAP_PROP_FPS)
    frame_count = cap_file.get(cv2.CAP_PROP_FRAME_COUNT)  # 774: [0: 773]の整数値が使える
    print('fps:', fps)
    print('frame_count:', frame_count)

    # 結果出力のためのtxt
    tsv_path = str(get_each_frame_tsv())

    with open(tsv_path, 'w') as f:
        header = ['frame_no', 'msec', 'string']
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(header)

        while True:
            ret, frame = cap_file.read()
            if not ret:
                break
            pos_frames = cap_file.get(cv2.CAP_PROP_POS_FRAMES)
            pos_msec = cap_file.get(cv2.CAP_PROP_POS_MSEC)

            # cv2 -> pillow
            img = cv2pillow(frame)

            # 文字読み取り
            txt = tool.image_to_string(
                img,
                lang="eng",
                builder=pyocr.builders.TextBuilder(tesseract_layout=3)
            )

            writer.writerow([pos_frames, pos_msec, txt])
            print(pos_frames, f'{round(pos_frames / frame_count, 4) * 100: .2}', txt)
