import heapq

def sort_k_sorted(arr, k):
    if not arr:
        return []
    if k <= 0:
        return list(arr)

    # If k >= len(arr), sorting whole array is safe
    if k >= len(arr):
        return sorted(arr)

    heap = arr[:k+1]
    heapq.heapify(heap)
    result = []

    for i in range(k+1, len(arr)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result
