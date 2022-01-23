1.What are Generators?
  1. Are functions that return traversable objects
  2. Produce items one at a time and only when required
  3. Are run along with 'for' loops
  
2.Advantages of using Generators
  1. Easy to Implement.
  2. Better memory management and utilization.
  3. Can be used to produce infinite items.
  4. Can also be used to pipeline a number of operations.
  
3.Normal functions vs Generators
  | Generator function  |  Normal Functions  |
  | ------------------- | ------------------ |
  | Make use of ‘yield’ keyword | Make use of ‘return’ keyword |
  

4.Writing Generators in Python
  1. Generators created using the ‘def’ keyword
  2. Make use of the yield keyword instead of return

5.Generators with Loops/
  To execute the generator function at once. You can ‘for’ loop. This loop iterates over all the objects and after all implementations, it executes StopIteration.

6.Generator Expressions\
  Resemble list comprehensions and like lambda functions, generator expressions create anonymous generator functions.

7.Use Cases
  1. Fibonacci Series: A series of numbers where in each number also called as the Fibonacci number is the sum of the two preceding numbers.
  2. Number Stream: Generating a stream of numbers.
  3. Sinewave: Generating sine waves using Seaborn.
