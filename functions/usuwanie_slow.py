def delete(path:str, list_delete:list[str]):
    txt = open(path, 'r', encoding='utf-8')
    rep = txt.read()
    txt.close()
    rep = rep.split(' ')
    for i, word in enumerate(rep):
        for y in list_delete:
            if word == y:
                rep[i] = ''
    rep = ' '.join(rep)
    return rep



