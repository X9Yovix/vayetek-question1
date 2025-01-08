def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_data(data):
    return data.split('\n')

def handle_values():
    data = read_from_file('document.txt')
    extracted_data = extract_data(data)
    result=[]
    for line in extracted_data:
        first=0
        last=0
        found=False
        for char in line:
            try:
                int(char)
                if (int(char)>=1 and int(char)<=9):
                    if first==0:
                        found=True
                    if found:
                        first=int(char)
                        found=False
                    last=int(char)
            except:
                continue
        if first!=0:
            result.append([line,first,last])
    return result

def main():
    result = handle_values()
    calibration = 0
    for i in range(len(result)):
        concatValues = (str(result[i][1]) + str(result[i][2]))
        calibration += int(concatValues)
    
    if(calibration>0):
        print("résultat attendu: ",calibration)

main()