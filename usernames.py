#!/bin/python3

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Generate usernames based on information of a person. Cupps didn't suffice.")
    parser.add_argument(
        '-fn', '--first-name',
        help='the first name of the person'
    )
    parser.add_argument(
        '-ln', '--last-name',
        help='the last name of the person'
    )
    parser.add_argument(
        '-o', '--output-file',
        help='write the list into an output file'
    )
    return parser.parse_args()


def generate_usernames(first_name: str, last_name: str) -> [str]:
    # Preprocessing
    # TODO: case sensitivity
    first_name_letter = first_name[:1]
    last_name_letter = last_name[:1]
    char_list = ['', '.', '-', '_']

    username_list = []

    # Singular
    username_list.append(first_name)
    username_list.append(last_name)
    
    # Basic
    for char in char_list:
        username_list.append(first_name + char + last_name)

    # First name 1
    for char in char_list:
        username_list.append(first_name_letter + char + last_name)

    # Last name 1
    for char in char_list:
        username_list.append(first_name + char + last_name_letter)

    # Birth year
    # TODO: Take all entries and:
    # 1. Add year at end
    # 2. Add last 2 digits at end
    # Make it so you can take a range if you dont know (1965-1970)?

    return username_list


def main():
    args = parse_args()
    username_list = generate_usernames(first_name=args.first_name, last_name=args.last_name)
    if args.output_file:
        with open(args.output_file, 'w') as output_writer:
            for username in username_list:
                output_writer.writelines(username + '\n')
    print(*username_list, sep="\n")

if __name__ == '__main__':
    main()
