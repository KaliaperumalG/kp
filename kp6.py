#KP
git = int(input(' '))
if(git % 4==0 and git % 100!=0 or git % 400==0):
 print('yes')
else:
 print('no')
