import csv
import os

def main():
    directory = 'workset/'
    these_results = []
    for subdir in os.listdir(directory):
        f = os.path.join(directory, subdir)
        print(f)
        if os.path.isdir(f):
            print(f)
            file_name = f.split('/')[1]
            infile_name = str(f)+"/"+file_name +".txt"
            these_results.append(gets_funding_data(infile_name, "copyright"))
    print(these_results)
    makes_results_csv(these_results, "results.csv")


# deprecated version of gets funding data that returns results as a list of strings instead of a massive string 
# def gets_funding_data(infile_name, search_term):
#     #need a try/ except block here 
#     infile = open(infile_name, 'r')
#     # turn the whole thing into one big list
#     lines = infile.read().splitlines()
#     i = 0
#     hits = []
#     results = []
#     for line in lines:
#         if search_term.lower() in line.lower():
#             print('found in line:', i, line)
#             hits.append(i)
#         i += 1
#     print(hits)
#     for hit in hits:
#         print(lines[(hit - 5):(hit + 20)])
#         result = (lines[(hit - 5):(hit + 20)])
#         results.append({'volume': infile_name, 'line' : hit, 'text':result})
#     headers = ['volume','line', 'text']
#     rows = results
#     return rows


def gets_funding_data(infile_name, search_term):
    infile = open(infile_name, 'r')
    # turn the whole thing into one big list
    lines = infile.read().splitlines()
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
        print(lines[(hit - 10):(hit + 10)])
        result = (lines[(hit - 5):(hit + 5)])
        result_string = ""
        for item in result:
            result_string = result_string + " " + item
        result_string = re.sub("\\\\", "", result_string)
        results.append({'volume': infile_name, 'line' : hit, 'text':result_string})
    headers = ['volume','line', 'text']
    rows = results
    return rows



def makes_results_csv(results, outfile_name):
    headers = ['volume', 'line', 'text']
    rows = results
    print(type(rows))
    with open(outfile_name, 'w', encoding='UTF-8', newline= '') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerows(row)


main()
