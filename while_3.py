number = 0
number_ori = 0
a=0
b=0
c=0
count=0

number = int(input())
number_ori = number
while True:
    a = number//10
    b = number%10
    c = (a + b) % 10
    number = b*10 + c
    count += 1
    if number == number_ori:
        print(count)
        break
# a 26/10 = 2
# b 26%10 = 6
# c 2+ 6 = 8 % 10
# b*10 + c =
#   60      8 =68
#
# a 68/10 = 6
# b 68%10 = 8
# c 6+ 8 = 14 %10
# b*10 + 4 = 84
#   80  + 4
#
# a 84/10 = 8
# b 84%10 = 4
# c 8+ 4 = 12 %10
# b*10 + 2 = 84
#   40  + 2 = 42
#
# a 42/10 = 4
# b 42%10 = 2
# c 4+ 2 = 6 %10
# b*10 + 6 = 26
#   20  + 6 = 26