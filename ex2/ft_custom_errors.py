class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering system problems."""
    pass


def check_garden(mode):
    """
    Simulate different garden error conditions.

    Args:
        mode: Type of error to raise ('plant' or 'water')

    Raises:
        PlantError: When mode is 'plant'
        WaterError: When mode is 'water'
    """
    if mode == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif mode == "water":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
        Demonstrate custom exception handling for garden management.

        Shows how to create and catch custom exceptions, and how inheritance
        allows catching multiple related errors with a base exception class.
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_garden("plant")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        check_garden("water")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        check_garden("plant")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_garden("water")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


test_custom_errors()
