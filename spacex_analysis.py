import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {url}: {response.status_code}")
        return []

def process_launches(launches):
    return pd.DataFrame([{
        "launch_id": launch["id"],
        "name": launch["name"],
        "date": launch["date_utc"],
        "success": launch["success"],
        "rocket_id": launch["rocket"],
        "launchpad_id": launch["launchpad"],
        "payloads": len(launch["payloads"])
    } for launch in launches])

def process_rockets(rockets):
    return pd.DataFrame([{
        "rocket_id": rocket["id"],
        "rocket_name": rocket["name"]
    } for rocket in rockets])

def process_launchpads(launchpads):
    return pd.DataFrame([{
        "launchpad_id": str(pad["id"]),
        "launchpad_name": pad["name"],
        "launchpad_location": pad["locality"]
    } for pad in launchpads])

def merge_data(df, rockets_df, launchpad_df):
    df = df.merge(rockets_df, on="rocket_id", how="left")
    df = df.merge(launchpad_df, on="launchpad_id", how="left")
    return df

def analyze_success(df):
    success_rate = df["success"].value_counts(normalize=True) * 100
    print("Successful launches:", success_rate.get(True, 0), "%")
    print("Failed launches:", success_rate.get(False, 0), "%")
    return success_rate

def plot_success(success_rate):
    success_rate.plot(kind='bar', color=['green', 'red'])
    plt.title('SpaceX Launch Success Rate')
    plt.xlabel('Launch Outcome')
    plt.ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('data/success_rate.png')
    plt.show()

def main():
    # API URLs
    launches_url = "https://api.spacexdata.com/v4/launches"
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    launchpads_url = "https://api.spacexdata.com/v4/launchpads"

    # Fetch data
    launches = fetch_data(launches_url)
    rockets = fetch_data(rockets_url)
    launchpads = fetch_data(launchpads_url)

    # Process data
    df = process_launches(launches)
    rockets_df = process_rockets(rockets)
    launchpad_df = process_launchpads(launchpads)

    # Merge data
    df = merge_data(df, rockets_df, launchpad_df)

    # Save to CSV
    df.to_csv("data/spacex_launches.csv", index=False)

    # Analysis
    success_rate = analyze_success(df)

    # Visualization
    plot_success(success_rate)

if __name__ == "__main__":
    main()
