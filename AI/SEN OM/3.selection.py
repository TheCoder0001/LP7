def sort(nums):
	for i in range (len(nums)-1):
		minpos=i
		for j in range (i,len(nums)):
			if nums[j]<nums[minpos]:
				minpos=j
		#swapping
		
		temp=nums[i]
		nums[i]=nums[minpos]
		nums[minpos]=temp
	
		print(nums)
	
user_ip=input("enter the numbers ")
nums=[int (x) for x in user_ip.split()]

sort(nums)
print("sorted list : ",nums)
