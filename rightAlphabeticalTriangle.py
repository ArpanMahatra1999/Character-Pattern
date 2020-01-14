def pattern(n):
    x = 65
    for i in range(0,n):
        character = chr(x)
        for j in range(0,i+1):
            print(character,end=" ")
        x = x + 1
        print("\r")

pattern(20)