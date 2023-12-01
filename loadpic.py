import os
import json
def load():
    dir1=os.path.join(os.path.dirname(__file__),'pic')
    txt1 = os.path.join(os.path.dirname(__file__),'picture.txt')
    with open(txt1,'w',encoding='utf8') as f1: 
        for path in os.listdir(dir1):
            # f1.write('"')
            f1.write(os.path.join(dir1,path))
            # f1.write('"')
            f1.write(",")
    
    with open(txt1,'r',encoding='utf8') as f3:
        str = f3.read()

    str_list = str.split(',')[:-2]

    with open('pic.json','r',encoding='utf8') as file:
        data = json.load(file)

    data['pic'] = str_list

    with open('pic.json','w',encoding='utf8') as file:
        json.dump(data,file)
    
    