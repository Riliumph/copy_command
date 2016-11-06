# -*- coding: utf-8 -*-
from argparse import ArgumentParser as ArgParser  # Unix like arguments
import shutil
import os


def Parser():
    usage = 'Usage: python {} FILE [input_file <file>] [out_dir <string>] [--tree] [--help]'.format(__file__)
    parser = ArgParser(usage=usage)
    parser.add_argument(nargs=None, type=str, dest='input_file', help='input data file path')
    parser.add_argument(nargs=None, type=str, dest='output_dir', help='output directory path')
    parser.add_argument('--tree', nargs='?', type=bool, const=True, default=False, dest='is_tree',
                        help='copy while keeping the directory structure')
    return parser.parse_args()


if __name__ == '__main__':
    args = Parser()
    print(args.input_file)
    print(args.output_dir)
    # Read input text
    path_list = []
    for path in open(args.input_file):
        path_list.append(path.rstrip('\n'))
    print('path_list:')
    print(path_list)
    # Make output dir
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    # Copy Loop
    for path in path_list:
        if not os.path.exists(path):
            print('[' + path + '] does not exist.')
            continue
        if args.is_tree:
            shutil.copytree(path, args.output_dir)
        else:
            shutil.copy2(path, args.output_dir)
