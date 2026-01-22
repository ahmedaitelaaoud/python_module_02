class GardenError(Exception):
    """Base exception for garden-related validation errors."""
    pass


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate plant health parameters.

    Checks if plant name is valid and if water level and sunlight hours
    are within acceptable ranges for healthy plant growth.

    Args:
        plant_name: Name of the plant to check
        water_level: Water level (must be between 1-10)
        sunlight_hours: Daily sunlight hours (must be between 2-12)

    Raises:
        GardenError: If any parameter is invalid
    """
    if not plant_name:
        raise GardenError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise GardenError(f"Error: Water level {water_level} "
                          f"is too high (max 10)")
    elif water_level < 1:
        raise GardenError(f"Error: Water level {water_level} "
                          f"is too low (min 1)")

    if sunlight_hours > 12:
        raise GardenError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours < 2:
        raise GardenError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Test plant health validation with various inputs.

    Demonstrates error raising and handling for invalid plant parameters.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except GardenError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except GardenError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except GardenError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except GardenError as e:
        print(e)

    print("\nAll error raising tests completed!")


test_plant_checks()
