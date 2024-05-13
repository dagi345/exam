array=[]
size = int(input("Enter the size  "))
print("Enter the elements")
for i in range(size):
    array.append(int(input()))
prompt=int(input("enter the number to be found:  "))

count=0
for i in array:
    if i==prompt:
        count+=1
print(f'{prompt} is fount {count} times in the  given array')
        