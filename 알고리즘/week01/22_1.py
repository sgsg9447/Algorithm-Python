def demical_def(num):
    if num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                return False
        return True
    return False

