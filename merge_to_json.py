import argparse
import json
import random

import sys
import logging
import datetime

logging.basicConfig(level=logging.WARNING)

def wlog(obj, newline=1):
    if newline == 1: sys.stderr.write('{} -> {}\n'.format(datetime.datetime.now(), obj))
    else: sys.stderr.write('{} -> {}'.format(datetime.datetime.now(), obj))
    #if newline == 1: wlog(obj, file=sys.stderr, flush=True)
    #else: wlog(obj, file=sys.stderr, end='', flush=True)
    sys.stderr.flush()

def check_duplicate_ids(file1, file2):
    # 读取第一个 JSON 文件
    with open(file1, 'r') as f1:
        data1 = json.load(f1)
    
    # 读取第二个 JSON 文件
    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    # 构建集合来存储已经遇到的 "id" 值
    encountered_ids = set()

    # 检查第一个文件的 "id" 是否有重复
    for item in data1:
        if 'id' in item:
            if item['id'] in encountered_ids:
                wlog(f'Duplicate id found in {file1}: {item["id"]}')
            else:
                encountered_ids.add(item['id'])

    # 检查第二个文件的 "id" 是否有重复
    for item in data2:
        if 'id' in item:
            if item['id'] in encountered_ids:
                wlog(f'Duplicate id found in {file2}: {item["id"]}')
            else:
                encountered_ids.add(item['id'])

    # 打印检查结果
    if len(encountered_ids) == len(data1) + len(data2):
        wlog('No duplicate ids found.')
    else:
        wlog('Duplicate ids found.')


def merge_and_shuffle_json(file1, file2, output_file):

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    # 统计每个输入中 "id" 的个数
    id_counts = {'file1': len(data1), 'file2': len(data2)}

    # 合并数据
    merged_data = data1 + data2

    # 打乱 "id" 的顺序
    # 注意：此处假设每个输入的 "id" 都不会重复，否则打乱顺序可能导致不正确的匹配
    random.shuffle(merged_data)

    # 写入合并后的 JSON 文件
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=2, ensure_ascii=False)

    # 打印统计结果
    wlog('Number of ids in file1: {}'.format(id_counts['file1']))
    wlog('Number of ids in file2: {}'.format(id_counts['file2']))
    wlog('total of ids in merged file: {}'.format(len(merged_data)))

if __name__ == "__main__":

    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="Merge and shuffle JSON files")
    # 添加位置参数
    parser.add_argument("file1", help="Path to the first JSON file")
    parser.add_argument("file2", help="Path to the second JSON file")
    parser.add_argument("output_file", help="Path to the output JSON file")

    # 解析命令行参数
    args = parser.parse_args()

    check_duplicate_ids(args.file1, args.file2)

    merge_and_shuffle_json(args.file1, args.file2, args.output_file)

