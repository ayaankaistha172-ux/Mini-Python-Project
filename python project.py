
import csv

def load_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            return [row for row in reader if row]

    except FileNotFoundError:
        return [
            ["BU001", "Aarav"],
            ["BU002", "Vivaan"],
            ["BU003", "Aditya"],
            ["BU004", "Arjun"],
            ["BU005", "Kabir"],
            ["BU006", "Rohan"],
            ["BU007", "Nuhan"],
            ["BU008", "Disha"],
            ["BU009", "Vansh"],
            ["BU010", "Divya"],
            ["BU011", "Ajay"],
            ["BU012", "Sumit"],
            ["BU013", "Rahul"],
            ["BU014", "Mukul"],
            ["BU015", "Neha"]
        ]


students = load_students()

rooms = {
    "R101": 5,
    "R102": 5,
    "R103": 5
}


def generate_seats():
    seating = []
    i = 0

    for room, capacity in rooms.items():
        for seat in range(1, capacity + 1):
            if i < len(students):
                seating.append([
                    students[i][0],
                    students[i][1],
                    room,
                    seat
                ])
                i += 1

    if i < len(students):
        print(f"Warning: {len(students) - i} student(s) could not be assigned due to lack of seats.")

    try:
        with open("Exam Seating Arrangement Generator.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Room", "Seat"])
            writer.writerows(seating)

        print("Successfully saved seating arrangement to 'Exam Seating Arrangement Generator.csv'.")

    except IOError as e:
        print(f"Error handling file operations: {e}")

    return seating


def search_student(seating):
    sid = input("Enter Student ID: ").strip().upper()

    for s in seating:
        if s[0].upper() == sid:
            print("Name:", s[1])
            print("Room:", s[2])
            print("Seat:", s[3])
            return

    print("Student not found.")


seating = generate_seats()

print("\n--- Exam Seating Arrangement ---")

for s in seating:
    print(s[0], s[1], "->", s[2], "Seat", s[3])

search_student(seating)
