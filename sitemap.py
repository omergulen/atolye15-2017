import requests

# http or https is required to send GET request in requests lib.
initUrl = "https://github.com/omergulen/".strip()

# get domain name
# @param initialUrl Url that needed to be parsed.
# @return domain string.
def parseUrl(initalUrl):
    if "www." == initalUrl[8:12]:
        return initalUrl[12:].split("/")[0]
    elif "www." == initalUrl[7:11]:
        return initalUrl[11:].split("/")[0]
    elif "http://" == initalUrl[:7]:
        return initalUrl[7:].split("/")[0]
    else:
        return initalUrl[8:].split("/")[0]

# printing header of the xml
print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
print("<urlset xmlns=" + initUrl + "schemas/sitemap/0.9\">")
domain = parseUrl(initUrl)

# final list of urls
lastList = []

# check if url stays in the domain
def isInside(url):
    if domain in url:
        return True
    return False

# send get request
# @param url that will be read
# @return text of the page
def makeRequest(url):
    return requests.get(url).text


# travels in the page
# @param myUrl Url that will be travelled in.
def travers(myUrl):

    c = makeRequest(myUrl).split("<a ")

    if len(lastList) > 500:
        return ""

    tempList = []
    for i in c:

        if c.index(i) == 0:
            continue


        try:
            b = i.split("href=\"")[1].split("\"")[0]
        except:
            continue

        if initUrl + b.strip() in totalList or b.strip() in totalList:
            continue

        try:
            if b[0] == "#":
                continue
        except:
            continue

        if b[:7] != "http://" and b[:8] != "https://":
            tempList.append(initUrl + b.strip())
        elif not isInside(b):
            continue
        else:
            tempList.append(b.strip())

    for i in tempList:
        if i in lastList:
            continue
        totalList.add(i)
        lastList.append(i)
        print("<url><loc>" + i + "</loc>")
        print("<priority>" + str(len(i.split("/"))-3) + "</priority></url>")
    while len(totalList) > 0:
        travers(totalList.pop())

# initiates totalList with initUrl
totalList = [initUrl]
totalList = set(totalList)
# Start traversing in initUrl
travers(initUrl)

# Close urlset tag
print("</urlset>")
