from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    """Test the run_python_file function with various inputs."""
    # Test 1: Run main.py without arguments (should print usage)
    print('run_python_file("calculator", "main.py"):')
    result = run_python_file("calculator", "main.py")
    print(result)
    print()
    
    # Test 2: Run main.py with calculation argument
    print('run_python_file("calculator", "main.py", ["3 + 5"]):')
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print()
    
    # Test 3: Run tests.py
    print('run_python_file("calculator", "tests.py"):')
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()
    
    # Test 4: Attempt to run file outside working directory
    print('run_python_file("calculator", "../main.py"):')
    result = run_python_file("calculator", "../main.py")
    print(result)
    print()
    
    # Test 5: Attempt to run non-existent file
    print('run_python_file("calculator", "nonexistent.py"):')
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print()
    
    # Test 6: Attempt to run non-Python file
    print('run_python_file("calculator", "lorem.txt"):')
    result = run_python_file("calculator", "lorem.txt")
    print(result)








#   """Test the write_file function with various inputs."""
#    # Test 1: Overwrite lorem.txt
#print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
#result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#print(result)
#print()

#    # Test 2: Create new file in pkg directory
#print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
#result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#print(result)
#print()

#    # Test 3: Attempt to write outside working directory
#print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
#result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#print(result)

#    """Test the get_files_info function with various inputs."""
#    
#    # Test 1: Current directory in calculator
#    print("get_files_info(\"calculator\", \".\"):")
#    print("Result for current directory:")
#    result = get_files_info("calculator", ".")
#    print(result)
#    print()
#    
#    # Test 2: pkg subdirectory
#    print("get_files_info(\"calculator\", \"pkg\"):")
#    print("Result for 'pkg' directory:")
#    result = get_files_info("calculator", "pkg")
#    print(result)
#    print()
#    
#    # Test 3: Absolute path outside working directory
#    print("get_files_info(\"calculator\", \"/bin\"):")
#    print("Result for '/bin' directory:")
#    result = get_files_info("calculator", "/bin")
#    print(f"    {result}")
#    print()
#    
#    # Test 4: Parent directory (outside working directory)
#    print("get_files_info(\"calculator\", \"../\"):")
#    print("Result for '../' directory:")
#    result = get_files_info("calculator", "../")
#    print(f"    {result}")
#
#       # Test 1: Read main.py
#    print("get_file_content(\"calculator\", \"main.py\"):")
#    result = get_file_content("calculator", "main.py")
#    print(result)
#    print()
#    
#    # Test 2: Read pkg/calculator.py
#    print("get_file_content(\"calculator\", \"pkg/calculator.py\"):")
#    result = get_file_content("calculator", "pkg/calculator.py")
#    print(result)
#    print()
#    
#    # Test 3: Attempt to read file outside working directory
#    print("get_file_content(\"calculator\", \"/bin/cat\"):")
#    result = get_file_content("calculator", "/bin/cat")
#    print(result)
#    print()
#    
#    # Test 4: Attempt to read non-existent file
#    print("get_file_content(\"calculator\", \"pkg/does_not_exist.py\"):")
#    result = get_file_content("calculator", "pkg/does_not_exist.py")
#    print(result)


if __name__ == "__main__":
    main()
