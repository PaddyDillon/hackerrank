import re

def convert_string(s):
     j=re.compile( s+"([^a-zA-Z0-9_])+" )
     return j
def test_string(regex,sen):
    return len(regex.findall(sen))

    
    


num_sen=int(input())
sentences=[]
for i in range(num_sen):
    sentences.append(input())


num_tests=int(input())
for i in range(num_tests):
    reg=convert_string(input())
    total=sum([test_string(reg,x) for x in sentences])
    print(total)
