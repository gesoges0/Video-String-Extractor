# video-string-detector


## 区切り位置を特定
Flourishの動画を用意

### 対象動画のみのディレクトリをつくると便利
```commandline
mkdir sample
mv sample.mp4 sample/sample.mp4
```

### 対象動画の絶対PATHを指定する
```commandline
vim base.py
```

### 動画から対象範囲を特定する
<動画名>_one_frame.pngと<動画名>_one_frame_marked.pngを生成する

範囲を記載したrange.txtを出力する
```commandline
python detect_range.py
```
![src_one_frame_marked](https://user-images.githubusercontent.com/33025417/175195282-c0c0b324-2f84-44c0-8897-4d47daf89384.png)

### 対象範囲の動画を生成する
range.txtを読み込み対象範囲の動画を生成する
```commandline
python make_target_range_video.py
```
https://user-images.githubusercontent.com/33025417/175195670-89adf99f-5a9e-44bc-af36-ff12bda45c82.mp4

### 対象範囲動画の各フレームを読み込みTSVを生成する
each_frame.tsvを作成
```commandline
python make_tsv_from_target_range_video.py
```

### stringの節目のみのtsvをつくる
milestone.tsv
```commandline
python make_milestone.py
```
```
label	start
01/01/17	33.333333333333336
01/02/17	3183.333333333333
01/03/17	4133.333333333333
01/04/17	5033.333333333333
01/05/17	5983.333333333333
01/06/17	6883.333333333333
01/07/17	7783.333333333333
01/08/17	8733.333333333332
01/09/17	9633.333333333332
```
