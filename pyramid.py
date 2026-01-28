n = int(input("Enter number: "))
for i in range(n):
    print(' '*i + '* '*(n-i))
    
    
print("Pyramid")

for i in range(1, n+1):
    print(' '*(n-i) +'* '*i)