### description of the project
to write a command interpreter to manage  AirBnB objects

### description of the command interpreter
It is exactly the same to shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc
Do operations on objects (count, compute stats, etc
Update attributes of an object
Destroy an object
### Execution
The command interpreter can be launched in interactive or non-interactive mode as follows:
* Interactive Mode: `$ ./console.py`
* Non-interactive Mode: `$ echo <command> | ./console.py`
Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
