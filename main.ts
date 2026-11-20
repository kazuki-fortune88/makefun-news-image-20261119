// News-image entry (Node 22, standard library only): the image is the
// entry.png beside this file — a front page summing up Thursday 19 November
// 2026, drawn by generate.py from fixed text, fonts and shapes — and the
// program copies it to /output/entry.png. The gate takes a whole PNG or
// JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly
// the bytes copied. Both runs write the same bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
