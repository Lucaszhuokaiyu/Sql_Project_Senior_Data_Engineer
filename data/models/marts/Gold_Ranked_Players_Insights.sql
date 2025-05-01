-- Selecting total count of players, count the enumber of veteran, inacive, new players, and percentage of each compare to the total. 
WITH base AS (
    SELECT *
    FROM {{ ref('fct_Gold_Ranked_Players') }}
),
aggregated AS (
    SELECT
        COUNT(*) AS total_gold_ranked_players,
        -- Counts
        SUM(CASE WHEN veteran THEN 1 ELSE 0 END) AS veteran_count,
        SUM(CASE WHEN inactive THEN 1 ELSE 0 END) AS inactive_count,
        SUM(CASE WHEN fresh_blood THEN 1 ELSE 0 END) AS new_players_count,
        -- Percentages
        ROUND(
            SUM(CASE WHEN veteran THEN 1 ELSE 0 END)::numeric 
            / NULLIF(COUNT(*), 0), 2
        ) AS pct_veteran_players,
        ROUND(
            SUM(CASE WHEN inactive THEN 1 ELSE 0 END)::numeric 
            / NULLIF(COUNT(*), 0), 2
        ) AS pct_inactive_players,
        ROUND(
            SUM(CASE WHEN fresh_blood THEN 1 ELSE 0 END)::numeric 
            / NULLIF(COUNT(*), 0), 2
        ) AS pct_new_players
    FROM base
)
SELECT * FROM aggregated
