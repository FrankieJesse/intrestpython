
```

### Complex Example
```python
try:
    <code_1>
except <exception_a>:
    <code_2_a>
except <exception_b>:
    <code_2_b>
else:
    <code_2_c>
finally:
    <code_3>
```

### Catching Exceptions
```python
except <exception>:
except <exception> as <name>:
except (<exception_1>, <exception_2>, ...):
except (<exception_1>, <exception_2>, ...) as <name>:
```
* **Also catches subclasses of the exception.**

### Raising Exceptions
```python
raise <exception>
raise <exception>()
raise <exception>(<el>)
raise <exception>(<el_1>, <el_2>, ...)
```

#### Useful built-in exceptions:
```python
raise ValueError('Argument is of right type but inappropriate value!')
raise TypeError('Argument is of wrong type!')
raise RuntimeError('None of above!')
```

#### Re-raising caught exception:
```python
except <exception>:
    <code>
    raise
```

### Common Built-in Exceptions
```text
BaseException
 +-- SystemExit                   # Raised by the sys.exit() function.
 +-- KeyboardInterrupt            # Raised when the user hits the interrupt key.
 +-- Exception                    # User-defined exceptions should be derived from this class.
      +-- StopIteration           # Raised by next() when run on an empty iterator.
      +-- ArithmeticError         # Base class for arithmetic errors.
      |    +-- ZeroDivisionError  # Raised when dividing by zero.
      +-- AttributeError          # Raised when an attribute is missing.
      +-- EOFError                # Raised by input() when it hits end-of-file condition.
      +-- LookupError             # Raised when a look-up on sequence or dict fails.
      |    +-- IndexError         # Raised when a sequence index is out of range.
      |    +-- KeyError           # Raised when a dictionary key is not found.
      +-- NameError               # Raised when a variable name is not found.
      +-- OSError                 # Failures such as “file not found” or “disk full”.
      |    +-- FileNotFoundError  # When a file or directory is requested but doesn't exist.
      +-- RuntimeError            # Raised by errors that don't fall in other categories.
      |    +-- RecursionError     # Raised when the the maximum recursion depth is exceeded.
      +-- TypeError               # Raised when an argument is of wrong type.
      +-- ValueError              # When an argument is of right type but inappropriate value.
           +-- UnicodeError       # Raised when encoding/decoding strings from/to bytes fails.
```

### User-defined Exceptions
```python
class MyError(Exception):
    pass

class MyInputError(MyError):
    pass
