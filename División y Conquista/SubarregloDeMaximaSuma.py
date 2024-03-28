def max_subarray_mid(start, mid, end, arr):
	left_sum = float("-inf")
	sum_parcial = 0
	left_start = 0
    
	for i in range(mid, start - 1, -1):
		sum_parcial = sum_parcial + arr[i]
		if sum_parcial > left_sum:
			left_sum = sum_parcial
			left_start = i
    
	right_sum = float("-inf")
	sum_parcial = 0 
	right_end = 0
    
	for i in range(mid + 1, end + 1):
		sum_parcial = sum_parcial + arr[i]
		if sum_parcial > right_sum:
			right_sum = sum_parcial
			right_end = i
            
	return left_start, right_end, left_sum + right_sum

def max_subarray_rec(start, end, arr):
    if start == end:
        return start, end, arr[start]
    
    mid = (start + end) // 2

    left_start, left_end, left_sum = max_subarray_rec(start, mid, arr)
    right_start, right_end, right_sum = max_subarray_rec(mid + 1, end, arr)
    mid_start, mid_end, mid_sum = max_subarray_mid(start, mid, end, arr)

    if left_sum >= right_sum and left_sum >= mid_sum:
        return left_start, left_end, left_sum
    elif right_sum >= left_sum and right_sum >= mid_sum:
    	return right_start, right_end, right_sum
    else:
    	return mid_start, mid_end, mid_sum
        
    
def max_subarray(arr):
    start, end, sum_max = max_subarray_rec(0, len(arr) - 1, arr)
    return arr[start : end + 1]

#La complejidad del algoritmo es O(nlogn), ya que el algoritmo divide la longitud del arreglo de forma recursiva(se hacen dos llamados) hasta llegar al caso base (long 1) y en la parte de conquista junta las soluciones con un O(n) por lo que la complejidad total del algoritmo nos queda O(nlogn).