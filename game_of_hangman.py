import random as a
print("SAVE THE MAN FROM THE HANG!!")
print('WELCOME TO THE HANGMAN 🌠🌠🌠')
l=['devil','bat','phone','bag','bottle','cricket','guitar','cooler','ball','sky']
out=a.choice(l)
print('🤔🤔🤔HINT TO FIND THE WORD👇👇👇👇')
if(out=='devil'):
  print("THE MAN WHO IS HALF DEMON AND HALF ANGEL")
elif(out=='bat'):
  print("THING USED TO HIT")
elif(out=='phone'):
  print("THING USED FOR CALLING")
elif(out=='bag'):
  print("THING USED FOR CARRY")
elif(out=='bottle'):
  print("STAY HYDRATED")
elif(out=='cricket'):
  print("GAME HAS THOUSAND OF FANS")
elif(out=='guitar'):
  print("MUSICAL INSTRUMENT")
elif(out=='cooler'):
  print("STAY YOURSELF FROM LOOO(HOT AIR BLOWN IN SUMMER)")
elif(out=='ball'):
  print("THING THAT IS HII BY SOME OTHER THING")
elif(out=='sky'):
  print("ENDLESS")
d=a.randrange(0,len(out))
for i in range(6):
  b=''
  for j in range(len(out)):
    if(j==d):
      b=b+out[d]+' '
    else:
      b+='_ '
  print(b)
  c=input("guess the word:\n")
  if(c==out):
    print("YOU WIN THE GAME 🎊🎊🎊🎊")
    print("YOU SAVE THE HANGMAN🥰️🥰️🥰️🥰️🥰️")
    break
  elif(i==0):
    print('''
        +---+
        o   |
            |
            |
           ===
''')
    print('PLEASE SAVE ME🥺️🥺️🥺️')
  elif(i==1):
    print('''
        +---+
        o   |
         \  |
            |
           ===
''')
    print('PLEASE PLEASE!!😥😥😥')
  elif(i==2):
    print('''
        +---+
        o   |
        |\  |
            |
           ===
''')
    print('HLEP ME !! THINKING WISELY  YOU CAN DO IT 🥲🥲🥲')
  elif(i==3):
    print('''
        +---+
        o   |
       /|\  |
            |
           ===
''')
    print('LISTEN!!,STOP!!...STOP!! CLAM AND THNIK ,SAVE ME😰😰😰')
  elif(i==4):
    print('''
        +---+
        o   |
       /|\  |
         \  |
           ===
''')
    print('USE YOUR BRAIN YOU ONLY YOU CAN SAVE ME😭😭😭')
  elif(i==5):
    print('''
        +---+
        o   |
       /|\  |
       / \  |
           ===
''')
    print('MAN HANGED!!☠️☠️☠️')
    print('GAME OVER . TRY AGAIN')
    
      
  

    
    

  
