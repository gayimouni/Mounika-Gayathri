def main():  
 num = int(input())
 sum = 0
 temp = num
 while temp > 0:
     dig = temp % 10
     sum += dig ** 3
     temp //= 10
 if num == sum:
     print("Yes")
 else:
     print("No")
if __name__ == '__main__':
    main()

   
