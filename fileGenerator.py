import random
import string

def generate_random_word(alphabet, min_size, max_size):
    word_size = random.randint(min_size, max_size)
    return ''.join(random.choice(alphabet) for _ in range(word_size))

def generate_text(num_words, alphabet, min_size, max_size):
    words = []
    for _ in range(num_words // 3):
        group = ' '.join(generate_random_word(alphabet, min_size, max_size) for _ in range(3))
        words.append(group)
    if num_words % 3 != 0:
        for _ in range(num_words % 3):
            words.append(generate_random_word(alphabet, min_size, max_size))
    return '\n'.join(words)

def file_generator(split, num_words, alphabet, min_size, max_size):
    text = generate_text(num_words, alphabet, min_size, max_size)
    words = text.split('\n')
    chunk_size = len(words) // split

    for i in range(split):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i < split - 1 else len(words)
        file_name = f"file_{i + 1}.txt"

        with open(file_name, 'w') as file:
            file.write('\n'.join(words[start_index:end_index]))

split = 4
num_words = 10000
alphabet = 'acegh'
min_size = 3
max_size = 6

file_generator(split, num_words, alphabet, min_size, max_size)
