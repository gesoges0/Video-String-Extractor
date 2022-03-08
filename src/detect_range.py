from base import VIDEO_PATH

import cv2
import os.path


def output_one_img(video_path, frame_no=0):
    cap_file: cv2.VideoCapture = cv2.VideoCapture(video_path)

    width = cap_file.get(cv2.CAP_PROP_FRAME_WIDTH)  # 192.0
    height = cap_file.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 1080.0
    frame_count = cap_file.get(cv2.CAP_PROP_FRAME_COUNT)  # 774: [0: 773]の整数値が使える
    print("width:", width)
    print("height:", height)
    print("総frame数:", frame_count)

    if frame_no != 0:
        cap_file.set(cv2.CAP_PROP_POS_FRAMES, frame_no - 1)
    ret, frame = cap_file.read()
    print(type(frame))  # numpy.ndarray
    print(frame.shape)  # (1080, 1920, 3)
    return frame


def output_img(output_path, nd_array):
    cv2.imwrite(output_path, nd_array)


def put_rect_on_img(nd_array, x, y, w, h):
    img = cv2.rectangle(nd_array, (x, y), (x + w, y + h), (255, 255, 0), 3)
    return img


if __name__ == '__main__':

    # 対象範囲を調べるための操作
    video_path = str(VIDEO_PATH)
    frame = output_one_img(video_path, frame_no=50)
    video_name, ext = os.path.splitext(video_path)
    output_path = video_name + "_one_frame" + ".png"
    output_img(output_path, frame)

    # 画像の対象範囲をマーキング
    x, y = 1100, 700
    w, h = 820, 200
    marked_img = put_rect_on_img(frame, x, y, w, h)
    output_path = video_name + "_one_frame_marked" + ".png"
    output_img(output_path, frame)

    # 画像の範囲を出力
    txt_path = './range.txt'
    with open(txt_path, 'w') as f:
        f.write(f'{x},{y},{w},{h}')
