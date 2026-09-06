# Bangladesh Election 2026 Dashboard

Interactive Streamlit presentation layer for the analysis in `Election_Analysis.ipynb`.

## Run locally

From the repository root:

```powershell
python -m pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

The app reads the processed CSVs in `data/processed/` and the published geographic HTML in `figures/`.

## Deploy permanently

Deploy this repository with [Streamlit Community Cloud](https://share.streamlit.io/):

1. Push the repository changes to GitHub.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Select `rsdina/Bangladesh_13th_Election2026`.
4. Set the main file to `dashboard/app.py`.
5. Click **Deploy**.

The resulting `streamlit.app` URL works independently of VS Code. The app may sleep after inactivity on the free tier, but opening the URL starts it again and the URL remains unchanged.