text = 'ThisIsCamelCased'
res = text[0]

for i in text[1:]:
    if i.isupper():
        res += '_'
    res += i

res = res.lower()

print(res)
