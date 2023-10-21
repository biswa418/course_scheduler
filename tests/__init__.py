# import unittest
# from unittest.mock import patch
# from geektrust import main  # Import the main function from main.py in the root folder
# from io import StringIO

# class TestMainFunctionality(unittest.TestCase):
#     @patch(
#         "sys.argv",
#         [
#             "geektrust.py",
#             "ADD-COURSE-OFFERING DATASCIENCE BOB 05062022 1 3\nREGISTER WOO@GMAIL.COM OFFERING-DATASCIENCE-BOB\nREGISTER ANDY@GMAIL.COM OFFERING-DATASCIENCE-BOB\nALLOT OFFERING-DATASCIENCE-BOB",
#         ],
#     )
#     def test_main_functionality_with_custom_input(self):
#         # Create a mock object to capture the printed output
#         with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
#             # Call the main function
#             with self.assertRaises(SystemExit):
#                 main()  # This will raise SystemExit as it calls sys.exit() in the main function

#             # Get the printed output from the mock object
#             output = mock_stdout.getvalue().strip()

#         # Expected output
#         expected_output = """OFFERING-DATASCIENCE-BOB
# REG-COURSE-WOO-DATASCIENCE ACCEPTED
# REG-COURSE-ANDY-DATASCIENCE ACCEPTED
# REG-COURSE-ANDY-DATASCIENCE ANDY@GMAIL.COM OFFERING-DATASCIENCE-BOB DATASCIENCE BOB 05062022 CONFIRMED
# REG-COURSE-WOO-DATASCIENCE WOO@GMAIL.COM OFFERING-DATASCIENCE-BOB DATASCIENCE BOB 05062022 CONFIRMED"""

#         # Assert that the printed output matches the expected output
#         self.assertEqual(output, expected_output)


# if __name__ == "__main__":
#     unittest.main()
