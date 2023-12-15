# def find_subsets_with_sum(arr, target_sum):
#     result = []

#     n = len(arr)

#     for i in range(n):
#         current_sum = arr[i]
#         if current_sum == target_sum:
#             result.append(current_sum)
#             return result
#         elif current_sum < target_sum:
#             result.append(current_sum)
#         for j in range(i + 1, n):
#             current_sum += arr[j]
#             if current_sum == target_sum:
#                 result.append(arr[i:j + 1])
#             elif current_sum < target_sum:
#                 result.append(arr[j])
#             elif current_sum >= target_sum:
#                 continue;

#     return result

# arr = [3,4,15,2]
# target_sum = 9

# subsets = find_subsets_with_sum(arr, target_sum)
# print(subsets)

def find_subsets_with_sum(arr, target_sum):
    result = []
    n = len(arr)

    for i in range(n):
        current_sum = arr[i]

        if current_sum == target_sum:
            result.append([arr[i]])
        elif current_sum < target_sum:
            subset = [arr[i]]

            for j in range(i + 1, n):
                current_sum += arr[j]

                if current_sum == target_sum:
                    subset.extend(arr[i:j + 1])
                    result.append(subset)
                    break
                elif current_sum < target_sum:
                    subset.append(arr[j])
                elif current_sum >= target_sum:
                    break

    return result

arr = [3, 4, 15, 2]
target_sum = 9

subsets = find_subsets_with_sum(arr, target_sum)
print(subsets)
