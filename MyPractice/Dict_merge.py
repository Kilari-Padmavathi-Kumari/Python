d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 3}

'''for k, v in d2.items():
    if d1.get(k) is not None:
        d1[k] += d2[k] 
    else:
        d1[k] = v

print(d1)'''




for k, v in d2.items():
    d1[k] = d1.get(k, 0) + v

print(d1)

d1.update(d2)
print(d1)
