'''
Project: Parse Logs for Reachability Statistics 

Objectives:

1. Create a script that:
    - Pings multiple hosts.
    - Saves the output to a log file.

2. Parses the log file to:
    - Count the number of sucessful and failed pings
    - Identify the hosts that were unreachable 


Key Concepts I'm Practicing 

- File I/O (reading and writing logs).
- String parsing and data manipulation.
- Combining subprocesses and log analysis. 


Externsions for More Practice

- Log the results to a file for later review

- Add a retry mechanism for unreachable hosts

- Accept hosts from a file rather than user input 
'''
import subprocess # Import the subprocess module to run external commands (like ping)

def ping_host(host):
    "Ping a host and return the output status."

    try:
        #Run the 'ping' command for the given host. '-n 1' sends 1 ping packet
        result = subprocess.run(
            ["ping", "-n", "1", host], # Command and arguments.
            stdout=subprocess.PIPE,    # Caputure the standard output. 
            stderr=subprocess.PIPE,    # Capture the standard error output
            text=True                  # Return the output as a string (instead of bytes) 
        )
        return result.stdout, result.returncode == 0 # Return the command's output and success status.
    except Exception as e:
        # Return an error message and a failure status if the ping fails unexpectedly.
        return f"Error pinging {host}: {e}", False 
