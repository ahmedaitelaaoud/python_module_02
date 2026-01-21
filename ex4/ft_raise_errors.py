class GardenError(Exception):
	pass


def check_plant_health(plant_name, water_level, sunlight_hours):
	if water_level > 10 or water_level < 0:
		raise GardenError(f"Error: Water level {water_level} is too high (max 10)")
	elif sunlight_hours < 2 or sunlight_hours > 12:
		raise GardenError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
	print(f"Plant {plant_name} is healthy!")


def test_plant_checks():
	print("=== Garden Plant Health Checker ===\n")
	print("Testing good values...")
	try:
		check_plant_health("tomato", 5, 5)
	except GardenError as e:
		print(e)
	print("\nTesting empty plant name...")
	try:
		check_plant_health(None, 5, 5)
	except GardenError:
		print("Error: Plant name cannot be empty!\n")
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
