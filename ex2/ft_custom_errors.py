class GardenError(Exception):
	pass


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def check_garden(mode):
	if mode == "plant":
		raise PlantError("The tomato plant is wilting!")
	elif mode == "water":
		raise WaterError("Not enough water in the tank!")


def test_custom_errors():
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
