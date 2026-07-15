"""Slide 18: a blocking call inside an async handler stalls the event loop.

Tripwire twin of the slide's magic-move steps. The slide shows one handler
morphing into the other, so both carry the name ``monthly_report`` on stage;
here the broken variant is suffixed to keep the module importable. Two apps
so both handlers can claim the same path; tests only build them —
registration is where Litestar validates ``sync_to_thread`` usage.
"""

import pandas as pd
from litestar import Litestar, get


# region blocking
@get("/reports/monthly")
async def monthly_report_blocking() -> dict[str, int]:
    # looks async - but there is no async pandas
    df = pd.read_csv("orders.csv")
    return {"orders": len(df)}
    # endregion


# region fixed
@get("/reports/monthly", sync_to_thread=True)
def monthly_report() -> dict[str, int]:
    # same work - declared, so it runs in a worker thread
    df = pd.read_csv("orders.csv")
    return {"orders": len(df)}
    # endregion


blocking_app = Litestar([monthly_report_blocking])
fixed_app = Litestar([monthly_report])
