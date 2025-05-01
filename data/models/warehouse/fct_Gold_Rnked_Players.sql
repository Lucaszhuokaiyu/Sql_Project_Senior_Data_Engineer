WITH source AS (
    SELECT * FROM {{ ref('stg_Gold_Ranked_Players') }}
)
SELECT
    league_id,
    wins,
    losses,
    veteran,
    inactive,
    fresh_blood 
    hot_streak,
    CURRENT_TIMESTAMP AS loaded_at
FROM source
