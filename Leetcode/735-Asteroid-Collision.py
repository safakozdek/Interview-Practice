class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        result = []

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                right.append(asteroids[i])
            else:
                check = True
                cur = abs(asteroids[i])
                while check and right:
                    r = right.pop()

                    if r > cur:
                        right.append(r)
                        check = False
                    elif cur == r:
                        check = False

                if check:
                    result.append(asteroids[i])

        return result + right
