import argparse

notes = """
Name                    Description
facility()              Filter messages based on the sending facility.
filter()                Call another filter function.
host()                  Filter messages based on the sending host.
inlist()                File-based whitelisting and blacklisting.
level() or priority()   Filter messages based on their priority.
match()                 Use a regular expression to filter messages based on a specified header or content field.
message()               Use a regular expression to filter messages based on their content.
netmask() or netmask6() Filter messages based on the IP address of the sending host.
program()               Filter messages based on the sending application.
source()                Select messages of the specified syslog-ng OSE source statement.
tags()                  Select messages having the specified tag.
"""

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Create a filter from IPs file")

# Define command line arguments
parser.add_argument('-fn', '--filter_name', type=str, required=True, help='Name of the filter')
parser.add_argument('-fp', '--file_path', type=str, required=True, help='Path to the file containing IP addresses')
parser.add_argument('-fx', '--function', type=str, required=True, help='Filter function to apply')
parser.add_argument('-lo', '--logical_operator', type=str, default='or', help='Logical operator to use between filters')
parser.add_argument('-R', '--readme', action='store_true', help='Display readme notes')

# Parse the command line arguments
args = parser.parse_args()

# Extract arguments
filter_name = args.filter_name
file_path = args.file_path
function = args.function
logical_operator = args.logical_operator
display_readme = args.readme

def readme():
    print(notes)

def create_filter_from_ips_file(file_path, function, filter_name, logical_operator):
    """
    Author: HudSeiduDaannaa
    Creates a syslog-ng filter rule from a list of IP addresses in a file.

    :param file_path: str - Path to the file containing IP addresses
    :param function: str - Filter function to apply (e.g., netmask)
    :param filter_name: str - Name of the filter
    :param logical_operator: str - Logical operator to use between filters (e.g., 'or', 'and')
    """
    with open(file_path, "r") as file:
        ip_list = file.read().splitlines()

    filter_rule = ""
    for ip in ip_list[:-1]:
        filter_rule += f"{function}('{ip}') {logical_operator} "

    filter_rule += f"{function}('{ip_list[-1]}')"
    rule = f"filter f_{filter_name} {{ {filter_rule} }};"
    
    print("\n\n" + rule + "\n\n")

# Display readme notes if requested
if display_readme:
    readme()
else:
    create_filter_from_ips_file(file_path, function, filter_name, logical_operator)
