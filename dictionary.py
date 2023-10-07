learners = []
numberOfLearner = int(input("Enter numbers of learner"))
totalFeedback = 0
for i in range(0, numberOfLearner, 1):
    name = input("enter the name")
    feedback = int(input("Enter Feedback"))
    learners.append({name, feedback})
    totalFeedback += feedback
print("avrage feedback is ", totalFeedback/numberOfLearner)
