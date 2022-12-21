from typing import List, Tuple


class TreetopTreeHouse:
    def __init__(self):
        pass

    def find_visible_trees(self, nodes_list: List[List[int]]) -> int:
        """Find the number of visible trees in a grid of nodes.

        Args:
            nodes_list: A list of lists of integers representing the grid of nodes.

        Returns:
            An integer representing the number of visible trees in the grid.
        """
        visible_trees = 0
        tree_blocker_counts = []
        for row, nodes in enumerate(nodes_list):
            if self.is_edge(row, nodes):
                visible_trees += len(nodes)
                continue

            for col, node in enumerate(nodes):
                if self.is_edge(col, nodes):
                    visible_trees += 1
                    continue

                position = (row, col)
                north, north_count = self.check_north(
                    node, position, nodes_list)
                south, south_count = self.check_south(
                    node, position, nodes_list)
                west, west_count = self.check_west(node, position, nodes)
                east, east_count = self.check_east(node, position, nodes)

                if west:
                    visible_trees += 1
                elif east:
                    visible_trees += 1
                elif north:
                    visible_trees += 1
                elif south:
                    visible_trees += 1

                blocker_count = (north_count * west_count *
                                 south_count * east_count)
                tree_blocker_counts.append(blocker_count)
        return visible_trees, max(tree_blocker_counts)

    def check_west(self, node: int, pos: tuple, row: List[int]) -> Tuple[bool, int]:
        """Check if the node to the west of the working node is valid.

        Args:
            node: An integer representing the value of the working node.
            pos: A tuple of integers representing the row and column indices of the working node.
            row: A list of integers representing the items in the row containing the working node.

        Returns:
            A tuple of a boolean and an integer. The boolean indicates whether the node to the west of the working node
            is valid, and the integer represents the number of nodes blocking the view of the working node.
        """
        blocker_count = 1
        row_index, col_index = pos
        for col in range(col_index - 1, -1, -1):
            if row[col] >= node:
                return False, blocker_count

            blocker_count += 1

        return True, blocker_count - 1

    def check_east(self, node: int, pos: tuple, row: List[int]) -> Tuple[bool, int]:
        """Check if the node to the east of the working node is valid.

        Args:
            node: An integer representing the value of the working node.
            pos: A tuple of integers representing the row and column indices of the working node.
            row: A list of integers representing the items in the row containing the working node.

        Returns:
            A tuple of a boolean and an integer. The boolean indicates whether the node to the east of the working node
            is valid, and the integer represents the number of nodes blocking the view of the working node.
        """
        blocker_count = 1
        row_index, col_index = pos
        for col in range(col_index + 1, len(row)):
            if row[col] >= node:
                return False, blocker_count
            blocker_count += 1
        return True, blocker_count - 1

    def check_north(self, node: int, pos: tuple, nodes: List[List[int]]) -> Tuple[bool, int]:
        """Check if all the nodes to the north of the working node are valid.

        Args:
            node: An integer representing the value of the working node.
            pos: A tuple of integers representing the row and column indices of the working node.
            nodes: A list of lists of integers representing the grid of nodes.

        Returns:
            A tuple of a boolean and an integer. The boolean indicates whether all the nodes to the north of the working node
            are valid, and the integer represents the number of nodes blocking the view of the working node.
        """
        blocker_count = 1
        row_index, col_index = pos
        while row_index > 0:
            row_index -= 1
            if nodes[row_index][col_index] >= node:
                return False, blocker_count
            blocker_count += 1

        return True, blocker_count - 1

    def check_south(self, node: int, pos: tuple, nodes: List[List[int]]) -> Tuple[bool, int]:
        """Check if all the nodes to the south of the working node are valid.

        Args:
            node: An integer representing the value of the working node.
            pos: A tuple of integers representing the row and column indices of the working node.
            nodes: A list of lists of integers representing the grid of nodes.

        Returns:
            A tuple of a boolean and an integer. The boolean indicates whether all the nodes to the south of the working node
            are valid, and the integer represents the number of nodes blocking the view of the working node.
        """
        blocker_count = 1
        row_index, col_index = pos
        while row_index < len(nodes) - 1:
            row_index += 1
            if nodes[row_index][col_index] >= node:
                return False, blocker_count
            blocker_count += 1
        return True, blocker_count - 1

    def is_edge(self, index: int, nodes: List[str]) -> bool:
        """
        Check if the node is an edge node.

        Args:
            index: An integer representing the index of the node.
            nodes: A list of strings representing the nodes.

        Returns:
            A boolean indicating whether the node is an edge node.
        """
        if index == 0 or index == (len(nodes) - 1):
            return True
        return False

    def build_nodes(self, lines: List[str]) -> List[List[str]]:
        """
        Build a list of nodes from a list of strings.

        Args:
            lines: A list of strings representing the nodes.

        Returns:
            A list of lists of strings representing the nodes.
        """
        nodes = []
        for line in lines:
            node = [int(char) for char in line]
            nodes.append(node)
        return nodes
