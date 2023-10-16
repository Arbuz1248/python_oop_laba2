class ArrHelper:
    def getSum(self, arr):
        res = 0
        for num in arr:
            res += num

        return res

    def getAvg(self, arr):
        if (len(arr) > 0):
            sum = self.getSum(arr)
            return sum / len(arr)
        else:
            return 0

arrHelper = ArrHelper()

sum1 = arrHelper.getSum([1, 2, 3])
print(sum1)

sum2 = arrHelper.getSum([3, 4, 5])
print(sum2)


class Validator:

    def isEmail(self, ):





