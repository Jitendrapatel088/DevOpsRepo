##list
#names=["jitendra", "rakesh", "ramesh", "suresh"]
#feedbacks=[4, 3, 4, 5]

#for i in range (0, 4, 1):
    #if (feedbacks[i]<5):
        #print(names[i])
        #print(feedbacks[i])



##list
#names=["jitendra", "rakesh", "ramesh", "suresh"]
#feedbacks=[4, 3, 4, 5]

#length=len(names)
#for i in range (0, len(names), 1):
    #if (feedbacks[i]<4):
        #print(names[i])
        #print(feedbacks[i])


names = []
feedbacks = []
sumFeedback = 0
for i in range(5):
    name = input("Enter the name")
    feedback = int(input("Enter the Feedback"))
    names.append(name)
    feedbacks.append(feedback)
    sumFeedback = sumFeedback+feedback

average = sumFeedback/len(names)
print(average)
print(names)
print(feedbacks)
