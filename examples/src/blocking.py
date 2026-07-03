"""Slide 17: a blocking call inside an async handler stalls the event loop.

Two apps so both handlers can claim the same path; tests only build them —
registration is where Litestar validates ``sync_to_thread`` usage.
"""

import pandas as pd
from litestar import Litestar, get


# region blocking
@get("/report")
async def report_blocking() -> dict[str, int]:
    # disk + CPU — blocks the loop
    df = pd.read_csv("orders.csv")
    return {"orders": len(df)}
    # endregion


# region fixed
@get("/report", sync_to_thread=True)
def report() -> dict[str, int]:
    # same work — in a worker thread
    df = pd.read_csv("orders.csv")
    return {"orders": len(df)}
    # endregion


blocking_app = Litestar([report_blocking])
fixed_app = Litestar([report])
