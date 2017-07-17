#by far the most challenging one solved, needed to take helof resources but learned it.
#Define a function and we loop till till length by 2 for first digit
#and length minus first value by 2 for second one
#could understand only one function


def is_additive_seq(self, num):
        length = len(num)
        for i in range(1, int(length/2 + 1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

