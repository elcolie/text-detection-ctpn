import os

import cv2
import numpy as np
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS


def write_text(boxes, scores, im_fn):
    with open(os.path.join(FLAGS.output_path, os.path.splitext(os.path.basename(im_fn))[0]) + ".txt",
              "w") as f:
        for i, box in enumerate(boxes):
            line = ",".join(str(box[k]) for k in range(8))
            line += "," + str(scores[i]) + "\r\n"
            f.writelines(line)


def draw_squares(boxes, img, rh, rw, im_fn, scores, resize=True, imwrite=True):
    for i, box in enumerate(boxes):
        cv2.polylines(img, [box[:8].astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0),
                      thickness=2)
    if resize:
        img = cv2.resize(img, None, None, fx=1.0 / rh, fy=1.0 / rw, interpolation=cv2.INTER_LINEAR)
    if imwrite:
        cv2.imwrite(os.path.join(FLAGS.output_path, os.path.basename(im_fn)), img[:, :, ::-1])

    write_text(boxes, scores, im_fn)
