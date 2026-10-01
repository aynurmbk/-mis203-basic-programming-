ş# MIS203 Basic Programming

Name: Aynur Mübek
Student Number:2404109057
Department: Management Information Systems
Course Name:Basic Programming

#Week 01
AI Tool Used: Gemini
Prompt Used: "Write a Python script that asks for Name, Department, Age, and Career Goal, then prints a formatted Student Profile."
What did you change?:I customized the prompt parameters and formatted the profile display to meet assignment requirements.


#Week 02
AI Tool Used: Gemini
Prompt Used:”How can ı write this code?”
What did you change? I reviewed the code,matched the output format to the example and checked the average calculaiton.
What does break do in your program? The break statement stops the loop when the user types ‘q’, so the program can calculate and print the average.


## Week 03
* **AI Tool Used:** ChatGPT/ Gemini
* **Prompt Used:** "I provided the assignment screenshots and asked to convert the logic into Python code with explanation."
* **What did you change?:** Added input validation handling with try-except for integer inputs to prevent crashing on string age inputs.
* **Tests:** 
  1. Input: Can, Age: 5, Weekend -> Result: Can: 0.00 TRY (Free)
  2. Input: Aynur, Age: 20, Weekday, Student: yes -> Result: Aynur: 140.00 TRY (Student)
  3. Input: Irmak, Age: 65, Weekday -> Result: Irmak: 100.00 TRY (Senior)
* **Why does the order of the rules matter?:** The order matters because if-elif statements execute top-to-bottom and stop at the first matching condition. If broader conditions like student discounts were checked before age limits (e.g., age under 6), a 5-year-old student might incorrectly receive a 30% discount instead of being free.
