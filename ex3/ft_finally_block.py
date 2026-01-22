def water_plants(plant_list):
    """
    Water all plants in the garden with automatic cleanup.

    Opens watering system, waters each plant, and ensures the system
    is properly closed even if errors occur.

    Args:
        plant_list: List of plant names to water
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)

    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


print("=== Garden Watering System ===\n")
print("Testing normal watering...")
normal_plants = ["Tomato", "lettuce", "carrots"]
water_plants(normal_plants)

print("\nWatering completed successfully!\n")

print("Testing with error...")
error_plants = ["tomato", None]
water_plants(error_plants)

print("\nCleanup always happens, even with errors!")
