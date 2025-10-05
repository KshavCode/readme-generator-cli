from fastapi import FastAPI
import os

app = FastAPI()

# TESTING 
@app.get("/")
async def root():
    return {"message": f"SERVER IS RUNNING at {os.getcwd()}"}

@app.get("/title={title}&description={description}&languages={languages}&packages={packages}&guide={guide}&plans={plans}")
async def root(title, description, languages:str, packages, guide, plans):
    languages = languages.strip().split(",")
    packages = packages.split(";")
    if plans=="None": 
        plans = "No Plans currently!"
    packs =[f'{languages[num]}: {packages[num]}' for num in range(len(languages))]
    language_pack_str = ";".join(packs)
    TotalString = f'''# {title}
{description}

## Language & Package Used
{language_pack_str}

## Installation Guide
{guide}

## Future Plans
{plans}
'''
    if not os.path.exists("READMEs") :
        os.mkdir("READMEs")
    with open(f"READMEs/{title}.md", "w") as f :
            f.write(TotalString)
    return {
                "success": True,
                "title": title, 
                "description": description, 
                "plan": plans,
                "language_pack_str": language_pack_str
            }
    
