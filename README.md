# Minimalist File Organizer
### A simple, portable solution for messy directories.

The Minimalist File Organizer is a standalone tool designed to clean up cluttered folders instantly. Whether you are dealing with a packed Downloads folder or a disorganized project directory, this tool identifies files by their extensions and neatly tucks them into categorized subfolders. 

### How it Works
When you run the executable, the script looks at every file in its current location. It ignores folders and its own program file to avoid loops. It then cross-references each file's extension against a predefined map and moves them into folders like Development, Data, and Media. If a folder doesn't exist yet, the organizer creates it on the spot.

### The Extension Map
The logic is built to handle a wide variety of professional and personal file types:
* **Development**: Handles your source code including Python, C#, and web files.
* **Data**: Manages spreadsheets and database files like CSV and SQLite.
* **Documents**: Sorts PDFs, Word documents, and text files.
* **Images**: Organizes photos and icons including PNG, JPG, and WebP.
* **Media**: Collects audio and video files into one place.
* **Archives**: Cleans up compressed files like ZIP and RAR.
* **System**: Separates executables, batch scripts, and log files.

### Usage Instructions
You do not need to install Python to use this tool if you are using the EXE version. Simply copy the **organizer.exe** file and paste it into the directory you want to organize. Double-click the file to start the process. A terminal window will appear to show you exactly which files are being moved. Once the process is finished, the window stays open so you can review the changes before closing it.

**"Once the process is finished, the window will close automatically, leaving your folder organized and clean."**