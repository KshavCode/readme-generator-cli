from fastapi import FastAPI
import os

app = FastAPI()

# TESTING
@app.get("/")
async def root():
    print("Hi there! The server is running.")
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


@app.get("/generate")
async def generate(title: str = None, description: str = None, languages: str = "", packages: str = "", guide: str = "", plans: str = "None"):
    """Accepts query parameters and writes a README into the READMEs/ folder.
    Example: /generate?title=MyProj&description=...&languages=Python,JS&packages=fastapi;react&guide=...&plans=None
    """
    if not title:
        return {"success": False, "error": "missing title"}

    # parse languages and packages
    languages_list = [s.strip() for s in languages.split(",")] if languages else []
    packages_list = [s.strip() for s in packages.split(";")] if packages else []

    if plans == "None":
        plans = "No Plans currently!"

    packs = []
    # pair languages and packages by index, ignore mismatches gracefully
    for i in range(min(len(languages_list), len(packages_list))):
        packs.append(f"{languages_list[i]}: {packages_list[i]}")

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
    with open(f"READMEs/{title}.md", "w", encoding="utf-8") as f :
            f.write(TotalString)

    return {
                "success": True,
                "title": title,
                "description": description,
                "plan": plans,
                "language_pack_str": language_pack_str,
                "message": f"Wrote READMEs/{title}.md"
            }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
