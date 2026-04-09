# POKER RUSH
## Game Design Document v0.2

---

# PART 1 — PITCH SUMMARY

## The One-Liner

**Poker Rush** is a single-player racing game where you race against AI opponents and your poker hands control your speed — the better you play, the faster you drive.

---

## Concept Overview

Poker Rush fuses two genres that have never been combined at speed: **video poker** and **arcade racing**. The player races against AI-controlled opponents in 3–5 minute races, playing rapid-fire video poker hands simultaneously. Every hand outcome directly translates into acceleration or deceleration on the track. Win big at the table, pull ahead. Go cold, fall behind.

The result is a game that rewards **skill**, **risk management**, and **clutch decision-making** — and creates a constantly shifting race where the outcome is never certain until the very last hand.

---

## The Core Loop

```
Play a poker hand → Earn/lose speed points → Watch your car move on the track
→ Decide whether to double down for more speed → Race ends → Collect rewards
→ Buy power-ups → Enter next race
```

---

## Why It Works

| Tension | Source |
|---|---|
| Poker tension | Am I making the optimal hold? Will the draw pay off? |
| Race tension | Am I gaining or losing ground on the AI opponents? |
| Risk tension | Do I double down for more speed, or cash out safely? |
| Meta tension | Do I use my power-up now or save it? |

Each layer of tension reinforces the others. A player trailing in the race is incentivized to take bigger poker risks. A player in the lead has something to protect. The AI opponents adapt their aggression based on the race situation, ensuring **come-from-behind moments** and **dramatic collapses** that make every race a story.

---

## Target Audience

- Casual to mid-core players who enjoy card games and single-player challenges
- Video poker fans looking for a competitive, high-stakes twist
- Racing game fans who want a fresh take on the genre
- Ages 18+ (gambling-themed mechanics)

---

## Platform & Format

- PC (primary), Mobile (secondary)
- Free-to-play with cosmetic monetization and chip purchases
- Single-player against AI bots (1–5 opponents per race); multiplayer support deferred to a future version

---

## Key Differentiators

1. **No equivalent exists** — the poker-racing hybrid genre is wide open
2. **High replayability** — 8 poker variants, configurable race settings, rotating power-up meta, and varied AI difficulty levels
3. **Meaningful skill ceiling** — AI opponents provide a genuine challenge; mastering hold strategy and double-down decisions determines race outcomes
4. **Leaderboard competition** — chase high scores and reputation rankings even in single-player

---
---

# PART 2 — FULL GAME DESIGN DOCUMENT

---

## Table of Contents

