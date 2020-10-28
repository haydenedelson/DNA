from sys import argv, exit
import csv

# argv[2] = .csv containing STR counts for a list of individuals
# argv[3] = .txt containing DNA sequence to identify

# Check arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Open database
dna_database = open(argv[1], newline='')

# Get sequences from database header
target_sequences_txt = dna_database.readline().rstrip()
fieldnames = target_sequences_txt.split(',')
sequence_dict = dict.fromkeys(fieldnames[1:], 0)

# Reset tracker to beginning of file
dna_database.seek(0)

# Create database reader
data_dict = csv.DictReader(dna_database)

# Open Sequence
individual_file = open(argv[2])
individual_reader = individual_file.read()

# Iterate over each nucleotide in the individual's DNA sequence
# For each nucleotide, check if it == the beginning nucleotide in any of the target sequences
# If yes, count the number of repetitions of each of those target sequences
# If the number of repetitions > current repetition count, overwrite current repeitition count
sequences = fieldnames[1:]
for i in range(len(individual_reader)):
    for curr_sequence in sequences:
        if individual_reader[i] == curr_sequence[0]:
        # Count number of repetitions of current sequence
            j = i
            curr_reps = 0
            sequence_length = len(curr_sequence)
            while individual_reader[j:j + sequence_length] == curr_sequence:
                curr_reps += 1
                j += sequence_length
            if curr_reps > sequence_dict[curr_sequence]:
                sequence_dict[curr_sequence] = curr_reps


num_sequences = len(sequences)
# For each person in the database
# Compare their STRs to the STRs in the current sequence_dict
# If they are the same, print the individual's name
for entry in data_dict:
    match = True
    for i in range(num_sequences):
        if (int(entry[sequences[i]]) != int(sequence_dict[sequences[i]])):
            match = False
            break
    if match == True:
        print(entry['name'])
        break
    
if match == False:
    print("No Match")

individual_file.close()
dna_database.close()
