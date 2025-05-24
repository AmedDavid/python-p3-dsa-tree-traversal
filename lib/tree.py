class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None
        
        def depth_first(node):
            if node['id'] == id:
                return node
            for child in node['children']:
                result = depth_first(child)
                if result:
                    return result
            return None

        return depth_first(self.root)

        # Alternative: Breadth-first traversal
        """
        from collections import deque
        nodes_to_visit = deque([self.root])
        while nodes_to_visit:
            node = nodes_to_visit.popleft()
            if node['id'] == id:
                return node
            nodes_to_visit.extend(node['children'])
        return None
        """