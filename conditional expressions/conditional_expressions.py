age = int(input('enter age \n'))

if(age>=80):
    print('too old to vote')

elif(age>=18):
  print('yes you can vote')

elif(age<18):
  print('too young to vote')

elif(age<0):
  print('enter a valid age')
