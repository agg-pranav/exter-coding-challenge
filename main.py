import tracemalloc
import csv
import os
import time
  

def create_set(file_name):
    ret = set()
    with open(file_name) as f:
        for line in f:
          ret.add(line.strip())
    return ret

def create_dict(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        d = dict(reader)
    return d

def main(text_file, french_dict, find_words):
    wc = dict()
    out_file = open('t8.shakespeare.translated.txt', 'w')
    with open(text_file) as tf:
      for line in tf:
        out = []
        l = line.split().copy()
        for word in l:
          if word in find_words:
            if word in wc: wc[word] += 1
            else:wc[word] = 1
            out.append(french_dict[word])
          else: 
            out.append(word)
        out_file.write(' '.join(out) + '\n')
    out_file.close()

    with open('frequency.csv', 'w') as f:
      f.write('English Word,French Word,Frequency\n')
      for key, value in wc.items():
        f.write("{},{},{}\n".format(key,french_dict[key], value))
      
        

if __name__ == '__main__':
    start_time = time.time()
    tracemalloc.start()

    french_dict = create_dict('french_dictionary.csv')
    find_words = create_set('find_words.txt')
    text_file = 't8.shakespeare.txt'
    translated_words_count = main(text_file, french_dict, find_words)
    
    end_time = time.time()
    with open('performance.txt', 'w') as f:
      f.write(f'Time to process: {end_time - start_time} seconds\n')
      f.write(f"Memory used: {(tracemalloc.get_traced_memory()[1] - tracemalloc.get_traced_memory()[0])*512/1000000} MB\n")