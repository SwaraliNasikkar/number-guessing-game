import random

secret_num = random.randint(1, 100)

print("pick a number from 1 to 100")
guess = None

while guess != secret_num :
      guess = int( input( "enter your guess: "))

      if guess < secret_num :
         print(" too low, go higher!")
      elif guess > secret_num :
         print("too high, go lower!")
      else :
          print("yayy!\nyou got it.")

input ("press enter to exit");