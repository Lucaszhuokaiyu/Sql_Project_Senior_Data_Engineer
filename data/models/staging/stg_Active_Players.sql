WITH raw_active AS (
    SELECT *
    FROM {{ source('data_engineer_project', 'Active_Players') }}
),
stg_active AS (
    SELECT
        "Month" AS month,
        "Avg Monthly Players" AS avg_monthly_players,
        "Monthly Gain/Loss" AS monthly_gain_loss,
        "Peak Players" AS peak_players,
        CURRENT_TIMESTAMP AS loaded_at
    FROM raw_active
)
SELECT *
FROM stg_active