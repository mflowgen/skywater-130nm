from glob import glob

def write_concat_file(outfilename, infilenames):
    with open(outfilename, 'w') as outfile:
        for fname in infilenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


