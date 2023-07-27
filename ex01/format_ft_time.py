#!/usr/bin/env python3.10

import time

print(f"Seconds since January 1, 1970: {time.time():,} or {time.time():e} in scientific notation\n{time.strftime('%b %d %Y')}")