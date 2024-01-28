# imported to use command line argument
import sys


def cat_data(file_path):  # function to get data of our cat
    """ 
    Analyze cat visitation data from a log file.

    Parameters:
        file_path (str): The path to the log file containing cat visit data.

    Returns:
        our_cat (int): Number of visits by our cat.
        intruder_cat (int): Number of visits by other cats.
        total_hours (int): Total hours our cat spent in the house.
        total_minutes (int): Remaining minutes our cat spent in the house.
        average_visit (int): Average visit length in minutes by our cat.
        longest_time (int): Longest visit length in minutes.
        shortest_time (int): Shortest visit length in minutes.
    """

    try:
        with open(file_path, "r") as f:  # open file in read mode
            our_cat = 0
            intruder_cat = 0
            total_time = 0
            visit_times = []  # List to store all visit times so it is iterable

            for line in f:
                if line == 'END':
                    break

                data = line.split(',')
                cat_data = data[0]
                entry_time = int(data[1])
                exit_time = int(data[2])

                if cat_data == "OURS":
                    our_cat += 1
                    visit_time = exit_time - entry_time
                    total_time += visit_time
                    visit_times.append(visit_time)
                else:
                    intruder_cat += 1

            total_hours = total_time // 60
            total_minutes = total_time % 60
            average_visit = total_time // our_cat
            longest_time = max(visit_times)
            shortest_time = min(visit_times)

            return our_cat, intruder_cat, total_hours, total_minutes, average_visit, longest_time, shortest_time

    except FileNotFoundError:
        print(f"Cannot open '{file_path}'!")
    except Exception as e:
        print(f"An error occurred: {e}")


# fuction to use data of our cat and print those data
def print_data(our_cat, intruder_cat, total_hours, total_minutes, average_visit, longest_time, shortest_time):
    """
    Prints the cat data analysis results.

    Parameters:
        our_cat (int): Number of visits by our cat.
        intruder_cat (int): Number of visits by other cats.
        total_hours (int): Total hours our cat spent in the house.
        total_minutes (int): Remaining minutes our cat spent in the house.
        average_visit (int): Average visit length in minutes by our cat.
        longest_time (int): Longest visit length in minutes.
        shortest_time (int): Shortest visit length in minutes.
    """

    name = "Log File Analysis"
    print(name)
    print("="*len(name))
    print()

    print(f"Cat Visits: {our_cat:>2}")
    print(f"Other Cats: {intruder_cat:>2}")
    print()

    print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minute" if total_minutes <= 1
          else f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes")
    print()

    print(f"Average Visit Length:{average_visit:>3} Minutes")
    print(f"Longest Visit:{longest_time:>10} Minutes")
    print(f"Shortest Visit:{shortest_time:>9} Minutes")


# Check if the script is run with the correct number of arguments
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    file_path = sys.argv[1]
    data = cat_data(file_path)
    if data:
        print_data(*data)
