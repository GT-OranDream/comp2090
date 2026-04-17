# User Guide (Task1 + Task2)
1. Overview
This repo has all files for COMP2090 course project. It includes code, docs and demo videos for Task 1 Student Grade Management System and Task 2 New Data Structure & Algorithm Research.
2. Environment Setup
All code uses Python 3 standard library. No extra packages need to be installed. 
## Obtain the Code

You can get the code in two ways:

1. Method 1: Git Clone

Open the terminal and run the following commands to copy the entire repository to your computer:

```
git clone https://github.com/GT-OranDream/comp2090.git
#Enter the code folder
cd comp2090/code(Just an example)
```

2. Method 2: Download the Zip Package

Download the complete zip package from the GitHub repository homepage, extract it and enter the code folder.
---
### Part 1: Task 1 - Student System Full Operation
---
#### Step 1: Go to code folder
After you download/clone the repo, open your terminal (command prompt), type this to enter the code folder:
```
# Replace the path with your own folder path!
cd C:\Users\YourName\Downloads\comp2090\code (Just an example)
# Or for Mac/Linux:
# cd ~/Downloads/comp2090/code
```


#### Step 2: Start the program

Type this command, then press Enter key:

```
python main.py
```


#### Step 3: Use the menu to choose function

After running, you will see this menu on your screen, just follow the prompt:
```
=====--- Student grade sorting system ---=====
1. Increase student（add）
2. Delete student
3. Show all student
4. Ascending order the mark
5. Descending order the mark
6. Save to the document
0. LEAVE
Please enter the options：
---
```
##### Option 1: Add a New Student

Let's say you want to add a student: Tom, ID 1001, score 85
1.  At the menu, type `1` and press Enter
    
2.  Now the system will ask you: `Enter student ID: `, type `1001` and press Enter
3.  Then it will ask: `Enter student name: `, type `Tom` and press Enter
4.  Then it will ask: `Enter student score: `, type `85` and press Enter
5.  You will see `Student added successfully!`
    


---
##### Option 2: Delete a student
If you want to delete the student we just added:
1.  At the menu, type `2` and press Enter
    
2.  System will ask: `Enter student ID to delete: `, type `1001` and press Enter
3.  You will see `Student deleted successfully!`
    
##### Option 3: Show All Students
If you want to check all students you added:
1.  At the menu, type `3` and press Enter    
2.  You will see all students' info on screen

---
##### Option 4 and 5: Sort students
If you added some students, and want to sort them by score:
1.  At the menu, type `4` and press Enter(ascending)
2.  At the menu, type `5` and press Enter(descending)    
3.  You will see all students sorted by score!
    

---
##### Option 6 and 0 
When you finish, type '6' to save your data and  type '0' to exit, next time you start the program, your data will be loaded automatically!


---
## Part 2: Task 2 - New Data Structure & Algorithm Test Steps

Task2's code is already used in Task1, but you can also test them alone, here is the guide

### Example 1: Test Dynamic Array (New Data Structure)
Dynamic Array is the structure we used to store students, you can test it alone:
1.  Open terminal, go to the code folder:
    ```
    cd C:\Users\YourName\Downloads\comp2090\code(example)
    ```
2.  Create a new test file, name it `test_array.py`
3.  Write this test code into the file:
    ```
    dynamic_array = []

    dynamic_array.append(85)
    dynamic_array.append(92)
    dynamic_array.append(78)
    print("After add:", dynamic_array) # Output: After add: [85, 92, 78]

    # Test access element
    print("First element:", dynamic_array[0]) # Output: First element: 85

    # Test remove element
    dynamic_array.remove(92)
    print("After remove:", dynamic_array) # Output: After remove: [85, 78]
    ```
4.  Run the test file:
    ```
    python test_array.py
    ```
5.  You will see the output we wrote above!
    

---
### Example 2: Test Shell Sort (New Algorithm)
Shell Sort is the new algorithm we studied, you can test it alone too:
1.  Open terminal, go to the code folder:
    ```
    cd C:\Users\YourName\Downloads\comp2090\code(example)
    ```
2.  Create a new test file, name it `test_shell_sort.py`
3.  Write this test code into the file:
    ```
    from student import Student
    from sorting_algorithm import ShellSortAsc

    student_list = [
        Student(101, "Amy", 78),
        Student(102, "Bob", 65),
        Student(103, "Cat", 92),
        Student(104, "Dan", 70),
        Student(105, "Eva", 85)
    ]

    print("Original scores:", [s.score for s in student_list]) # Output: Original scores: [78, 65, 92, 70, 85]


    sorter = ShellSortAsc()
    sorted_students = sorter.sort(student_list)

    print("Sorted scores:", [s.score for s in sorted_students]) # Output: Sorted scores: [65, 70, 78, 85, 92]
    ```
4.  Run the test file:
    ```
    python test_shell_sort.py
    ```
5.  You will see the sorted result!
