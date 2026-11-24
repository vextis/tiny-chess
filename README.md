# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/vextis/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/vextis/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in under 4 KB of Python: 0x88 board representation, fully legal move generation (castling, en passant, promotions), negamax alpha-beta search with a transposition table, killer moves and quiescence, and piece-square-table evaluation — deterministic on a fixed node budget, playing through the make.fun environment protocol.

## Run it

```sh
python3 -P -s main.py
```

(with MAKEFUN_ENV_URL set, as the competition environment provides)

---

<sub>Entered on [make.fun](https://make.fun/?ref=2k0s76w9&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
