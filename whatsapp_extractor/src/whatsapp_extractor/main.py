#!/usr/bin/env python
import sys
import warnings
import json
from whatsapp_extractor.crew import WhatsappExtractor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the WhatsApp extraction crew.
    """
    inputs = {
        'chat_name': 'Family Group',  # Replace with target chat name
        'max_messages': 100  # Maximum number of messages to extract
    }
    results = WhatsappExtractor().crew().kickoff(inputs=inputs)
    
    # Save results to file
    with open('whatsapp_data.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("Data extraction completed. Results saved to whatsapp_data.json")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'chat_name': 'Test Group',
        'max_messages': 10
    }
    try:
        WhatsappExtractor().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        WhatsappExtractor().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'chat_name': 'Test Group',
        'max_messages': 5
    }
    return WhatsappExtractor().crew().kickoff(inputs=inputs)
