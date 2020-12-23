from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"Node({self.value},{self.left.value if self.left else None},{self.right.value if self.right else None})"

def execute(cups, n_moves):
    highest_cup = max(cups)

    indexes = {}
    nodes = {}
    for i, cup in enumerate(cups):
        indexes[cup] = i
        node = Node(cup)
        nodes[cup] = node

    for node in nodes.values():
        index = indexes[node.value]
        left_cup = cups[index - 1]
        right_cup = cups[(index + 1) % len(cups)]
        node.left = nodes[left_cup]
        node.right = nodes[right_cup]

    current_node = nodes[cups[0]]
    for _ in range(n_moves):
        removed_nodes = [current_node.right, current_node.right.right, current_node.right.right.right]
        new_right = removed_nodes[-1].right
        current_node.right = new_right
        new_right.left = current_node

        destination_cup = current_node.value - 1
        while destination_cup < 1 or destination_cup in [node.value for node in removed_nodes]:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = highest_cup
        destination_node = nodes[destination_cup]

        right = destination_node.right
        destination_node.right = removed_nodes[0]
        removed_nodes[0].left = destination_node
        removed_nodes[-1].right = right
        right.left = removed_nodes[-1]

        current_node = current_node.right

    node = nodes[1]
    first = True
    result = []
    while first or node.value != 1:
        if first:
            first = False
        result.append(node.value)
        node = node.right
    return result
if __name__ == '__main__':
    # cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = [8, 7, 2, 4, 9, 5, 1, 3, 6]

    answer_part_1 = "".join(map(str, execute(cups, 100)[1:]))
    print(f"Part 1: {answer_part_1}")

    n_cups = 1000000
    for cup in range(max(cups) + 1, n_cups + 1):
        cups.append(cup)

    result_part_2 = execute(cups, 10000000)
    answer_part_2 = result_part_2[1] * result_part_2[2]
    print(f"Part 2: {answer_part_2}")



