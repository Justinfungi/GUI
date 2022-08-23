but_lst=[]
for i in range(9):
    myStr = "button"+str(i)
    globals()[myStr]= i
    but_lst.append(myStr)

print(but_lst)
print(type(but_lst[1]))
print(but_lst[1])
print(button1)
