#! /usr/bin/env python3

def readMap():
    ips = {}
    with open("ip.map", 'r') as f:
        content = f.read()
        for line in content.split('\n'):
            if line == "":
                break;
            else:
                t = line.split('$')
                ips[t[0]] = (t[1], t[2])
    return ips

def printDict(d):
    for e in d:
        print(e + "\t" + str(d.get(e)))

def filterLog(log, f):
    return [x for x in log if f(x)]

def isQuery(line):
    return ("query" in line)
def isArecord(line):
    return ("[A]" in line)


#open filter functions: only [A] records
#idea: create csv file / table /w person date, query, device

def main():
    d = readMap()
    printDict(d)

    log = None
    with open("pihole.log", 'r') as f:
        content = f.read()
        log = content.split('\n')

    log = filterLog(log, isQuery)
    log = filterLog(log, isArecord)


    with open("out.log", 'w') as f:
        f.write("\n".join(log))


if __name__ == "__main__":
    main()
