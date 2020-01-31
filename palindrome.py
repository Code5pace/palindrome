w = input().lower() 
w = w.replace(' ','')
n = 0
m = len(w) -1
palindrome = True
while n < m:
    if w[n] != w[m]:
        palindrome = False
    n += 1
    m -= 1
if palindrome:
    print("Պալինդրոմ")
else:
    print('Ոչ պալինդրոմ')
