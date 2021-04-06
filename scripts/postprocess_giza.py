import argparse
import re
from typing import List

def read_file(file_path: str):
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]

def get_boundaries(line: str):
    boundaries = [0]
    for i in range(len(line)):
        if line[i] == '}' and line[i+1] == ')':
            boundaries.append(i+2)

    return boundaries


def process_line_block(lines: List[str]):
    hindi = lines[1].split()
    en = lines[2]
    boundaries = get_boundaries(en)
    en_words = []
    hindi_words = []
    for i in range(len(boundaries)-1):
        word = en[boundaries[i]:boundaries[i+1]]
        word = word.strip()
        word, numbers = word.split(" ", 1)
        en_words.append(word)
        hindi_words.append([])
        for number in re.findall('\d+', numbers):
            hindi_words[-1].append(hindi[int(number)-1])

    return hindi, en_words, hindi_words

def print_format(hindi, en_words, hindi_words):
    print(" ".join(en_words[1:]))
    print(" ".join(hindi))
    for en, cor_hindi_words in zip(en_words, hindi_words):
        print(en, end='')
        for word in cor_hindi_words:
            print(f'\t{word}', end='')
        print()
    print()


def convert(file_path: str):
    lines = read_file(file_path)
    for line_num in range(len(lines)//3):
        start, end = line_num*3, line_num*3+3
        hindi, en_words, hindi_words = process_line_block(lines[start: end])
        print_format(hindi, en_words, hindi_words)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Postprocess of GIZA++ output.')
    parser.add_argument('--file', help='Path to GIZA++ output')
    args = parser.parse_args()
    convert(args.file)
