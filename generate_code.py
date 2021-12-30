import argparse
import string
import secrets # important library
from pathlib import Path
import os
import pandas as pd

def output_code(path, length, num):
    # check if the input path is valid or not
    if not (os.path.exists(path) or os.path.isdir(path)):
        raise Exception('The input path is not valid')

    combination = string.ascii_uppercase + string.digits # the code will only contain upper case character and number
    setOfValues = set() # a set avoids duplication whenb adding to it

    if Path(path + 'code.csv').is_file(): # if the output folder already has the code.csv file
        df = pd.read_csv(path + 'code.csv', header=None) # read it to the DataFrame variable
        setOfValues = set(df[0].values.tolist()) # transform the values from DataFrame to the set variable
        # Remove the current csv file
        os.remove(path + 'code.csv')

    while len(setOfValues) < num: # continue adding to the set until the requirement is reached
        # use the secrets library to choose 'length' number of letter/digit from the combination
        code = ''.join(secrets.choice(combination) for i in range(length))
        if (any(c.isdigit() for c in code) and any(c.isalpha() for c in code)):
            # Only add the code if it contains at least 1 number and 1 character
            setOfValues.add(code)

    # convert the set into a list into a DataFrame
    df = pd.DataFrame(list(setOfValues))
    # saving the codes to the .csv file
    df.to_csv(path + 'code.csv', sep=',', encoding='utf-8', index=False, header=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Changing the path of the output.')
    parser.add_argument('-p', help="Change from default path", dest='path', type=str, default='./output/')
    parser.add_argument('-l', help="Length of the code", dest='length', type=int, default=6)
    parser.add_argument('-n', help="Amount of codes output to the .csv file", dest='num', type=int, default=200)
    args = parser.parse_args() # read from command line
    output_code(args.path, args.length, args.num)