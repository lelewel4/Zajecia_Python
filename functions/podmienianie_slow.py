def replace(path:str,list_delete:list[str], list_replace:list[str]):
    txt = open(path, 'r', encoding='utf-8')
    rep = txt.read()
    txt.close()
    rep = rep.split(' ')
    for i, word in enumerate(rep):
        for j, y in enumerate(list_delete):
            if word == y:
                rep[i] = list_replace[j]
    rep = ' '.join(rep)
    return rep

