import random
a1=["rock","paper","scissor"]
c=random.choice(a1)
print(c)
p=input("Enter your choice: ")
if (c=="rock" and p=="paper") or (c=="paper" and p=="scissor") or (c=="scissor" and p=="rock"):
    print("player won")
elif c==p:
    print("enter a valid choice")
else:
    print("computer won")