def check_temperature(temp_str):
	try:
		temp_int = int(temp_str)
		if temp_int > 40:
			print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
		elif temp_int < 0:
			print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
		else:
			print(f"Temperature {temp_int}°C is perfect for plants!")
	except ValueError:
		print(f"Error: '{temp_str}' is garbage data (not a number)")


print("=== Garden Temperature Checker ===\n")

test_cases = ["25", "abc", "100", "-50"]

for temp in test_cases:
	print(f"Testing temperature: {temp}")
	check_temperature(temp)
	print()

print("All tests completed - program didn't crash")
