from pathlib import Path

if __name__ == '__main__':
    s = 'dlaczego ja'
    s = s.replace('dlaczego', '')
    print(s)

    dir_path = Path(r'C:\python_lab_jh\TXTs')
    infile = Path(dir_path / 'tekst1.txt')
    outfile = "tekst1_cleaned.txt"

    f = open(infile)

    delete_list = ["się", "i", "oraz", "nigdy", "dlaczego"]
    lst = []

    for line in f:
        for word in delete_list:
            if word in line:
                line = line.replace(word, '')
        lst.append(line)
    f.close()
    #with open(infile) as fin, open(outfile, "w+") as fout:
    #    for line in fin:
    #for word in delete_list:
    #line = line.replace(word, "")
    #        fout.write(line)
