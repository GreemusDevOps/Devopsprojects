print("exam result")
marks=32
if marks==35:
    print("you are promoted")
elif marks>35:
    print("you pass the exam")
    if marks>=80:
        print("you got A grade")
    elif marks>=50:
        print("you got B grade")
    else:
        print("you got C grade")
else:
    print("you failed the exam")
    print("you got D grade")