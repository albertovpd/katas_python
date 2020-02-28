# The Supermarket Queue

def queue_time(customers, n):
    boxes = [0 for i in range(n)]
    for c in customers:
      boxes[0] += c
      boxes = sorted(boxes)
    return max(boxes)