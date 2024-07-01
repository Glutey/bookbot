def count_characters(file_contents):
    char_counts = {}
    for char in file_contents:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Count characters in a case-insensitive manner
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def generate_report(file_path, word_count, char_counts):
    # Convert dictionary to list of tuples
    char_count_items = list(char_counts.items())
    
    # Sort the list of tuples by count in descending order
    sorted_char_counts = sorted(char_count_items, key=lambda item: item[1], reverse=True)
    
    # Generate the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def book_to_string(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    path_to_file = "/home/tom_linux/workspace/bookbot/books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    # Call the book_to_string function and get the word count
    word_count = book_to_string(file_contents)
    
    # Call the count_characters function to get character counts
    char_counts = count_characters(file_contents)
    
    # Generate the report
    generate_report(path_to_file, word_count, char_counts)

if __name__ == "__main__":
    main()
