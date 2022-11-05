if __name__ == '__main__':
    import os

for dirpath, dirnames, filenames in os.walk(r'C:\python_lab_jh'):
    print(
        f"Root: {dirpath}\n"
        f"Sub-directories: {dirnames}\n"
        f"Files: {filenames}\n"
    )
