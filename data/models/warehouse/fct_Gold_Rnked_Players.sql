WITH deduped AS (
    SELECT
        * ,
        ROW_NUMBER() OVER (
            PARTITION BY league_id
            ORDER BY league_id
        ) AS row_num
    FROM {{ ref('stg_Gold_Ranked_Players') }}
)
SELECT
    league_id,
    wins,
    losses,
    veteran,
    inactive,
    fresh_blood,
    hot_streak
FROM deduped
WHERE row_num = 1

