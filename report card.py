name=input("enter name:")
grades=int(input("enter your score:"))

if grades >= 95 :
    print("excellent score" +  name  + " - A+ ")
elif grades  >=85 and grades  <95 :
    print("good score"  +  name  +   " - A")
elif grades  >=75 and grades  <85 :
    print(" u can do much better "  + name +  "- B")
elif grades  <75 :
    print("work hard"  + name +  ", need improvement - C")
