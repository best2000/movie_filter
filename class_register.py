import re

class star:
    def __init__(self, num, name):
        self.num = num
        self.name = name

def get_starlis():
    linelis = []
    with open("star_map.txt", 'r') as file:
        while True:
            line = file.readline()
            if line == "EOF":
                break
            linelis.append(line)
    #linelis = ['00=dummy\n', '01=aoi tsukasa\n', '02=yui hatano\n', ...]

    starlis = []
    for line in linelis:
        line = re.split('=', line)
        object = star(line[0], line[1][:-1])
        starlis.append(object)

    return starlis