def find_two_sum_and_multiply(filename="puzzle1.txt"):
    with open(filename, "r") as numfile:
        nums = []
        for num in numfile.readlines():
            nums.append(int(num))
        for num in nums:
            complement = 2020 - num
            if complement in nums:
                print(num * complement)
                print("The two numbers are", num, complement)
                break

def find_three_sum_and_multiply(filename="puzzle1.txt"):
    with open(filename, "r") as numfile:
        nums = []
        for num in numfile.readlines():
            nums.append(int(num))
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])
                    print("The three numbers are", nums[i], nums[j], nums[k])

if __name__ == "__main__":
    find_two_sum_and_multiply()
    find_three_sum_and_multiply()