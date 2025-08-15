from src.fetch import get_launch_data, get_rocket_data, get_launchpad_data
from src.process import transform, summarize_launches

def main():
    # Fetch data
    launches = get_launch_data()
    rockets = get_rocket_data()
    pads = get_launchpad_data()

    # Transform data
    df = transform(launches, rockets, pads)

    # Summarize launches
    summary = summarize_launches(df)

    summary.to_csv("data/summary.csv", index=False)
    print("SpaceX Launch Summary pipeline completed successfully!")
    # Display results
    

if __name__ == "__main__":
    main()