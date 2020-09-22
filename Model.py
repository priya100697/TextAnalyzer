from collections import defaultdict
ml_model = {}
total_words = {}

def train_using_default_dict(path):

    data = list()
    with open(path, "r", encoding='utf8') as f:
        for line in f:
            data.append(line)

    dic1 = defaultdict(list)
    for chat in data:
        dic1[chat.split(":")[0]].append(chat.split(":")[1])

    for k,v in dic1.items():
        tdict = {}
        total=0
        for chat in v:
            for word in chat.lower().strip().split(' '):
                total+=1
                if word not in tdict:
                    tdict[word]=1
                else:
                    tdict[word]+=1

        for key in tdict:
            tdict[key]=tdict[key]/total

        ml_model[k]=tdict
        total_words[k]=total

def test(txt):
    pdict={}

    iprob = 1/len(ml_model.keys())
    for person,wordlist in ml_model.items():
        prob=iprob
        for string in txt.lower().strip().split(" "):
            if string in wordlist:
                prob*=wordlist[string]
            else:
                prob*=0.2/total_words[person]
        pdict[person]=prob
    m=-1
    user=""
    for person,prob in pdict.items():
        if prob > m:
            m=prob
            user = person
    print(user)
    print(pdict)






