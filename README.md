This is only backend part. Here is client part - 
[https://github.com/Arboker/photocheck](https://github.com/Arboker/photocheck)


# Python
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. 

## What we used
* Flask
* BeautifulSoup
* Python library Json
* Python library Requests
## Installation
To install all modules, firstly you need to install python. Then you need to go to https://pypi.org/ and search module that you need. And there will be guid how to install.

## Something before code
After you have installed and configured your python project, you will need to put it on the hosting. For example on heroku. We put our python project with spell and grammar checker on heroku.

If you want to check app with the server you can use our server url, but it can not work it future or you can have troubles with it, so we recommend to put code on your own hosting!

Link with our server side - https://photocheck.herokuapp.com/spellcheck

If it is not working then we deleted code from hosting or something like this!

If it happens sorry! We will try to avoid it!

## Flask
First of all, we use Flask for set up the server. Flask is really good option when it comes to write simple API, like we made here. We imported class with the name Flask and one more with the name Requests likewise from "flask" library.

Firstly, we have to create an object with parameter "__name__" that belongs to class Flask, which we imported earlier.

Next we have to make route. It is pretty simple stuff: "@" + name_of_object make sure you do not make space between. Next in parameters we have to set essentialy our root. As a first parameter we must set '/spellcheck' and for the second our methods. It should look like this 'methods=["GET", "POST"]'. Make sure it has type of LIST.

The last thing we have to do - is to create a function which is essentialy goint to be our API and it is going to make the whole magic of checking. Just type keyword "def" + name_of_function + () and leave it without parameters.

In this function we have to get the text to check from our user. It is pretty easy to do... Firstly make a variable and from request get the method 'data' ==> text = request.data. And final step is going to be converting the variable to String type ==> text = str(text). str() function is a built in function that converts other data types into a String.

Here our work with almost done!

## Requests
Requests is an open-source Python library Requests allows you to send simple HTTP/1.1 requests, without the need for manual labor. There's no need to manually add query strings to your URLs, or to form-encode your POST data.

We will use it for sending a request to get the actually HTML page which in the near future we will give to BeautifulSoup to essentialy get the required data.

First step: import Requests library as follows 'import requests'.

Create a variable 'url' and it will hold our URL. It looks like this: url = 'https://www.ask.com/web?q='

The last step is simple. We have to create a variable that actually holds our request. It looks like this: rq = requests.get(url + text). requests.get function requires two parameters: 1)URL 2)String that is going to search.

## BeautifulSoup
BeautifulSoup is very popular HTML parser. A parser is a compiler or interpreter component that breaks data into smaller elements for easy translation into another language. It is an open-source Python library which is comon used for web-scrapping.

The main goal of BS4(what stands for 'BeautifulSoup') here is to get the data from a HTML page.

First step: Import BeautifulSoup like this "from bs4 import BeautifulSoup"

Next step: In the 'check' function we create an object that belongs to class BeautifulSoup. soup = BeautifulSoup(name_of_request_variable.text, 'encoding') ==> soup = BeautifulSoup(rq.text, 'lxml'). '.text' methods allows us to get the HTML page in just a plain text, 'lxml' is an encoding which allows us to simple get the right format of page.

Next step: In the same function create an empty list ==> words = []

The last step here is going to be to iterate through the 'soup' and select the required elements. It should look like this: 'for element in soup.select('a.PartialSpellCheck-link'): '. We have to pass the 'a.PartialSpellCheck-link' parameter to 'soup.select' function in order to get the CSS class of page. Then in this loop we write in our 'words' list the value, which is a plain text of CSS class we got priviously. It must look as follows: words.append(element.text). 'append' is a build in function that allows us to write a value to a Python list. Make sure to pass '.text' parameter for element in order to make it plain text.

## Json
Our work is almost done...

Last thing which remains - is to pass the corrected words to user.

In order to do this we have to import a Json library. It is quite easy to do ==> import json

JSON stands for JavaScript Object Notation - is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.

After we imported this module(class is also named module), we have to return the JSON value to the user, because machines communicate by JSON.

Our 'check()' function have to return something, otherwise is going to be just useless. In the end of whole function enter something like this: 'return'. But what should it return? Remember I said it has to return some JSON encoded result. So after 'return' type this code ==> json.dumps(words). You may wonder, WHAT IT DOES??? Essentialy it converts our Python list with corrected words to JSON type object, so all the mechines understand what to pass to the user.

## Final preparation
Almost there...

The last thing that remains is to start our app.

Thankful Flask got some usefull stuff for us. In the end of whole file type this code:

```python
if __name__ == '__main__':

app.run(debug=True)
```

The main goal of this code is to check either the app is called or not. If it is, so the Python interpreter will run the code.

## Congratulation! You have just created your own working RESTful API!
