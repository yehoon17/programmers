class Node:
    def __init__(self, start, size, nextNode):
        self.start = start
        self.size = size
        self.nextNode = nextNode

    def find(self, t):
        earliest_node = self
        previous = self
        node = self.nextNode
        while node.start > t:
            if node.start < earliest_node.nextNode.start:
                earliest_node = previous
            previous = node
            node = node.nextNode
            if not node:
                previous = earliest_node
                node = earliest_node.nextNode
                break
        previous.nextNode = node.nextNode

        return node


def solution(jobs):
    jobs.sort(key=lambda x: x[1])

    tail = None
    nextNode = tail
    for start, size in jobs[::-1]:
        node = Node(start, size, nextNode)
        nextNode = node
    head = Node(1001, -1, nextNode)

    t = 0
    total = 0
    node = head
    while head.nextNode:
        node = head.find(t)
        s = node.size + max(0, t - node.start)
        total += s
        t = max(t, node.start) + node.size

    return total // len(jobs)
