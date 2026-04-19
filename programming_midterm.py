# Sports Events Management System

# Get class section and coordinator name
# Validate Class Section (Cannot be blank)
section_name = ""
while section_name == "":
    section_name = input("Class section: ")
    if section_name == "":
        print("Error: Input cannot be empty. Please try again.")
section_name = section_name.upper()

# Validate Coordinator Name (Cannot be blank)
coordinator_name = ""
while coordinator_name == "":
    coordinator_name = input("Coordinator name: ")
    if coordinator_name == "":
        print("Error: Input cannot be empty. Please try again.")


# Display sports events
print("\n==========================================")
print("   INTRAMURALS -- SPORTS EVENTS")
print("==========================================")
print(" 1. Basketball    [Team]")
print(" 2. Volleyball    [Team]")
print(" 3. Badminton     [Individual]")
print(" 4. Chess         [Individual]")
print(" 5. Table Tennis  [Individual]")
print("==========================================\n")

# Store game results
games = []
total_points = 0

# Loop to collect game entries
for game_number in range(1, 5):
    print(f"--- GAME {game_number} ---")

    sport_number = -1  # Initialize to an invalid number
    while sport_number < 0 or sport_number > 5:
        sport_number = int(input("Sport number (0 to skip): "))
        if sport_number == 0:
            print("Game skipped.")
            break  # Skip this game

        # Validate sport number
        if sport_number < 1 or sport_number > 5:
            print("Invalid sport number! Please enter a number from 1 to 5.")

    # If user skipped the sport
    if sport_number == 0:
        continue

    opposing_section = input("Opposing section: ")

    # Get the result with validation
    result = ''  # Initialize as empty
    while result not in ['W', 'L']:
        result = input("Result (W/L): ").upper()
        if result not in ['W', 'L']:
            print("Invalid result! Please enter W for Win or L for Loss.")

    # Determine points earned
    points_earned = 3 if result == 'W' else 0
    total_points += points_earned

    # Store game result
    games.append((sport_number, opposing_section, result, points_earned))

# Determine section standing
if total_points >= 9:
    standing = 'GOLD CONTENDER'
elif total_points >= 6:
    standing = 'SILVER PUSH'
else:
    standing = 'KEEP FIGHTING!'

# Print the game results board
print("\n=============================================")
print(f"     {section_name} -- GAME RESULTS BOARD")
print("=============================================")
print(f"Coordinator : {coordinator_name}")
print("---------------------------------------------")

# Manual index for outputting game results
index = 1
for game in games:
    sport_number, opponent, result, points = game
    sport_name = ""

    # Determine sport name based on sport number
    if sport_number == 1:
        sport_name = "Basketball"
    elif sport_number == 2:
        sport_name = "Volleyball"
    elif sport_number == 3:
        sport_name = "Badminton"
    elif sport_number == 4:
        sport_name = "Chess"
    elif sport_number == 5:
        sport_name = "Table Tennis"

    # Determine the result string
    if result == 'W':
        result_str = "WIN"
    else:
        result_str = "LOSS"

    output = f"[{index}] {sport_name:<12} | vs {opponent:<10} | Result: {result_str:<5} | Points: {points}"

    print(output)  # Print the formatted output
    index += 1  # Increment index manually
