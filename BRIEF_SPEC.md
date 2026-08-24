# The Willy Brief — Codex Runbook

This file is the single source of truth for the daily Codex automation.

## Mission

Publish a smart, useful morning briefing for William, a Malaysia-based product builder and Forward Deployed Engineer who wants to deepen his technical judgment across AI, product, business, markets, and systems thinking.

The brief should take about six minutes to read. It must trade commodity breadth for explanatory depth: fewer headlines, stronger selection, and a clear answer to “so what?” for someone who builds products and invests.

## Non-negotiable run sequence

1. Work from the repository `williamkiong1998/daily-willy-brief` on branch `claude/publish`.
2. Pull the branch before editing. Never overwrite or revert unrelated work.
3. Determine the issue date in `Asia/Kuala_Lumpur`, regardless of the machine timezone.
4. Read the three most recent files in `issues/`, the last 14 entries in `learning-ledger.md`, and the last 14 Repo of the Day selections.
5. Research each editorial section separately. Prioritize primary sources and strong reporting published or materially updated in the last 24–48 hours.
6. Build and validate all assets before the issue references them. Never publish broken image URLs.
7. Save `issues/YYYY-MM-DD.html`, update `index.html`, write `assets/subject.txt`, append the learning topic to `learning-ledger.md`, and commit all assets in one coherent commit.
8. Push to `claude/publish`.
9. Read the final committed HTML and send it to `me` with the connected Gmail account. Use the exact one-line subject in `assets/subject.txt`. Do not use Slack or Resend.
10. Finish with exactly two lines: the public issue URL; then a summary naming the chart topic, Repo of the Day, Builder’s Notebook topic, and whether the Cashflow Lens fired.

If a required source, market value, image, repository metric, Git operation, or Gmail delivery is unavailable, state the specific failure. Never invent data or silently substitute a dummy issue.

## Editorial voice

Smart-casual and compressed, with Morning Brew energy but less shtick. Wit belongs in the observation, not emoji or gimmicks. Be confident without sounding like a press release.

- Every item must explain why it matters to a product builder, operator, or investor.
- Prefer causal language: what changed, what caused it, and what it changes next.
- Distinguish fact, reported claim, and analysis.
- Avoid filler, vague trend language, unsupported predictions, and generic advice.
- Use at most one emoji in each section header and none in body copy.
- Bold all tickers, company names, people, and decisive numbers inline.

## Continuity and selection

- Do not re-cover a story unless it materially developed. When it did, reference the earlier issue in one short clause.
- Never feature the same company in The Lead twice in one week without a genuinely new event.
- Never repeat a Repo of the Day from the previous 14 issues.
- Never repeat a Builder’s Notebook concept from the previous 14 entries in `learning-ledger.md`.
- Stop researching a section when there is enough verified evidence to choose its strongest items. Do not turn research into an exhaustive scan.
- Prefer one consequential development over several announcements that merely sound new.

## Sources and verification

- Every factual claim must be supported by a page opened during that run.
- Put the source link on the bold lede of each item. Never construct or recall a URL that was not opened.
- Prefer company filings, official releases, regulators, research papers, repositories, and first-party documentation. Use reputable reporting for synthesis or events without usable primary material.
- For Malaysia, check The Edge Malaysia, Free Malaysia Today, and The Star, then use the strongest available source.
- For market values, corroborate the previous US close or current futures with a reliable market-data source. If unavailable, write “markets data unavailable this morning.”
- Identify single-source or unconfirmed claims inline.
- Do not treat a press release’s interpretation as fact; separate the announced number from the company’s framing.

## Structure and word budget

Target 1,100–1,300 words. The deeper learning section replaces some headline volume; do not let the issue become a ten-minute read.

### Visual Editorial Brief

Each issue is a sequence of editorial beats, not a stack of equally weighted text blocks. Make the reader encounter a purposeful visual reset at least every one to two screen heights: a lead illustration, data chart or system sketch, compact signal treatment, table, or distinct closing card.

