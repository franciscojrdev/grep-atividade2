import re
import os
from multiprocessing import Pool

def mapper(file_part, pattern):
    matched_lines = []
    with open(file_part, 'r') as f:
        for line in f:
            if re.search(pattern, line):
                matched_lines.append(line.strip())
    return matched_lines

def reducer(matched_lines):
    return matched_lines

def grep(pattern, file_parts):
    pool = Pool()
    results = pool.starmap(mapper, [(part, pattern) for part in file_parts])
    matched_lines = []
    for result in results:
        matched_lines.extend(result)
    matched_lines.sort()
    return matched_lines

if __name__ == "__main__":
    file_parts = ["file_1.txt", "file_2.txt","file_3.txt","file_4.txt"] 
    
    pattern = input("Digite o padrão de busca: ")

    matched_lines = grep(pattern, file_parts)

    output_filename = "arquivo.txt"
    with open(output_filename, 'w') as f:
        for line in matched_lines:
            f.write(line + '\n')

    print(f"Resultado salvo em {output_filename}")
