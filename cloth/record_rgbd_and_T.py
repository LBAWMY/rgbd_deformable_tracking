import os
import sys

import numpy as np
import argparse
import h5py

import roslib

roslib.load_manifest('rosbag')
import rosbag

import warnings
import progressbar
import cv2
import transformations as tf

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="the .bag file")
    parser.add_argument('--max_strlen', type=int, default=255,
                        help="maximum length of encoded strings")
    parser.add_argument('--out', type=str, default=None,
                        help="name of output file")
    parser.add_argument('--topic', type=str, nargs='*',
                        help="topic name to convert. defaults to all. "
                             "multiple may be specified.")
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print >> sys.stderr, 'No file %s' % args.filename
        sys.exit(1)
    fname = os.path.splitext(args.filename)[0]
    if args.out is not None:
        output_fname = args.out
    else:
        output_fname = fname + '.hdf5'
        if os.path.exists(output_fname):
            print >> sys.stderr, 'will not overwrite %s' % output_fname
            sys.exit(1)

    bag = rosbag.Bag(args.filename)

    db = h5py.File(output_fname, mode='w')

    height, width = 480, 640
    len = 500
    images = db.create_dataset('rgb', (len, height, width, 4), dtype=np.uint8)
    depths = db.create_dataset('depth', (len, height, width), dtype=np.float)
    T_ws = db.create_dataset('T_w_k', (len, 4, 4), dtype=np.float)
    img_idx = 0
    depth_idx = 0
    T_ws_idx = 0

    # progressbar
    _pbw = ['converting %s: ' % fname, progressbar.Percentage()]
    pbar = progressbar.ProgressBar(widgets=_pbw, maxval=bag.size).start()

    for topic, msg, t in bag.read_messages(topics=args.topic):
        msg_type_str = str(type(msg))
        if args.topic is not None and topic not in args.topic:
            continue
        if 'sensor_msgs' in msg_type_str and 'Image' in msg_type_str and 'image' in topic:
            img_array = np.fromstring(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 4)
            if img_idx >= len:
                print('ignored the rest of the data: img_idx is full')
                continue
            images[img_idx] = img_array[:, :, ::-1]
            img_idx += 1
        elif 'sensor_msgs' in msg_type_str and 'Image' in msg_type_str and 'depth' in topic:
            depth_array = np.frombuffer(msg.data, dtype=np.float32).reshape(msg.height, msg.width)
            # depth_array = cv2.flip(depth_array, 0)
            if depth_idx >= len:
                print('ignored the rest of the data: depth_idx is full')
                continue
            depths[depth_idx] = depth_array
            depth_idx += 1
        elif topic == '/tf':
            for transform in msg.transforms:
                p = transform.transform
                T_w = tf.quaternion_matrix([p.rotation.w, p.rotation.x, p.rotation.y, p.rotation.z])
                T_w[:3, 3] = np.array([p.translation.x, p.translation.y, p.translation.z])
                if T_ws_idx >= len:
                    print('ignored the rest of the data: T_w_k is full')
                    continue
                T_ws[T_ws_idx] = T_w
                T_ws_idx += 1
        pbar.update(bag._file.tell())

    cv2.imwrite('rgb.png', img_array)
    cv2.imwrite('depth.png', depth_array)
    print('finished. the index of rgb is %d, the index of depth is %d, the index of T_w_k is %d' % (img_idx, depth_idx, T_ws_idx))