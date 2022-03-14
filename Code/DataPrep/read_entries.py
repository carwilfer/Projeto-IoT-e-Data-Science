import time as t
import re



def read_last_entries(current_line=0):
    with open("./Data/Raw/NYC_Motor.csv","r") as entries:
        entries.seek(current_line)
        for line in entries:
            yield line

def filter_content(line, pattern="PERSON_INJURY"): 
    if re.search(pattern,line):
        value = re.search(r"\d+\.\d+",line).group(0)
        return float(value)
    return None

if __name__ == "__main__":
    read_from_line = 0
    while True:
        for idx, line in enumerate(read_last_entries(current_line=read_from_line)):
            content = filter_content(line)
            if content:
                print(content)
        read_from_line = idx
        t.sleep(4)

