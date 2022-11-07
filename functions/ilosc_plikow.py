from pathlib import Path

def liczenie(path:str):
    count = 0
    p = Path(path)
    for x in p.iterdir():
        if x.is_dir():
            count += 1
    return count
