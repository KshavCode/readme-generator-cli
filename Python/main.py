import os, json
from time import sleep

class ReadMeGenerate:
    def __init__(self):
        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists("data/data.json"):
            with open("data/data.json", "w") as f:
                text_format = {'languages': ['Python', 'Javascript', 'HTML', 'CSS'], 'Python': ['None', 'Flask', 'Pandas', 'OpenCV', 'Numpy', 'Matplotlib', 'Pillow', 'Plotly', 'Seaborn', 'JSON', 'Requests', 'Django'], 'Javascript': ['None', 'React'], 'HTML': ['None', 'Bootstrap'], 'CSS': ['None', 'Tailwind']}
                json.dump(text_format, f, indent=2)
    def read_data(self) :
        with open("data/data.json", "r") as f:
            data = json.load(f)
        return data
    
    def createFile(self):
        title = input("Project Name: ")
        desc = input("Project Description: ")
        while True: 
            data = self.read_data()
            for idx, lang in enumerate(data['languages']):
                print(f"{idx+1} - {lang}")
            language = input("Language(s) Used (use commas if multiple or type 0 to add langs): ")
            if language=="0":
                newLang = input("New Language Name: ").title()
                data['languages'].append(newLang)
                data[newLang] = []
                with open("data/data.json", "w") as f:
                    json.dump(data, f, indent=2)
                print(f"New Language {newLang} Added Successfully!")
                sleep(1)
            else : 
                break
        language = language.split(",")
        language = [data['languages'][int(langidx)-1] for langidx in language]
        packages = {}
        for lang in language:
            while True: 
                data = self.read_data()
                for idx, pack in enumerate(data[lang]):
                    print(f"{idx+1} - {pack}")
                package = input(f"Package(s) Used in {lang} (use commas if multiple or type 0 to add langs): ")
                if package=="0":
                    newPack = input("New Package Name: ").title()
                    data[lang].append(newPack)
                    with open("data/data.json", "w") as f:
                        json.dump(data, f, indent=2)
                    print(f"Package '{newPack}' Added In {lang} Successfully!")
                    sleep(1)
                else : 
                    break
            package = package.split(",")
            packages[lang] = [data[lang][int(packidx)-1] for packidx in package]
        lang_pack_str = "\n".join([f"{lang}: " + ", ".join(packages[lang]) for lang in packages])
        plans = []
        while True: 
            plan = input("Future Plans (leave empty when done): ")
            if plan.strip()=="":
                break
            else:
                plans.append(plan)
        plans = "\n".join([f"{idx+1}. {plan}" for idx, plan in enumerate(plans)])
        guide = input("Installation Guide: ")
        TotalString = f'''# {title}
{desc}

## Language & Package Used
{lang_pack_str}

## Installation Guide
{guide}

## Future Plans
{plans if plans.strip()!="" else "No Future Plans Yet!"}
'''
        
        addColumn = input("Enter more Titles? (y/n, default n): ")
        while addColumn.lower()=="y":
            subTitle = input("Sub-Title: ")
            addDescription = input(f"Description for {subTitle}: ")
            TotalString += f"\n\n## {subTitle}\n{addDescription}"
            addColumn = input("Enter more sub-Titles? (y/n, default n): ")
        with open(f"{title}.md", "w") as f :
            f.write(TotalString)
        return None
    
if __name__ == "__main__":
    choice = "y"
    obj = ReadMeGenerate()
    while choice.lower()=="y":
        obj.createFile()
        choice = input("Continue? (y/n, default n): ")
    