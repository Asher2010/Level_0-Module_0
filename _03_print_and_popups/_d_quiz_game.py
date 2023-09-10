from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question = simpledialog.askstring(title='question', prompt="Do you like soccer?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question == "yes":
        score += 1
    else:
        score -= 1
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    question2 = simpledialog.askstring(title='question', prompt="Is the best player in the world Foden?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question2 == "yes":
        score += 1
    else:
        score -= 1

    question2 = simpledialog.askstring(title='question', prompt="Is Messi better than Ronaldo?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question2 == "no":
        score += 1
    else:
        score -= 1
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print("Your score is:")
    print(score)
    # Run the window's .mainloop() method
    window.mainloop()
