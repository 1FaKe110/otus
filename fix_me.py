"""Get average module"""


def calculate_average(nums):
    """
    Get average from list
    :param nums: List[int]
    :return: float
    """
    return sum(nums) / len(nums)


def main():
    """
    main function of module
    :return: None
    """
    nums = [10, 15, 20]
    result = calculate_average(nums)
    print("The average is:", result)


if __name__ == '__main__':
    main()
