# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Game

Open `game.html` directly in a browser — no build step, no server required. All game code lives in this single file (~2,300 lines).

To regenerate the PDF design doc:
```
python convert_to_pdf.py
```

## Architecture

**Single-file HTML app** — `game.html` contains all HTML, CSS, and JavaScript inline. No frameworks, no bundler, no npm.

### Screen State Machine

Three screens controlled by `showScreen(name)`: `welcome-screen` → `menu-screen` → `game-screen`. Game launches via `launchGame(variant)`.

### Game Loop

`gameLoop(now)` runs at 60fps via `requestAnimationFrame`. Each frame it:
1. Advances race timer and racer positions (based on `speedMod`)
2. Schedules and resolves bot poker hands
3. Checks for final-lap threshold and finishing order
4. Calls `renderCanvas(now)` to draw the elliptical track + vehicles

### Racer State

Each of the 4 racers (1 player + 3 bots) is a plain object with `distance`, `speedMod`, `boostUntil/boostPct`, `debuffUntil/debuffPct`, and `finishedAt`. Effective speed = `BASE × clamp(1 + speedMod/100, SPEED_FLOOR, SPEED_CEIL)` plus any active boost/debuff.

Key constants: `RACE_DURATION = 180`, `SPEED_FLOOR = 0.3`, `SPEED_CEIL = 2.0`.

### Poker → Speed Pipeline

Winning a hand adds speed points (e.g. Royal Flush = +20, Loss = -2) to `speedMod`. The pay table and speed deltas are defined per-variant in the `VARIANTS` object. Hand phase state: `idle` → `deal` → `doubledown` or `mitigate` → back to `idle`.

### Power-Up System

`CARD_POOL` defines 6 cards (4 boosts, 2 hazards). Three are randomly assigned at race start. Each activates once, directly modifying racer boost/debuff fields.

### Bot AI

`BOT_HANDS` is a weighted array of hand outcomes. Bots resolve hands every 1–3 seconds via `processBotHands()`. No double-down logic for bots.

### Canvas Rendering

`trackGeom()` returns ellipse parameters. `getCarPos(progress, geom, laneScale)` maps 0–N laps to an (x, y) canvas coordinate. Vehicles are PNG images preloaded into `carImgCache`.

## Key Extension Points

- **New poker variant:** Add to `VARIANTS` object; unlock in menu card HTML.
- **New power-up:** Add PNG to `Powerups/`, add entry to `CARD_POOL` with an `activate()` method.
- **Bot difficulty:** Adjust weights in `BOT_HANDS` and scheduling interval in `processBotHands()`.
- **Balance tuning:** `HAND_SPEED_PCT`, `HAND_CHIP_MULT`, `RACE_DURATION`, `CARD_POOL` durations.

## Design Reference

- `Game Design Document - Poker Rush.md` — full design spec (v0.2, 520 lines)
- `Claude Jam II.txt` — quick reference summary of mechanics
