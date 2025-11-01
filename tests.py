import unittest
from functions.get_files_info import get_files_info
from functions.file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class GetPathInfo(unittest.TestCase):
    def setUp(self):
        pass

    #def test_base(self):
    #    result = get_files_info("calculator",".")
    #    print(result)
    #    correct = """Result for current directory:\n- main.py: file_size=730 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=128 bytes, is_dir=True"""
    #    self.assertEqual(result, correct)
#
    #def test_sub_dir(self):
    #    result = get_files_info("calculator","pkg")
    #    print(result)
    #    correct = """Result for 'pkg' directory:\n- calculator.py: file_size=1738 bytes, is_dir=False\n- render.py: file_size=389 bytes, is_dir=False"""
    #    self.assertEqual(result, correct)
#
    #def test_missing_path(self):
    #    result = get_files_info("calculator","/bin")
    #    print(result)
    #    correct = """Result for '/bin' directory:\nError: Cannot list "/bin" as it is outside the permitted working directory"""
    #    self.assertEqual(result, correct)
#
    #def test_outside_dir(self):
    #    result = get_files_info("calculator","../")
    #    print(result)
    #    correct = """Result for '../' directory:\nError: Cannot list "../" as it is outside the permitted working directory"""
    #    self.assertEqual(result, correct)
#
#    def test_main(self):
#        result = get_file_content("calculator", "main.py")
#        print(result)
#        self.assertNotEqual("Error:", result[0:6])
#
#    def test_sub_folder(self):
#        result = get_file_content("calculator", "pkg/calculator.py")
#        print(result)
#        self.assertNotEqual("Error:", result[0:6])
#
#    def test_not_file(self):
#        result = get_file_content("calculator", "/bin/cat")
#        print(result)
#        self.assertEqual("Error:", result[0:6])
#
#    def test_file_does_not_exist(self):
#        result = get_file_content("calculator", "pkg/does_not_exist.py")
#        print(result)
#        self.assertEqual("Error:", result[0:6])
# 
    # def test_existing_write(self):
    #     content = "wait, this isn't lorem ipsum"
    #     result = write_file("calculator","lorem.txt", content) 
    #     print(result)
    #     self.assertEqual(f'Successfully wrote to "lorem.txt" ({len(content)} characters written)', result)

    # def test_new_write(self):
    #     content =  "lorem ipsum dolor sit amet"       
    #     result = write_file("calculator","pkg/morelorem.txt", content) 
    #     print(result)
    #     self.assertEqual(f'Successfully wrote to "pkg/morelorem.txt" ({len(content)} characters written)', result)

    # def test_invalid_write(self):
    #     content = "this should not be allowed"
    #     result = write_file("calculator","/tmp/temp.txt", content) 
    #     print(result)
    #     self.assertEqual(f'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory' , result)

    # def test_main(self):
    #     result = run_python_file("calculator","main.py") 
    #     print(result)
    #     self.assertNotIn(f'Error:' , result)

    # def test_main_with_args(self):
    #     result = run_python_file("calculator","main.py", ["3 + 5"]) 
    #     print(result)
    #     self.assertNotIn(f'Error:' , result)

    # def test_tests(self):
    #     result = run_python_file("calculator","tests.py") 
    #     print(result)
    #     self.assertNotEqual(f'Error:' , result[:6])

    # def test_invalid_path(self):
    #     result = run_python_file("calculator","../main.py") 
    #     print(result)
    #     self.assertEqual(f'Error: Cannot execute "../main.py" as it is outside the permitted working directory' , result)

    # def test_file_not_found(self):
    #     result = run_python_file("calculator","nonexistent.py") 
    #     print(result)
    #     self.assertEqual(f'Error: File "nonexistent.py" not found.' , result)

    # def test_invalid_file(self):
    #     result = run_python_file("calculator","lorem.txt") 
    #     print(result)
    #     self.assertEqual(f'Error: "lorem.txt" is not a Python file.' , result)



if __name__ == "__main__":
    unittest.main()
