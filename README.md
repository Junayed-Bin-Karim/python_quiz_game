## Quiz Game Project
Overview
This is a simple quiz game written in Python. It includes multiple-choice questions and checks the user's answers. The game evaluates the answers, provides feedback, and calculates a score based on correct answers.

## Features
Displays a series of multiple-choice questions.

The user inputs their answer (A, B, C, or D).

The program checks if the answer is correct.

The final score is displayed at the end.

## Questions
The game currently contains 5 questions related to general knowledge:

How many elements are in the periodic table?

Which animal lays the largest eggs?

What is the most abundant gas in Earth's atmosphere?

How many bones are in the human body?

Which planet in the solar system is the hottest?

## Code Explanation
The game consists of the following components:

questions: A tuple containing the questions.

options: A tuple containing the answer options corresponding to each question.

answers: A tuple containing the correct answers for each question.

guesses: A list that stores the user's answers.

score: A variable to calculate the score based on correct answers.

question_num: Keeps track of the question number.

The game loops through each question, displays the options, accepts user input, and then checks if the input is correct or not. The final score is calculated by dividing the number of correct answers by the total number of questions and multiplying by 100.

## How to Run
Clone the repository to your local machine:


git clone https://github.com/your-username/quiz-game.git
Navigate to the project directory:


cd quiz-game
Run the Python script:


python quiz_game.py
Sample Output
mathematica

----------------------
How many elements are in the periodic table?:
A. 116
B. 117
C. 118
D. 119
Enter (A, B, C, D): C
CORRECT!

----------------------
       RESULTS        
----------------------
answers: C D A A B 
guesses: C D A A B 
Your score is: 100%


## Author
This project is created and maintained by Junayed Bin Karim. You can reach out to me through:

Email: junayedbin.karim@gmail.com
