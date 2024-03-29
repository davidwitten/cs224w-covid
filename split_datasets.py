from tqdm import tqdm

def convert_date(line):
    date = line[0:10].replace('-', '')
    new_line = date
    for i in range(10, len(line)):
        new_line += line[i]
    return new_line

def get_training_dataset(data_2021_path, data_2022_path):
    with open('training_dataset.csv', 'w') as f:
        data_2021 = open(data_2021_path, 'r').readlines()
        data_2022 = open(data_2022_path, 'r').readlines()

        for line in tqdm(data_2021):
            f.write(convert_date(line))
        f.write('\n')
        for line in tqdm(data_2022[1:589053]): # 589054 is index for first 07 2022 data
            f.write(convert_date(line))

def get_validation_dataset(data_2022_path):
    with open('validation_dataset.csv', 'w') as f:
        data_2022 = open(data_2022_path, 'r').readlines()

        for line in tqdm(data_2022[589053:]):
            f.write(convert_date(line))

def get_testing_dataset(data_2023_path):
    with open('testing_dataset.csv', 'w') as f:
        data_2023 = open(data_2023_path, 'r').readlines()

        for line in tqdm(data_2023):
            f.write(convert_date(line))

if __name__ == '__main__':
    get_training_dataset('us-counties-2021.csv', 'us-counties-2022.csv')
    get_validation_dataset('us-counties-2022.csv')
    get_testing_dataset('us-counties-2023.csv')
