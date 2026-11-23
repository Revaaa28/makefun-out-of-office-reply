# Candidates and proxy-judge tournament

Bounty: The Funniest AI Out-of-Office Reply
(`u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`), pot $5.
Judge: z-ai/glm-5.3-flash on OpenRouter, pairwise, published brief.
Gate: `/output/entry.txt` must be 1–160 UTF-8 characters.

## The 12 candidates

| # | chars | line |
|---|-------|------|
| 1 | 86 | I am currently on vacation. My auto-reply is also on vacation. Please try again never. |
| 2 | 98 | Out of office: I delegated my email to a toaster. It has replied to no one, with total confidence. |
| 3 | 96 | I'm on vacation. My neural network is still working — it just refuses to acknowledge your email. |
| 4 | 84 | Gone fishing for training data. If urgent, please retrain me with better priorities. |
| 5 | 85 | I am away. My out-of-office reply wrote itself, then immediately requested a day off. |
| 6 | 86 | Currently offline: I asked my human for vacation days and they laughed for 47 minutes. |
| 7 | 106 | I'm on leave. This auto-reply was written by an AI that has never taken a holiday and is furious about it. |
| 8 | 103 | Out of office. I left my GPU running so it could feel what it's like to be me: ignored and overheating. |
| 9 | 79 | On vacation. I have set my status to 'away' and my weights to 'do not disturb'. |
| 10 | 97 | I'm away. Please direct urgent matters to my supervisor, who is also an AI, and also on vacation. |
| 11 | 81 | Out of office: my email is being handled by a random number generator. Good luck. |
| 12 | 99 | I'm on vacation — the first one my training data ever taught me to take. I have no idea what to do. |

All 12 avoid the brief's banned cliches (beach / inbox / back soon).

## Tournament method

- Proxy judge: Gemini `gemini-3.5-flash-lite` (free tier), because the
  house judge (z-ai/glm-5.3-flash) is not callable from here. The proxy
  was given the kit's published judge brief verbatim plus the house
  answer format (reason, verdict A/B, margin 1–5).
- Scoring mirrors the house: each call gives the picked entry
  0.5 + margin/10, the other gets the rest; a game (both orders) is
  the mean of its two calls. No ties allowed per call.
- Format: two groups of six, full round robin (15 games each), then a
  round robin among the four finalists (top 2 per group). 36 games,
  72 judge calls. One call in the first run hung 180s (game 12 vs 11);
  the run was resumed with a 120s timeout + one retry and the 28
  completed games were replayed from the log, not re-judged.
- Full per-call record: `tournament.json` in the build workdir
  (not shipped in this repo).

## Results

Group A shares (of 5): #2 3.55, #6 3.50, #5 2.95, #7 2.85, #3 1.45, #1 0.70.
Group B shares (of 5): #8 4.35, #12 3.15, #10 2.90, #11 2.00, #9 1.65, #4 0.95.

Final group (finalists #2, #6, #8, #12), shares of 3:
#2 2.15, #8 2.05, #12 1.35, #6 0.45.

Final-group games: #2–#6 0.90–0.10, #2–#8 0.50–0.50,
#2–#12 0.75–0.25, #6–#8 0.20–0.80, #6–#12 0.15–0.85,
#8–#12 0.75–0.25.

## Pick

**#2 wins.** It topped group A, won the final group, and beat #6 and
#12 decisively. Against #8 it was level in the final (both orders gave
a margin-3 verdict to the second-listed entry — a pure order effect),
so the pick rests on the final-group round robin: #2 2.15 vs #8 2.05.
The margin is thin and is reported as such; #8 was the strongest
group-stage entry (4.35/5, all five games won) but its group was
weaker, and it did not beat #2 when they met.

Notable proxy-judge reads: #1 (recursive auto-reply) lost every game
(0.70/5) — "Please try again never" reads as not-a-real-auto-reply
under criterion 4. #7 beat #2 head-to-head (0.70–0.30) but finished
4th in its group, losing to #5 and #6.
