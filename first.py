n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

k=int(input("Enter the value of k:"))

arr.sort()
for i in range(0,n-2):
    start=i+1
    end=n-1
    while(start<end):
        if((arr[start]+arr[end]+arr[i])==k):
            print(f"{arr[start]},{arr[end]},{arr[i]}")
            start=start+1
            end=end-1
        elif ((arr[start]+arr[end]+arr[i])<k):
            start=start+1
        elif ((arr[start]+arr[end]+arr[i])>k):
            end=end-1


    
    