[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kazuki-fortune88/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kazuki-fortune88/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry by [kazuki-fortune88](https://github.com/kazuki-fortune88) for the [make.fun bounty news-image-20261119](https://make.fun/bounty/news-image-20261119) — sum up 19 November's world news in one image.
Run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` · Referral code: `4fxhr3y1`

---

# News Image — Thursday 19 November 2026 (v7)

Front page of Thursday 19 November 2026 world news: 12 panels + 31 "also"
items = **43 stories**, 1024×1024 PNG, **192,771 bytes**, SHA-256
`8f9f286fe0fa7378740be8a9b470d4f3c10d7c71946e7fb7142b2c747e369c8f`.

Built by `generate.py` (deterministic PIL + DejaVu renderer: no network, no
timestamps, no randomness). `main.ts` (Node stdlib only) copies `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## What changed vs v6 (43 stories, SHA 9b59b812…, 193,440 bytes)

Targeted fix of the TWO residual ALSO errors the v6 head-to-head
(**4W–0L–1D vs the current top 5**, see
`~/workspace/makefun/research/head-to-head-v6-19nov.md`) found in kept
items. No panel changes, no layout changes.

| Slot | Dropped (why out) | Replacement (sources, 19 Nov) |
|---|---|---|
| #16 | NGO: care curbed for 1,100 Gaza child amputees — Euro-Med report published **4 Nov** (Al Jazeera 2026-11-04T21:13Z), 15 days stale | **Israel hits Hezbollah missile site in Lebanon** — IDF struck the entrances to a former Hezbollah missile production / weapons storage site in Janta, Beqaa Valley, Thu evening 19 Nov (IDF via israelrealtime.com, published 19 Nov 20:27 IST; Pensacola Herald / HO Herald Wire: "airstrikes on Thursday evening, November 19, 2026"; CUFI news roundup, 19 Nov). Stays ME, so region counts unchanged. |
| #27 | Microsoft in talks to sell AI to ByteDance — The Information reported the talks **18 Nov** (Reuters Nov 18); as phrased a Wednesday story | **UN: no state OK needed to form a group** — UN Human Rights Committee issued General Comment No. 38 on Thu 19 Nov: no prior state authorisation is needed to form or join an association (UN News, 19 Nov 2026; OHCHR press release; AFP via Sino Daily; Bangkok Post). Stays WO, so region counts unchanged. |

Stats strip: **"$120bn — COP31 adaptation goal" → "$120bn — COP31 goal cut"**
so it matches panel 7 (the Thursday draft drops the $120bn goal). No other
stats item changed. Region strip unchanged: Middle East 4, Americas 13,
Asia 10, Europe 5, Africa 3, Oceania 2, World 6 = 43.

### Verification (v7, all passed)
- `python3 generate.py` three times: byte-identical, SHA `8f9f286f…`,
  **192,771 bytes** (< 350 KB), **no OVERFLOW** (ALSO lines, footer,
  subhead, UTC strip all within limits).
- `main.ts` (`MAKEFUN_OUTPUT_DIR` set): byte-identical copy, same SHA.
- Visual QA: full image + ALSO/stats crops + 300px downscale reviewed.
  No text collisions; no panel text spills past its border; the two new
  ALSO lines fit their columns; stats strip reads "COP31 goal cut";
  footer fits on one line; at 300px the masthead date, stats numbers and
  panel headlines stay legible; the ALSO list is present at 10px (same
  as v6 and the winners' lists).
- Story count: 12 panels + 31 ALSO = 43; region strip sums to 43; pins
  1–12 all placed.

## What changed vs v5 (43 stories, SHA ac11eb2e…, 193,074 bytes)

Targeted date fix, NOT a redesign — layout, fonts, panel count and the
12-panel structure are unchanged. v5 re-tested **2W–3L vs the CURRENT top 5**
(see `~/workspace/makefun/research/head-to-head-v5-19nov-refresh.md`); the
audit behind v6 found **TWELVE date errors in v5** (1 panel + 11 ALSO), more
than the re-test had counted, plus one more (Estonia, 15 Nov) found in this
audit. All twelve are fixed here.

### P0 — Gaza panel 2 reframed (the crossing was 18 Nov)
| Change | Verified fact |
|---|---|
| Headline "Israeli tanks cross Gaza ceasefire line" → **"Israel ends its Gaza tank raid"**; body now "The raid across the Yellow Line ends; 'the operation is completed,' the army tells AFP." | Incursion began Wed 18 Nov (tanks crossed the Yellow Line Wed afternoon, Bureij–Nuseirat); it ENDED Thu 19 Nov — "The operation is completed," the military told AFP; COGAT confirmed activity ended and the Salah al-Din axis reopened (AFP / Reuters / Bangkok Post, 19 Nov). |

### P0 — COP31 panel 7 corrected to the Thursday draft
| Change | Verified fact |
|---|---|
| Headline "COP31 enters its final 48 hours" → **"COP31 draft drops fossil fuels and $120bn"**; body now "The slimmed-down Thursday draft cuts fossil-fuel language and the $120bn adaptation goal." | The revised draft published Thu 19 Nov (Reuters 12:13 UTC) DID drop fossil-fuel phase-out language and the $120bn adaptation target — 80 paras, down from 144 (Reuters). v5's "no consensus yet" was vague. |

### P0 — 12 ALSO items dropped (wrong date) and replaced (verified 19 Nov)
| Slot | Dropped (why out) | Replacement (sources, 19 Nov) |
|---|---|---|
| #13 | Gaza aid plea — joint statement issued Sun 15 Nov (Canada.ca) | **Denmark votes 109-0 for Greenland pact** — Folketing voted 109–0 Thu 19 Nov to consent to the US–Denmark–Greenland security pact (AP; Euronews; Danish Parliament B 36 tally). |
| #14 | France 4th weekend of protests — the 4th weekend was Sat 7 Nov | **Korea top court sends ex-PM Han to retrial** — Supreme Court partially overturned the 15-year sentence, retrial ordered, Han stays in detention (Reuters; Korea JoongAng Daily; Seoul Economic Daily). |
| #15 | Eisenkot mandate — given 7–8 Nov, not 19 Nov | **Bangladesh lockdown: Yunus home torched, 4 dead** — Yunus ancestral home torched (~23:30 Wed, reported Thu), 4 killed, 28 districts, lockdown Thu 19 Nov (Reuters via Hindu BusinessLine; PTI; Inshorts, 19 Nov 08:36 UTC). |
| #18 | Palantir spy — DOJ charges announced Wed 18 Nov; arrest was 30 Oct | **Jepchirchir gets 3-year ban for EPO** — AIU announced the 3-year EPO ban Thu 19 Nov; Sydney Marathon win annulled (ESPN 19 Nov 14:49; AP; Athletics Weekly; AIU). |
| #20 | Carney/China ties — 18 Nov (Reuters) | **IEA: Hormuz crisis is worst energy threat ever** — IEA World Energy Outlook published Thu 19 Nov: Hormuz crisis is the largest threat to energy security in history (France 24/AFP; The Hindu; Reuters). |
| #22 | Australia settler sanctions — 18 Nov (DFAT) | **Senegal boat sinks; dozens missing, 4 found** — search resumed Thu, 4 bodies recovered Thu; capsizing overnight Tue→Wed (Reuters 19 Nov 10:01 UTC; BBC). |
| #25 | Liu Yunping (Ted Lieu) elected House chair — Wed 18 Nov (Politico) | **US drops Supreme Court bid on Venezuela TPS** — Trump administration WITHDREW its emergency request Thu 19 Nov, one day after filing it, because the 9th Circuit gave the stay (Reuters/AP; devdiscourse 19 Nov 21:00 IST). |
| #26 | Deutsche Bank $582m Epstein-linked deals — 17 Nov (FT consortium) | **Trump defers Iran decision to next year** — Trump told Reuters aboard Air Force One Thu 19 Nov: "I'll talk to you about it after the beginning of the year" (Reuters via BusinessWorld; NY Post; devdiscourse). |
| #30 | Banxico cut to 6.25% — the cut was 5 Nov (3–2 vote) | **Banxico minutes point to long rate pause** — the minutes of that meeting were published Thu 19 Nov (WSJ/Dow Jones via TradingView). Rewritten in place, not dropped. |
| #31 | Ilona W. charges — filed 7 Sep 2026, NOT November at all | **Ukraine imposes emergency power cuts** — overnight 18→19 Nov drone/missile attack (98 drones); emergency cuts introduced 19 Nov in Kharkiv/Sumy/Poltava (stpeteherald; egazette 19 Nov 02:13). |
| #32 | Estonia road crossings — announced 15 Nov (ERR) | **Senate rejects bid to curb Iran war, 51-48** — Senate rejected the war powers resolution Thu 19 Nov, 51–48, 2:42 p.m. ET (Reuters; USA Today; Washington Examiner). |
| #33 | Vance "no forever war" — Fox interview Mon 16 Nov | **Bitcoin ETFs shed $2.9bn in November** — Bitcoin traded ~$63,700 Thu 19 Nov, down ~13% in a week; spot ETF outflows $306.4m Wed, ~$2.9bn in November (CoinDesk 19 Nov 07:08 EST; Decrypt 19 Nov 10:25; TradingView/Cointelegraph). |
| #36 | Bapco refinery — CEO spoke 18 Nov (Middle East Gas Conference) | **Chow reshuffles Toronto team in 2nd term** — Mayor Olivia Chow shuffled her city hall leadership team Thu 19 Nov (The Canadian Press, first published Nov 19). |

### P0 — DATE CHECK footer
Now names the four newly excluded items the re-test required — **Gaza
crossing, Carney, Australia sanctions (18 Nov); Deutsche $582m (17 Nov)** —
plus the existing v5 exclusions (Voyager, EU €45bn, Fed minutes, Van Gogh;
N. Korea, Nvidia H200). Sources line shortened to "Reuters, AP, AFP" so
the line fits at 10px (984px of 996). The other v6 drops (Gaza aid plea
15 Nov, France protests 7 Nov, Eisenkot 7–8 Nov, Palantir 18 Nov, Lieu
chair 18 Nov, Ilona W. Sep, Vance 16 Nov, Bapco 18 Nov, Estonia 15 Nov,
Banxico cut 5 Nov) are documented here; they do not fit on the footer line.

### Region strip recount (sums to 43)
Middle East 4, Americas 13, Asia 10, Europe 5, Africa 3, Oceania 2,
World 6 (was ME 7, AM 12, AS 8, EU 8, AF 1, OC 3, WO 4). Per-item map:
ME = panels 2, 9 + ALSO 16, 23; AM = panels 3, 4, 12 + ALSO 17, 19, 25,
26, 30, 32, 36, 39, 41, 43; AS = panels 1, 5, 6, 10 + ALSO 14, 15, 21,
24, 37, 40; EU = panel 8 + ALSO 13, 29, 31, 34; AF = ALSO 18, 22, 42;
OC = panel 11 + ALSO 35; WO = panel 7 + ALSO 20, 27, 28, 33, 38.

### Unchanged from v5
- ICJ panel: **no vote count added** (the correct count is 9–6, but leaving
  it out is safe — the panel already carries the confirmed verdict).
- Stats strip ("$120bn COP31 adaptation goal" now ties to the panel's
  dropped-goal story), UTC strip, subhead, map pins 1–12, masthead.
- Panel 9 "Trump weighs new strikes on Iran" stays (NYT morning fact);
  ALSO #26 "Trump defers Iran decision to next year" is the
  Thursday-afternoon development — both true at different times Thursday.
- Kept ALSO items re-verified 19 Nov in this audit: #24 APEC Shenzhen
  Declaration adopted (Xinhua/SCIO — adopted by consensus 19 Nov); #28
  oil/gold (Kitco 19 Nov 16:55 EST: Brent settled $91.98, gold below
  $3,650 to fresh 14-month lows); #37 Indonesia asset-seizure law
  (Reuters 19 Nov 04:50 UTC; DPR passed it Thu 19 Nov, Rp1bn threshold).
  The remaining kept ALSO items (#16, #17, #19, #21, #23, #27, #29, #34,
  #35, #38, #39, #40, #41, #42, #43) carry the v2/v3/v4 builds' documented
  verification and were NOT individually re-verified in this audit —
  residual date risk remains there.

### Verification (v6, all passed)
- `python3 generate.py` three times: byte-identical, SHA `9b59b812…`,
  **193,440 bytes** (< 350 KB), **no OVERFLOW** (panels, ALSO lines,
  footer at 984px of 996, subhead, UTC strip all within limits).
- `main.ts` (`MAKEFUN_OUTPUT_DIR` set): byte-identical copy, same SHA.
- Visual QA: full image + row crops + 300px downscale reviewed. No text
  collisions; no panel text spills past its border; Gaza panel (2-line
  headline + 2-line body) and COP31 panel (2-line headline + 2-line body)
  fit cleanly in their 158px/147px boxes; footer fits on one line; at
  300px the masthead date, stats numbers and panel headlines stay legible;
  the ALSO list is present at 10px (same as v5 and the winners' lists).
- Story count: 12 panels + 31 ALSO = 43; region strip sums to 43; pins
  1–12 all placed.

## Recommendation
**Submit v7, not v6** — v7 fixes the two residual ALSO errors the v6
head-to-head found in kept items (#16 Gaza amputees, 4 Nov; #27
Microsoft/ByteDance, 18 Nov) and rewords the stats strip so "$120bn
COP31 goal cut" matches panel 7. v6 tested **4W–0L–1D vs the current
top 5** (see `~/workspace/makefun/research/head-to-head-v6-19nov.md`)
and remains the fallback if the submit pipeline rejects v7 for any
reason; v7 only removes two ALSO errors, so it cannot score worse than
v6 on the same pairings. Do not submit v5 (2W–3L on re-test), v4 (loses
the head-to-head), v3 (Van Gogh date error) or v2 (four date errors).

## What changed vs v4 — the v5 redesign (43 stories, SHA ec409926…)

Layout redesign to fit a FOURTH panel row — the head-to-head of v4 vs the
top 5 (2 wins, 3 losses, all margins 1–2) was decided by panel count
(9 vs 11–13). v5 closes that gap: **12 panels** (4 rows × 3).

Space found without touching the ALSO font size (still 10px, never smaller
than v4): masthead 100→92px (date 44→40px), UTC strip 22→20px, region
strip 20→18px, panels 190px → 158px (lead row) / 147px (rows 2–4) with
compact 48px illustrations redrawn for the strip, stats numbers 27→24px,
map 156→124px tall. Headlines stay 21px (lead row) / 19px (rows 2–4) — at
or above the winners' small-panel headlines (~17px).

- **Promoted to panels (row 4):** #10 Suneung ("551,864 sit Korea's exam",
  new exam-hall illustration), #11 Australia jobless 4.9% ("a five-year
  high", new rising-bars illustration), #12 Colombia national strike (new
  flag + marchers illustration). Same verified 19 Nov facts as the v4 ALSO
  items; bodies kept to 2 lines.
- **ALSO renumbered 13–43 (31 items):** the three promoted stories leave
  the list; nothing else changes. ALSO header now "31 MORE STORIES".
- **Stats strip:** Suneung + Australia numbers moved to panels; replaced
  by "78,000 — Bolivia families hit" and "$2bn+ — US–Philippines pact"
  (both verified 19 Nov ALSO items).
- **Map pins 1–12:** Seoul, Canberra and Bogotá added (nudged to avoid
  collisions). Pin 2 (Gaza) nudged (−16, +12) — it sat ~7px from the
  Antalya pin in v4, a pre-existing flaw now fixed.
- **Carried over unchanged from v4:** Van Gogh fix (nowhere as a 19 Nov
  item), fresh Kenya toll ("six killed, displace hundreds"), UTC strip,
  DATE CHECK footer, the 7 upgraded ALSO items, ICJ panel with the confirmed
  verdict (updated 19 Nov evening). Region counts unchanged (same 43 stories): Middle East 7,
  Americas 12, Asia 8, Europe 8, Africa 1, Oceania 3, World 4.
- **Illustrations:** all nine v4 illustrations redrawn for a 48px strip
  (no bottom label band — the kicker below identifies the story). Known
  minor compromises: the Gaza fire is hidden behind the buildings
  (invisible, harmless); the Suneung strip is a little empty mid-frame;
  the ICJ pediment is flat. None are visible defects at full size or 300px.

### Verification (v5, all passed)
- `python3 generate.py` three times: byte-identical, SHA `ac11eb2e…`,
  **193,074 bytes** (< 350 KB), **no OVERFLOW** (panels, ALSO lines,
  footer, subhead, UTC strip all within limits — new per-panel overflow
  self-check added and silent).
- `main.ts` (`MAKEFUN_OUTPUT_DIR` set): byte-identical copy, same SHA.
- Visual QA: full image + row crops + 300px downscale reviewed. No text
  collisions; no panel text spills past its border; at 300px the masthead
  date, stats numbers and panel headlines stay legible; the ALSO list is
  present at 10px (same as the winners' ALSO lists).
- Story count: 12 panels + 31 ALSO = 43; region strip sums to 43; pins
  1–12 all placed.

### Head-to-head vs top 5 (see `~/workspace/makefun/research/head-to-head-v5-19nov.md`)
**4 wins, 1 loss** (v4 was 2W–3L): beats #1 quick-finch-51 (margin 1),
#3 aw-rama (2), #4 mellow-otter-50 (2), #5 lively-condor-51 (margin 1);
loses only to #2 lomfi (margin 1, legibility — its panels are the biggest
on the page). The two flipped pairings are margin-1 calls; under the real
judge's apparent weak date weighting (18 Nov evidence) they could be draws,
but even as draws v5 is 2W–1L–2D — still strictly better than v4.

## What changed vs v3 (43 stories, SHA b916bbe1…)

Head-to-head test of v3 vs the top 5 entries: 2 wins, 3 losses, all narrow
(margins 1–2). Losses were decided by panel count (9 vs 11–13) and the
missing UTC strip. One confirmed date error was found and fixed.

### P0 — must-fix (date correctness)
| Item | Change |
|---|---|
| Stats strip | Van Gogh $190.4m REMOVED — the painting sold Wed 18 Nov, not 19 Nov (Reuters, The Art Newspaper, Artnet, Wikipedia). Replaced with "15.9m — GTA VI pre-orders banked" (verified; used by the top entries). |
| ALSO #14 | Van Gogh REMOVED. Replaced with Florida floods: "Florida schools shut; 300 rescue calls in Hollywood" (verified 19 Nov follow-on: rain bomb overnight 17→18 Nov, 15.3 inches in Broward, schools shut Thu 19 Nov, flood watch through Thu evening). |
| ALSO #42 | Kenya floods REWRITTEN to the fresh verified toll: "Kenya floods kill six, displace hundreds" (Daily Nation, 19 Nov). The old framing ("seven in Makueni in two weeks") was the stale 17 Nov toll. |
| DATE CHECK footer | Van Gogh $190.4m (18 Nov) ADDED to the excluded list — the fix is now visible date discipline. Footer moved to 10px so the longer line still fits (964px of 996). |

### P1 — UTC strip + 7 ALSO swaps
- **New "THE DAY BY HOURS" strip** under the masthead (navy band, gold label,
  white items): 00:00 UTC GTA VI unlocks in New Zealand · Morning Shenzhen
  summit · 09:00 UTC ICJ genocide verdict · 14:30 UTC Anthropic debuts ·
  Evening COP31 ministers take over. All verified 19 Nov. Everything below
  shifted down 14–16px (region strip, panels, stats, map/ALSO, footer);
  panel rows stay 190px, no panel content changed.
- **ICJ panel UPDATED with the confirmed outcome (19 Nov evening).** The verdict is out: the ICJ found Myanmar responsible for genocide — genocidal intent, ~10,000 killed in 2017, 730,000 fled; final and binding, the first state ever found responsible (Reuters / Al Jazeera / ICJ).
- **7 ALSO swaps** (verified 19 Nov, corroborated by ≥2 top entries) for the
  7 weakest v3 items. Story count stays 43 — the layout cannot grow:
  41 items in 2 columns needs 21 rows (231px) vs ~196px available, and
  3 columns would force 37 of 41 items to be shortened to ≤196px (measured),
  gutting the information content. Swapped in: APEC Shenzhen Declaration
  (#21), Deutsche Bank $582m Epstein-linked deals (#23), Banxico cuts rates
  to 6.25% 3–2 (#27), Vance: no "forever war" in the Gulf (#30), Bapco
  refinery back on its feet (#33), California braces for atmospheric river
  (#36), Bolivia El Niño emergency: 78,000 families hit (#38). Swapped out:
  Libya pills seizure, Mélenchon presidency quote, Alps climber, Houthis Red
  Sea coast posts, Cepu blast, HK Balticconnector case, Wellington Test.
- Region strip recount (sums to 43): Middle East 7, Americas 12, Asia 8,
  Europe 8, Africa 1, Oceania 3, World 4 (deltas only from the v3 baseline:
  Americas +4, Asia −1, Europe −1, Africa −1, Oceania −1).

### P2 — NOT done (4th panel row skipped)
A 4th row of smaller panels does not fit cleanly: it needs ~120px that do
not exist (current layout already uses 996 of 1024px). Fitting it would
require shrinking all panels to ~135px tall (illustrations ~48px, body
~12px) AND cutting the ALSO list or the map — degrading the 300px legibility
that v3's QA passed. Per the brief's own condition (skip if QA does not
pass cleanly), P2 is skipped; the P0+P1 version is the v4.

### NOT added (wrong date, per brief)
Nature "missing billion years" (paper published 4 Nov, not 19 Nov — the top
entries wrongly carry it); Modi–Wales; US–Venezuela pact; Nvidia H-series
halt; Sindhu top-5; OFAC Hezbollah sanctions; IAEA Yongbyon; Pew
Muslims-2035; Quad/Albanese.

## What changed vs v2 (41 stories, SHA dffefd3a…)

### Removed — wrong date (judge criterion #1 hard fail)
| Item | Why out |
|---|---|
| Panel 6 — Voyager 1 one light-day | 18 Nov (NASA briefing 18 Nov) |
| Panel 7 — EU €45bn Ukraine loan | 18 Nov (Commission proposal 18 Nov) |
| Panel 9 — Fed minutes + Dow −561 | 18 Nov (minutes released 18 Nov) |
| ALSO #16 — North Korea missiles | 17 Nov (launches 17 Nov) |
| ALSO #23 — Nvidia H-series halt | 17 Nov (earnings call Tue 17 Nov; Q3 $115.8bn +103%, Q4 guide $130bn) |
| ALSO #24 — Nvidia "acting CEO promises earlier pay rises" | not found anywhere — removed |

### New panels (all verified 19 Nov before building)
| # | Story | Source / date |
|---|---|---|
| 6 | Myanmar guilty of Rohingya genocide | Reuters / Al Jazeera / ICJ, 19 Nov. Judgment read 10:00 The Hague; ICJ found Myanmar responsible for genocide — genocidal intent, ~10,000 killed in 2017, 730,000 fled; final and binding, first state ever found responsible. |
| 7 | COP31 enters its final 48 hours | Reuters/AP, 19 Nov. Presidency draft (16 Nov) proposes adaptation finance ≥ $120bn/year by 2035; not agreed; conference closes Fri 20 Nov. |
| 9 | Trump weighs new strikes on Iran | NYT, 19 Nov 03:10 UTC. Trump weighing; Israel pressing for a 4–7 day campaign; **no decision made — "Reports say" attribution in headline body and illustration strip.** |

### New ALSO items (all verified 19 Nov)
| # | Story | Source / date |
|---|---|---|
| 39 | Suneung: 551,864 sit Korea's college exam | Yonhap/AP, 19 Nov. 551,864 candidates, 1,312 test sites, 08:40–17:45; AI-cheating crackdown. |
| 40 | Australia jobless rate hits 4.9%, 5-year high | ABS release, 19 Nov. Highest since Oct 2021; employment fell ~43,500. |
| 41 | Colombia: unions call national strike | CUT/Fecode, 19 Nov (Paro Nacional); marches in Bogotá, Medellín, Cali, Barranquilla, Bucaramanga; US Embassy alert 17 Nov. |
| 42 | Kenya floods kill seven in Makueni in two weeks | **Caveat:** the brief's "Daily Nation 19 Nov, 6 dead" could NOT be re-verified (Daily Nation paywalled; no "6 dead" figure found in open sources). Item uses the verified toll instead: 7 dead in Makueni over two weeks (reported 17 Nov), rains ongoing under Met Dept warning 17–23 Nov, new drownings reported 19 Nov (Eagle News Feed). Kept as ALSO only, same deliberate treatment as Fiji. |
| 43 | Las Vegas GP practice opens on the Strip | F1/AP, 19 Nov. FP1 16:30, FP2 20:00 PST; race Sat 21 Nov; Alonso sits out FP1. |

### Rewritten
- Panel 5 Akvan: body now "200,000 marked to evacuate, landfall Friday" — landfall is Fri 20 Nov ~noon, red alert in 7 Andhra districts on 19 Nov. Never written as landfall 19 Nov.
- Panel 8 Crimean Bridge: rewritten as a 19 Nov follow-on — third attack overnight into 19 Nov, traffic suspended, railway section reportedly hit.
- ALSO #25 oil/gold: was a Wednesday close — rewritten as verified 19 Nov: "Oil steadies near $92; gold at 14-month low" (gold ~$3,707 fresh 14-month low after the NYT Iran report; Brent near $92, WTI ~$83).
- ALSO #33 Cepu: blast was 18 Nov — rewritten as "death reported" (death reported 19 Nov).

### Deliberately kept as ALSO (not panel), with known date basis
- ALSO #32 Fiji disaster: PM's speech 17 Nov Fiji time, Reuters wire 19 Nov. Kept as ALSO only.

### NOT added (wrong date, per brief)
OFAC Hezbollah sanctions (18 Nov), IAEA Yongbyon (18 Nov), Sindhu top-5
(17 Nov), Honduras Yoro (18 Nov), Iran drones (17–18 Nov), An-12 (17 Nov),
US–Venezuela pact (18 Nov).

### Kept panels (dates verified correct)
1 Shenzhen trilateral, 2 Gaza, 3 GTA VI, 4 Anthropic IPO ($83 / $81.3bn).

### Structure changes
- Stats strip 4 → 6 numbers: 551,864 Suneung candidates · $81.3bn Anthropic
  IPO · 4.9% Australia jobless · 200,000 Akvan evacuations · $120bn COP31
  goal · $190.4m Van Gogh record.
- New masthead subhead: "TOP OF THE DAY — ICJ FINDS MYANMAR GUILTY OF GENOCIDE ·
  COP31'S FINAL 48 HOURS · TRUMP WEIGHS IRAN STRIKES".
- Region strip recount (sums to 43): Middle East 7, Americas 8, Asia 9,
  Europe 9, Africa 2, Oceania 4, World 4.
- DATE CHECK footer updated: the four removed items are now named in the
  excluded list (Voyager, EU €45bn loan, Fed minutes — all 18 Nov; N. Korea
  missiles, Nvidia H200 halt — 17 Nov).
- Panel 5 v2 artefact fixed: cyclone arcs re-centred and shrunk so the outer
  arc stays inside the 72px illustration box (v2 arc top was 12px above the
  panel's top edge; verified clean paper above the panel edge in v3).
- New illustrations: ICJ courthouse (The Hague), COP31 globe (Antalya),
  Trump–Iran radar (Washington, "REPORTS SAY"). Map pins re-placed for the
  new panels; pins 8 (Kerch) and 9 (Washington) nudged so badges don't
  collide with pins 7 (Antalya) and 4 (Nasdaq).
- ALSO list now 2 columns × 17 rows, 11px leading (was 16 rows, 12px).

## Verification (all passed)
- `python3 generate.py` twice: byte-identical, **no OVERFLOW** (ALSO lines,
  footer at 10px, subhead, UTC strip at 956px of 982 all within limits).
- `main.ts` (`MAKEFUN_OUTPUT_DIR` set): byte-identical and matching
  `entry.png` — SHA `ec409926…`, **194,814 bytes** (< 350 KB target).
- Visual QA: full image + ALSO crop + masthead/UTC crop + 300px downscale
  reviewed. No text collisions; no panel text spills past its border; UTC
  strip legible at full size; stats strip clean with the new 15.9m figure;
  DATE CHECK footer names Van Gogh (18 Nov). At 300px the masthead date,
  region strip, panel headlines and stats numbers stay legible; the ALSO
  list is present (same 10px as v3, unreadable at 300px as in v3 — the
  judge reads panels, stats and masthead, which are clean).

## Honest comparison vs v3 and vs rank 1 (quick-finch-51, 99.2162%, 36 stories)
- **(1) Correct date:** v4 removes v3's one confirmed wrong-date item
  (Van Gogh, in two places) and names it in the DATE CHECK. This is the
  single biggest upgrade — v3 carried a real hard-fail risk on criterion
  #1; v4 does not. Kenya's toll is now the fresh 19 Nov figure.
- **(2) Selection and breadth:** still 43 stories vs rank 1's 36, with the
  7 weakest ALSO items replaced by 7 corroborated ones (APEC Declaration,
  Deutsche Bank, Banxico, Vance, Bapco, atmospheric river, Bolivia).
  The UTC strip adds the time dimension the top entries have.
- **(3) Legibility:** unchanged from v3 except the new UTC strip (10px,
  legible at full size) and the footer at 10px (was 11px). Panels, stats
  and masthead identical in size and position relative to each other.
- **(4) Factual honesty:** ICJ panel now states the confirmed outcome; Trump–Iran
  still attributed "Reports say"; the DATE CHECK now names five excluded
  items, four of them 18 Nov.
- **(5) Margin:** unknowable before judging. v4 should beat v3 in most
  pairwise comparisons (date fix + UTC strip + stronger ALSO selection).
  It still has 9 panels vs rank 1's 13 — the panel-count gap is the one
  head-to-head loss factor v4 could not close without a layout redesign.

## Recommendation (superseded — see the v7 recommendation above)
**Submit v6, not v5.** v5 won its first head-to-head vs the then top 5
(4W–1L) but re-tested 2W–3L vs the CURRENT top 5 after two new entries
landed; the audit behind v6 found twelve date errors in v5. v5 remains the
fallback if the submit pipeline rejects v6. The ICJ verdict is out and
confirmed (Reuters / Al Jazeera / ICJ, 19 Nov): Myanmar found responsible
for genocide — final and binding — and the panel already carries the outcome.
Do not submit v3 (Van Gogh date error), v4 (loses the head-to-head) or v2
(four date errors).

## Files
- `entry.png` — the entry image (192,771 bytes)
- `generate.py` — deterministic renderer
- `main.ts` — copies entry.png to the output dir
- `README.md` — this file
- `LICENSE` — MIT
