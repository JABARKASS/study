import json

def load_schedule():
  try:
    with open("schedule.json", "r") as file:
      schedule = json.load(file)
    return schedule
  except FileNotFoundError:
    return []



def save_schedule(schedule):
  with open("schedule.json", "w") as file:
    json.dump(schedule, file, indent=2)



def display_schedule():
  schedule = load_schedule()
  print(json.dumps(schedule, indent=2))



def add_train():
  schedule = load_schedule()
  train_number = int(input("Enter train number: "))
  destination = input("Enter destination: ")
  arrival_hours = int(input("Enter arrival hours: "))
  arrival_minutes = int(input("Enter arrival minutes: "))
  departure_hours = int(input("Enter departure hours: "))
  departure_minutes = int(input("Enter departure minutes: "))

  new_train = {
      "train_number": train_number,
      "destination": destination,
      "arrival_time": {
          "hours": arrival_hours,
          "minutes": arrival_minutes
      },
      "departure_time": {
          "hours": departure_hours,
          "minutes": departure_minutes
      }
  }

  schedule.append(new_train)
  save_schedule(schedule)
  print("Train added successfully!")



def find_trains_at_time():
  schedule = load_schedule()
  search_hours = int(input("Enter search hours: "))
  search_minutes = int(input("Enter search minutes: "))

  matching_trains = [
      train for train in schedule
      if train["departure_time"]["hours"] == search_hours
      and train["departure_time"]["minutes"] == search_minutes
  ]

  if matching_trains:
    print("Trains at the specified time:")
    for train in matching_trains:
      print(
          f"Train {train['train_number']}, Destination: {train['destination']}"
      )
  else:
    print("No trains found at the specified time.")



while True:
  print(
      "\n1. Display schedule\n2. Add train\n3. Find trains at a specific time\n4. Exit"
  )
  choice = input("Enter your choice (1/2/3/4): ")

  if choice == "1":
    display_schedule()
  elif choice == "2":
    add_train()
  elif choice == "3":
    find_trains_at_time()
  elif choice == "4":
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please enter a valid option.")
