import sys

def file_extensions(filename):
    file_without_ext = []
    files = {}

    with open(filename, 'r') as f:
        for line in f.readlines():
            s = line.replace('\n', '')
            if '.' not in s:
                file_without_ext.append(s)
            else:
                ext = s.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(s)

    return (file_without_ext, files)

def main():
    file = sys.argv[1:]
    file_without_ext, files = file_extensions(file)
    print(f"{len(file_without_ext)} files with no extension")
    for k, v in files.items():
        print(f"{k} {len(v)}")

if __name__ == "__main__":
    main()
