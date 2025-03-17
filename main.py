import os
class ReadMeGenerate:
    def checkExist() :
        fileName = "README"
        if os.path.exists(f"{fileName}.md") : 
            c = 1 
            while os.path.exists(f"{fileName+str(c)}.md") :
                c += 1
            fileName += str(c)
        return fileName
        
    @classmethod
    def createFile(cls):
        fileName = cls.checkExist()
        title = input("Project Name: ")
        desc = input("Project Description: ")
        package = input("Package(s) Name: ")
        codeVersion = input("Code Version (OPTIONAL): ")
        if not codeVersion: 
            codeVersion = "3.8.10"
        plan = input("Future Plans: ")
        guide = input("Installation Guide: ")
        
        TotalString = f'''# {title}
{desc}

## Required Package(s)
Python Version Used: {codeVersion}\n
{package}
```bash
pip install {package}
```

## Installation Guide
{guide}

## Future Plans
{plan}
'''
        
        addColumn = input("Enter more sub-Titles? (y/n, default n): ")
        while addColumn.lower()=="y":
            subTitle = input("Sub-Title: ")
            addDescription = input(f"Description for {subTitle}: ")
            TotalString += f"\n\n## {subTitle}\n{addDescription}"
            addColumn = input("Enter more sub-Titles? (y/n, default n): ")
        
        with open(f"{fileName}.md", "w") as f :
            f.write(TotalString)
        return f"Stored in {fileName}.md"
if __name__ == "__main__":
    choice = "y"
    while choice.lower()=="y":
        ReadMeGenerate.createFile()
        choice = input("Continue? (y/n, default n): ")
    