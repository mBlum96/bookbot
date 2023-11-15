

def count_characters(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

# create main function
def main():
    with open("frankenstein.txt", "r") as f:
        file_content = f.read()
        char_count = count_characters(file_content)
        
    char_count_list = [(char, count) for char, count in char_count.items()]
    char_count_list.sort(key=lambda x: x[1], reverse=True)
    word_count = len(file_content.split())
    print(f"{word_count} words found in the document\n")
    for char, count in char_count_list:
        print(f"\nThe '{char}' character was found {count} times")

# call main function
if __name__ == "__main__":
    main()