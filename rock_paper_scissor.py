import random as a
print('''rock = 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
print(''' paper = 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
print(''' scissor =
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

#Write your code below this line 👇
n= int(input("Enter your no. which you  haven chosen. 0 show 'rock',1 shows 'paper',2 shows 'scissor'\n"))
ls=['rock','paper','scissor']
out=a.choice(ls)
print(f' {ls[n]} V/s {out}')
if(ls[n]=='rock' and out=='scissor'):
  print('you win the game')
elif (ls[n]=='paper' and out =='rock'):
  print('you win the game')
elif(ls[n]=='scissor' and out=='paper'):
  print('you win the game')
elif (ls[n]==out):
  print("oppps!! match draw .try again")
else:
  print('you lost the game. Try again')

             

