1. What is an exception? 
    * An exception is an event, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.

2. What is exception handling?
    * Process of responding to the occurrence, during computation, of exceptional conditions requiring special processing often changing the normal flow of program execution.

3. Important Terms
    * try: Keyword used to keep the code segment under check (Run this code)
    * exception: Segment to handle the exception after catching it (Execute this code when there is an exception)
    * else: Run this when no exceptions exist (No exceptions? Run this code)
    * finally: No matter what run this code if/if not for exception (Always run this code)

4. Try and Except Block
    * The try and except block in Python is used to catch and handle exceptions
    * A try clause is executed up until the point where the first exception is encountered.
    * Inside the except clause, or the exception handler, you determine how the program responds to the exception.
    * You can anticipate multiple exceptions and differentiate how the program should respond to them.
    * Avoid using bare except clauses.

5. The else Clause
    * Using the else statement, you can instruct a program to execute a certain block of code only in the absence of exceptions.

6. The finally Clause
    * Finally is used for cleaning up!

7. Summary
    * raise allows you to throw an exception at any time.
    * assert enables you to verify if a certain condition is met and throw an exception if it isn't.
    * In the try clause, all statements are executed until an exception is encountered.
    * except is used to catch and handle the exception(s) that are encountered in the try clause.
    * else lets you code sections that should run only when no exceptions are encountered in the try clause.
    * finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.
