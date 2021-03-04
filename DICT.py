#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
print(type(d1))


# In[2]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
d1["Group"]="IS-202"
print(d1, "- Добавил ключ Group")
print("---------------")
print(type(d1))


# In[3]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
del d1["Name"]
print(d1, "- Удалил ключ Name")
print("-----------------")
print(type(d1))


# In[4]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

if "Name" in d1:
    print("True")
else:
    print("False")


print(type(d1))


# In[5]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

"Name" in d1

print("Проверил существует ли ключ - Name")

print(type(d1))


# In[6]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
d1.clear()
print(d1, "- Deleted dict all")
print(type(d1))


# In[7]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
d2 = d1.copy()
print(d2, "- Copied all elements from d1")
print("-------------------")
d2["Name"]= "Amirka"
print(d2, "- Changed key - Name")

print("----------------------")

print(d1,"- d1")

print(type(d1))
print(type(d2))


# In[8]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
d1.get("Name")

print("Took key - (Name) and shows in IDLE")


# In[9]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")
d1.keys()

print("- Shows all keys in dict")


# In[10]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

d1.values()

print("- Shows all values in (dict)")


# In[11]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

d1.update({"Name":"AMIRCHIK", "City":"Nur-Sultan"})
print(d1, "- изменил Ключ (Name) и добавил новый ключ (city)")

print(type(d1))


# In[12]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

d1.setdefault("CITY", "ASTANA")
print(d1)
print("-----------------")
d1.setdefault("Name")
print(d1)
d1.setdefault("Number", "8700")
d1
print(d1)


# In[13]:


d = {"КАМ":"Купжасаров Амир Маратулы", "КМК":"Кажи Марат Казбекулы" }
d.get("КМК")


# In[14]:


d = {"Алгоритмы и структуры данных":"Таржибаева Баян Еркебековна",
     "Казахский язык":"Сабира Сапина","Современная История Казахстана":"Ешпанов Владимир", 
     "НПБ":"Куаншбек Г.К","Математика":"Бирликов С.М","Физра":"Советханов А.А"}
d.keys()

d.get("НПБ")


# In[15]:


d1 = {"Name":"Amir", "Surname":"Kupzhassarov"}
print(d1)
print("-----------------")

d1.popitem()
