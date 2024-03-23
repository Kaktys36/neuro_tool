import unittest
from unittest.mock import patch
from io import StringIO
import sys
import main


class TestMain(unittest.TestCase):
    @patch("streamlit.selectbox", return_value="Стартовая страница")
    def test_start_page_info(self, mock_selectbox):
        captured_output = StringIO()
        sys.stdout = captured_output
        main.selected_model = "Стартовая страница"
        main.show_start_page = True
        main.show_info = False
        main.info_func(main.info, main.show_info)
        sys.stdout = sys.__stdout__
        self.assertIn("Neurotool_v.1.1.2", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
