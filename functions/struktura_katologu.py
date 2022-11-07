from pathlib import Path

def check(path:str):
    print(f"*****\nEntered: {path}\n***")
    p = Path(path)
    for x in p.iterdir():
        if x.is_dir():
            check(x)
        elif x.is_file():
            print(x)

if __name__ == '__main__':
    check(r"../venv")        #sciezka do pliku


