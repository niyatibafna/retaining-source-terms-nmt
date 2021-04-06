import argparse
import os


def process(text: str):
    words = text.split()
    result = []
    for word in words:
        if word == '<s>':
            continue

        splitted = word.split('|')
        result.append(splitted[0].lower())

    return ' '.join(result)


def preprocess_file(input_file: str, output_dir: str):
    hindi_file = []
    en_file = []
    with open(input_file, 'r') as f:
        for line in f:
            stripped_line = line.rstrip()
            splitted_line = stripped_line.split('\t')
            en_file.append(process(splitted_line[3]))
            hindi_file.append(process(splitted_line[4]))

    with open(os.path.join(output_dir, 'hindi.data'), 'w') as f:
        for line in hindi_file:
            print(line, file=f)

    with open(os.path.join(output_dir, 'en.data'), 'w') as f:
        for line in en_file:
            print(line, file=f)






if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tokenizes and outputs to two separeate files to use later for GIZA++.')
    parser.add_argument('--input-file', help='Path to export file from corpus.')
    parser.add_argument('--output-dir', help='Directory where will be files outputed.')
    args = parser.parse_args()
    preprocess_file(args.input_file, args.output_dir)
