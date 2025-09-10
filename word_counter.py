def word_counter(filename):
    try:
        # File ni open cheyadam
        with open(filename, 'r') as file:
            content = file.read()
        
        # Content ni words ga split cheyadam
        words = content.split()
        
        # Words count
        count = len(words)
        
        print(f"Total number of words in {filename}: {count}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")

# Example usage
filename = "sample.txt"
word_counter(filename)
