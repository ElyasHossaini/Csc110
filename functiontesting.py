def reverse(x: int) -> int:
        x = list(str(x))
        y = []
        for i in range(len(x)-1,-1, -1):
            y.append(x[i])
        
        num = ""
        for i in y:
            num = num + i
        print(num)
        return int(num)
reverse(123)