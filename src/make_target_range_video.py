from base import VIDEO_PATH
import ffmpeg


def video_trimming(video_path, x, y, w, h):
    """
    video_path # ファイルの絶対パス
    start_x = 850  # 切り取りたい区画のx座標（px）
    start_y = 500  # 切り取りたい区画のy座標（px）
    width = 700  # 切り取りたい区画の幅（px）
    height = 580  # 切り取りたい区画の高さ（px）
    """

    # トリミングファイル・パラメータ指定
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.crop(stream, x, y, w, h)

    # 出力ファイル名生成
    output_file_str = video_path.split(".")
    output_file_name = output_file_str[0] + "_trimed." + output_file_str[1]
    stream = ffmpeg.output(stream, output_file_name)

    # 実行(ファイルがあると上書き)
    ffmpeg.run(stream, overwrite_output=True)


if __name__ == '__main__':

    # rangeを読み込む
    txt_path = './range.txt'
    with open(txt_path) as f:
        x, y, w, h = map(int, f.read().split(','))
        print(x, y, w, h)

    # 上の2つで調整が出来たらx,y,w,hを使ってクロッピング
    video_path = str(VIDEO_PATH)
    video_trimming(video_path, x, y, w, h)