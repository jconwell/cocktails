

def clean_cocktail_list(in_path, out_path):
    # open text file and iterate through each line
    out_list = []
    with open(in_path, 'r') as handle:
        for line in handle.readlines():
            # remove trailing newline
            line = line.strip()
            if line is None or len(line) == 0:
                continue
            # remove the space parenthesis and everything after
            line = line.split(' (')[0]
            # remove the word cocktail
            line = line.replace(' cocktail', '').replace(' Cocktail', '').strip()
            # upper case each word
            line = ' '.join([word.capitalize() for word in line.split(' ')])
            out_list.append(line)

    #  sort new list and remove duplicates
    out_list = list(set(out_list))
    out_list.sort()

    # write new list to file
    with open(out_path, 'w') as handle:
        for line in out_list:
            handle.write(f"{line}\n")
    print(f'{len(out_list)} cocktails')
    # 744 cocktails


def main():
    in_path = "cocktails_raw.txt"
    out_path = "cocktails.txt"
    clean_cocktail_list(in_path, out_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

