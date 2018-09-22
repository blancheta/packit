import run
from run import *
from unittest import TestCase
from unittest.mock import patch

class TestContainerPrompt(TestCase):

    @patch('run.get_input', return_value=(4, 4, 2))
    def test_can_save_container_dimensions(self, mock_get_input):

        """
        Test can save container dimensions
        """

        res = container_prompt()
        self.assertEqual((4, 4, 2), res)

    @patch('run.container', return_value={ 'dim' : (2, 2, 2)})
    def test_can_validate_a_box_inside_a_container_box(self, mock_container_dim):

        """
        Test can validate a box inside a containerbox
        """

        res = validate_size((1, 1, 1))
        self.assertTrue(res)

    @patch('run.container', return_value={ 'dim' : (2, 2, 2)})
    def test_cannot_validate_a_box_inside_a_container_box(self, mock_container_dim):
        """
        Test cannot validate a box inside a containerbox
        """

        res = validate_size((2, 2, 2))
        self.assertEqual(False, res)

    @patch('run.container', return_value={'dim': (2, 2, 2)})
    def test_cannot_validate_a_box_inside_a_container_box(self, mock_container_dim):
        """
        Test cannot validate a box inside a containerbox
        """

        res = validate_size((3, 3, 3))
        self.assertEqual(False, res)

    @patch('run.container', return_value={'dim': (2, 2, 2)})
    @patch('run.get_input', return_value=(1, 1, 1))
    def test_can_save_a_content_block(self, mock_container_dim, mock_get_input):
        """
        Test can save a content block
        """

        res = content_prompt()
        self.assertTrue(res)

class TestBoxInBox(TestCase):

    def test_can_add_a_box_in_a_container(self):

        """
        Test can add a box in a container
        """

        container = {
            'dim': (2,2,2),
            'in': []
        }

        add_box_into_container({
                'dim': (2,2,2),
                'pos': (0,1,0)
            }, container)
        self.assertTrue(list(container['in']))

    def test_can_add_boxes_in_a_container(self):

        """
        Test can add a box in a container
        """

        container = {
            'dim': (2,2,2),
            'in': []
        }

        add_box_into_container({
                'dim': (2,1,2),
                'pos': (0,1,0)
            }, container)

        add_box_into_container({
            'dim': (2, 1, 2),
            'pos': (0, 1, 0)
        }, container)

        self.assertTrue(list(container['in']))

    def test_cannot_add_box_in_a_container(self):

        """
        Test cannot add a box in a container, too high
        """

        container = {
            'dim': (2, 2, 2),
            'in': [
                {
                    'dim': (2,1,2),
                    'pos': (0,0,0)
                }
            ]
        }

        with self.assertRaises(Exception):
            add_box_into_container({
                'dim': (2,2,2),
                'pos': (0,1,0)
            }, container)
