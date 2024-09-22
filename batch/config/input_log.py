import logging

# Configure the logging
logging.basicConfig(
    filename='input_log.log',    # Log file name
    level=logging.DEBUG,         # Log all levels of messages
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_input(data):
    try:
        # Simulate processing input
        if isinstance(data, int):
            # Log success
            logging.info(f"Input success: {data}")
            # Perform processing (placeholder)
            result = data * 2
            return result
        else:
            raise ValueError("Invalid input type")
    except Exception as e:
        # Log failure
        logging.error(f"Input failure: {data} - Error: {e}")
        return None

# Example usage
result1 = process_input(10)     # This should log a success
result2 = process_input('test') # This should log a failure
