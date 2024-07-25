import sys
from test_job_posting.crew import JobPostingCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company_domain':'crewai.com',
        'company_descriptio': 'crewai.com',
        'hiring_needs': '',
        'specific_benefits':'',
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'crewai.com',
        'company_descriptio': 'crewai.com',
        'hiring_needs': '',
        'specific_benefits':'',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
