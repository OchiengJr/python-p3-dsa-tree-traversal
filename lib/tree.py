class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        """Recursively search for an element with the given ID."""
        if self.root is None:
            return None
        return self._search_element_by_id(self.root, target_id)

    def _search_element_by_id(self, node, target_id):
        """Helper function for recursive search."""
        if node['id'] == target_id:
            return node
        for child in node['children']:
            result = self._search_element_by_id(child, target_id)
            if result:
                return result
        return None
