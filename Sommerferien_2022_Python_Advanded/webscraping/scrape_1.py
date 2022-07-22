from bs4 import BeautifulSoup

with open("test.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


##print(doc)
#print(doc.prettify())

#tag = doc.title
    
##tag = doc.as
#tag = doc.p
#print(tag)

##print(tag.string)
#print(type(tag.string))

##tag.string = "Hallo"

##print(doc.prettify())

tags = doc.find_all("a")
print(tags)
print(type(tags))
print(len(tags))

for i in tags:
    print(i.string)

print(tags[1].string)
