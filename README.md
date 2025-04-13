## Description
Developed a GUI-based Website Blocker using Python and Tkinter to efficiently block or unblock access to websites by modifying the system's hosts file. This tool is ideal for implementing parental controls, improving productivity, or managing access to inappropriate or distracting websites. It supports both Windows and Linux platforms and includes proper error handling for permission-related issues.

## Run 

To run the application, execute:
```bash
python websiteblocker.py
```

- Note: Administrator/root privileges are required to modify the hosts file.
- On Windows: Run the terminal or Python interpreter as Administrator.
- On Linux: Use `sudo python3 websiteblocker.py`


## Usage

### Block

- Click on the "Block" button from the main interface.
- View the current list of blocked websites.
- Use the "Add New" button to enter a new URL to block.
- URLs are validated before being added and redirected to `127.0.0.1`.

### Unblock

- Click on the "Unblock" button from the main interface.
- View a list of currently blocked websites.
- Click the "X" button next to any site to unblock it.

## Hosts File Location

| OS      | Hosts File Path                              |
|---------|----------------------------------------------|
| Windows | `C:\Windows\System32\drivers\etc\hosts`      |
| Linux   | `/etc/hosts`                                 |

## Permissions

This application modifies the system's hosts file. Ensure you have the necessary permissions:

- On Windows: Run the script as Administrator
- On Linux: Use `sudo` to execute the script

If the application encounters a `PermissionError`, it will display a warning message and exit gracefully.



## Credits

- [Sameer singh bhandari](https://github.com/xtrimDev)