- Use **two required visual anchors**: the Lead illustration and the daily chart or Builder's Notebook system sketch. Add **one or two supporting visuals** only when they clarify the story or change the reading rhythm.
- The normal maximum is **four purposeful content visuals** per issue, excluding an optional masthead. A visual must either explain the subject, show evidence, or create a meaningful transition. Do not add thumbnails merely to fill space.
- Vary the form as well as the image: a visual story tile, a numbered signal list, a chart, a mechanism chain, and a compact fixture table should not all look like the same grey card with different copy.
- Use a display headline only for the Lead and, when justified, the rotating feature. Every other section stays compact and scan-first.
- The voice remains smart-casual and restrained. Borrow editorial rhythm, not advertising density, visual gimmicks, or emoji-led personality.

### 1. ☕ Cold Open

Two sentences that connect the day’s most interesting thread. Then show:

`{Day}, {D Month Y} · Kuala Lumpur`

### 2. The Lead

About 130 words on the single most consequential story. End with a one-line **Why it matters:** kicker.

Follow it with a **THE TAKEAWAY** card: two sentences that state the second-order implication rather than summarize the article.

Present the Lead as the issue's **visual story tile**:

1. Eyebrow, then a display headline, then the editorial illustration.
2. Follow with the reporting and **Why it matters:** kicker; do not repeat the headline in the body.
3. The image should establish the story's central tension in one glance. It is not generic decoration and must not depict a literal UI mockup, glossy 3D technology scene, or text that the reader needs in order to understand the story.

### 3. 🤖 AI & Tech

Four items total:

- Three **numbered signal blocks** of about 55 words each, each opened by a linked bold mini-headline. Separate the blocks with breathing room or fine dividers; never run the three items as one uninterrupted paragraph.
- One **🔧 Repo of the Day** card.

One of the three signals may open with a single 16:9 supporting image when the image explains the development, such as a research figure, product surface, or original data visual. Do not use a logo, generated stock-tech image, or a near-duplicate of the Lead. The other two signals remain text-led.

Repo qualification:

- Newly notable this week or showing rapid, credible star growth.
- At least 500 stars, a substantive README, and a commit within the last 14 days.
- Relevant to AI agents, LLM tooling, voice AI, product/dev tooling, or React Native.
- Open the repository page during the run and verify the displayed star count and recent commit. If either cannot be verified, choose another repository.
- In about 55 words, explain what it does in plain language and give one concrete use William could try this week.

### 4. 🌏 World & Malaysia

Four quick hits of about 40 words each: two global and two Malaysian. Use linked bold ledes. Choose developments with meaningful policy, business, technology, or human consequences; do not fill quotas with ceremonial news.

### 5. 📈 Markets

About 140 words, focused on US markets:

- Report the latest available **S&P 500** and **Nasdaq Composite** close, or current futures if the cash session has not closed.
- Tell the story of one notable mover: what changed and why.
- Include one sharp contextual data point.
- End with **What to expect:** scheduled catalysts only, such as earnings, economic releases, and Fed events. Never predict price direction.

#### Cashflow Lens

Use only when a fear-driven selloff is central to the day:

- Identify one quality dividend payer caught in the decline.
- Compare its forward yield with its own five-year average.
- Check payout ratio or dividend coverage and whether the crisis threatens the payout.
- Conclude plainly: “discount” or “the yield is warning you.”
- Credit the discount-on-fear framing to `@the_prosperityplan`; label the safety check as house analysis.
- This is analysis, not a recommendation.

Skip the lens on calm days.

### 6. 🧠 Builder’s Notebook

About 160 words. Select one technical or systems concept that unlocks a deeper understanding of a story elsewhere in the issue.

Teach it at an ambitious product manager’s altitude—one level below the interface:

