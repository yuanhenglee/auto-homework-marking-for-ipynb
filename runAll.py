import os
import sys

fileTypes = ['.ipynb', '.py']
codeDir = ''
inputDir = ''

def handle_file( file ):
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]

    outputFilename = '%s.output' % filename
    errFilename = '%s.err' % filename
    txtFilename = '%s.txt' % filename

    outputFilePath = os.path.join(path, outputFilename)
    errFilePath = os.path.join(path, errFilename)
    txtFilePath = os.path.join(path, txtFilename)

    if os.path.splitext(file)[1] == '.ipynb':
        os.system("jupyter nbconvert --to script " + file)
        cmd = "python3 "+ txtFilePath + " < " + inputDir + " > " + outputFilePath + " 2> " + errFilePath
    elif os.path.splitext(file)[1] == '.py':
        cmd = "python3 "+file + " < " + inputDir + " > " + outputFilePath + " 2> " + errFilePath
    os.system(cmd)



if __name__ == '__main__':
    try:
        codeDir = sys.argv[1]
        inputDir = sys.argv[2]
    except:
        raise Exception("Usage: python3 runAll.py codeDir inputDir")

    print("code dir:",codeDir)

    for root, dirs, files in os.walk(codeDir):
        print( "Dir: ", root)
        for filename in files:
            filePath = os.path.join(root, filename)
            os.rename( filePath, filePath.encode('utf-8') )
            if os.path.splitext(filePath)[1] in fileTypes:
                print("└ Match file: ", filePath)
                handle_file(os.path.abspath(filePath))

            else:
                print("└ Unknown file: ", filePath)


    # os.system('python file.py')