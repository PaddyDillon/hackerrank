import re 
start_match=re.compile("^hackerrank")
end_match=re.compile(".*hackerrank$")
full=re.compile("hackerrank")

stuff=int(input())
for i in range(stuff):
    k=input()
    if  full.fullmatch(k)!=None: print(0)
    elif end_match.match(k)!=None: print(2)
    elif start_match.match(k)!=None: print(1)
    else: print(-1)
