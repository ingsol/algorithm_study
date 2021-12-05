#!/usr/bin/env python
# coding: utf-8

# # 스택_LIFO=DFS(깊이우선탐색)에 사용

# In[32]:


class Stack:
    # 리스트를 이용한 스택 구현
    def __init__(self):
        self.top=[]
    def __len__(self):
        return len(self.top)
    
    def push(self, item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("Stack underflow")
            exit()
    
    def isEmpty(self):
        if not self:
            return True
        else:
            return False
    
    


# In[31]:


a=Stack()
a.push(1)
a.push(2)
a.top
a.peek()


# # 큐_FIFO=BFS(너비우선탐색)에 사용

# In[47]:


class Queue:
    def __init__(self):
        self.top=[]
    def __len__(self):
        return len(self.top)
    
    def enqueue(self, item):
        self.top.append(item)
        
    def dequeue(self):
        return self.top.pop(0)
    
    def is_empty(self):
        if not self:
            return True
        else:
            return False
        


# In[48]:


b=Queue()


# In[49]:


b.enqueue(1)
b.enqueue(2)
b.enqueue(3)
b.top


# In[50]:


b.dequeue()


# # 백준_9012번

# In[ ]:


import sys
input=sys.stdin.readline()


# In[180]:


class Stack_Queue:
    def __init__(self):
        self.top=[]
    
    def __len__(self):
        return len(self.top)
    
    def push(self, item):
        self.top.append(item)
    
    def dequeue(self):
        return self.top.pop(0)
    
    def first(self):
        return self.top[0]

    def pop(self):
        return self.top.pop(-1)
    
    def last(self):
        return self.top[-1]
    


# In[181]:


input="()"
ls=Stack_Queue()

for i in input:
    ls.push(i)


# In[182]:


ls.top


# In[183]:


if len(ls) <= 1:
    print("NO")
    
elif ls.dequeue()==")":
    print("NO")

else:
    while len(ls)>1:
        if ls.first() != ls.last():
            ls.dequeue()
            ls.pop()
            pass
    
        elif ls.dequeue() == ls.pop():
            print("NO")
            break
        
    if len(ls) == 0:
        print("YEST")
    
    else:
        print("NO")


# In[184]:


ls.top


# In[173]:


len(ls)


# In[161]:


if ls.dequeue() != ls.pop():
    print("YES")
else:
    print("NO")


# In[ ]:


((ls.dequeue() == "(") & (ls.pop() ==")")) or ((ls.dequeue() == ")") & (ls.pop() =="("))


# In[162]:


ls.top


# In[155]:


ls.pop()


# In[156]:


ls.top


# In[163]:


len(ls)


# In[ ]:


import sys
input=sys.stdin.readline()

class Stack_Queue:
    def __init__(self):
        self.top=[]
    
    def __len__(self):
        return len(self.top)
    
    def push(self, item):
        self.top.append(item)

    def pop(self):
        return self.top.pop(-1)
    
    def dequeue(self):
        return self.top[0]

ls=Stack_Queue()

for i in input:
    ls.push(i)
    
if len(ls) <= 1:
    print("NO")
    
elif ls[0]==")":
    print("NO")

else:
    while len(ls)>1:
        if ls.dequeue() != ls.pop():
            pass
    
        elif ls.dequeue() == ls.pop():
            print("NO")
            break
    
        elif ls.top == []:
            print("YES")
            break


# In[122]:


A=[1]


# In[123]:


A[-1]


# In[135]:


A.pop(-1)


# In[ ]:





# In[ ]:


import sys
input=sys.stdin.readline()


# In[201]:


input="(()())((()))"
ls=[]

for i in input:
    ls.append(i)


# In[193]:


ls


# In[202]:


if len(ls) <=1:
    print("NO")

elif ls[0]==")" or ls[-1]=="(" :
    print("NO")

else:
    while len(ls) > 1:
        if ls[0] != ls[-1]:
            del ls[0]
            del ls[-1]
            if len(ls)==0:
                print("YES")
                break
            else:
                pass
            
        elif ls[0] == ls[-1]:
            print("NO")
            break
        
    if len(ls)==1:
        print("NOPE")


# In[ ]:


import sys
input=sys.stdin.readline()

if len(ls) <=1:
    print("NO")

elif ls[0]==")" or ls[-1]=="(" :
    print("NO")

else:
    while len(ls) > 1:
        if ls[0] != ls[-1]:
            del ls[0]
            del ls[-1]
            if len(ls)==0:
                print("YES")
                break
            else:
                pass
            
        elif ls[0] == ls[-1]:
            print("NO")
            break
        
    if len(ls)==1:
        print("NOPE")


# In[272]:


input="(()())((()))"
ls=[]

for i in input:
    ls.append(i)


# In[333]:


aa=[]
aa.extend("(")


# In[334]:


aa


# In[35]:


input='(())'


# In[37]:


ls=[]

for i in input:
    ls.append(i)
    
ls_sorted=[]

if ls[0]==")" or ls[-1]=="(":
    print("NO")
    
else:
    for i in ls:
        if i == "(":
            ls_sorted.insert(0, i)
        elif i == ")":
            ls_sorted.extend(i)
    
    if len(ls_sorted)==0:
        pass
    
    elif len(ls_sorted)%2 == 0:
        k = int(len(ls_sorted)/2)
        if ls_sorted[k-1] != ls_sorted[k]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


# In[38]:


ls_sorted


# In[39]:


ls_sorted.count("(")


# In[47]:


input='()))((()'


# In[48]:


ls=[]

for i in input:
    ls.append(i)

if ls[0]==")" or ls[-1]=="(":
    print("NO")

else:
    if len(ls)==1:
        pass
    
    else:
        if ls.count("(") == ls.count(")"):
            print("YES")
        else:
            print("NO")


# In[52]:


input='()))((()'


# In[50]:


input_ls=[]
stack_ls=[]

for i in input:
    input_ls.append(i)
    
if input_ls[0]==")" or input_ls[-1]=="(":
    print("NO")

else:
    for i in 
    if input_ls[i] == "(":
        stack_ls.append(input_ls[i])
    elif input_ls[i] == ")":
        stack_ls.pop(-1)
        
if len(stack_ls)==0:
    print("YES")
else:
    print("NO")


# "("이면 stack_ls에 append()해주고, ﻿﻿")"이면 stack_ls에서 pop() 해줬습니다. 
# 
# 만약 ")"이 나왔는데 stack_ls가 비어있어서 뺄게 없으면 retrun 0과 break를 해줬습니다.
# 
# 파이썬 자꾸 틀렸다고 나오네요..뭐가 틀린걸까요...
# ﻿

# In[160]:


input='(((()))))))'


# In[161]:


input_ls=[]
stack_ls=[]


for i in input:
    input_ls.append(i)

def stack_func(input_ls):
    if input_ls[0]==")" or input_ls[-1]=="(":
        return 0

    elif input_ls[0]!="(":
        return 2

    else:
        for i in input_ls:
            if i == "(":
                stack_ls.append(i)
            elif i == ")":
                if (len(stack_ls) ==0):
                    stack_ls.append('0')
                    return 0
                    break
                else:
                    stack_ls.pop(-1)
        
        if len(stack_ls)==0:
            return 1
        else:
            return 0
    
if stack_func(input_ls)==1:
    print("YES")
elif stack_func(input_ls)==0:
    print("NO")
else:
    pass


# "("이면 stack_ls에 append()해주고, ﻿﻿")"이면 stack_ls에서 pop() 해줬습니다.
# 
# 만약 ")"이 나왔는데 stack_ls가 비어있어서 뺄게 없으면 retrun 0과 break를 해줬습니다.
# ﻿그래서 stack_func(input_ls) == 1 이면 print("YES")를 해주고, 0이면 print("NO")를 해줬습니다.
# 
# 맨 처음 숫자 input은 pass되도록 만들었습니다.
# 
# 여기서 틀린게 도대체 뭘까요??
# 
# 
# cf) input=sys.stdin.readline().rstrip()을 하면 런타임에러가 뜨는 것은 왜일까요??
# 
# 파이썬 자꾸 틀렸다고 나오네요..뭐가 틀린걸까요??

# ## 해결책!!
# - num=int(input())을 해줌으로써 몇번 입력을 받을지를 정해준다. 
# - ex) num=3이라면
# - for i in range(3):
# - ....char=sys.stdin.readline().strip()
# - ....0, 1, 2 이렇게 세번 입력이 받아지는 것이다.

# In[9]:


import sys
num=int(input())

for i in range(num):
    char = sys.stdin.readline().strip()
    ls=[]
    if char[0]==")" or char[-1]=="(":
        print("NO")
    else:
        for j in char:
            if j == "(":
                ls.append(j)
            elif j==")":
                if len(ls) == 0:
                    ls.append('0')
                    break
                else:
                    ls.pop(-1)
        
        if len(ls)==0:
            print('YES')
        else:
            print('NO')

