import sys
from test_job_posting.crew import JobPostingCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company_domain':'baskinrobins.com',
        'company_description': 'Baskin-Robbins is an American multinational chain of ice cream and cake specialty shops owned by Inspire Brands',
        'hiring_needs': 'Cake decorator,  at least 1 - 2 years cake decorating experience, stand for long periods of time, cake decorator needs',
        'specific_benefits':'Weekly Pay, Employee Meals',
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'baskinrobins.com',
        'company_description': 'Baskin-Robbins is an American multinational chain of ice cream and cake specialty shops owned by Inspire Brands',
        'hiring_needs': 'Cake decorator,  at least 1 - 2 years cake decorating experience, stand for long periods of time, cake decorator needs',
        'specific_benefits':'Weekly Pay, Employee Meals',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
