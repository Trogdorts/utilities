import os

def count_file_types(folder_path):
    """
    Count the occurrences of each file type (extension) in a folder and its subdirectories.

    Args:
        folder_path (str): The path to the folder to be scanned.

    Returns:
        dict: A dictionary containing file type (extension) counts, sorted by counts in descending order.

    Raises:
        ValueError: If folder_path is not a valid directory.
    """
    if not os.path.isdir(folder_path):
        raise ValueError("Invalid directory path")

    file_type_counts = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension:
                file_type_counts[file_extension] = file_type_counts.get(file_extension, 0) + 1

    # Sort the dictionary by values (counts) in descending order
    sorted_file_type_counts = dict(sorted(file_type_counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_file_type_counts

# Example usage:
if __name__ == "__main__":
    from printing_utils import kvprint
    folder_path = r'Z:\media\audiobooks\all'
    try:
        file_type_counts = count_file_types(folder_path)
        kvprint(file_type_counts)
    except ValueError as e:
        print(f"Error: {e}")
