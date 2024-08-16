# Sample data for 5 employees
employees = [
    {
        'name': 'Rasmus',
        'salesTarget': 130,  # Excellent
        'customerSatisfaction': 9,  # Good
        'attendance': 28,  # Excellent
        'peerFeedback': 10,  # Excellent
        'performanceRating': 'Outstanding',
        'yearsOfService': 6
    },
    {
        'name': 'Karl',
        'salesTarget': 90,  # Average
        'customerSatisfaction': 5,  # Poor
        'attendance': 22,  # Average
        'peerFeedback': 7,  # Good
        'performanceRating': 'Satisfactory',
        'yearsOfService': 3
    },
    {
        'name': 'Sofie',
        'salesTarget': 75,  # Poor
        'customerSatisfaction': 8,  # Good
        'attendance': 19,  # Poor
        'peerFeedback': 6,  # Average
        'performanceRating': 'Needs Improvement',
        'yearsOfService': 1
    },
    {
        'name': 'Kamilla',
        'salesTarget': 105,  # Good
        'customerSatisfaction': 10,  # Excellent
        'attendance': 26,  # Good
        'peerFeedback': 9,  # Excellent
        'performanceRating': 'Strong Performer',
        'yearsOfService': 4
    },
    {
        'name': 'Kim',
        'salesTarget': 85,  # Average
        'customerSatisfaction': 7,  # Average
        'attendance': 25,  # Good
        'peerFeedback': 5,  # Average
        'performanceRating': 'Satisfactory',
        'yearsOfService': 7
    }
]

def evaluate_sales_target(salesTarget):
    if salesTarget < 80:
        return "Poor"
    elif 80 <= salesTarget <= 100:
        return "Average"
    elif 100 < salesTarget <= 120:
        return "Good"
    else:
        return "Excellent"

def evaluate_customer_satisfaction(customerSatisfaction):
    if customerSatisfaction < 6:
        return "Poor"
    elif 6 <= customerSatisfaction <= 7:
        return "Average"
    elif 8 <= customerSatisfaction <= 9:
        return "Good"
    else:
        return "Excellent"

def evaluate_attendance(attendance):
    if attendance < 20:
        return "Poor"
    elif 20 <= attendance <= 24:
        return "Average"
    elif 25 <= attendance <= 27:
        return "Good"
    else:
        return "Excellent"

def evaluate_peer_feedback(peerFeedback):
    if peerFeedback < 4:
        return "Poor"
    elif 4 <= peerFeedback <= 6:
        return "Average"
    elif 7 <= peerFeedback <= 8:
        return "Good"
    else:
        return "Excellent"

def evaluate_performance(data):
    sales_rating = evaluate_sales_target(data['salesTarget'])
    customer_rating = evaluate_customer_satisfaction(data['customerSatisfaction'])
    attendance_rating = evaluate_attendance(data['attendance'])
    peer_rating = evaluate_peer_feedback(data['peerFeedback'])

    ratings = [sales_rating, customer_rating, attendance_rating, peer_rating]

    if ratings.count("Excellent") == 4:
        return "Outstanding"
    elif ratings.count("Poor") >= 2:
        return "Needs Improvement"
    elif ratings.count("Good") + ratings.count("Excellent") >= 3:
        return "Strong Performer"
    else:
        return "Satisfactory"
    
def calculate_bonus(data):
    performance_rating = data['performanceRating']
    years_of_service = data['yearsOfService']

    # Determine base bonus based on performance rating
    if performance_rating == "Outstanding":
        base_bonus = 1000
    elif performance_rating == "Strong Performer":
        base_bonus = 800
    elif performance_rating == "Satisfactory":
        base_bonus = 500
    else:  # "Needs Improvement"
        base_bonus = 200

    # Determine multiplier based on years of service
    if years_of_service < 2:
        multiplier = 1
    elif 2 <= years_of_service <= 5:
        multiplier = 1.5
    else:  # More than 5 years
        multiplier = 2

    # Calculate total bonus
    total_bonus = base_bonus * multiplier
    return total_bonus

# Test the evaluate_performance function
for employee in employees:
    performance_data = {
        'salesTarget': employee['salesTarget'],
        'customerSatisfaction': employee['customerSatisfaction'],
        'attendance': employee['attendance'],
        'peerFeedback': employee['peerFeedback']
    }
    performance_rating = evaluate_performance(performance_data)
    print(f"{employee['name']} - Performance Rating: {performance_rating}")

# Test the calculate_bonus function
for employee in employees:
    bonus_data = {
        'performanceRating': employee['performanceRating'],
        'yearsOfService': employee['yearsOfService']
    }
    annual_bonus = calculate_bonus(bonus_data)
    print(f"{employee['name']} - Annual Bonus: ${annual_bonus}")