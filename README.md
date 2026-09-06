# Bangladesh 13th Election 2026 Analytics

Interactive election analytics for Bangladesh's 13th parliamentary election. The project combines a reproducible analysis notebook with a multipage Streamlit dashboard for exploring constituency results, parties, demographics, socioeconomic indicators, geography, and referendum results.

## Live Dashboard

Open the permanently hosted dashboard:

**[Bangladesh Election 2026 Analytics Dashboard](https://bangladesh13thelection2026-lfv7rddrfpq8tc75wsqurd.streamlit.app/)**

The dashboard is hosted on Streamlit Community Cloud and can be opened independently of VS Code or a local development machine.

## Project Goals

- Summarize election results at constituency and division level.
- Compare winning parties and winning margins.
- Explore competitiveness using reported winner and runner-up votes.
- Analyze registered voter demographics by division.
- Examine poverty, literacy, and electoral relationships.
- Provide an interactive constituency search and filtering experience.
- Present referendum results included in the source data.
- Keep analytical limitations visible and avoid unsupported turnout claims.

## Dashboard Pages

The Streamlit application includes:

1. **Overview**: national KPIs, constituencies by division, party wins, margin distribution, and socioeconomic comparison.
2. **Electoral Analysis**: competitiveness categories, winner share of top-two reported votes, and margin comparisons.
3. **Demographic Analysis**: registered male, female, and transgender voter distributions and gender gaps.
4. **Socioeconomic Analysis**: poverty, literacy, division comparisons, and constituency-level relationships.
5. **Party Analysis**: constituency wins, average margins, and party wins by division.
6. **Constituency Explorer**: search and filter individual constituencies by name, division, and winning party.
7. **Geographic Analysis**: division-level voter comparisons and the published interactive Bangladesh election map.
8. **Referendum Analysis**: reported Yes/No vote totals and percentages.
9. **Data Quality**: completeness, uniqueness, duplicate-record checks, and interpretation boundaries.

## Repository Structure

```text
.
├── Election_Analysis.ipynb          # Research and analysis notebook
├── data/
│   └── processed/                   # Cleaned datasets used by the dashboard
├── figures/                         # Published charts and interactive map outputs
├── tables/                          # Aggregated analytical tables
├── dashboard/
│   ├── app.py                       # Streamlit application entry point
│   ├── pages/                       # Dashboard pages
│   ├── utils/                       # Data loading, styling, and chart helpers
│   ├── requirements.txt             # Dashboard dependency list
│   └── README.md                    # Dashboard-specific instructions
├── .streamlit/config.toml           # Hosted dashboard theme and server settings
└── requirements.txt                 # Deployment dependencies
```

## Data Sources and Measures

The dashboard reads the processed files in `data/processed/`:

- `election_clean.csv`: constituency results, winner and runner-up information, registered voters, division, poverty, literacy, gender measures, margins, and competitiveness.
- `election_with_clusters.csv`: election data with cluster-analysis outputs.
- `gonovote_clean.csv`: referendum choices, reported votes, and percentages.

Important measures include:

- **Winning margin**: winner votes minus runner-up votes.
- **Winner share of top-two reported votes**: winner votes divided by winner plus runner-up votes.
- **Top-two reported votes**: winner votes plus runner-up votes.
- **Registered voters**: the reported registered voter count in the processed dataset.

### Interpretation Boundary

The election dataset contains winner and runner-up vote counts, but it does not contain total ballots cast. Therefore, this project does **not** present voter turnout as a KPI. Top-two reported vote share, winning margin, top-two reported votes, and registered voters are used instead.

## Technology Stack

- **Python** for data processing and application code.
- **Pandas** for loading, cleaning, grouping, and summarizing data.
- **Plotly** for interactive charts.
- **Streamlit** for the multipage dashboard and deployment.
- **PySpark** for preprocessing and analytics in the research workflow where applicable.
- **Jupyter Notebook** for exploratory analysis and research documentation.
- **Streamlit Community Cloud** for permanent public hosting.

## Run Locally

From the repository root:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run dashboard/app.py
```

Then open the local URL shown by Streamlit, usually `http://localhost:8501`.

On Windows, using `python -m streamlit` ensures Streamlit runs through the active Python environment.

## Deployment

The live app is deployed from this GitHub repository using Streamlit Community Cloud.

To deploy a new copy or reconnect the application:

1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
2. Select `rsdina/Bangladesh_13th_Election2026`.
3. Select the `main` branch.
4. Set the main file path to `dashboard/app.py`.
5. Click **Deploy**.

Future commits pushed to `main` can be used to update the hosted dashboard. The free hosting tier may put the app to sleep after inactivity, but the permanent URL remains available.

## Development Workflow

1. Use `Election_Analysis.ipynb` for research, exploratory analysis, preprocessing, and analytical validation.
2. Store dashboard-ready datasets in `data/processed/`.
3. Add or update reusable dashboard logic in `dashboard/utils/`.
4. Add individual views as modules in `dashboard/pages/`.
5. Run the dashboard locally and verify charts, filters, tables, and data-quality checks.
6. Commit changes and push them to the `main` branch.
7. Streamlit Community Cloud rebuilds the hosted application from the updated repository.

## Project Status

The dashboard is deployed and available at:

https://bangladesh13thelection2026-lfv7rddrfpq8tc75wsqurd.streamlit.app/