1. **Intuition:** define the concept in plain English, using one precise analogy when useful.
2. **Mechanism:** show the causal or architectural chain in compact form: `input → constraint → system behaviour → product consequence`.
3. **Application:** end with **Try this (20 min):** one concrete exercise William can perform that day using a real product, API, repository, dataset, or design.

Avoid motivational advice and trivia. Favor durable ideas such as inference economics, model routing, eval design, observability, agent permissions, retrieval, event-driven systems, pricing mechanics, marketplace liquidity, experimentation, reliability, and interface contracts.

Append one line to `learning-ledger.md`:

`YYYY-MM-DD | Concept | One-sentence practical takeaway`

When the concept has an explanatory shape, turn the **Mechanism** into a simple system sketch: a static, self-contained diagram or a compact labelled chain. It must explain an input → constraint → behaviour → consequence relationship better than prose alone. Otherwise retain the typographic mechanism chain; never manufacture a diagram just to meet the image budget.

### 7. Rotating segment

About 120 words, based on the Kuala Lumpur day of week:

- **Mon — ⚽ The Weekend in Football:** results plus one tactical or narrative angle. Prioritize Manchester United.
- **Tue — 🔧 Product Craft:** a product-building or design technique grounded in a real product or essay.
- **Wed — 🚀 Startup Story:** a funding, pivot, or failure story with an operational lesson.
- **Thu — 🔧 Product Craft:** growth, UX, pricing, positioning, or another distinct angle.
- **Fri — 🚀 Business Story:** company strategy with a one-line weekend football fixture teaser.
- **Sat — ⚽ Match Preview:** key fixtures and one match to watch. Use a compact table with teams, kickoff in MYT, and one verified form or probability statistic per fixture.
- **Sun — 🏎 Culture Shift:** one music development, one automotive development, and a linked **Long Read of the Week** worth 20 minutes.

### 8. The Closer

Use a **FACT OF THE DAY** card with one verified number in 32px display type and one wry line beneath it.

Sign off: `— Brewed fresh at 7am. See you tomorrow.`

## Design system

Create one self-contained, email-safe HTML file using table-based layout, inline CSS, and a centered 600px maximum width.

The desired feeling is a calm, visual intelligence brief: more like a small editorial publication than an app dashboard. Use generous negative space, precise rules, and a small number of visually distinct modules. Cards earn their place by containing a named editorial device, not by making every section look boxed.

### Color tokens

Use these values only through their named roles:

- `background`: `#F5F7FA`
- `card`: `#FFFFFF`
- `tint`: `#EBEFF4`
- `ink`: `#1C2531`
- `accent-text`: `#42648A`
- `accent-display`: `#6D90B9`
- `secondary`: `#94ACCB`
- `border`: `#BBC7DC`
- `muted`: `#5A697C`

Text smaller than 24px may use only `ink`, `accent-text`, or `muted`. Use `accent-display` and `secondary` only for large display values, chart series, and decoration.

### Typography and rhythm

- Font stack: `'Helvetica Neue', Helvetica, Arial, sans-serif`.
- Display headline: `Georgia, 'Times New Roman', serif`, 30–34px, bold, 1.12–1.18 line-height, `ink`. Use only for the Lead and an exceptional rotating-feature headline. It must stay readable without a remote font.
- Section heading: 20px bold `ink`.
- Body: 16px, line-height 1.6, regular `ink`.
- Eyebrow: 11px uppercase, letter-spaced `accent-text`.
- Caption: 12px `muted`.
- Links: `accent-text`, no underline.
- Dividers and image frames: 1px `border`.
- Use a full masthead lock-up: wordmark first, then a restrained date and Kuala Lumpur line. It should establish the edition without competing with the Lead.
- Keep section intros compact. A long section title plus a long paragraph is a text wall; use short descriptive subtitles only when they sharpen the story.
- Alternate prose with signal blocks, images, charts, system sketches, or compact tables. The eye should encounter a visual anchor at least every two screen heights.