1. [Game Overview](#1-game-overview)
2. [Screen Flow & Navigation](#2-screen-flow--navigation)
3. [Player Profile & Progression](#3-player-profile--progression)
4. [Poker Gameplay](#4-poker-gameplay)
5. [Race Mechanics](#5-race-mechanics)
6. [Speed Point System](#6-speed-point-system)
7. [Double Down System](#7-double-down-system)
8. [Power-Up System](#8-power-up-system)
9. [Race Setup](#9-race-setup)
10. [Betting System](#10-betting-system) *(deferred)*
11. [Rewards & Economy](#11-rewards--economy)
12. [Leaderboard & Reputation](#12-leaderboard--reputation)
13. [UI/UX Layout](#13-uiux-layout)

---

## 1. Game Overview

### Genre
Single-Player Arcade Racing / Video Poker Hybrid

### Core Premise
The player races against 1–5 AI bot opponents on a looping track. Each racer controls their own vehicle, but vehicle speed is determined entirely by the results of rapid-fire video poker hands resolved in real time. AI bots play their own poker hands autonomously. Races last 3–5 minutes, with a "final lap" triggered at time expiry.

### Pillars
- **Speed of play** — Hands resolve fast. No waiting. Action is constant.
- **Meaningful decisions** — Every hold, every double-down, every power-up activation matters.
- **Competitive pressure** — AI opponents race in real time; every hand matters relative to the field.
- **Accessible depth** — Easy to jump in, hard to master.

---

## 2. Screen Flow & Navigation

### 2.1 Welcome / Main Menu Screen

The entry point of the game. From here, players can:

| Action | Description |
|---|---|
| **Quick Play** | Immediately start a race using saved profile preferences (variant, bot count, difficulty) |
| **Play** | Navigate to the Game Mode Selection screen to choose poker variant and configure a race |
| **Profile** | View and edit profile, stats, and power-up loadout |
| **Leaderboard** | View the top 20 global players by reputation points |

---

### 2.2 Game Mode Selection Screen

Players select their preferred poker variant before entering a race. Options:

- Triple Double Bonus Poker
- All American
- Loose Deuces
- Bonus Draw Poker
- Double Joker Poker
- Double Bonus Draw Poker
- Double Double Draw Poker
- Triple Double Draw Poker

After selecting, the player proceeds to the Race Setup screen to configure bot count, difficulty, and other race settings.

---

### 2.3 Race Setup Screen

A configuration screen where the player sets bot count, AI difficulty, race duration, and other options before starting a race. See Section 9 for full detail.

---

### 2.4 Race Screen

The primary gameplay screen. See Section 13 for full UI layout detail.

---

## 3. Player Profile & Progression

### 3.1 Profile Fields

| Field | Description |
|---|---|
| Username | Display name shown to all players |
| Default Poker Variant | Pre-selected game type for Quick Play |
| Avatar / Vehicle Skin | Visual customization (cosmetic) |
| Racing Profile | Default race preferences for matchmaking queue (player count, power-ups on/off, skill level) |

### 3.2 Stats Tracked

**Poker Stats:**
- Hands played
- Win rate by hand type
- Total chips won / lost
- Favorite variant

**Racing Stats:**
- Races entered / won / lost
- Win rate by player count
- Average finishing position
- Best streak

### 3.3 Starting Conditions

- New players receive a **10,000 chip bankroll** upon registration.
- Players who run out of chips have three options:
  1. **Purchase chips** (real-money or in-game purchase)
  2. **Claim daily chip drop** (free replenishment on a 24-hour cooldown)
  3. **Profile reset** — wipes all stats and rep, restores 10k chip bankroll

---

## 4. Poker Gameplay

### 4.1 Format

Each player plays an independent video poker session on their own client. All players use the same poker variant for the duration of a race (set by the race creator or assigned randomly).

Hands are dealt and resolved as fast as the player can act — there is no forced timer per hand, but the race clock is always ticking, incentivizing fast play.

### 4.2 Supported Variants

All 8 variants use standard video poker rules for their respective type. Pay tables follow industry-standard configurations for each variant:

| Variant | Key Feature |
|---|---|
| Triple Double Bonus Poker | High premium on 4-of-a-kind hands with kicker bonuses |
| All American | Elevated pay on straights, flushes, and straight flushes |
| Loose Deuces | All 2s are wild; aggressive pay table |
| Bonus Draw Poker | Bonus pay on 4 Aces |
| Double Joker Poker | 2 jokers wild; natural royal flush pays premium |
| Double Bonus Draw Poker | Bonus payouts on all 4-of-a-kind hands |
| Double Double Draw Poker | Additional kicker bonus on top of Double Bonus pay table |
| Triple Double Draw Poker | Further escalated 4-of-a-kind bonuses |

### 4.3 Chip Wagering

Each hand requires a chip wager. Standard bet is 1 unit (configurable). Chips won/lost per hand follow the poker variant's pay table multiplied by bet amount. The chip economy runs in parallel to, and independently from, the speed point system.

---

## 5. Race Mechanics

### 5.1 Track & Vehicles

- Races take place on a looping circuit with a configurable visual theme (set by race creator).
- Each player controls one vehicle. Vehicle position on track is calculated from accumulated speed points in real time.
- Vehicles are purely cosmetic — performance is driven entirely by poker results and power-ups.

### 5.2 Race Duration

- Minimum: **3 minutes**
- Maximum: **5 minutes**
- At time expiry, a **Final Lap** is triggered. The race ends when the leading car completes one additional full lap. All cars finish after the leader.

### 5.3 Skill Levels

Races can be filtered by skill level to ensure fair competition:

| Level | Description |
|---|---|
| Newbie | Recommended for new players; lower entry-level poker variant difficulty |
| Advanced | Mid-tier; standard competition |
| Pro | High-level players; no restrictions on aggressive play styles |

### 5.4 Field Size

- 1 human player + **1–5 AI bot opponents**
- Total racers on track: **2–6**

---

## 6. Speed Point System

### 6.1 Base Rules

Every hand result generates a speed modifier applied to the player's vehicle:

| Outcome | Speed Change |
|---|---|
| Any loss | −3% speed |
| Pair | +1 point → +2% speed |
| Two Pair | +2 points → +4% speed |
| Three of a Kind | +3 points → +6% speed |
| Straight | +4 points → +8% speed |
| Flush | +5 points → +10% speed |
| Full House | +6 points → +12% speed |
| Four of a Kind | +7 points → +14% speed |
| Straight Flush | +8 points → +16% speed |
| Royal Flush | +10 points → +20% speed |

*Formula: each speed point = +2% speed modifier applied cumulatively over the race.*

### 6.2 Speed Calculation

Speed is calculated as a running cumulative modifier from race start. Speed cannot go below a minimum floor (preventing vehicles from stopping entirely) and has a soft cap at maximum speed to prevent runaway leaders.

> **Design note:** The exact floor and ceiling values are tuning parameters. Suggested starting values: floor = 30% of base speed, ceiling = 200% of base speed.

---

## 7. Double Down System

The Double Down system introduces a risk/reward decision after every hand, creating micro-moments of drama.

### 7.1 After a Winning Hand — Boost Mode

After any winning hand, the player is prompted to guess: **Red or Black** (next card drawn from a fresh deck).

| Result | Outcome |
|---|---|
| Correct guess | Speed points for that hand are **doubled** |
| Incorrect guess | Speed points for that hand are **lost** (treated as 0, not a loss) |

Players may double down **up to 3 times** on a single winning hand:
- After guess 1: Cash out or double again
- After guess 2: Cash out or double again (final)
- After guess 3: Automatic cash out with tripled base points

### 7.2 After a Losing Hand — Mitigation Mode

After any losing hand, the player may attempt to reduce the penalty. One guess only.

| Result | Speed Change |
|---|---|
| Correct guess | Loss penalty reduced by **50%** (−1.5% instead of −3%) |
| Incorrect guess | Loss penalty **increased to −4.5%** |

This forces meaningful risk assessment even on bad hands — sometimes it's better to absorb the −3% than risk −4.5%.

---

## 8. Power-Up System

### 8.1 Overview

Power-ups provide temporary in-race advantages. They are purchased with chips between races and equipped before a race starts (up to 3 active slots).

### 8.2 Acquiring Power-Ups

| Source | Method |
|---|---|
| **Chip Store** | Direct purchase between races |
| **Raffle Tickets** | Earned by finishing in top positions; tickets enter a draw for rare power-ups |

### 8.3 Equipping Power-Ups

- Players have **3 power-up slots**.
- Power-ups are equipped from the Profile screen or the Matchmaking Room.
- Each power-up may only be used **once per race**.

### 8.4 Activation

During a race, the Power-Up Panel is visible on the right side of the race display. Each slot has an **Activate** button. Power-ups can be toggled on/off per race (set by race creator — either all players have power-ups enabled, or none do).

### 8.5 Power-Up Design Space (Examples)

> *Specific power-ups to be defined in a follow-up balance pass. Below are illustrative concepts:*

| Power-Up | Effect |
|---|---|
| Nitro Burst | Instant +15% speed for 20 seconds |
| Speed Lock | Freeze your current speed for 15 seconds (immune to loss penalties) |
| Sabotage | Apply a one-time −5% speed hit to a targeted opponent |
| Double Points | Next winning hand gives 2× speed points |
| Safety Net | Negate the next losing hand's speed penalty entirely |
| Comeback Engine | Grants +10% speed if currently in last place |

---

## 9. Race Setup

### 9.1 Race Setup Screen Overview

The Race Setup screen is where the player configures a race before it begins. All opponents are AI bots — no waiting for other players.

### 9.2 Race Configuration

| Setting | Options |
|---|---|
| Poker Game Type | Select specific variant, or "Random" |
| Number of AI Bots | 1 to 5 |
| AI Difficulty | Newbie / Advanced / Pro |
| Power-Ups | Enabled or Disabled |
| Race Duration | 3 to 5 minutes |
| Race Visual | Choose track/environment theme |

If any field is left blank, the system uses the player's saved profile defaults.

A **Start Race** button launches immediately — no wait time.

### 9.3 Quick Play

From the main menu, Quick Play bypasses the Race Setup screen and launches a race immediately using the player's saved **profile defaults** (bot count, AI difficulty, poker variant, power-ups preference).

### 9.4 AI Bot Behaviour

> *To be defined during technical design. Suggested approach: each difficulty tier maps to a target hold-strategy accuracy and double-down aggression level. "Pro" bots play near-optimal video poker; "Newbie" bots make frequent suboptimal holds. Bot speed updates are computed server-side to prevent cheating.*

---

## 10. Betting System

> **Deferred — single-player version only.** The betting system (pre-race wagering on outcomes, spectator bets) requires real human opponents to function meaningfully and is removed for this version. It remains a planned feature for when multiplayer support is added.

---

## 11. Rewards & Economy

### 11.1 Race Finish Rewards

Rewards are distributed based on finishing position and race size:

#### 2-Player Race
| Place | Rep | Chips | Raffle Tickets |
|---|---|---|---|
| 1st | +100 | +25,000 | 1 |
| 2nd | −50 | 0 | 0 |

#### 3-Player Race
| Place | Rep | Chips | Raffle Tickets |
|---|---|---|---|
| 1st | +125 | +40,000 | 1 |
| 2nd | +25 | +5,000 | 0 |
| 3rd | −50 | 0 | 0 |

#### 4-Player Race
| Place | Rep | Chips | Raffle Tickets |
|---|---|---|---|
| 1st | +150 | +50,000 | 1 |
| 2nd | +25 | +10,000 | 0 |
| 3rd | +10 | +2,000 | 0 |
| 4th | −50 | 0 | 0 |

#### 5-Player Race
| Place | Rep | Chips | Raffle Tickets |
|---|---|---|---|
| 1st | +175 | +60,000 | 2 |
| 2nd | +75 | +15,000 | 1 |
| 3rd | +15 | +5,000 | 0 |
| 4th | 0 | 0 | 0 |
| 5th | −50 | 0 | 0 |

#### 6-Player Race
| Place | Rep | Chips | Raffle Tickets |
|---|---|---|---|
| 1st | +200 | +75,000 | 3 |
| 2nd | +100 | +25,000 | 2 |
| 3rd | +50 | +10,000 | 1 |
| 4th | +10 | 0 | 0 |
| 5th | −25 | 0 | 0 |
| 6th | −50 | 0 | 0 |

*All chip and rep amounts are in addition to any race bet winnings.*

### 11.2 Economy Overview

| Currency | Earned By | Spent On |
|---|---|---|
| Chips | Race prizes, poker winnings, daily drop, purchase | Power-ups, chip bets, larger poker wagers |
| Rep Points | Race finishes | Not spent — progression/ranking metric only |
| Raffle Tickets | Top race finishes | Entered into power-up draws |

---

## 12. Leaderboard & Reputation

### 12.1 Global Leaderboard

Displays the **top 20 players** ranked by total Reputation Points. Visible from the main menu.

### 12.2 Reputation Design Notes

Rep rewards finishing ahead of AI opponents. Higher AI difficulty levels award more rep for equivalent finishes, incentivising players to race at their skill ceiling. Rep loss still applies for poor finishes to prevent idle grinding.

> *Consider season resets (monthly/quarterly) to keep the leaderboard accessible and competitive for newer players.*

---

## 13. UI/UX Layout

### 13.1 Race Screen Layout

The race screen uses a **vertical split** design:

```
┌─────────────────────────────────────────┐
│                                         │
│           RACE DISPLAY (top)            │  ← Track view, vehicle positions,
│                                 [PUPS]  │     race timer, opponent info
│                                         │     Power-up panel on right edge (3 slots)
├─────────────────────────────────────────┤
│                                         │
│          POKER GAMEPLAY (bottom)        │  ← Dealt cards, Hold buttons,
│                                         │     Draw button, chip balance,
│                                         │     Double down prompt overlay
└─────────────────────────────────────────┘
```

### 13.2 Race Display Panel (Top)

- Live track showing all player vehicles with name labels
- Race timer (counting down to Final Lap trigger)
- Player speed delta indicators (who is accelerating / decelerating)
- Current standings (position 1 through N)
- Power-Up Panel — 3 slots with individual Activate buttons, visible at all times

### 13.3 Poker Panel (Bottom)

- Card display (5 cards, face up after deal)
- Hold / Unhold buttons beneath each card
- Draw button
- Current chip balance and current hand wager
- Double Down overlay — appears after hand resolution (Red / Black choice, Cash Out option)
- Last hand result indicator (win type + speed change applied)

### 13.4 Race Setup Screen Layout

- Top: Poker variant selector
- Middle: Race configuration panel (bot count slider, AI difficulty toggle, duration, visual theme, power-ups toggle)
- Bottom bar: Start Race button, Quick Play defaults button, Back button
- Profile quick-edit accessible via header

---

## 14. Open Design Questions

The following items require further design or balancing work before production:

1. **Speed floor / ceiling values** — Prevent runaway leaders and stalled trailers
2. **Power-up catalogue** — Full list with names, costs, cooldowns, and balance pass
3. **Poker chip bet sizing** — Default wager and min/max wager per hand
4. **AI bot difficulty tuning** — Hold-strategy accuracy, double-down aggression, and pacing per difficulty tier
5. **AI bot speed calculation** — Server-authoritative or client-simulated; how bot hand results are generated and communicated to the race view
6. **Rep rewards by difficulty** — How much extra rep to award for beating Pro vs. Newbie bots
7. **Season reset cadence** — Leaderboard freshness vs. long-term progression
8. **Daily chip drop amount** — Generosity vs. chip economy health
9. **Mobile UI adaptation** — Split-screen layout needs redesign for portrait/landscape on small screens
10. **Multiplayer roadmap** — Future re-introduction of human opponents and the betting system; what single-player infrastructure carries over

---

*Document version 0.2 — April 2026 — Updated for single-player with AI bots; multiplayer and betting system deferred*
*Game title "Poker Rush" is a working title and subject to change.*
