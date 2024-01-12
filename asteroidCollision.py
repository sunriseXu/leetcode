# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            if i < 0:
                flag = False
                while stack:
                    tmp = stack[len(stack)-1]
                    if tmp > 0:
                        if tmp < abs(i):
                            stack.pop()
                        elif tmp == abs(i):
                            stack.pop()
                            flag = True
                            break
                        else:
                            # dont enter
                            break
                    else:
                        stack.append(i)
                        break
                if not stack and not flag:
                    stack.append(i)
            else:
                stack.append(i)
        return stack
sol = Solution()
res = sol.asteroidCollision([-2,-2,1,-2])
print(res)