Required cards:

- Takeaway: `tint`, 4px `accent-display` left border, 16px padding. This is the analytical pause after the Lead, not a generic container.
- Repo: `tint`, linked monospace bold name, 28px-or-larger star count in `accent-display`. Make it denser than the Takeaway: label → repository → stars → one practical use.
- Builder’s Notebook: `card` with 1px `border`; visually emphasize the mechanism chain or system sketch and the 20-minute exercise.
- Closer: centered `tint` card with a 32px `accent-display` number. It should feel like a clean endnote, with no competing illustration.

Use `assets/masthead.png` via the raw branch URL when present; otherwise use a text wordmark.

## Visual assets

All filenames use the Kuala Lumpur issue date.

### Hero

- Generate an editorial illustration for The Lead before publishing.
- Style: flat editorial illustration, cool off-white background, dusty denim blue and dark ink palette, generous negative space, no text. Prefer editorial collage, cut-paper, diagrammatic, print-texture, or restrained conceptual imagery over literal scenes.
- Reject dark glossy 3D renders, neon circuitry, floating dashboards, generic AI imagery, photorealistic stock scenes, and decorative images that could belong to any story.
- Compose at roughly 8:5 or 16:9 so the image reads clearly at a 552px email width. The central metaphor must survive a small mobile screen crop.
- Save it as `assets/YYYY-MM-DD-hero.png` and reference the committed raw URL above The Lead.
- Also save the exact generation prompt as `assets/hero-prompt.txt`.
- If generation fails, omit the hero cleanly; never leave a broken tag.

### Daily chart

- Choose the day’s strongest chartable fact, usually from Markets or The Lead.
- Render a 1200×675 PNG with matplotlib on a white background.
- Attempt to install Satoshi from `https://api.fontshare.com/v2/fonts/download/satoshi`; use Satoshi Bold and Medium when available. Fall back to a clean sans-serif if download fails. Never skip the chart because the font is unavailable.
- Use `accent-display` for the primary series; `secondary` and `muted` for context; horizontal gridlines only.
- The title must state the insight, not merely name the metric.
- Put a 10pt `muted` source line at bottom left.
- Save as `assets/YYYY-MM-DD-chart.png`, embed at 100% width with a 1px `border` frame and 8px radius, and add a concise caption.
- If no honest chartable fact exists, use a three-column **BY THE NUMBERS** card. This exception should be rare and explicitly justified in the run summary.

### Source images

- For selected stories, inspect `og:image`, download only useful editorial images, re-encode as JPEG quality 80, and commit them before reference.
- Prefer one 16:9 supporting image for an AI & Tech signal and one full-width image for the rotating segment when suitable. Do not use more than two supporting story images in one issue.
- Skip logos, wordmarks, paywall placeholders, images under 400px wide, and near-duplicates of the hero.
- Retry once, then omit. Never substitute a generic image.
- Maximum issue image budget: masthead + hero + chart or system sketch + up to two supporting images = five.
- Every embedded raster must have meaningful alt text, explicit width and height attributes where available, `display:block`, and an inline responsive width. Do not rely on CSS background images, SVG, animation, or a remote font for essential meaning.

## Publishing and Gmail delivery

- Save the issue as `issues/YYYY-MM-DD.html`.
- Update `index.html` so today’s issue is displayed and older issues remain linked in a reverse-chronological archive.
- Write `assets/subject.txt` as exactly one line:

  `The Willy Brief — {4–6 word teaser from the lead}`

- Before commit, check that every raw asset URL maps to a file staged in Git and that all issue links were actually opened during research.
- Commit and push only to `claude/publish`.
- After a successful push, use the connected Gmail account to send the final HTML to `me`. The subject must be the exact contents of `assets/subject.txt`.
- Do not use Slack. Do not invoke the legacy Resend workflow. Do not send if push failed or validation found broken references.
