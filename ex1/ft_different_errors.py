def garden_operations(mode):
    """
        Simulate different types of errors in garden operations.

        Args:
            mode: Type of error to demonstrate (typemistake, mathmistake,
                  missingfile, missingkey)
     """
    if mode == "typemistake":
        int("cat")
    elif mode == "mathmistake":
        10 / 0
    elif mode == "missingfile":
        open("ghost_file.txt")
    elif mode == "missingkey":
        my_dict = {"a": 1}
        print(my_dict["b"])


def test_error_types():
    """
        Demonstrate different error types and how to catch them.

        Shows ValueError, ZeroDivisionError, FileNotFoundError, and KeyError
        handling in agricultural data processing scenarios.
    """
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("typemistake")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("mathmistake")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("missingfile")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden_operations("missingkey")
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("typemistake")
        garden_operations("mathmistake")
    except ValueError:
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


test_error_types()