```


Print
-----
```python
print(<el_1>, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

* **Use `'file=sys.stderr'` for errors.**
* **Use `'flush=True'` to forcibly flush the stream.**

### Pretty Print
```python
>>> from pprint import pprint
>>> pprint(dir())
['__annotations__',
 '__builtins__',
 '__doc__', ...]
```


Input
-----
* **Reads a line from user input or pipe if present.**
* **Trailing newline gets stripped.**
* **Prompt string is printed to the standard output before reading input.**

```python
<str> = input(prompt=None)
```

#### Prints lines until EOF:
```python
while True:
    try:
        print(input())
    except EOFError:
        break
```


Command Line Arguments
----------------------
```python
import sys
script_name = sys.argv[0]
arguments   = sys.argv[1:]
```

### Argparse
```python
from argparse import ArgumentParser, FileType
p = ArgumentParser(description=<str>)
p.add_argument('-<short_name>', '--<name>', action='store_true')  # Flag
p.add_argument('-<short_name>', '--<name>', type=<type>)          # Option
p.add_argument('<name>', type=<type>, nargs=1)                    # Argument
p.add_argument('<name>', type=<type>, nargs='+')                  # Arguments
args  = p.parse_args()
value = args.<name>
```

* **Use `'help=<str>'` for argument description.**
* **Use `'type=FileType(<mode>)'` for files.**


Open
----
**Opens a file and returns a corresponding file object.**

```python
<file> = open('<path>', mode='r', encoding=None, newline=None)
```
* **`'encoding=None'` means default encoding is used, which is platform dependent. Best practice is to use `'encoding="utf-8"'` whenever possible.**
* **`'newline=None'` means all different end of line combinations are converted to '\n' on read, while on write all '\n' characters are converted to system's default line separator.**
* **`'newline=""'` means no conversions take place, but lines are still broken by readline() on either '\n', '\r' or '\r\n'.**

### Modes
* **`'r'`  - Read (default).**
* **`'w'`  - Write (truncate).**
* **`'x'`  - Write or fail if the file already exists.**
* **`'a'`  - Append.**
* **`'w+'` - Read and write (truncate).**
* **`'r+'` - Read and write from the start.**
* **`'a+'` - Read and write from the end.**
* **`'t'`  - Text mode (default).**
* **`'b'`  - Binary mode.**

### Exceptions
* **`'FileNotFoundError'` can be risen when reading with `'r'` or `'r+'`.**
* **`'FileExistsError'` can be risen when writing with `'x'`.**
* **`'IsADirectoryError'` and `'PermissionError'` can be risen by any.**
* **`'OSError'` is the parent class of all listed exceptions.**

### File
```python
<file>.seek(0)                      # Moves to the start of the file.
<file>.seek(offset)                 # Moves 'offset' chars/bytes from the start.
<file>.seek(0, 2)                   # Moves to the end of the file.
<bin_file>.seek(±offset, <anchor>)  # Anchor: 0 start, 1 current pos., 2 end.
```

```python
<str/bytes> = <file>.read(size=-1)  # Reads 'size' chars/bytes or until EOF.
<str/bytes> = <file>.readline()     # Returns a line or empty string on EOF.
<list>      = <file>.readlines()    # Returns a list of lines or empty list.
<str/bytes> = next(<file>)          # Returns a line using buffer. Do not mix.
```

```python
<file>.write(<str/bytes>)           # Writes a string or bytes object.
<file>.writelines(<coll.>)          # Writes a coll. of strings or bytes objects.
<file>.flush()                      # Flushes write buffer.
```
* **Methods do not add or strip trailing newlines, even writelines().**

### Read Text from File
```python
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()
```

### Write Text to File
```python
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
```


Path
----
```python
from os import path, listdir
from glob import glob
```

```python
<bool> = path.exists('<path>')
<bool> = path.isfile('<path>')
<bool> = path.isdir('<path>')
```

```python
<list> = listdir('<path>')         # List of filenames located at 'path'.
<list> = glob('<pattern>')         # Filenames matching the wildcard pattern.
```

### Pathlib
```python
from pathlib import Path
```

```python
cwd    = Path()
<Path> = Path('<path>' [, '<path>', <Path>, ...])
<Path> = <Path> / '<dir>' / '<file>'
```

```python
<bool> = <Path>.exists()
<bool> = <Path>.is_file()
<bool> = <Path>.is_dir()
```

```python
<iter> = <Path>.iterdir()          # Iterator of filenames located at path.
<iter> = <Path>.glob('<pattern>')  # Filenames matching the wildcard pattern.
```

```python
<str>  = str(<Path>)               # Returns path as a string.
<tup.> = <Path>.parts              # Returns all components as strings.
<Path> = <Path>.resolve()          # Returns absolute Path without symlinks.
```

```python
<str>  = <Path>.name               # Final component.
<str>  = <Path>.stem               # Final component without extension.
<str>  = <Path>.suffix             # Final component's extension.
<Path> = <Path>.parent             # Path without final component.
```


Command Execution
-----------------
### Files and Directories Commands
* **Paths can be either strings or Path objects.**
* **All exceptions are either 'OSError' or its subclasses.**

```python
import os
os.chdir(<path>)                  # Changes the current working directory.
<str> = os.getcwd()               # Returns current working directory.
```

```python
os.remove(<path>)                 # Deletes the file.
os.rmdir(<path>)                  # Deletes empty directory.
shutil.rmtree(<path>)             # Deletes an entire directory tree.
```

```python
os.rename(from, to)               # Renames the file or directory.
os.replace(from, to)              # Same, but overwrites 'to' if it exists.
```

```python
os.mkdir(<path>, mode=0o777)      # Creates a directory.
<iter> = os.scandir(path='.')     # Returns os.DirEntry objects located at path.
```

#### DirEntry:
```python
<str>  = <DirEntry>.name          # Final component of the path.
<str>  = <DirEntry>.path          # Path with final component.
<Path> = Path(<DirEntry>)         # Path object.
```

```python
<bool> = <DirEntry>.is_file()
<bool> = <DirEntry>.is_dir()
<bool> = <DirEntry>.is_symlink()
```

### Shell Commands
```python
import os
<str> = os.popen('<shell_command>').read()
```

#### Using subprocess:
```python
>>> import subprocess, shlex
>>> a = subprocess.run(shlex.split('ls -a'), stdout=subprocess.PIPE)
>>> a.stdout
b'.\n..\nfile1.txt\nfile2.txt\n'
>>> a.returncode
0
```


CSV
---
```python
import csv
<reader> = csv.reader(<file>, dialect='excel', delimiter=',')
<list>   = next(<reader>)  # Returns a row as list of strings.
```

```python
<writer> = csv.writer(<file>, dialect='excel', delimiter=',')
<writer>.writerow(<collection>)
<writer>.writerows(<coll_of_coll>)
```

### Parameters
* **`'dialect'` - Master parameter that sets the default values.**
* **`'delimiter'` - A one-character string used to separate fields.**
* **`'quotechar'` - Character for quoting fields that contain special characters.**
* **`'doublequote'` - Whether quotechars inside fields get doubled or escaped.**
* **`'skipinitialspace'` - Whether whitespace after delimiter gets stripped.**
* **`'lineterminator'` - How does writer terminate lines.**
* **`'quoting'` - Controls the amount of quoting: 0 - as necessary, 1 - all.**
* **`'escapechar'` - Character for escaping quotechar if doublequote is false.**

### Dialects
```text
+------------------+-----------+-----------+--------------+
|                  |   excel   | excel_tab | unix_dialect |
+------------------+-----------+-----------+--------------+
| delimiter        |      ','  |     '\t'  |       ','    |
| quotechar        |      '"'  |      '"'  |       '"'    |
| doublequote      |     True  |     True  |      True    |
| skipinitialspace |    False  |    False  |     False    |
| lineterminator   |   '\r\n'  |   '\r\n'  |      '\n'    |
| quoting          |        0  |        0  |         1    |
| escapechar       |     None  |     None  |      None    |
+------------------+-----------+-----------+--------------+
```

### Read Rows from CSV File
```python
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        return csv.reader(file)
```
* **If `'newline=""'` is not specified, then newlines embedded inside quoted fields will not be interpreted correctly.**

### Write Rows to CSV File
```python
def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
```


JSON
----
```python
import json
<str>    = json.dumps(<object>, ensure_ascii=True, indent=None)
<object> = json.loads(<str>)
```

### Read Object from JSON File
```python
def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
```

### Write Object to JSON File
```python
def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
```


Pickle
------
```python
import pickle
<bytes>  = pickle.dumps(<object>)
<object> = pickle.loads(<bytes>)
```

### Read Object from File
```python
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
```

### Write Object to File
```python
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)
```


SQLite
------
**Server-less database engine that stores each database into separate file.**
```python
import sqlite3
db = sqlite3.connect('<path>')                # Also ':memory:'.
...
db.close()
```
* **New database will be created if path doesn't exist.**

### Read
```python
cursor = db.execute('<query>')
if cursor:
    <tuple> = cursor.fetchone()               # First row.
    <list>  = cursor.fetchall()               # Remaining rows.
```
* **Returned values can be of type str, int, float, bytes or None.**

### Write
```python
db.execute('<query>')
db.commit()
```

### Placeholders
```python
db.execute('<query>', <list/tuple>)           # Replaces '?'s in query with values.
db.execute('<query>', <dict/namedtuple>)      # Replaces ':<key>'s with values.
db.executemany('<query>', <coll_of_above>)    # Runs execute() many times.
```
* **Passed values can be of type str, int, float, bytes, None, bool, datetime.date or datetime.datetme.**

### MySQL
**Has a very similar interface, with differences listed below.**
```python
# $ pip3 install mysql-connector
from mysql import connector
db = connector.connect(host=<str>, user=<str>, password=<str>, database=<str>)
cursor = db.cursor()
cursor.execute('<query>')                     # Connector doesn't have execute method.
cursor.execute('<query>', <list/tuple>)       # Replaces '%s's in query with values.
cursor.execute('<query>', <dict/namedtuple>)  # Replaces '%(<key>)s's with values.
```


Bytes
-----
**Bytes object is an immutable sequence of single bytes. Mutable version is called 'bytearray'.**

```python
<bytes> = b'<str>'                       # Only accepts ASCII characters and \x00 - \xff.
<int>   = <bytes>[<index>]               # Returns int in range from 0 to 255.
<bytes> = <bytes>[<slice>]               # Returns bytes even if it has only one element.
<bytes> = <bytes>.join(<coll_of_bytes>)  # Joins elements using bytes object as separator.
```

### Encode
```python
<bytes> = <str>.encode('utf-8')          # Or: bytes(<str>, 'utf-8')
<bytes> = bytes(<coll_of_ints>)          # Ints must be in range from 0 to 255.
<bytes> = <int>.to_bytes(<length>, byteorder='big|little', signed=False)
<bytes> = bytes.fromhex('<hex>')
```

### Decode
```python
<str>   = <bytes>.decode('utf-8')        # Or: str(<bytes>, 'utf-8')
<list>  = list(<bytes>)                  # Returns ints in range from 0 to 255.
<int>   = int.from_bytes(<bytes>, byteorder='big|little', signed=False)
'<hex>' = <bytes>.hex()
```

### Read Bytes from File
```python
def read_bytes(filename):
    with open(filename, 'rb') as file:
        return file.read()
```

### Write Bytes to File
```python
def write_bytes(filename, bytes_obj):
    with open(filename, 'wb') as file:
        file.write(bytes_obj)
```


Struct
------
* **Module that performs conversions between a sequence of numbers and a C struct, represented as a Python bytes object.**
* **Machine’s native type sizes and byte order are used by default.**

```python
from struct import pack, unpack, iter_unpack, calcsize
<bytes>  = pack('<format>', <num_1> [, <num_2>, ...])
<tuple>  = unpack('<format>', <bytes>)
<tuples> = iter_unpack('<format>', <bytes>)
```

### Example
```python
>>> pack('>hhl', 1, 2, 3)
b'\x00\x01\x00\x02\x00\x00\x00\x03'
>>> unpack('>hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
(1, 2, 3)
>>> calcsize('>hhl')
8
```

### Format
#### For standard sizes start format string with:
* **`'='` - native byte order**
* **`'<'` - little-endian**
* **`'>'` - big-endian**

#### Integer types. Use capital letter for unsigned type. Standard sizes are in brackets:
* **`'x'` - pad byte**
* **`'b'` - char (1)**
* **`'h'` - short (2)**
* **`'i'` - int (4)**
* **`'l'` - long (4)**
* **`'q'` - long long (8)**

#### Floating point types:
* **`'f'` - float (4)**
* **`'d'` - double (8)**


Array
-----
**List that can only hold numbers of predefined type. Available types and their sizes in bytes are listed above.**

```python
from array import array
<array> = array('<typecode>' [, <collection>])
```


Memory View
-----------
**Used for accessing the internal data of an object that supports the buffer protocol.**

```python
<memoryview> = memoryview(<bytes> / <bytearray> / <array>)
<memoryview>.release()
```


Deque
-----
**A thread-safe list with efficient appends and pops from either side. Pronounced "deck".**

```python
from collections import deque
<deque> = deque(<collection>, maxlen=None)
```

```python
<deque>.appendleft(<el>)
<el> = <deque>.popleft()
<deque>.extendleft(<collection>)            # Collection gets reversed.
<deque>.rotate(n=1)                         # Rotates elements to the right.
```

```python
>>> a = deque([1, 2, 3], maxlen=3)
>>> a.append(4)
[2, 3, 4]
>>> a.appendleft(5)
[5, 2, 3]
>>> a.insert(1, 6)
IndexError: deque already at its maximum size
```


Threading
---------
```python
from threading import Thread, RLock
```

### Thread
```python
thread = Thread(target=<function>, args=(<first_arg>, ))
thread.start()
...
thread.join()
```

### Lock
```python
lock = RLock()
lock.acquire()
...
lock.release()
```

#### Or:
```python
lock = RLock()
with lock:
    ...
```


Introspection
-------------
**Inspecting code at runtime.**

### Variables
```python
<list> = dir()      # Names of variables in current scope.
<dict> = locals()   # Dict of local variables. Also vars().
<dict> = globals()  # Dict of global variables.
```

### Attributes
```python
<dict> = vars(<object>)
<bool> = hasattr(<object>, '<attr_name>')
value  = getattr(<object>, '<attr_name>')
setattr(<object>, '<attr_name>', value)
```

### Parameters
```python
from inspect import signature
<sig>        = signature(<function>)
no_of_params = len(<sig>.parameters)
param_names  = list(<sig>.parameters.keys())
```


Metaprograming
--------------
**Code that generates code.**

### Type
**Type is the root class. If only passed an object it returns its type (class). Otherwise it creates a new class.**

```python
<class> = type(<class_name>, <parents_tuple>, <attributes_dict>)
```

```python
>>> Z = type('Z', (), {'a': 'abcde', 'b': 12345})
>>> z = Z()
```

### Meta Class
**Class that creates class.**

```python
def my_meta_class(name, parents, attrs):
    attrs['a'] = 'abcde'
    return type(name, parents, attrs)
```

#### Or:
```python
class MyMetaClass(type):
    def __new__(cls, name, parents, attrs):
        attrs['a'] = 'abcde'
        return type.__new__(cls, name, parents, attrs)
```
* **New() is a class method that gets called before init(). If it returns an instance of its class, then that instance gets passed to init() as a 'self' argument.**
* **It receives the same arguments as init(), except for the first one that specifies the desired class of returned instance (**`'MyMetaClass'` **in our case).**
* **New() can also be called directly, usually from a new() method of a child class (**`def __new__(cls): return super().__new__(cls)`**), in which case init() is not called.**

### Metaclass Attribute
**Right before a class is created it checks if it has metaclass defined. If not, it recursively checks if any of his parents has it defined and eventually comes to type().**

```python
class MyClass(metaclass=MyMetaClass):
    b = 12345
```

```python
>>> MyClass.a, MyClass.b
('abcde', 12345)
```

### Type Diagram
```python
type(MyClass)     == MyMetaClass  # MyClass is an instance of MyMetaClass.
type(MyMetaClass) == type         # MyMetaClass is an instance of type.
```

```text
+---------+-------------+
| Classes | Metaclasses |
+---------+-------------|
| MyClass > MyMetaClass |
|         |     v       |
|  object ---> type <+  |
|         |    ^ +---+  |
|   str -------+        |
+---------+-------------+
```

### Inheritance Diagram
```python
MyClass.__base__     == object    # MyClass is a subclass of object.
MyMetaClass.__base__ == type      # MyMetaClass is a subclass of type.
```

```text
+---------+-------------+
| Classes | Metaclasses |
+---------+-------------|
| MyClass | MyMetaClass |
|    v    |     v       |
|  object <--- type     |
|    ^    |             |
|   str   |             |
+---------+-------------+
```


Operator
--------
```python
from operator import add, sub, mul, truediv, floordiv, mod, pow, neg, abs
from operator import eq, ne, lt, le, gt, ge
from operator import and_, or_, not_
from operator import itemgetter, attrgetter, methodcaller
```

```python
import operator as op
sorted_by_second = sorted(<collection>, key=op.itemgetter(1))
sorted_by_both   = sorted(<collection>, key=op.itemgetter(1, 0))
product_of_elems = functools.reduce(op.mul, <collection>)
LogicOp          = enum.Enum('LogicOp', {'AND': op.and_, 'OR' : op.or_})
last_el          = op.methodcaller('pop')(<list>)
```


Eval
----
```python
>>> from ast import literal_eval
>>> literal_eval('1 + 2')
3
>>> literal_eval('[1, 2, 3]')
[1, 2, 3]
>>> literal_eval('abs(1)')
ValueError: malformed node or string
```


Coroutine
---------
* **Similar to generator, but generator pulls data through the pipe with iteration, while coroutine pushes data into the pipeline with send().**
* **Coroutines provide more powerful data routing possibilities than iterators.**
* **If you build a collection of simple data processing components, you can glue them together into complex arrangements of pipes, branches, merging, etc.**

### Helper Decorator
* **All coroutines must be "primed" by first calling next().**
* **Remembering to call next() is easy to forget.**
* **Solved by wrapping coroutines with a decorator:**

```python
def coroutine(func):
    def out(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return out
```

### Pipeline Example
```python
def reader(target):
    for i in range(10):
        target.send(i)
    target.close()

@coroutine
def adder(target):
    while True:
        value = (yield)
        target.send(value + 100)

@coroutine
def printer():
    while True:
        value = (yield)
        print(value)

reader(adder(printer()))  # 100, 101, ..., 109
```

<br><br>

Libraries
=========

Progress Bar
------------
```python
# $ pip3 install tqdm
from tqdm import tqdm
from time import sleep
for i in tqdm([1, 2, 3]):
    sleep(0.2)
for i in tqdm(range(100)):
    sleep(0.02)
```


Plot
----
```python
# $ pip3 install matplotlib
from matplotlib import pyplot
pyplot.plot(<data_1> [, <data_2>, ...])  # Or: hist(<data>).
pyplot.savefig(<filename>)
pyplot.show()
pyplot.clf()                             # Clears figure.
```


Table
-----
#### Prints a CSV file as an ASCII table:
```python
# $ pip3 install tabulate
from tabulate import tabulate
import csv
with open(<filename>, encoding='utf-8', newline='') as file:
    lines   = csv.reader(file)
    headers = [header.title() for header in next(lines)]
    table   = tabulate(lines, headers)
    print(table)
```


Curses
------
```python
from curses import wrapper, ascii

def main():
    wrapper(draw)

def draw(screen):
    screen.clear()
    screen.addstr(0, 0, 'Press ESC to quit.')
    while screen.getch() != ascii.ESC:
        pass

def get_border(screen):
    from collections import namedtuple
    P = namedtuple('P', 'y x')
    height, width = screen.getmaxyx()
    return P(height-1, width-1)

if __name__ == '__main__':
    main()
```


Logging
-------
```python
# $ pip3 install loguru
from loguru import logger
```

```python
logger.add('debug_{time}.log', colorize=True)  # Connects a log file.
logger.add('error_{time}.log', level='ERROR')  # Another file for errors or higher.
logger.<level>('A logging message.')
```
* **Levels: `'debug'`, `'info'`, `'success'`, `'warning'`, `'error'`, `'critical'`.**

### Exceptions
**Error description, stack trace and values of variables are appended automatically.**

```python
try:
    ...
except <exception>:
    logger.exception('An error happened.')
```

### Rotation
**Argument that sets a condition when a new log file is created.**
```python
rotation=<int>|<datetime.timedelta>|<datetime.time>|<str>
```
* **`'<int>'` - Max file size in bytes.**
* **`'<timedelta>'` - Max age of a file.**
* **`'<time>'` - Time of day.**
* **`'<str>'` - Any of above as a string: `'100 MB'`, `'1 month'`, `'monday at 12:00'`, ...**

### Retention
**Sets a condition which old log files are deleted.**
```python
retention=<int>|<datetime.timedelta>|<str>
```
* **`'<int>'` - Max number of files.**
* **`'<timedelta>'` - Max age of a file.**
* **`'<str>'` - Max age as a string: `'1 week, 3 days'`, `'2 months'`, ...**


Scraping
--------
#### Scrapes and prints Python's URL and version number from Wikipedia:
```python
# $ pip3 install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
url   = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
page  = requests.get(url)
doc   = BeautifulSoup(page.text, 'html.parser')
table = doc.find('table', class_='infobox vevent')
rows  = table.find_all('tr')
link  = rows[11].find('a')['href']
ver   = rows[6].find('div').text.split()[0]
print(link, ver)
```


Web
---
```python
# $ pip3 install bottle
from bottle import run, route, post, template, request, response
import json
```

### Run
```python
run(host='localhost', port=8080)
run(host='0.0.0.0', port=80, server='cherrypy')
```

### Static Request
```python
@route('/img/<image>')
def send_image(image):
    return static_file(image, 'images/', mimetype='image/png')
```

### Dynamic Request
```python
@route('/<sport>')
def send_page(sport):
    return template('<h1>{{title}}</h1>', title=sport)
```

### REST Request
```python
@post('/odds/<sport>')
def odds_handler(sport):
    team = request.forms.get('team')
    home_odds, away_odds = 2.44, 3.29
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps([team, home_odds, away_odds])
```

#### Test:
```python
# $ pip3 install requests
>>> import requests
>>> url  = 'http://localhost:8080/odds/football'
>>> data = {'team': 'arsenal f.c.'}
>>> response = requests.post(url, data=data)
>>> response.json()
['arsenal f.c.', 2.44, 3.29]
```


Profile
-------
### Basic
```python
from time import time
start_time = time()                  # Seconds since Epoch.
...
duration = time() - start_time
```

### High Performance
```python
from time import perf_counter as pc
start_time = pc()                    # Seconds since restart.
...
duration = pc() - start_time
```

### Timing a Snippet
```python
>>> from timeit import timeit
>>> timeit('"-".join(str(a) for a in range(100))',
...        number=10000, globals=globals(), setup='pass')
0.34986
```

### Line Profiler
```python
# $ pip3 install line_profiler
@profile
def main():
    a = [*range(10000)]
    b = {*range(10000)}
main()
```

#### Usage:
```text
$ kernprof -lv test.py
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           @profile
     2                                           def main():
     3         1       1128.0   1128.0     27.4      a = [*range(10000)]
     4         1       2994.0   2994.0     72.6      b = {*range(10000)}
```

### Call Graph
#### Generates a PNG image of a call graph with highlighted bottlenecks:

```python
# $ pip3 install pycallgraph
from pycallgraph import output, PyCallGraph
from datetime import datetime
time_str = datetime.now().strftime('%Y%m%d%H%M%S')
filename = f'profile-{time_str}.png'
drawer = output.GraphvizOutput(output_file=filename)
with PyCallGraph(drawer):
    <code_to_be_profiled>
```


NumPy
-----
**Array manipulation mini language. Can run up to one hundred times faster than equivalent Python code.**

```python
# $ pip3 install numpy
import numpy as np
```

```python
<array> = np.array(<list>)
<array> = np.arange(from_inclusive, to_exclusive, ±step_size)
<array> = np.ones(<shape>)
<array> = np.random.randint(from_inclusive, to_exclusive, <shape>)
```

```python
<array>.shape = <shape>
<view>  = <array>.reshape(<shape>)
<view>  = np.broadcast_to(<array>, <shape>)
```

```python
<array> = <array>.sum(axis)
indexes = <array>.argmin(axis)
```

* **Shape is a tuple of dimension sizes.**
* **Axis is an index of dimension that gets collapsed. Leftmost dimension has index 0.**

### Indexing
```bash
<el>       = <2d_array>[0, 0]        # First element.
<1d_view>  = <2d_array>[0]           # First row.
<1d_view>  = <2d_array>[:, 0]        # First column. Also [..., 0].
<3d_view>  = <2d_array>[None, :, :]  # Expanded by dimension of size 1.
```

```bash
<1d_array> = <2d_array>[<1d_row_indexes>, <1d_column_indexes>]
<2d_array> = <2d_array>[<2d_row_indexes>, <2d_column_indexes>]
```

```bash
<2d_bools> = <2d_array> > 0
<1d_array> = <2d_array>[<2d_bools>]
```

* **If row and column indexes differ in shape, they are combined with broadcasting.**

### Broadcasting
**Broadcasting is a set of rules by which NumPy functions operate on arrays of different sizes and/or dimensions.**

```python
left  = [[0.1], [0.6], [0.8]]  # Shape: (3, 1)
right = [ 0.1 ,  0.6 ,  0.8 ]  # Shape: (3)
```

#### 1. If array shapes differ in length, left-pad the shorter shape with ones:
```python
left  = [[0.1], [0.6], [0.8]]  # Shape: (3, 1)
right = [[0.1 ,  0.6 ,  0.8]]  # Shape: (1, 3) <- !
```

#### 2. If any dimensions differ in size, expand the ones that have size 1 by duplicating their elements:
```python
left  = [[0.1, 0.1, 0.1], [0.6, 0.6, 0.6], [0.8, 0.8, 0.8]]  # Shape: (3, 3) <- !
right = [[0.1, 0.6, 0.8], [0.1, 0.6, 0.8], [0.1, 0.6, 0.8]]  # Shape: (3, 3) <- !
```

#### 3. If neither non-matching dimension has size 1, rise an error.


### Example
#### For each point returns index of its nearest point (`[0.1, 0.6, 0.8] => [1, 2, 1]`):

```python
>>> points = np.array([0.1, 0.6, 0.8])
[ 0.1,  0.6,  0.8]
>>> wrapped_points = points.reshape(3, 1)
[[ 0.1],
 [ 0.6],
 [ 0.8]]
>>> distances = wrapped_points - points
[[ 0. , -0.5, -0.7],
 [ 0.5,  0. , -0.2],
 [ 0.7,  0.2,  0. ]]
>>> distances = np.abs(distances)
[[ 0. ,  0.5,  0.7],
 [ 0.5,  0. ,  0.2],
 [ 0.7,  0.2,  0. ]]
>>> i = np.arange(3)
[0, 1, 2]
>>> distances[i, i] = np.inf
[[ inf,  0.5,  0.7],
 [ 0.5,  inf,  0.2],
 [ 0.7,  0.2,  inf]]
>>> distances.argmin(1)
[1, 2, 1]
```


Image
-----
```python
# $ pip3 install pillow
from PIL import Image
```

#### Creates a PNG image of a rainbow gradient:
```python
width  = 100
height = 100
size   = width * height
pixels = [255 * i/size for i in range(size)]

img = Image.new('HSV', (width, height))
img.putdata([(int(a), 255, 255) for a in pixels])
img.convert(mode='RGB').save('test.png')
```

#### Adds noise to a PNG image:
```python
from random import randint
add_noise = lambda value: max(0, min(255, value + randint(-20, 20)))
img = Image.open('test.png').convert(mode='HSV')
img.putdata([(add_noise(h), s, v) for h, s, v in img.getdata()])
img.convert(mode='RGB').save('test.png')
```

### Modes
* **`'1'` - 1-bit pixels, black and white, stored with one pixel per byte.**
* **`'L'` - 8-bit pixels, greyscale.**
* **`'RGB'` - 3x8-bit pixels, true color.**
* **`'RGBA'` - 4x8-bit pixels, true color with transparency mask.**
* **`'HSV'` - 3x8-bit pixels, Hue, Saturation, Value color space.**


Audio
-----
```python
import wave
from struct import pack, iter_unpack
```

### Read Frames from WAV File
```python
def read_wav_file(filename):
    with wave.open(filename, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        return [a[0] for a in iter_unpack('<h', frames)]
```

### Write Frames to WAV File
```python
def write_to_wav_file(filename, frames_int, mono=True):
    frames_short = (pack('<h', a) for a in frames_int)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1 if mono else 2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames_short))
```

### Examples
#### Saves a sine wave to a mono WAV file:
```python
from math import pi, sin
frames_f = (sin(i * 2 * pi * 440 / 44100) for i in range(100000))
frames_i = (int(a * 30000) for a in frames_f)
write_to_wav_file('test.wav', frames_i)
```

#### Adds noise to a mono WAV file:
```python
from random import randint
add_noise = lambda value: max(-32768, min(32767, value + randint(-500, 500)))
frames_i  = (add_noise(a) for a in read_wav_file('test.wav'))
write_to_wav_file('test.wav', frames_i)
```

### Synthesizer
```python
# $ pip3 install simpleaudio
import simpleaudio, math, struct
from itertools import chain, repeat
F  = 44100
P1 = '71♪,69,,71♪,66,,62♪,66,,59♪,,,'
P2 = '71♪,73,,74♪,73,,74,,71,,73♪,71,,73,,69,,71♪,69,,71,,67,,71♪,,,'
get_pause  = lambda seconds: repeat(0, int(seconds * F))
sin_f      = lambda i, hz: math.sin(i * 2 * math.pi * hz / F)
get_wave   = lambda hz, seconds: (sin_f(i, hz) for i in range(int(seconds * F)))
get_hz     = lambda key: 8.176 * 2 ** (int(key) / 12)
parse_note = lambda note: (get_hz(note[:2]), 0.25 if '♪' in note else 0.125)
get_frames = lambda note: get_wave(*parse_note(note)) if note else get_pause(0.125)
frames_f   = chain.from_iterable(get_frames(n) for n in f'{P1}{P1}{P2}'.split(','))
frames_b   = b''.join(struct.pack('<h', int(f * 30000)) for f in frames_f)
simpleaudio.play_buffer(frames_b, 1, 2, F)
```


Basic Script Template
---------------------
```python
#!/usr/bin/env python3
#
# Usage: .py
#

from collections import namedtuple
from dataclasses import make_dataclass
from enum import Enum
import re
import sys


def main():
    pass


###
##  UTIL
#

def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    main()

```
