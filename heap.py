import heapq

heap = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    heapq.heappush(heap, value)

print("Min Heap:", heap)

if heap:
    print("Minimum Element:", heap[0])

    removed = heapq.heappop(heap)

    print("Removed Element:", removed)
    print("Heap After Removal:", heap)
else:
    print("Heap is empty.")
