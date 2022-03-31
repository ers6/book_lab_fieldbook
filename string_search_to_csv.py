# this file searches for a string in a text file, scrapes the lines surrounding that string, and appends the results to a csv file. Will be used to scrape funding info from Hathi 
import csv
import re

def main():
    search_term = 'pickle'
    infile_name = 'data/testing.txt'
    infile = open(infile_name, 'r')
    # turn the whole thing into one big list
    lines = infile.read().splitlines()
    results = get_results(lines, search_term)
    makes_results_csv(results)



def get_results(lines, search_term):
    i = 0
    hits = []
    results = []
    for line in lines:
        if search_term.lower() in line.lower():
            print('found in line:', i, line)
            hits.append(i)
        i += 1
    print(hits)
    for hit in hits:
        print(lines[(hit-10):(hit+10)])
        result = (lines[(hit-5):(hit+5)])
        results.append({'line' : hit, 'text':result})
    return results


def makes_results_csv(results):
    headers = ['line', 'text']
    rows = results
    with open('data/table.csv', 'w', encoding='UTF-8', newline= '') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


main()

