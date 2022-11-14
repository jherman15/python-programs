from pathlib import Path

if __name__ == '__main__':

    dir_path = Path(r'C:\python_lab_jh\TXTs')
    infile = Path('tekst1.txt')
    outfile = Path('out.txt')

    replaced_words = {
        'i': 'oraz',
        'oraz': 'i',
        'nigdy': 'prawie nigdy',
        'dlaczego': 'czemu'
    }

    with open(dir_path/infile, 'r') as f:
        input_text = f.read()

    new_text_words = []
    for word in input_text.split():
        if word in replaced_words.keys():
            new_text_words.append(replaced_words[word])
        else:
            new_text_words.append(word)

    new_text = " ".join(new_text_words)

    if dir_path.is_dir():
        with open(dir_path/outfile, "w") as f:
            f.write(new_text)
            print('File with exchanged words created.')
    else:
        print("Directory doesn't exist.")