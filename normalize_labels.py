from __future__ import division
from PIL import Image
import os


img_dir = 'images'
lab_dir = 'labels'
out_dir = 'normalized-labels'


def normalize_label(label, width, height):
    cl, cx, cy, wx, wy = label
    return int(cl), cx/width, cy/height, wx/width, wy/height


if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for filename in os.listdir(img_dir):
    if filename.endswith(".jpg"):
        im_path = os.path.join(img_dir, filename)
        filename_txt = filename.split('.')[0] + '.txt'
        lab_path = os.path.join(lab_dir, filename_txt)
        norm_lab_path = os.path.join(out_dir, filename_txt)

        # Open image
        im = Image.open(im_path)
        width, height = im.size

        # Open labels
        with open(lab_path, "r") as f:
            # there may be multiple bboxes, hence multiple lines
            split_lines = [l.strip().split() for l in f.readlines()]
            labels = [map(float, l) for l in split_lines])

        # Create normalized label
        norm_labels = [normalize_label(label, width, height) for label in labels]

        # Save new label
        with open(norm_lab_path, "w") as f:
            for norm_label in norm_labels:
                c, x, y, w, h = norm_label
                print(f"{int(c)} {x} {y} {w} {h}", file=f)
            # print(str_norm_label)

        # print(im_path, width, height, label, norm_label)

