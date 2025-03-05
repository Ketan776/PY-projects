print("-----------Welcome to  Quiz-Game----------- ")

playing=input("Do you want to play?\nyes/no\n")

if playing.lower() != "yes":
    quit()
    
print("Okay! let's play '-' ")
score=0
ans=input("1. What does CPU stand for?\na) control processing unit\nb) central processing unit\nc) central programing unit\nd) None of above\n")
if ans.lower()  == "b":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
   
    
ans=input("2. Sum of first 10 natural numbers?\na) 50\nb) 60\nc) 55\nd) 65\n")
if ans.lower()  == "c":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
    
ans=input("3.Which planet is known as the Red Planet?\na) Venus\nb) Mars\nc) Jupiter\nd) Saturn\n")
if ans.lower()  == "b":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")

ans=input("4. Which is the largest ocean on Earth?\na) Atlantic Ocean\nb) INdian Ocean\nc) Arctic Ocean\nd) Pacific Ocean\n")
if ans.lower()  == "d":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
    
ans=input("5. Which element has the chemical symbol'O'?\na) Oxygen\nb) Gold\nc) Osmium\nd) Silver\n")
if ans.lower()  == "a":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
    
ans=input("6. HOw many continents are there on Earth?\na) 5\nb) 6\nc) 7\nd) 8\n")
if ans.lower()  == "c":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
 
ans=input("7. Which country is famous for inventing pizza?\na) France\nb) Greece\nc) Italy\nd) Spain\n")
if ans.lower()  == "c":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")

ans=input("8. What is the square root of 64?\na) 6\nb) 7\nc) 8\nd) 9\n")
if ans.lower()  == "c":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
 
ans=input("9. Which animal is knows as the 'king of the Jungle'?\na) Lion\nb) Tiger\nc) Elephant\nd) Cheetah\n")
if ans.lower()  == "a":
    print("Correct !")
    score+=1
else:
    print("INcorrect!")
      

    

print("Your Score for is: ",score)
if(score==10):
    print("Star = *****")
elif(score<10 and score>=8):
    print("Star = ****")
elif(score<=7 and score>5):
    print("Star = ***")
elif(score<=5 and score >=3):
    print("Star = **")
else:
    print("Star = *")
