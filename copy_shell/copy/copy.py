# -*- coding: utf-8 -*-
import argparse
import os
import shutil
import sys


def create_parser():
    usage = 'Usage: python {} FILE [input_file <file>] [out_dir <string>] [--skip] [--help]'.format(__file__)
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(nargs=None, type=str, dest='input_file', help='input data file path')
    parser.add_argument(nargs=None, type=str, dest='output_dir', help='output directory path')
    parser.add_argument("-s", "--skip",
                        action="store_true",
                        default=False,
                        dest="skip_overlap",
                        help='skip instead of over writing')
    return parser.parse_args()


def print_progress(now_count, max_count):
    percentage = now_count / max_count * 100
    descriptor = "\r{0:.1f}%({1} of {2}) : [{3:<10}]"
    sys.stdout.write(descriptor.format(percentage, now_count, max_count, "#" * (now_count % 10)))


if __name__ == '__main__':
    args = create_parser()
    print(args.input_file, " ----------> ", args.output_dir)
    # Read input text
    path_list = [line.rstrip('\n') for line in open(args.input_file, "r", encoding="UTF-8")]
    # Make output dir
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    # Check not exist element
    if any(not os.path.exists(file_path) for file_path in path_list):
        not_exist = list(filter(lambda x: not os.path.exists(x), path_list))
        path_list = list(set(path_list) - set(not_exist))
        print("Not exist: ", not_exist)
        print()
    # Check overlap element
    if args.skip_overlap:
        overlap_list = [file_path for file_path in path_list
                        if os.path.exists(os.path.join(args.output_dir, os.path.basename(file_path)))]
        path_list = list(set(path_list) - set(overlap_list))
        print("skipping: ", overlap_list)
        print()
    # Copy Loop
    for i in range(0, len(path_list)):
        file_path = path_list[i]
        try:
            if os.path.isfile(file_path):
                shutil.copy(file_path, args.output_dir)
            else:
                shutil.copytree(fike_path, args.output_dir)
        finally:
            print_progress(i + 1, len(path_list))
