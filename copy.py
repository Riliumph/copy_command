# -*- coding: utf-8 -*-
from argparse import ArgumentParser as ArgParser  # Unix like arguments
import os
import shutil
import sys
import time


def create_parser():
    usage = 'Usage: python ' + __file__ + ' FILE [input_file <file>] [out_dir <string>] [--tree] [--help]'
    parser = ArgParser(usage=usage)
    parser.add_argument(nargs=None, type=str, dest='input_file', help='input data file path')
    parser.add_argument(nargs=None, type=str, dest='output_dir', help='output directory path')
    return parser.parse_args()


if __name__ == '__main__':
    args = create_parser()
    print(args.input_file, " ----------> ", args.output_dir)
    # Read input text
    path_list = []
    for path in open(args.input_file, "r", encoding="UTF-8"):
        path_list.append(path.rstrip('\n'))
    # Make output dir
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    # Filter
    not_exist = [path for path in path_list if not os.path.exists(path)]
    if len(not_exist) != 0:
        print("Not exist:")
        for path in not_exist:
            print(path)
        print()
    # Copy Loop
    exist_list = [path for path in path_list if os.path.exists(path)]
    for i in range(0, len(exist_list)):
        path = exist_list[i]
        time.sleep(0.01)
        try:
            if os.path.isfile(path):
                shutil.copy(path, args.output_dir)
            else:
                shutil.copytree(path, args.output_dir)
        finally:
            now_count = i + 1
            max_count = len(path_list)
            percentage = now_count / max_count * 100
            descriptor = "\r{0:.1f}%({1} of {2}) : [{3:<10}]"
            sys.stdout.write(descriptor.format(percentage, now_count, max_count, "#" * (now_count % 10)))
