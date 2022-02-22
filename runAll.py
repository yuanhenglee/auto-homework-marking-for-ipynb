import os
import sys

fileTypes = ['.ipynb', '.py']
codeDir = ''
inputDir = ''
outputDir = ''

def appendToFile( outputDir, txt ):
    print("echo \"" + txt + "\" >> " + outputDir)
    os.system("echo \"" + txt + "\" >> " + outputDir )

def runSingleFile(fileDir, inputDir = inputDir, outputDir = outputDir):
    path, file = os.path.split(fileDir)
    filename = os.path.splitext(file)[0]
    fileType = os.path.splitext(file)[1]

    if fileType == '.ipynb':
        os.system("jupyter nbconvert --to script " + fileDir)
        fileDir = os.path.join(path, filename + ".txt")

    codeFile = open(fileDir, 'r')
    inputFile = open(inputDir, 'r')
    outputFile = open(outputDir, 'w')


    appendToFile( outputDir, "#"*5 + "source code start" + "#"*5 )
    os.system("cat " + fileDir + " >> " + outputDir)
    appendToFile( outputDir, "#"*5 + "source code end" + "#"*5 )
    
    appendToFile( outputDir, "#"*5 + "output" + "#"*5 )
    os.system("python3 "+ fileDir + " < " + inputDir + " >> " + outputDir + " 2>&1 ")
    appendToFile( outputDir, "#"*5 + "output" + "#"*5 )


if __name__ == '__main__':
    try:
        codeDir = sys.argv[1]
        inputDir = sys.argv[2]
        outputDir = sys.argv[3]
    except:
        raise Exception("Usage: python3 runAll.py codeDir inputDir outputDir")

    print("code dir:",codeDir)

    runSingleFile(codeDir, inputDir, outputDir)
    # for root, dirs, files in os.walk(codeDir):
    #     print( "Dir: ", root)
    #     for filename in files:
    #         filePath = os.path.join(root, filename)
    #         os.rename( filePath, filePath.encode('utf-8') )
    #         if os.path.splitext(filePath)[1] in fileTypes:
    #             print("└ Match file: ", filePath)
    #             handle_file(os.path.abspath(filePath))

    #         else:
    #             print("└ Unknown file: ", filePath)


    # os.system('python file.py')