WITH raw_gold AS (
    SELECT *
    FROM {{ source('data_engineer_project', 'Gold_Ranked_Players') }}
),
stg_gold AS (
    SELECT
        "leagueId" AS league_id,
        wins,
        losses,
        veteran,
        inactive,
        "freshBlood" AS fresh_blood,
        "hotStreak" AS hot_streak,
        CURRENT_TIMESTAMP AS loaded_at
    FROM raw_gold
)
SELECT *
FROM stg_gold