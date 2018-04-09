import os
import datetime
import sys


# print without "l" parameter
def defaultPrint(a):
    files = os.listdir()
    printString = ""
    for i in files:
        if isAll(i, a):
            printString += i + "\t"

    print(printString)

# get time stats of files. -u or not
def getTime(name, u):
    if u:
        return os.stat(name).st_atime
    return os.stat(name).st_mtime

# get size human readable -r
def humanRead(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Y', suffix)


# get permission info
def getPermissionsAndSize(name, h):
    a = os.stat(name)
    permissionString = ""
    for i in str(oct(a.st_mode)[-3:]):
        i = int(i)
        if i == 7:
            permissionString += "xrw"
        elif i == 6:
            permissionString += "-rw"
        elif i == 5:
            permissionString += "xr-"
        elif i == 4:
            permissionString += "-r-"
        elif i == 3:
            permissionString += "x-w"
        elif i == 2:
            permissionString += "--w"
        elif i == 1:
            permissionString += "x--"
        else:
            permissionString += "---"


    return permissionString, str(a.st_uid), a.st_size


# sort files respected to -s and -t
def sortFiles(lst, t, s):
    if t:
        return sorted(lst, key=lambda param: param[3], reverse=True)
    elif s:
        return sorted(lst, key=lambda param: param[2], reverse=True)


# print method with -l
def advancedPrint( a, t, s, h, u):
    files = os.listdir()
    listItems = []
    for i in files:
        if isAll(i, a):
            permissions, owner, size = getPermissionsAndSize(i, True)
            listItems.append([permissions, owner, size, getTime(i, u), i])

    a = sortFiles(listItems, t, s)
    if a != None:
        listItems = a
    printResult(listItems, h)


# check method of -a
def isAll(name, a):
    if a:
        return True
    if name[0] == ".":
        return False
    return True


# display method
def printResult(files, h):
    for i in files:
        text = ""
        for j in i:
            if i.index(j) == 2 and h:
                text += str(humanRead(j)) + "\t"
            elif i.index(j) == 3:
                text += datetime.datetime.fromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S') + "\t"
            else:
                text += str(j) + "\t"
        print(text)


# main method
if __name__ == '__main__':
    a, l, t, s, u, h = False, False, False, False, False, False
    try:
        user_input = sys.argv[1]
    except:
        user_input = ""

    if user_input == "--help":
        print("Usage -> ls [filename] [-parameters]")
        exit(0)

    try:
        indexOf = user_input.index("-")
    except:
        indexOf = 0

    if "a" in user_input[indexOf:]:
        a = True
    if "l" in user_input[indexOf:]:
        l = True
    if "t" in user_input[indexOf:]:
        t = True
    if "s" in user_input[indexOf:]:
        s = True
    if "u" in user_input[indexOf:]:
        u = True
    if "h" in user_input[indexOf:]:
        h = True

    if not l:
        defaultPrint(a)
    elif l:
        advancedPrint(a, t, s, h, u)
