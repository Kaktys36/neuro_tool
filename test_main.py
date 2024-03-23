import pytest
from unittest.mock import patch
from io import StringIO
import sys
from main import selected_model, show_start_page, show_info, info_func, info, models

def test_show_start_page():
    selected_model = "Some_model"
    show_start_page = True
    show_info = False
    info = ["Some", "info", "here"]
    with patch("streamlit.selectbox", return_value="Some_model"):
        captured_output = StringIO()
        sys.stdout = captured_output
        if selected_model == "GPT_3.5_turbo":  
            assert show_start_page == False
        elif selected_model == "YOLO8_face_detector":  
            assert show_start_page == False

if __name__ == "__main__":
    pytest.main()
