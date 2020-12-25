import pandas as pd
import lxml.html as lh
import requests

Url = 'Inster your website URL'

page = requests.get(Url) 

docs = lh.fromstring(page.content)  #Reads the content from the page

tr_element = docs.xpath('//tr')

#print ([len(T) for T in tr_element[:12]]) # This prints out the number of rows within the datatable 

tr_element = docs.xpath('//tr') 

# this creates and empty list 
col = []
i=0

# Stores the first element in each row (the header) within the empty list
for t in tr_element[0]:
    i+=1
    name=t.text_content()
    #print('%d: "%s"'% (i,name)) # Used as a placeholder for string ans numbers
    col.append((name, []))

for j in range(1, len(tr_element)):
    T=tr_element[j]

    if len(T) !=5:
        break

    i=0

    for t in T.iterchildren():
        data=t.text_content()
        # Checks if a row is empty
        if i>0: 
            try:
                data=int(data) # If the row is empty, it check for an int, if there is none, the program knows the table has ended
            except:
                pass
        col [i][1].append(data)
        i+=1
#print([len(C) for (title,C) in col])

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
print("")
print("Data Table Collected\n----------------------")
print(df)


