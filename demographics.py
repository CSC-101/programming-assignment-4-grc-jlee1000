# demographics.py
import sys
from county_demographics import CountyDemographics


# Function to simulate loading data
def load_data():
    """Simulate loading the data"""
    data = [
        CountyDemographics(
            age={'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
            county='San Luis Obispo County',
            education={"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
            ethnicities={'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                         'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                         'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
            income={'Median Household Income': 58697, 'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3},
            population={'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5,
                        'Population per Square Mile': 81.7},
            state='CA'
        ),

    ]
    return data


# Function to load and parse an operations file
def load_operations(file_path):
    with open(file_path, 'r') as file:
        operations = file.readlines()
    return operations


# Modify existing process_operations function to handle operations
def process_operations(data, operations):
    for entry in data:
        for operation in operations:
            operation = operation.strip()
            operation_parts = operation.split(':')  # Split into command and arguments

            if len(operation_parts) == 2:
                command, args = operation_parts
                args = args.strip()  # Clean up the arguments

                if command == 'filter_state':
                    # Perform state filtering operation
                    if entry.filter_state(args):
                        print(f"Processing {entry.county} in {entry.state}")
                elif command == 'filter_gt':
                    # Perform filter greater than operation
                    field, number = args.rsplit(' ', 1)
                    number = float(number)
                    if entry.filter_gt(field, number):
                        print(f"County {entry.county} meets filter: {field} > {number}")
                elif command == 'display':
                    # Display all demographic data
                    entry.display()
                elif command == 'population_field':
                    # Example population calculation
                    print(f"Population for {entry.county}: {entry.population_field(args)}")
                elif command == 'percent_field':
                    # Example of a percentage field
                    print(f"Percent of {args} in {entry.county}: {entry.percent_field(args)}%")


# Main entry point
def main():
    try:
        # Load the data
        data = load_data()
        print(f"Loaded data with {len(data)} entries.")

        # Load operations file
        operations_file = 'operations_files/task2_a.ops'
        operations = load_operations(operations_file)

        # Process operations based on the data
        process_operations(data, operations)

    except Exception as e:
        print(f"Error processing data: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

