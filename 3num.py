#Grade of studient
print(input('enter your mark'))
sub1 = 78
sub2 = 85
sub3 = 95
sub4 = 74
sub5 = 88

total_marks = sub1+sub2+sub3+sub4+sub5
print ("total_makrs",'total_makars/5')

percentage = 500/5
if percentage > 90:
    print('grad is A+')
elif percentage > 80 and  90:
     print('grade is A')
elif percentage >= 70 and  80:
     print('grad is B')
elif percentage >= 60 and 70 :
     print('grad is c')
elif percentage >= 50 and 60 :
     print('gad is D')
else:
     print('failed')