# Programming Foundations with Python (Udacity)

### Scripting
Python scripts can follow the typical "script" pattern... imports at the top, followed by function defintiions, followed by the "main" statements:

Example

```python
import os

def sleep():
    time.sleep(10)
    
sleep()    
```

### Classes
* Python also allows the use of classes (i.e. object orientation).

* Unlike Java, the file name and class name don't need to match (ex. ```media.Movie```)

```python
media.py

class Movie():
	...
```

* Unlike Java, does not use a "new" keywork to create a new instance

Example:

```python
shape_machine = turtle.Turtle()
```

* The ```__init__``` function gets called when a new instance of a class is created.

* The first argument of each **instance** function or variable (by convention ```self``` used) is a reference to the object itself (similar to ```this``` in Java). It is implied when calling, but explicitly listed when defining.

* Class variables and functions (i.e. *static* in Java terms) are also supported; they don't use the ```self```

Example:

```python
class Movie():
	...
    def printTitle(self):
    	print self.title
    ...
    
toy_story.printTitle()
```

* The class documentation is the first line after the class definition; it can be viewed programmatically by printing the ```__doc__``` class variable

Example:
```python
class Movie():
	"""This class provides a way to store movie related information"""
    ...

print media.Movie.__doc__
```

* The class variable ```__module__``` will return a string of the module name
* The class variable ```__name__``` will return a string of the class name

* Inheritence is supported; differences from Java:
* * The parent is specified by including it inside the open braces of the class definition: ```class Man(Person):```
* * The child explicitly calls the parent's constructor using the class function syntax for the ```__init__``` function

Example:

```python
class Man(Person):
        def __init__(self, last_name, eye_color, shoe_size):
                Parent.__init__(self, last_name, eye_color)
                self.shoe_size = shoe_size
```

### Imports
* There are utility functions in Python which don't require an import. These are called built-in functions. Example: ```open```
* Python allows classes to be several levels deep within a module. When this occurs, you can use the ```from...import``` to do the import.

Example:
```python
from twilio.rest import TwilioRestClient
```


### Installing new modules
```easy_install``` comes standard with python. Install new modules with the command ```sudo easy_install <module>```

Example:
```bash
sudo easy_install twilio
```

### Looping

```python
for i in range(1,5):
    print i
```

### IO
Include an "r" at the beginning of the file path so that python doesn't try to do any interpretation

Example

```python
os.listdir(r"/home")
```

### Strings
* string.translate is an easy way to remove unwanted characters from a string

Example

```python
"48athens.jpg".translate(None,"0123456789") == "athens.jpg"
```

* ```if <word> in <text>``` is a good way to check if certain words are in some text

Example:

```python

text = "The cat is black"
if "cat" in text:
   print "The text describes cats"

```

### Reading from the web
Example:

```python
import urllib

connection = urllib.urlopen("http://www.google.com")
output = connection.read()
print output
connection.close()
```
