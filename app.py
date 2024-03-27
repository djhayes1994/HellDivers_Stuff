import helldivers

hd = helldivers.helldivers()

campaigns = hd.campaigns(major_order=False)

if campaigns != [] and "ERROR:" not in campaigns:
    for campaign in campaigns:
        name = campaign['name']
        faction = campaign['faction']
        description = campaign['biome']['description']

        output = f"""
Name: {name}
Faction: {faction}
Message: {description}
"""
        print(output)

elif campaigns == []:
    print(f"No active planets found that match the criteria")
else:
    print(f"Something is wrong with the code and we could not grab current campaign info on planets. Error if provided: {campaigns}")