one_million:list = []
for i in range (0, 1000000 + 1):
    one_million.append(i)
    
print(one_million)

n=0

while n < 1000000:
    one_million.append(n)
    n += 1

print(one_million)

#4-5
#using the one million list above (not repeating the for loop)
A:int = min(one_million)
B:int = max(one_million)
C:int = sum(one_million)
print(A, B, C)