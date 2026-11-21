# Barebones Stopwatch

A compact, offline desktop stopwatch built completely from scratch in Python using `tkinter`.

## Features
* **Clear Readout:** Centered `HH:MM:SS` timer display in a compact, fixed-size window (`320x180`).
* **Drift-Free Timing:** Uses `time.perf_counter()` with banked elapsed time so pausing and resuming stays accurate without timer drift.
* **Non-Blocking UI:** Driven by `root.after()` callbacks so the window never freezes while counting.
* **Color-Coded Controls:** Distinct **Start**, **Stop**, and **Reset** buttons with duplicate-click protection.

## Run Locally

```bash
uv run barebone-stopwatch
```
