#CTRL+J
if __name__ == '__main__':
    import os
    dir_path = r'C:\python_lab_jh'
    count = 0

    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)