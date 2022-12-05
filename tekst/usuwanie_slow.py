from pathlib import Path

if __name__ == '__main__':

    # s = 'dlaczego ja'
    # s = s.replace('dlaczego', '')
    # print(s)

    dir_path = Path(r'C:\Users\herma\PycharmProjects\python-programs\tekst\files')
    infile = Path('infile.txt')
    outfile = Path('outfile_deleting.txt')
    #infile_path = dir_path.joinpath(infile)
    #outfile_path = dir_path.joinpath(outfile)
    delete_list = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']

    if dir_path.is_dir():
        with open(dir_path/infile, 'r') as f:
            input_text = f.read()

    input_words = input_text.split()
    new_words = [word for word in input_words if word not in delete_list]
    new_text = " ".join(new_words)

    if dir_path.is_dir():
        with open(dir_path/outfile, "w") as f:
            f.write(new_text)
            print('File with deleted words created.')
    else:
        print("Directory doesn't exist.")


    # dir_path = Path(r'C:\python_lab_jh')
    # a = Path('image2.jpg')
    # b = a.with_suffix('.png')
    #
    # im1 = Image.open(dir_path / 'JPGs' / a)
    # im1.save(dir_path / 'PNGs' / b)

    # for line in infile:
    #    for word in delete_list:
    #        if word in line:
    #            line = line.replace(word, '')
       # lst.append(line)
    #f.close()
    #with open(infile) as fin, open(outfile, "w+") as fout:
    #    for line in fin:
    #for word in delete_list:
    #line = line.replace(word, "")
    #        fout.write(line)
