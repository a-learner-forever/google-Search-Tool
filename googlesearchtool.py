from googlesearch import search
print("welcome to Google search tool")
query=input("What do you want to search on Google:")
for i in search(query,start=0,stop=10):
    print(i)