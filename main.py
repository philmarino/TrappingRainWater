
def trap(heights):
    highestLeft = [0 for x in range(len(heights))]
    highestRight = [0 for x in range(len(heights))]

    #cycle through the array to find the highest point to the left of each point and the highest point to the right
    for i in range(len(heights)):
        highestLeft[i] = 0
        for j in range(0, i):
            if heights[j] > highestLeft[i]:
                highestLeft[i] = heights[j]

        highestRight[i]=0
        for j in range(i, len(heights)):
            if heights[j] > highestRight[i]:
                highestRight[i] = heights[j]

    #cycle through a second time and determine how much water is standing on this point. Add it to the sum
    sum = 0
    for i in range(len(heights)):
        #debug = i
        if min(highestLeft[i], highestRight[i]) - heights[i] > 0:
            sum += min(highestLeft[i], highestRight[i]) - heights[i]

    return sum


#Example 1:
#Input: 
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

#Example 2:
#Input: 
height = [4,2,0,3,2,5]
print(trap(height))
#Output: 9

