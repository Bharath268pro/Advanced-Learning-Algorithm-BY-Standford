import heapq

def create_min_heap():
    n = int(input("Enter number of elements for the min-heap: "))
    min_heap = []
    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        heapq.heappush(min_heap, val)  # push into min-heap
    return min_heap

def create_max_heap():
    n = int(input("Enter number of elements for the max-heap: "))
    max_heap = []
    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        # Push negative value to simulate max-heap
        heapq.heappush(max_heap, val)
    # Convert back to positive values for viewing
    return max_heap[::-1]

# Main program
print("\n--- Creating Min Heap ---")
min_heap = create_min_heap()
print("Min Heap (internal structure):", min_heap)
print("Smallest element:", min_heap[0])

print("\n--- Creating Max Heap ---")
max_heap = create_max_heap()
print("Max Heap (simulated):", max_heap)
print("Largest element:", max_heap[0])
