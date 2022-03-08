import csv
from base import get_each_frame_tsv, get_milestone_tsv
from dataclasses import dataclass

@dataclass
class Frame:
    label: str
    start: float


if __name__ == '__main__':
    tsv_path = get_each_frame_tsv()
    with open(tsv_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)

        x = None
        frames = []
        for row in reader:
            frame_no, msec, string = row
            msec = float(msec)
            if x != string:
                frame = Frame(label=string, start=msec)
                frames.append(frame)
                x = string

    tsv_path = get_milestone_tsv()
    with open(tsv_path, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        header = ['label', 'start']
        writer.writerow(header)
        for frame in frames:
            writer.writerow([frame.label, frame.start])
