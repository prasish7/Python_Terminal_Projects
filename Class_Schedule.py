
class_schedule =  {
  "Monday": [
    {"class": "Math", "start": "09:00", "end": "10:30"},
    {"class": "Physics", "start": "11:00", "end": "12:30"}
  ],
  "Tuesday": [
    {"class": "Chemistry", "start": "10:00", "end": "11:30"},
    {"class": "English", "start": "13:00", "end": "14:00"}
  ],
  "Wednesday": [
    {"class": "Biology", "start": "09:30", "end": "11:00"}
  ],
  "Thursday": [
    {"class": "History", "start": "10:00", "end": "11:30"},
    {"class": "Math", "start": "12:00", "end": "13:30"}
  ],
  "Friday": [
    {"class": "Computer Science", "start": "09:00", "end": "10:30"},
    {"class": "Art", "start": "11:00", "end": "12:00"}
  ]
}

user_input = input("Enter a day of the week to view your class schedule: ")
day = user_input.strip().capitalize()
if day in class_schedule:
    print(f"Class schedule for {day}:")
    for cls in class_schedule[day]:
        print(f"{cls['class']}: {cls['start']} - {cls['end']}") 
else:
    print("No classes scheduled for that day or invalid day entered.")


