
def count_words_in_file(filename):
    word_counts = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                # Remove non-alphabetic and non-digit characters using join
                cleaned = ''.join([c for c in word if ('a' <= c <= 'z') or ('0' <= c <= '9')])
                if cleaned:
                    if cleaned in word_counts:
                        word_counts[cleaned] += 1
                    else:
                        word_counts[cleaned] = 1
    for word in sorted(word_counts):
        print(word + ":", word_counts[word])

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    count_words_in_file(filename)




