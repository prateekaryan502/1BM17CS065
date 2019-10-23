
def isHeap(arr, n): 
	for i in range(int((n - 2) / 2) + 1): 
		
		if arr[2 * i + 1] > arr[i]: 
				return False
		if (2 * i + 2 < n and
			arr[2 * i + 2] > arr[i]): 
				return False
	return True


 
arr = [90, 10, 15, 7, 12, 2, 7, 3] 
n = len(arr) 
arr1 = [90, 15, 10, 7, 12, 2, 7, 3] 
print(isHeap(arr, n))
print(isHeap(arr1, n))

