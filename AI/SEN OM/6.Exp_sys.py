def evaluate_employee():
    print("Welcome to the Employee Performance Evaluation System!")

    # Get inputs from the user
    try:
        work_quality = int(input("\nRate the work quality (1-5): "))
        attendance = int(input("Enter the number of days present out of 30: "))
        teamwork = int(input("Rate teamwork and collaboration (1-5): "))

        # Validate inputs
        if work_quality < 1 or work_quality > 5 or teamwork < 1 or teamwork > 5:
            print("\nPlease enter ratings between 1 and 5 for Work Quality and Teamwork.")
            return
        
        if attendance < 0 or attendance > 30:
            print("\nPlease enter a valid attendance number (0 to 30 days).")
            return

    except ValueError:
        print("\nInvalid input. Please enter numeric values.")
        return

    # Calculate performance score
    performance_score = (work_quality + teamwork + (attendance / 30) * 5) / 3

    # Evaluate performance
    if performance_score >= 4.5:
        evaluation = "Excellent"
        feedback = "Outstanding work. Keep up the great performance!"
    elif performance_score >= 3.5:
        evaluation = "Good"
        feedback = "Good job! There is room for improvement in some areas."
    elif performance_score >= 2.5:
        evaluation = "Needs Improvement"
        feedback = "Performance is below expectations. Focus on improvement."
    else:
        evaluation = "Poor"
        feedback = "Performance is unsatisfactory. Consider taking corrective actions."

    # Output evaluation result
    print(f"\nPerformance Evaluation: {evaluation}")
    print(f"Feedback: {feedback}")


# Run the system
evaluate_employee()
