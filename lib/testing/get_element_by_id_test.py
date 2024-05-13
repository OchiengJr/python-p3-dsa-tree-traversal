from tree import Tree

class TestStack:
    """Test cases for the Tree class."""

    def test_get_element_by_id(self):
        """Test get_element_by_id method."""

        # Define the tree structure
        tree = Tree(
            {
                'tag_name': 'body',
                'id': None,
                'children': [
                    {
                        'tag_name': 'div',
                        'id': 'main',
                        'children': [
                            {
                                'tag_name': 'h1',
                                'id': 'heading',
                                'text_content': 'Title',
                                'children': []
                            },
                            {
                                'tag_name': 'h2',
                                'id': None,
                                'text_content': 'Subtitle',
                                'children': []
                            }
                        ]
                    }
                ]
            }
        )

        # Test case: element with ID exists
        expected_element = {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
        }
        assert tree.get_element_by_id('heading') == expected_element, "Element with ID 'heading' not found."

        # Test case: element with ID does not exist
        assert tree.get_element_by_id('nope') is None, "Element with ID 'nope' found unexpectedly."
