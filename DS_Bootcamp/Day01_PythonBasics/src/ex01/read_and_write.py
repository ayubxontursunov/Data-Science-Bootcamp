def read_and_write():

    with open('ds.csv', 'r') as infile:

        with open('ds.tsv', 'w') as outfile:

            for line in infile:

                modified_line = line.strip().replace(',', '\t')


                outfile.write(modified_line + '\n')



if __name__ == '__main__':
    read_and_write()
