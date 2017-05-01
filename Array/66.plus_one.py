def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    digits.append(digits.pop()+1)
    print(digits)
    for i in range(len(digits)-1, -1, -1):
        num += digits[i] * pow(10, len(digits)-i-1)
        print(num)
    return print([int(i) for i in str(num)])


plusOne([3, 9, 9, 9])