def water_plants(plant_list):
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
plant_list = ["Tomato", "lettuce", "carrots"]
water_plants(plant_list)

print("\nWatering completed successfully!\n")

print("Testing with error...")
plant_list1 = ["tomato", None]
water_plants(plant_list1)

print("\nCleanup always happens, even with errors!")
