# Programming Foundations with Python (Udacity)

### General
Python scripts can follow the typical "script" pattern... imports at the top, followed by function defintiions, followed by the "main" statements:

Example

```python
import os

def sleep():
    time.sleep(10)
    
sleep()    
```

Python also allows the use of classes (i.e. object orientation).

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
