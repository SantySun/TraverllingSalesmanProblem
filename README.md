# Traverlling Salesman Problem
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

**This project is a brute force solution for this problem:**
Enumerate all posible routes and calculate their total distance respectively, then get the shortest path.

Sample output:
```bash
Given points are [(1, 1), (2, 3), (2, 1), (3, 6), (7, 5)]
The shortest round distance of given points is 19.574857040591564, and the route is [(1, 1), (2, 3), (3, 6), (7, 5), (2, 1)]
```
A python tupple is used to represent the coordinate of a point, such as `(1, 2)`
