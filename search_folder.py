#############################################################
#
#   This script searches a folder for a string.
#   After executing the script, it will ask for the string
#   to search. Afterwards it will generate a file called
#   "search_folder_results.txt" in the folder where you executed
#   the script.
#
############################################################

import os

excluded_dirs = [
    ".svn",
    ".vsobj",
    "bin",
    "obj",
    "$RECYCLE.BIN",
    "wwwroot",
]
excluded_file_types = [
    ".cache",
    ".dll",
    ".exe",
    ".svg",
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf"
]
result_file = os.path.join(os.getcwd(), "search_folder_results.txt")


def search_in_file(file_path, search_text):
    """Search for the given text in a single file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if search_text.lower() in line.lower():
                    result = f"     Match found in {file_path} at line {line_number}: {line.strip()}"
                    print(result)
                    with open(result_file, "a", encoding="utf-8") as rf:
                        rf.write(result.strip() + "\n\n")
    except (UnicodeDecodeError, IOError):
        pass


def search_in_directory(directory, search_text, excluded_dirs):
    """Recursively search through all files in the directory for the given text, excluding specified directories."""
    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file_name in files:
            if any(file_name.endswith(ext) for ext in excluded_file_types):
                continue
            file_path = os.path.join(root, file_name)
            print(f"Searching in {root}...")
            search_in_file(file_path, search_text)


def main():
    directory = input("Enter folder path: ").strip()
    directory = os.path.normpath(directory)
    if not os.path.exists(directory):
        print("The path doesn not exist")
        return

    search_text = input("Enter search text: ").strip()
    if search_text == "":
        print("Please enter a valid search string")
        return

    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    # Clear the result file if it exists
    with open(result_file, "w", encoding="utf-8") as rf:
        rf.write("")

    search_in_directory(directory, search_text, excluded_dirs)
    print("Finished searching...")


if __name__ == "__main__":
    main()
