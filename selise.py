
def revP(s):
    p=0;p1=0
    for i in range(len(s)):
        if s[i] == '(':
            p = i
        if s[i] == ')':
            p1 = i

    t='';t1='';t2=''
    for j in range(p):
        t+=s[j]
    for k in range(p+1,p1):
        t1=s[k]+t1
    for l in range(p1+1,len(s)):
        t2+=s[l]
    
    return t+t1+t2


def revP1(s):
    p=0;p1=0
    for i in range(len(s)):
        if s[i] == '(':p = i
        if s[i] == ')':p1 = i    
    return s[0:p] + rev(s[p+1:p1])+ s[p1+1:]



def rev(s):
    r=''
    for i in s:
        r=i+r
    return r



def revP2(s):
    p=0;p1=0
    for i in range(len(s)):
        if s[i] == '(':p = i
        if s[i] == ')':p1 = i    
    return s[0:p] + s[p+1:p1][::-1]+ s[p1+1:]


def coun(s):
    return 0 if not s else s.count(' ') + 1

# Driver Code
if __name__ == "__main__":
    print(revP('abc(xyz)abc'))
    print(revP1('abc(xyz)abc'))
    print(revP2('abc(xyz)abc'))
    print(coun('nima is a coder'))

