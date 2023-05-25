def max_points(points):
    """
    Returns the maximum number of points that lie on the same straight line.
    """
    n = len(points)
    if n < 3:
        return n

    max_points = 0
    for i in range(n - 1):
        lines = {}
        for j in range(i + 1, n):
            x_diff = points[j][0] - points[i][0]
            y_diff = points[j][1] - points[i][1]

            if x_diff == 0:
                slope = "inf"
            else:
                slope = y_diff / x_diff

            if slope in lines:
                lines[slope] += 1
            else:
                lines[slope] = 1

            max_points = max(max_points, lines[slope])

    return max_points + 1

points = [[1,1],[2,2],[3,3]]
print(max_points(points))   # 3

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(max_points(points))   # 4
