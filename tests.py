from functions.get_files_info import get_files_info


def main():
    """Test the get_files_info function with various inputs."""
    
    # Test 1: Current directory in calculator
    print("get_files_info(\"calculator\", \".\"):")
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    print(result)
    print()
    
    # Test 2: pkg subdirectory
    print("get_files_info(\"calculator\", \"pkg\"):")
    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print(result)
    print()
    
    # Test 3: Absolute path outside working directory
    print("get_files_info(\"calculator\", \"/bin\"):")
    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print(f"    {result}")
    print()
    
    # Test 4: Parent directory (outside working directory)
    print("get_files_info(\"calculator\", \"../\"):")
    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    print(f"    {result}")


if __name__ == "__main__":
    main()
