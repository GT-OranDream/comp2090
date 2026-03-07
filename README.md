#Student grade sorting system

##Project Overiew
This is a command-line based student grade management system designed to help teachers or administrators manage student information efficiently. The system supports adding, deleting, and searching for students

##Key Feature
• Add student information

• Delete student by student ID

• Display all students

• Sort students by score in ascending / descending order (Shell Sort)

• Save and load data from file

##OOP Concepts Used
1. Encapsulation: Student attributes are private, accessed via property

2. Inheritance: Student inherits from Person

3. Polymorphism: SortStrategy interface with multiple sorting strategies

4. Composition: StudentManager contains a student list

5. Static methods: File reading and writing in FileIO

6. Exception handling: Duplicate ID, invalid score, file exceptions, etc.

##Module Files
• student.py: Person base class, Student subclass

• student_manager.py: Student management class (composition)

• sorting_algorithm.py: Sorting strategy (polymorphism, Shell Sort)

• file_io.py: File reading and writing (static methods)

• main.py: Main program entry, exception handling

##New Data Structure 
• New Data Structure: Array / List

• New Algorithm: Shell Sort

##How to Run
Run main.py.

##Author
14179817 CHEN haozhe
14184840 HE Yuze
14180109 Wei Songen
