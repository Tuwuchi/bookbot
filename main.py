def main():
    with open("C:/Users/Trey/workspace/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        
    
        char_count = count_characters(file_contents)
        
    
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print("\n")
        print("--- Character count ---")
        
        for char in sorted(char_count.keys()):
            if char.isalpha():
                print(f"The '{char}' character was found {char_count[char]} times")
                
        print("--- End report ---")

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1 
        else:
            char_counts[char] = 1
    return char_counts

if __name__ == "__main__":
    main()