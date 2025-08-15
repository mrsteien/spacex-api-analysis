import pandas as pd

def transform(launches, rockets, pads):
    launches["date"] = pd.to_datetime(launches["date"])
    launches["year"] = launches["date"].dt.year

    # Merge DataFrames
    df = launches.merge(rockets, on="rocket_id", how="left")
    # Merge launchpad data
    df = df.merge(pads, on="launchpad_id", how="left")

    return df

def summarize_launches(df):
    grouped_df = df.groupby(["rocket_name","launchpad_name","year"])
    # Group by rocket name, launchpad name, and year
    # Calculate total launches, successful launches, and success rate
    summary = grouped_df["success"].agg(
        total_launches="count"
        ,successful_launches = lambda x: x.sum()
        ,success_rate=lambda x:(x.sum() / x.count()) * 100
    ).reset_index()

    return summary.sort_values(by="success_rate", ascending=False)