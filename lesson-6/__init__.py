def visualize_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        print(f"low: {low}, high: {high}")
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def generate_array(size):
    array = []
    for i in range(size):
        array.append(i)
    return array


if __name__ == '__main__':
    print(visualize_binary_search(generate_array(1000), 50))
