import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    now = datetime.fromisoformat(iso_string)
    cf = now.strftime("%A %d %B %Y")
    return (cf)


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    
    celcius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(celcius,1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    converted_numbers = []
    for number in weather_data:
        converted_numbers.append(float(number))
    return float(sum(converted_numbers)) / len(converted_numbers)


def load_data_from_csv(csv_file_path):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    with open(csv_file_path) as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row !=[] : 
                    converted_row = [row[0],int(row[1]), int(row[2])]
                    data_list.append(converted_row)
    return(data_list)
    


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    converted_numbers = []
    for number in weather_data:
        converted_numbers.append(float(number))
    minimum = min(converted_numbers)
    minimum_index = len(converted_numbers) - 1 - converted_numbers[::-1].index(minimum)
    return minimum, minimum_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    converted_numbers = []
    for number in weather_data:
        converted_numbers.append(float(number))
    maximum = max(converted_numbers)
    maximum_index = len(converted_numbers) - 1 - converted_numbers[::-1].index(maximum)
    return maximum, maximum_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    number_days = len(weather_data)
    total_min_temp = []
    total_max_temp = []
    for row in weather_data:
        min_temperature = row[1]
        total_min_temp.append(min_temperature)
        max_temperature = row[2]
        total_max_temp.append(max_temperature)
    min_value,min_index = find_min(total_min_temp)
    max_value,max_index = find_max(total_max_temp)

    min_temperature_c = convert_f_to_c(min_value)
    max_temperature_c = convert_f_to_c(max_value)

    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])

    min_average = convert_f_to_c(calculate_mean(total_min_temp))
    max_average = convert_f_to_c(calculate_mean(total_max_temp))
    
    summary = f"{number_days } Day Overview\n"
    summary += f"  The lowest temperature will be {format_temperature(min_temperature_c)}, and will occur on {min_date}.\n"
    summary += f"  The highest temperature will be {format_temperature(max_temperature_c)}, and will occur on {max_date}.\n"
    summary += f"  The average low this week is {format_temperature(min_average)}.\n"
    summary += f"  The average high this week is {format_temperature(max_average)}.\n"

    return summary
    



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for row in weather_data:
        day = convert_date(row[0])
        
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))

        summary += f"---- {day} ----\n"
        summary += f"  Minimum Temperature: {min_temp}\n"
        summary += f"  Maximum Temperature: {max_temp}\n\n"
    return summary


