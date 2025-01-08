def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_data(data):
    return data.split('\n')

def main():
    data = read_from_file('doc.txt')
    extracted_data = extract_data(data)
    #print(extracted_data)
    result=[]
    for line in extracted_data:
        print(line)
        first=0
        last=0
        found=False
        for char in line:
            try:
                int(char)
                #print('this is a number and', end=" ")
                if (int(char)>=1 and int(char)<=9):
                    #print('in range')
                    if first==0:
                        found=True
                    if found:
                        first=int(char)
                        found=False
                    last=int(char)
                #else:
                    #print('exceeds the limit')
            except:
                #print('this is not a number')
                continue
        if first!=0:
            result.append([first,last])
    #print(result)
    for i in range(len(result)):
        print(f"{result[i]}: {result[i][0] + result[i][1]}")
        print()


main()