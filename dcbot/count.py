import os
def count():
    dir = os.path.join(os.path.dirname(__file__),'not_only_for_kai')
    i =0 
    for file in os.listdir(dir):
        i = i+1
    return i