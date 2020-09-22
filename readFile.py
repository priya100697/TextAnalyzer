def read_file(path):
    with open(path, "r" , encoding='UTF8') as file:
        with open("chat.txt", "w" ,encoding='UTF8') as wfile:
            li = []
            for line in file:
                if not line.lower().strip().isspace():
                    text=line.strip().split('-')
                    if len(text)  > 1 :
                        person=text[1].strip().split(":")[0]
                        li.append(text[1])
                    else:
                        text1=person+':'+text[0].strip()
                        li.append(text1)
            for i in li:
                if i.find(':') != -1:
                    wfile.write(f'{i}\n')
    return 0