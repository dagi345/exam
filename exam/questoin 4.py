list=['n', 'm' ,'r', 't', 'y', 'x', 'w', 'b']

for i in range(len(list)-1):
    for j in range (len(list)-i-1):
        if ord(list[j])> ord(list[j+1]):
            temp=list[j+1]
            list[j+1]=list[j]
            list[j]=temp
            
            
print(list)
    