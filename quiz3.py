import tkinter as tk
from tkinter import messagebox
import random
import time
import winsound  # For sound effects (Windows only)
from tkinter import ttk

# Quiz data with Python questions
quiz_data = [
    {"question": "What is the output of the following code?\nprint(type([]) is list)", 
     "options": ["True", "False", "None", "Error"], "answer": "True"},
    
    {"question": "Which of the following is used to create a function in Python?", 
     "options": ["def", "function", "func", "create"], "answer": "def"},
    
    {"question": "What does the len() function do?", 
     "options": ["Returns the number of elements in a list or string", 
                 "Returns the maximum value in a list", 
                 "Returns the length of a variable name", 
                 "None of the above"], "answer": "Returns the number of elements in a list or string"},
    
    {"question": "What will be the output of the following code?\nx = [1, 2, 3]\nprint(x * 2)", 
     "options": ["[1, 2, 3, 1, 2, 3]", "[2, 4, 6]", "Error", "[1, 2, 3]"], "answer": "[1, 2, 3, 1, 2, 3]"},
    
    {"question": "How do you declare a variable in Python?", 
     "options": ["int x = 5", "x := 5", "x = 5", "var x = 5"], "answer": "x = 5"},
    
    {"question": "What will be the output of the following code?\nx = {'a': 1, 'b': 2}\nprint(x['c'])", 
     "options": ["None", "Error", "0", "Undefined"], "answer": "Error"},
    
    {"question": "Which of the following is a mutable type in Python?", 
     "options": ["Tuple", "String", "List", "Integer"], "answer": "List"},
    
    {"question": "What does the break statement do in a loop?", 
     "options": ["Skips the current iteration", "Exits the loop entirely", "Stops the program", "Does nothing"], "answer": "Exits the loop entirely"},
    
    {"question": "What is the correct syntax for a for loop in Python?", 
     "options": ["for x to y:", "for (x = 0; x < y; x++)", "for x in range(y):", "loop x in range(y):"], "answer": "for x in range(y):"},
    
    {"question": "What will be the output of the following code?\nx = [1, 2, 3]\nprint(x[3])", 
     "options": ["3", "None", "Error", "Undefined"], "answer": "Error"},
]

random.shuffle(quiz_data)  # Shuffle questions

# Quiz Application
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x600")
        self.root.config(bg="#f0f8ff")
        
        # Initialize the quiz attributes
        self.current_question = 0
        self.total_questions = len(quiz_data)
        self.score = 0
        self.timer_value = 10
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Header Label
        self.header_label = tk.Label(self.main_frame, text="Python Quiz", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#4caf50")
        self.header_label.pack(pady=10)
        
        # Timer and Progress Bar
        self.timer_label = tk.Label(self.main_frame, text="", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#ff6347")
        self.timer_label.pack(pady=10)

        self.progress_label = tk.Label(self.main_frame, text="Progress: 0%", font=("Arial", 12), bg="#f0f8ff")
        self.progress_label.pack(pady=5)
        
        # Question Label
        self.question_label = tk.Label(self.main_frame, text="", font=("Arial", 18, "bold"), bg="#f0f8ff", wraplength=500, justify="center")
        self.question_label.pack(pady=20)
        
        # Options
        self.options_var = tk.StringVar(value="")
        self.options_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.main_frame, text="", font=("Arial", 14), variable=self.options_var, value=f"option_{i}", bg="#f0f8ff", anchor="w", width=30)
            btn.pack(anchor="w", padx=10, pady=5)
            self.options_buttons.append(btn)
        
        # Navigation Buttons
        self.next_button = tk.Button(self.main_frame, text="Submit", command=self.next_question, font=("Arial", 14), bg="#4caf50", fg="white", relief="raised")
        self.next_button.pack(pady=20)
        
        # Reset Button
        self.reset_button = tk.Button(self.main_frame, text="Restart Quiz", command=self.reset_quiz, font=("Arial", 14), bg="#f44336", fg="white", relief="raised")
        self.reset_button.pack(pady=10)

        # Load the first question
        self.load_question()
        self.start_timer()

    def load_question(self):
        if self.current_question < self.total_questions:
            question_data = quiz_data[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
            
            for i, option in enumerate(question_data["options"]):
                self.options_buttons[i].config(text=option, value=option, bg="#f0f8ff")
            
            self.options_var.set("")  # Clear selection
            self.update_progress()
            self.timer_value = 10  # Reset timer to 10 seconds
        else:
            self.show_result()
    
    def next_question(self):
        selected_option = self.options_var.get()
        if not selected_option:
            messagebox.showwarning("No Selection", "Please select an answer!")
            return
        
        question_data = quiz_data[self.current_question]
        if selected_option == question_data["answer"]:
            self.score += 1
            winsound.Beep(1000, 300)  # Correct answer sound
        else:
            winsound.Beep(500, 300)  # Incorrect answer sound
        
        self.current_question += 1
        self.load_question()
    
    def update_progress(self):
        progress = int((self.current_question / self.total_questions) * 100)
        self.progress_label.config(text=f"Progress: {progress}%")
    
    def start_timer(self):
        if self.timer_value > 0:
            self.timer_label.config(text=f"Time Left: {self.timer_value} seconds")
            self.timer_value -= 1
            self.root.after(1000, self.start_timer)
        else:
            # If time runs out, add 10 seconds for the next question
            self.timer_value = 10
            self.next_question()
    
    def show_result(self):
        percentage = (self.score / self.total_questions) * 100
        result_message = (
            f"Quiz Completed!\n\n"
            f"Score: {self.score}/{self.total_questions}\n"
            f"Percentage: {percentage:.2f}%"
        )
        messagebox.showinfo("Quiz Result", result_message)
        self.root.quit()
    
    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.load_question()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
