# Game Performance Analytics: Player Engagement & Growth Insights
🛠️ Tech Stack
This project applies a full modern data workflow using the following tools:

Python – Data extraction via APIs and web scraping

SQL (PostgreSQL & MySQL) – Data transformation and analytics

AWS RDS – Cloud-hosted databases for scalability and reliability

dbt – Data modeling and transformation automation

GitHub Actions – Workflow orchestration and CI/CD

Looker Studio – Interactive dashboards and visual insights

Jupyter Notebook – EDA, transformation, and data storytelling

🎯 Project Objective
This project is designed to help game data teams and possible stakeholders to visualize game performance, new player growth and engagement trends. 

Problem:
Many multiplayer games face churn from new players due to performance imbalances, and engagement metrics are often misread due to heavy reliance on peak activity rather than sustained usage.

Solution:
Using historical and current data on player activity and ranked behavior, this project identifies what differentiates retained players from those who churn, helping teams:

Improve matchmaking and early player experience

Detect when engagement is driven by events vs. organic usage

Build dashboards to guide game lifecycle decisions

💼 Job Description
Riot's data engineer help shape the data architecture that provide experiences to millions of League of Legends players around the world. 

The project here directly match the job's core responsibilities—querying and visualizing behavioral data, building predictive insights on player churn, and using modern data pipelines to maintain scalable analytics infrastructure.

📊 Data
🔗 Sources
Active Players (Web-Scraped): Historical monthly player stats

Gold Ranked Players (API): Player performance attributes such as win/loss, hotStreak, freshBlood, etc.

📈 Characteristics
Cleaned for consistency and missing values

Categorized by player types, engagement periods, and match behavior

Joined and staged for transformation using dbt

📓 Notebooks / Python Scripts
                  File	                                    Purpose
active_players_web_scrape_extract_load_raw.ipynb	Web scrapes player activity data and stores it into MySQL
gold_ranked_players_api_extract_load_raw.ipynb	    Collects Gold Ranked player metadata via Riot API
active_players_web_scrape_analysis.ipynb	        Executes analytics queries and stores results for Looker dashboards
gold_ranked_players_api_analysis.ipynb	            Executes analytics queries and stores results for Looker dashboards

🚀 Future Improvements
The balance between technical precision and stakeholder-friendly solutions.


