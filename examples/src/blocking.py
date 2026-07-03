"""Slide 17: a blocking call inside an async handler stalls the event loop.

Two apps so both handlers can claim the same path; tests only build them —
registration is where Litestar validates ``sync_to_thread`` usage.
"""

import time

from litestar import Litestar, get


# region blocking
@get("/report")
async def report_blocking() -> dict[str, int]:
    time.sleep(2)  # requests.get(...), pandas, bcrypt…
    return {"total": 42}
    # endregion


# region fixed
@get("/report", sync_to_thread=True)
def report() -> dict[str, int]:
    time.sleep(2)  # same work — in a worker thread
    return {"total": 42}
    # endregion


blocking_app = Litestar([report_blocking])
fixed_app = Litestar([report])
