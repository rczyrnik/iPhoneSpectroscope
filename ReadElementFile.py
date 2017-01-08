'''
To read in the file Elementfile.txt,
each line in the file is an element followed by some major peaks
it returns a dictionary where the key's are elements
and the items are lists of wavelengths
'''

def ReadElementFile():
    elements = {}
    for line in open('ElementFile.txt'):
        columns = line.split()
        name = columns[0]
        i = 1
        wavelengths = []
        while i < len(columns):
            wavelengths.append(float(columns[i]))
            i += 1
        elements[name] = wavelengths
    return elements

if __name__ == '__main__':
    ReadElementFile()
