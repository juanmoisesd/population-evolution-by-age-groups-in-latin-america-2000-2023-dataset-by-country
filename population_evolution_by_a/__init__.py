"""This dataset contains data on the population evolution by age groups in 11 Latin American countries 
DOI: https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country | GitHub: https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). This dataset contains data on the population evolution by age groups in 11 Latin. Zenodo. https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country'
def info(): print(f"Dataset: This dataset contains data on the population evolution by age groups in 11 Latin\nDOI: https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country\nGitHub: https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country")