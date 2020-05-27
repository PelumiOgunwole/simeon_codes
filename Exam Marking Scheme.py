print("University of Benue Current Affairs Education Exam","\n")
print("The Course Title of this Exam is: CAE301","\n","Lecturer: Prof Bozzco" )

class MarkingScheme:
    def __init__(self,question,answers,student):
        self.question=question
        self.answers=answers
        self.student=student

"""The list below stores the questions"""

questionBag=ask=["In What Year Was Nigeria Almagamated? \n(a)1918 \n(b)1960 \n(c)1914 \n(d)1999 \n\n",
    "When taking a penalty kick, a footballer applies a force 30N for a period of 0.05s.If the mass of the ball is 0.075kg.What is the speed with which the ball moves off? \n(a)4.5 (b)11.25 (c)45 (d)20 \n",
    "The S.I unit of moment of a force is: \n(a)kgm \n(b)Nm \n(c)Jm \n(d)Nm^-1 \n\n",
    "Which character's nose grows long when he tells a lie?: \n(a)Dickson \n(b)Sparrow \n(c)Pinnochio \n(d)Helen \n\n",
    "Who is the CEO of Nairaland?  \n(a)Bobrisky \n(b)Seun Osewa \n(c)Don Jazzy \n(d)DJ Cuppy",
    "The color which radiates heat better is: \n(a)Brown \n(b)Bluish green \n(c)Darkish Blue \n(d)Black \n\n",
    "What's the name of the world trade center destroyed by Osama Biladen: \n(a)Hexagon Centre \n(b)Pentagon Building \n(c)White House \n(d)None \n\n",
    "An Optamologist takes care of ? \n(a)Liver \n(b)Ears \n(c)Knees \n(d)Eyes \n\n",
    "A Mason works with ? \n(a)stones \n(b)Wood \n(c)Concrete \n(d)Sand \n\n,",
    "Who is the story writer in the movie 'October 1' ? \n(a)Edwin Edward \n(b)Tunde Babalola \n(c)Jim Mike \n(d)Mohammed Salah \n\n",
    "The literature 'Providential Provisions' is a ____?: \n(a)Comedy \n(b)Prose \n(c)Farce \n(d)Poem \n\n",
    "The biggest planet is \n(a)Mercury \n(b)Jupivenus \n(c)Jupiter \n(d)Indiana \n\n",
    "What is the color of Petroleum in it's raw form?  \n(a)brown \n(b)black \n(c)yellowish-black \n(d)blackish-yellow \n\n",
    "The youngest president of France is ____: \n(a)Emmanuel Macron \n(b)Tim Macron \n(c)James Macron \n(d)Emmy Macron \n\n",
    "Who is the first Africa president that went with millitary troops to destroy Bokoharam Hide outs: \n(a)Buhari \n(b)Idris Debby \n(c)Boss Mustapha \n(d)Nana Akufo \n\n",
    "What is the speed of sound ? \n(a)200 m/s \n(b)310 m/s \n(c)343 m/s \n(d)344 m/s \n\n",
    "Which of the following is an example of second order lever ? \n(a)Scissors \n(b)Thongs \n(c)Pliers \n(d)Wheel barrow \n\n",
    "Which animal was accused of swallowing Billions of Naira in Nigerian History?  \n(a)Rat \n(b)Snake \n(c)Lion \n(d) Goat \n\n",
    "Which of the following countries practice Monarchy \n(a)Russia \n(b)Sweden \n(c)USA \n(d)UK \n\n",
    "What is the spanish name of the movie 'Money Heist' \n(a)Lacasa De Papel \n(b)Papel De Lacasa \n(c)De Lacasa Papel \n(d)Lacasa Papel De \n\n"

                     ]
answerList=[]
"""File to read Professor's answer"""
with open("Answers.txt") as fileObject:
    answerReader=fileObject.readlines()
    for r in answerReader:
        answerList.append(r.rstrip().split('\n'))
    fileObject.close()

"""File to read student's answer"""
studentArray=[]
with open("EXAM.txt") as newfile:
    studentAnswersReader= newfile.readlines()
    for p in studentAnswersReader:
        studentArray.append(p.rstrip().split("\n"))

"""Questions and their respective answers"""
questionAndAnswer=[]
for position in range(20):
    questionAndAnswer.append(MarkingScheme(questionBag[position],answerList[position],studentArray[position]))

"""Function to display answers"""

def displayQuestions(questionAndAnswer):
    scores=0
    numbers=0
    for point in questionAndAnswer:
        numbers+=1

        if point.student == point.answers:
            print("Question",numbers,"answer is correct")
            scores += 1
        else:
            print("Question",numbers,"answer is wrong, the right answer should be: ",point.answers[0:numbers])
    print(" You got " + str(scores) + "/" + str(len(questionBag)) + " of the answers correctly" + " and you now have " + str(scores) + " marks")
    print()
    print("You got: ", (20-scores), " questions wrong")
    print()
    percentageScore=scores/(20-scores) * 100
    if percentageScore>=70:
        print("Your percentage scores is: ",percentageScore,' and you passed, Congrats!!!')

    else:
        print("Your percentage scores is: ", round(percentageScore,2), ' and you failed. Read harder next time')

displayQuestions(questionAndAnswer)

