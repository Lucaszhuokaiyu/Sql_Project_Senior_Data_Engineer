WITH base AS ( 
    SELECT *
    FROM {{ ref('fct_Active_Players') }}
)
SELECT
    month,
    avg_monthly_players,
    monthly_gain_loss,
    peak_players,
    CURRENT_TIMESTAMP AS loaded_at
FROM base


