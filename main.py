import math

# Define the list of points (tuples representing x, y coordinates)
points = [(1, 2), (4, 6), (5, 8), (2, 3), (7, 9)]

# Define the function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Create a list to store the distances between every pair of points
distances = []

# Loop through each pair of points and calculate the distances
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        print(f"Distance between {points[i]} and {points[j]}: {dist:.2f}")

# Find the minimum distance
min_distance = min(distances)

print(f"\nThe minimum Euclidean distance is: {min_distance:.2f}")
