# take marks as input from use
print("enter marks obtained in 4 subjects:")
math= int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
gps =int(input("gps :"))

# let calculate the percentage of marks
sum = math+english+science+gps
print("sum of math,english,science and gps")

perc = (sum/400)*100

print(end="percentage mark =")
print(perc)