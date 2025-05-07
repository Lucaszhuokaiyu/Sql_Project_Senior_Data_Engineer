# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
# 1. Connect to your PostgreSQL database
engine = create_engine('postgresql://postgres:isba_4715@isba-dev-02.cmb4w8cmqb26.us-east-1.rds.amazonaws.com:5432/data_engineer_project')
# %%
# 2. Define your four SQL queries
query1 = """
WITH player_types AS (
    SELECT
        CASE
            WHEN "freshBlood" = 'TRUE' THEN 'New Player'
            ELSE 'Experienced Player'
        END AS player_type,
        wins,
        losses
    FROM raw."Gold_Ranked_Players"
)
SELECT
    player_type,
    COUNT(*) AS player_count,
    ROUND(AVG(wins)::numeric / NULLIF(AVG(losses), 0), 2) AS win_loss_ratio
FROM player_types
GROUP BY player_type
ORDER BY player_type;
"""
query2 = """
WITH new_players AS (
    SELECT 
        "hotStreak",
        wins,
        losses,
        ROW_NUMBER() OVER (PARTITION BY "hotStreak" ORDER BY wins DESC) AS rn
    FROM raw."Gold_Ranked_Players"
    WHERE "freshBlood" = 'TRUE'
),
joined_players AS (
    SELECT a."hotStreak", a.wins, a.losses
    FROM new_players a
    JOIN (SELECT 1 AS dummy) b ON 1 = 1
)
SELECT 
    "hotStreak",
    COUNT(*) AS player_count,
    ROUND(AVG(wins::numeric / NULLIF(losses, 0)), 2) AS avg_win_loss_ratio
FROM joined_players
GROUP BY "hotStreak"
ORDER BY "hotStreak" DESC;
"""
query3 = """
WITH filtered AS (
    SELECT 
        "Month",
        "Avg Monthly Players",
        "Peak Players",
        CASE 
            WHEN "Month" IN ('20-Jan', '20-Feb', '20-Mar', '20-Apr', '20-May', '20-Jun',
                             '20-Jul', '20-Aug', '20-Sep', '20-Oct', '20-Nov', '20-Dec')
                THEN '2020'
            WHEN "Month" IN ('24-Jan', '24-Feb', '24-Mar', '24-Apr', '24-May', '24-Jun',
                             '24-Jul', '24-Aug', '24-Sep', '24-Oct', '24-Nov', '24-Dec',
                             '25-Jan', '25-Feb', '25-Mar', 'Last 30 Days')
                THEN 'Now'
            ELSE 'Other'
        END AS period
    FROM raw."Active_Players"
)
SELECT 
    period,
    ROUND(AVG("Avg Monthly Players")::numeric) AS avg_players,
    ROUND(AVG("Peak Players")::numeric) AS avg_peak_players
FROM filtered
WHERE period IN ('2020', 'Now')
GROUP BY period
ORDER BY period;
"""
query4 = """
WITH ranked_months AS (
    SELECT 
        "Month",
        "Avg Monthly Players",
        "Peak Players",
        ROUND("Avg Monthly Players"::numeric / NULLIF("Peak Players", 0), 2) AS avg_to_peak_ratio,
        ROW_NUMBER() OVER (ORDER BY "Month") AS rn_asc,
        ROW_NUMBER() OVER (ORDER BY "Month" DESC) AS rn_desc
    FROM raw."Active_Players"
)
SELECT "Month", avg_to_peak_ratio
FROM ranked_months
WHERE rn_asc = 1 OR rn_desc = 1
ORDER BY "Month";
"""
# %%
# 3. Execute each query and store in DataFrames
df1 = pd.read_sql(query1, engine)
df2 = pd.read_sql(query2, engine)
df3 = pd.read_sql(query3, engine)
df4 = pd.read_sql(query4, engine)
# %%
# 4. Save each DataFrame as a separate CSV file
df1.to_csv("player_type_win_loss.csv", index=False)
df2.to_csv("hot_streak_comparison.csv", index=False)
df3.to_csv("avg_players_comparison.csv", index=False)
df4.to_csv("avg_to_peak_ratio.csv", index=False)
# %%
print("CSV files exported successfully!")
# %%
import os
print(os.getcwd())


