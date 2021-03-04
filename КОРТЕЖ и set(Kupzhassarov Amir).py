#!/usr/bin/env python
# coding: utf-8

# In[1]:


tuple(range(20))

print("")

# In[2]:


tuple(range(10,-10,-5))
print("")

# In[3]:


a = tuple(range(10))
type(a)

print("")
# In[4]:


a = tuple(range(10))
print(a)

print("")
# In[5]:


#a = (1,2,3,4,5,6,7)
#del a[0]
#print(a)


# In[6]:


a = (1,2,3,4,5,6,7)
b = list(a)
print(b)
print("")

# In[7]:


b = [1,2,3,4,5,6,7,8]
b.remove(b[1])
print(b, "удалил 1 элемент массива")

print("")
# In[8]:


b = [1,2,3,4,5,6,7,8]
b.remove(b[0])
print(b)
tpl = tuple(b)
print(b)
print("")

# In[9]:


b = [1,2,3,4,5,6,7,8]
b.remove(b[0])
print(b)
print(type(b), "произвел из списка в кортеж")
tpl = tuple(b)
print(tpl)

print("")
# In[10]:


q = z,z1 = ("Hello", 10)
print(z, "- 1 элемент")
print(z1, "- 2 элемент")
print(type(q))
print("-------------------")
z,z1 = z1,z
print(z,z1, "(Поменял местами содержимое)")
print("-------------------")
b = list(q)
print(b, "произвел из кортежа в массив(список)")
print(type(b), "- изменился на список")

del b[0]
print(b)

print("")
# In[11]:


#Множества
s = set([1,2,5,6,8,9,10,11,10,11])
print(s)
print(type(s))

print("")
# In[12]:


t = set("Hello World")
print(t)
print(type(t))

print("")
# In[13]:


s = set([1,2,5,6,8,9,10,11,10,11])
t = set("Hello World")
mn = s|t
print(mn, "- Объеденил 2 множества")

print("")
# In[14]:


s = set([1,2,5,6,8,9,10,11,10,11])
t = set("Hello World")
mn = s&t
print(mn, "- Будет пустым так как нет одинаковых элементов")

print("")
# In[15]:


s = set([1,2,5,6,8,9,10,11,10,11])
t = set("Hello World")
mn = s-t
print(mn, "- убрал содержимое (t)")

print("")
# In[16]:


t = set("Hello World")
t.add(" Okay")
print(t, "- added str(Okay) in(t) argumnet")

print("")
# In[17]:


t = set("Hello World")
t.add(1)
print(t)
t.remove(1)
print(t, "- deleted argument in set(t)")

print("")





