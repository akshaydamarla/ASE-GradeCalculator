def calculate_average(marks):
    """Return the average of a non-empty list of marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Each mark must be between 0 and 100")
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Convert an average mark into a letter grade."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    """Read marks, then display the average and grade."""
    try:
        raw_marks = input("Enter marks separated by spaces: ")
        marks = [float(value) for value in raw_marks.split()]
        average = calculate_average(marks)
        grade = calculate_grade(average)
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
