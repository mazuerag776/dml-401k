import pandas as pd
from paths import DATA_DIR, RESULTS_DIR

data = pd.read_csv(DATA_DIR / "raw/401k.csv")

print(data.shape)

print(data[["net_tfa", "e401", "p401"]].describe())

print(data.groupby("e401")["net_tfa"].mean())

covariates = ["age", "inc", "educ", "fsize", 
              "marr", "twoearn", "db", "hown",
              "pira"]

print(
        data.groupby("e401")[covariates]
        .mean()
        .T
)
