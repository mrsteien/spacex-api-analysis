import pandas as pd
import requests 

def get_launch_data(): #launch_df
    # Fetch data
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
    # Extract relevant fields
        return pd.DataFrame([{
            "launch_name": launch["name"],
            "date": launch["date_utc"],
            "success": launch["success"],
            "rocket_id": launch["rocket"],
            "payloads": len(launch["payloads"]),
            "launchpad_id": str(launch["launchpad"])
        } for launch in launches])   
    else:
        print("Error fetching data:", response.status_code)
        return pd.DataFrame()


def get_rocket_data(): #rocket_df

    all_rockets_url = f"https://api.spacexdata.com/v4/rockets"
    response = requests.get(all_rockets_url)
    if response.status_code == 200:
        rockets = response.json()
        return pd.DataFrame([{
            "rocket_id": rocket["id"]
            ,"rocket_name": rocket["name"]
        } for rocket in rockets])
    else:
        print("Error fetching rocket data:", response.status_code)
        return pd.DataFrame()
    
    
def get_launchpad_data(): #launchpad_df
    launchpads_url = "https://api.spacexdata.com/v4/launchpads"

    response = requests.get(launchpads_url)
    if response.status_code == 200:
        launchpads = response.json()

        return pd.DataFrame([{
            "launchpad_id": pad["id"]
            ,"launchpad_name": pad["name"]
            ,"launchpad_location": pad["locality"]
        } for pad in launchpads ])
    else:
        print("Error fetching launchpad data:", response.status_code)
        return pd.DataFrame()

#df = df.merge(launchpad_df, on="launchpad_id", how="left").dropna()