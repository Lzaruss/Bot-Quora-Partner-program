# Bot-Quora-Partner-program
Automatize process of Partner Program of es.quora.com

This script uses the Selenium library to automate tasks in a web browser. In this case, the task consists of making questions on the Quora platform and requesting answers to those questions.

The request_question() function reads a text file called 'questions.txt' and extracts the first line of the file. It then removes that first line from the file and closes the file. This function is used to obtain a question to ask on Quora.

The code then opens a Chrome browser window and navigates to the Quora page. After a few seconds, an element on the page is clicked and the question obtained with the request_question() function is sent to a text box on the page. Then, a button is clicked to send the question and a similar process is followed to request answers to the question. If exceptions occur during the process, an error message is printed and the next iteration of the loop is continued.

Feel free to use

# Update 
First of all is create the credentials.json with your credentials.

The only step you have to do is to start the script with neccesary arguments, seconds later the script will automatically start asking questions (first of all you must have a file with questions, which in my case I have called preguntas.txt, 1 question per line).

**Arguments Update**

```python script.py -n 50 -L```

-n is for the number of questions do you want for the script does <br>
-L is because the login sometimes fails due to Captcha, and this argument pauses the automated login and you must manually login by bypassing the Captcha and pressing the login button.

# EXAMPLE 

https://user-images.githubusercontent.com/104428151/208221313-317581cd-6587-40ec-955c-ccb9d1c78086.mp4

![Captura JPG](https://user-images.githubusercontent.com/104428151/208221529-d535035e-7f73-4f9e-9d13-21e66d7a7867.png)

