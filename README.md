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

### 対象範囲の動画を生成する
range.txtを読み込み対象範囲の動画を生成する
```commandline
python make_target_range_video.py
```

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


## Premiere Proへ挿入
ラベルと挿絵URL, PATHのTSVを用意

## TSVとラベルTSVからPremiereProで元の動画に挿絵を挿入する
```commandline
pass
```