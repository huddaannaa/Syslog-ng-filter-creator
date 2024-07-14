## High-Level Document on Using the IP Filter Script

### Overview

The IP Filter Script is designed to create a syslog-ng filter rule from a list of IP addresses provided in a file. This document provides a high-level guide on how to use the script, including setup, usage instructions, and examples.

### Prerequisites

1. **Python 3.x:** Ensure that Python 3.x is installed on your system.
2. **argparse Library:** The script uses the `argparse` library, which is included in the Python Standard Library.

### Script Description

The script takes several command-line arguments to create a syslog-ng filter rule from a file containing IP addresses. It supports filtering based on different criteria and applying logical operators between filters.

### Command-Line Arguments

- `-fn, --filter_name`: (Required) The name of the filter.
- `-fp, --file_path`: (Required) The path to the file containing IP addresses.
- `-fx, --function`: (Required) The filter function to apply (e.g., `netmask`).
- `-lo, --logical_operator`: (Optional) The logical operator to use between filters (default is `or`).
- `-R, --readme`: (Optional) Displays readme notes describing available filter functions.

### Setup

1. **Download the Script:**
   Save the script to a file, for example, `create_filter.py`.

2. **Make the Script Executable:**
   If you're using a Unix-based system (Linux/Mac), make the script executable:
   ```sh
   chmod +x create_filter.py
   ```

### Usage

To use the script, run it from the command line with the required arguments.

#### Display Readme Notes

To display the readme notes with descriptions of available filter functions:
```sh
python create_filter.py -R
```

#### Create a Filter Rule

To create a filter rule, provide the required arguments. For example:
```sh
python create_filter.py -fn my_filter -fp /path/to/ip_file.txt -fx netmask -lo and
```

### Examples

#### Example 1: Display Readme Notes

```sh
python create_filter.py -R
```

Output:
```
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
```

#### Example 2: Create a Filter Rule

Assume `ip_file.txt` contains the following IP addresses:
```
192.168.1.17
192.168.1.18
192.168.1.2
192.168.1.20
```

Run the script with the following command:
```sh
python create_filter.py -fn my_filter -fp ip_file.txt -fx netmask -lo and
```

Output:
```
filter f_my_filter { netmask('192.168.1.17') and netmask('192.168.1.18') and netmask('192.168.1.2') and netmask('192.168.1.20') };
```

### Script Breakdown

1. **Argument Parsing:**
   The script uses the `argparse` library to parse command-line arguments.
   
2. **Readme Function:**
   The `readme` function displays the readme notes describing available filter functions.
   
3. **Filter Creation Function:**
   The `create_filter_from_ips_file` function reads IP addresses from the specified file and constructs a syslog-ng filter rule based on the provided filter function and logical operator.

### Additional Information

- Ensure the IP addresses in the file are listed one per line.
- The logical operator can be `or`, `and`, or any other valid logical operator supported by syslog-ng.
- The filter function can be any valid function used in syslog-ng filters (e.g., `netmask`, `host`, `program`).

By following this guide, users can effectively use the IP Filter Script to create custom syslog-ng filter rules based on IP addresses listed in a file.
