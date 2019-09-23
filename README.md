# PR301_Code_Refactoring
## Worst bad smells before refactoring
- Lazy Class in AbstractSourceReader
- Inappropriate Intimacy between front-ends and parsers
- Shotgun Surgery in the drawers and front-ends
- Alternative Classes with Different Interfaces in two Frontends
- Switch statement in the drawers and the parsers
- Refused-bequest in MainTIGr


## Refactoring 
### Name: Lazy Class 
### Location
- refactored_code
   - source_reader_kieran.py 
        - Whole MainTIGr class
   - tigr.py
        - AbstractSourceReader line 48~62

### Reasons
The system has no proper implementation of AbstractSourceReader for file reading which is required for Assignment1. The only implementation AbstractSourceReader is MainTIGr class and it is used as the entry point of the system; the MainTIGr twists the role of AbstractSourceReader and makes AbstractSourceReader a Lazy Class. In addition, the current system distributes the function of reading file into multiples frontend interfaces which create other bad smells including inappropriate intimacy, shotgun surgery and refused-bequest. Therefore, I think the Lazy Class of AbstractSourceReader is the most critical bad smell at this stage.
### Strategies/ approaches
- Break the relationship between MainTIGr and AbstractSourceReader.
- Implement a proper SourceReader for source reading.
- Rename the drawers. Three drawers with different implementation sharing the same name before refactoring.
- Rename the parsers. Three parser with different implementation sharing the same name before refactoring.
- Redirect the functions needing source reading to the new SourceReader.
### Result Evaluation
#### Has the bad smell been removed?
Yes
#### Did you bring new bad smells into the program?
No, only a new SourceReader is created. It is a well-behaved source reader absented from the original system.
#### How well is your program now in terms of software quality?
- Low coupling: The classes, including drawers, source reader and GUI, have lower connections now.
- No global variable: The refactoring removes the global variable “interface” in the frontend classes.
- Separated responsibilities of classes: The front-end classes don’t have the responsibility of SourceReader now. In addition, the SourceReader is not used as entry point anymore.
### Worst bad smells after refactoring1
- Alternative Classes with Different Interfaces in two Frontend
- Switch statement in the drawers and the parsers
- Duplicate code




## Refactoring 2
### Name: Alternative Classes with Different Interfaces
### Location
- refactored_code
    - front_end_jerry.py
        - GuiInterface whole class
    - front_end_kieran.py 
        - TkinterInterface whole class

### Reasons
These two classes have similar functions with different implementations and names. Parts of them have duplicate codes
### Strategies/ approaches
1. Extract Superclass: Create a superclass which inherited by two classes
Result Evaluation
### Result Evaluation
#### Has the bad smell been removed?
Yes
#### Did you bring new bad smells into the program?
No. 
#### How well is your program now in terms of software quality?
- Code consistency is increased. 
- Code readability is increased.
- Code duplication is greatly reduced.




## Refactoring 3
### Name: Inappropriate Intimacy
### Location: 
assignment_2_refactored_code
    front_end_jerry.py
        GuiInterface
            draw() line 63
            
assignment_2_refactored_code
    front_end_kieran.py
        TkinterInterface
            draw() line 73~74
### Reasons
1. placeholder
2. placeholder
### Strategies/ approaches