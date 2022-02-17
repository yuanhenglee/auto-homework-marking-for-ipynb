import os
import sys

fileTypes = ['.ipynb', '.py']

def handle_ipynb( file ):
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    outputFilename = '%s.output' % filename
    errFilename = '%s.err' % filename
    outputFilePath = os.path.join(path, outputFilename)
    errFilePath = os.path.join(path, errFilename)
    print("RUN:\n runipy "+file+" > "+outputFilePath+" 2> "+errFilePath)
    os.system("runipy "+file+" > "+outputFilePath+" 2> "+errFilePath)



if __name__ == '__main__':
    try:
        codeDir = sys.argv[1]
        outputDir = sys.argv[2]
    except:
        raise Exception("Usage: python3 codeRootDirectory")
    if len(sys.argv) >= 4:
        if sys.argv[3] == '--type':
            fileTypes = sys.argv[4:]

    print("code dir:",codeDir)

    for root, dirs, files in os.walk(codeDir):
        print( "Dir: ", root)
        for filename in files:
            filePath = os.path.join(root, filename)
            os.rename( filePath, filePath.encode('utf-8') )
            if os.path.splitext(filePath)[1] in fileTypes:
                print("└ Match file: ", filePath)
                if os.path.splitext(filePath)[1] == '.ipynb':
                    handle_ipynb(os.path.abspath(filePath))

            else:
                print("└ Unknown file: ", filePath)


    # os.system('python file.py')