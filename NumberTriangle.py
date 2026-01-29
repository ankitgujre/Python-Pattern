n = 4
st = ""
# for i in range(1, n+1):
#     st += str(i)
#     print(st + " "*(n-i))


    

# for i in range(1, n+1):
#     print(str(i) * i)
st = 1
    
for row in range(1,6):
    for col in range(1,6):
        if col<=row:
            print(st, end="")
            st += 1