# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


def addTwoNumbers(l1, l2):
    digit = 0
    newL = []
    prevGreaterThanTen = False
    minLen = min(len(l1),len(l2))
    for i in range(minLen):
        sum = l1[i] + l2[i]
        if prevGreaterThanTen :
            sum +=  1
        if sum >= 10 :
            digit = sum - 10
            prevGreaterThanTen = True
        else :
            prevGreaterThanTen = False

        newL.append(digit)
    # Get the larger list
    ln = l2 if minLen == len(l1) else l1
    for i in range(minLen, len(ln)):
        sum = ln[i]
        if prevGreaterThanTen :
           sum+=1
        if sum >= 10 :
            digit = sum - 10
            prevGreaterThanTen = True
        else :
            prevGreaterThanTen = False

        newL.append(digit)

    if prevGreaterThanTen :
        newL.append(1)
    return newL

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
l1 = [5,5,5,5]
l2 = [5,5,5,5]

print(addTwoNumbers(l1,l2))

