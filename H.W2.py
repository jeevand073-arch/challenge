number = list(range(1,100))
even_number = (n for n in number if n % 2==0)
odd_number = (n for n in number if n % 2 !=0)
Divid_by_3_and_5 = (n for n in number if n % 3 == 0 and n % 5 == 0 )

print("first 100 number", number)
print("even number",even_number)
print("odd_number",odd_number)
print("number divisible",Divid_by_3_and_5)