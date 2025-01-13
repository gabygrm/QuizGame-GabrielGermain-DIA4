# QuizGame-GabrielGermain-DIA4

Name : Gabriel Germain
Date : 13/01/2025
TD : DIA 4

Welcome to the **General Culture Quiz Game**! This is a Python-based console application where players answer 10 multiple-choice questions to test their general knowledge.

## Features
- 10 questions on various topics such as science, literature, and geography.
- Multiple-choice format: each question has 4 possible answers.
- User-friendly input: players select an answer by typing a number (1-4).
- Immediate feedback for correct or incorrect answers.
- Final score displayed with a performance-based message.

## How to Run
1. Ensure you have Python installed on your system (version 3.6 or higher).
2. Open your terminal
3. Type  ' git clone https://github.com/gabygrm/QuizGame-GabrielGermain-DIA4.git '
4. Type ' cd QuizGame-GabrielGermain-DIA4 '
5. And Type 'python quizz.py ' to play 

## Example Gameplay
```
Welcome to the General Culture Quiz!
You will answer 10 questions, each with 4 possible answers.
Type the number corresponding to your choice and press Enter.
Let's see how much you know!

What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Rome
Your answer: 3
Correct!

...

Quiz Complete!
You scored 8/10.
Good job! You know quite a bit.
```

## Customization
To add or modify questions, edit the `questions` list in the script. Each question is a tuple with the following structure:
```python
("Question text", ["Option 1", "Option 2", "Option 3", "Option 4"], correct_option_number)
```

## Requirements
- Python 3.6 or higher

## License
This project is released under the MIT License.

---
Enjoy testing your knowledge with the General Culture Quiz Game!
