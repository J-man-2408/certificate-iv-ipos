# Session 3 - 2d structures:

## Revision Questions:
1. **How can you create a 2D list in Python both with and without list comprehension? Provide an example for each?**
> Without list comprehension you can use loops or manually define rows:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
> With list comprehension you just create a 3x3 filled with 0s:
```python
matrix = [[0 for j in range(3)] for i in range(3)]
```

2. **How would you access the element at row i and column j of a 2D list? Is this sequential or random access?**
> It is done by random access as it jumps directly to the location
```python 
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Output: 3
```

3. **Explain the difference between sequential and random access when working with 2D lists. When would you use one over the other?**
> Sequential access is when you go through the elements in order. You use this when you want to process every element, or are applying modifications to the whole dataset. <br> Random access is when you target a specific element using indices. You use this when you already know the position you need and when you what to update a specific cell. 

4. **What are some practical uses of 2D lists in Python? Provide at least two examples where 2D lists could be useful.**
> 2D lists are useful for grids or game boards, tables of data, images, matrixes in math or science.

5. **What are some potential pitfalls or limitations when working with 2D lists in Python? How might you work around these?**
> Slow performance, memory inefficiency, harder math operations. You can use NumPy to deal with large dataset or heavy math tasks. 

6. **Why might you use libraries like NumPy or Pandas for working with 2D data structures instead of native Python lists? Discuss the benefits they offer and how they build upon Python's native lists and NumPy's arrays.**
>NumPy vectorizes operations (no loops needed), it doesn't use a great deal of memory and has built in math functions. <br> Pandas is best for tables that have labels, data analysis, and missing data handling. 
