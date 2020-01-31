w = input().lower()
w = w.replace(' ','')
r = w[::-1]
if w == r:
    print('Պալինդրոմ')
else:
    print('Ոչ պալինդրոմ')
