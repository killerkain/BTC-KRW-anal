from pathlib import Path
import argparse
import numpy as np
import pandas as pd

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="outputs")
    args = p.parse_args()

    n = 500
    t = pd.date_range("2024-01-01", periods=n, freq="H")
    price = 50000000 + np.cumsum(np.random.normal(0, 100000, n))
    df = pd.DataFrame({"datetime": t, "close": price})

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "ohlcv.csv", index=False)

    ret = df["close"].pct_change().fillna(0)
    eq = (1 + ret * 0.1).cumprod()
    mdd = ((eq - eq.cummax()) / eq.cummax()).min()
    metrics = pd.DataFrame([{"total_return": float(eq.iloc[-1]-1), "mdd": float(mdd)}])
    metrics.to_csv(out / "metrics.csv", index=False)

    print("done:", out)

if __name__ == "__main__":
    main()
