
import random

# Divide and conquer algorithm for finding the index of smallest element in a list of integers 
# with only one smalles element in the list.
def findLightestBox2(boxes, initialIndex = [], steps=0):
    """
    Find the lightest box in a list of boxes.
    """
    initialIndex = [x for x in range(len(boxes))] if initialIndex == [] else initialIndex
    if len(boxes) == 1:
        print("Steps:", steps)
        return initialIndex[0]
    elif len(boxes) == 2:
        print("Steps:", steps+1)
        return initialIndex[0] if boxes[0] < boxes[1] else initialIndex[1]
    else:
        isEven = len(boxes) % 2 == 0
        if isEven:
            mid = len(boxes) // 2
            if sum(boxes[:mid]) < sum(boxes[mid:]):
                return findLightestBox2(boxes[:mid], initialIndex[:mid], steps+1)
            else:
                return findLightestBox2(boxes[mid:], initialIndex[mid:], steps+1)
        else:
            mid = (len(boxes)+1) // 2
            if sum(boxes[:mid]) < sum(boxes[mid:]) + max(boxes):
                return findLightestBox2(boxes[:mid], initialIndex[:mid], steps+1)
            else:
                return findLightestBox2(boxes[mid:], initialIndex[mid:], steps+1)

# get distance number so that the sum of the distance and the number is divisible by 3
def getDistanceSoItDiffisibleBy3(n):
    """
    get distance number so that the sum of the distance and the number is divisible by 3.
    """
    if n < 3:
        if n == 0:
            return 0
        return 3-n
    else:
        return getDistanceSoItDiffisibleBy3(n-3)

def findLightestBox3(boxes, initialIndex = [], steps=0):
    """
    Find the lightest box in a list of boxes.
    """
    initialIndex = [x for x in range(len(boxes))] if initialIndex == [] else initialIndex
    if len(boxes) == 1:
        print("Steps:", steps)
        return initialIndex[0]
    elif len(boxes) == 2:
        print("Steps:", steps+1)
        return initialIndex[0] if boxes[0] < boxes[1] else initialIndex[1]
    else:
        distance = getDistanceSoItDiffisibleBy3(len(boxes))
        oneThird = (len(boxes)+distance) // 3
        twoThird = (len(boxes)+distance) // 3 * 2
        if sum(boxes[:oneThird]) == sum(boxes[oneThird:twoThird]):
            return findLightestBox3(boxes[twoThird:], initialIndex[twoThird:], steps+1)
        else:
            if sum(boxes[:oneThird]) < sum(boxes[oneThird:twoThird]):
                return findLightestBox3(boxes[:oneThird], initialIndex[:oneThird], steps+1)
            else:
                return findLightestBox3(boxes[oneThird:twoThird], initialIndex[oneThird:twoThird], steps+1)

if __name__ == '__main__':
    n = int(input('Enter number of boxes: '))
    w = int(input('Enter a width of each box: '))
    if n < 1 or w < 1:
        raise ValueError("Invalid input!")
    boxes = [w for i in range(n)]
    i = random.randint(0, len(boxes)-1)   
    boxes[i] = w - 1
    print(boxes)
    distance = getDistanceSoItDiffisibleBy3(len(boxes))
    print(len(boxes),distance)
    print("The lightest box is at index:", findLightestBox2(boxes))
    print("The lightest box is at index:", findLightestBox3(boxes))
