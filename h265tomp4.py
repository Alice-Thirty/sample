import os
import time
import argparse
import shutil
import cv2
import numpy as np
import random
from tqdm import tqdm
from pathlib import Path
import subprocess


def main(arg):

    path = os.path.dirname(arg.input)
    # h264  h265
    img_paths = [p.as_posix() for p in list(Path(path).glob(os.path.join('**', '*.26*')))]
    for i in img_paths:
        if i.endswith('.png'):
            continue
        elif i.endswith('.264'):
            newPath = i.replace('.264','.mp4')
        elif i.endswith('.265'):
            newPath = i.replace('.265','.mp4')

        newPath = newPath.split('/')[-1]
        newPath = os.path.join(arg.output, newPath)
        if not os.path.isdir(arg.output):
            os.makedirs(arg.output, exist_ok=True)
        print(newPath)
        subprocess.run(f'ffmpeg -i {i} -vcodec copy -f mp4  {newPath}', shell=True, check=True)
        #shutil.move(i, arg.output)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", default='input',
                        help="input dir ", required=False, type=str)
    parser.add_argument('-o', "--output", default='output',
                        help="output dir", required=False, type=str)
    arg = parser.parse_args()

    main(arg)
