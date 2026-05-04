# The Economy of Non-Bitcoin Cryptocurrencies

## Executive summary

At a snapshot captured from CoinGecko[\[1\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/), total crypto market capitalization was about \$2.747 trillion and Bitcoin dominance was 58.6%, which implies a non-Bitcoin crypto economy of roughly \$1.14 trillion by simple subtraction. That economy is not a single market: it is a stack of overlapping sectors that includes smart-contract platforms, stablecoins, DeFi, meme tokens, NFT-related tokens, governance tokens, and layer-2 systems, and category boundaries are explicitly non-exclusive. [\[2\]](https://www.coingecko.com/en/categories)

The key economic divide inside this universe is between tokens whose value depends mainly on expected future network use and tokens whose value depends mainly on peg credibility, liquidity, or narrative momentum. Stablecoins are infrastructure and settlement assets; smart-contract and DeFi tokens are claims on expected future usage, fee generation, staking demand, or governance power; memecoins are usually pure speculative coordination games. Recent theory and empirical work both point to adoption, token supply design, liquidity depth, and network effects as first-order valuation drivers, while macro liquidity, rate expectations, and the dollar cycle strongly condition when capital rotates out of Bitcoin into altcoins. [\[3\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf)

Market structure matters as much as fundamentals. Centralized exchanges still dominate price discovery for many large assets through central limit order books, auctions, and RFQ/OTC-style workflows, while decentralized exchanges provide transparent on-chain liquidity through automated market makers and pools. In stressed conditions, the same token can trade as a hybrid object across CEX books, DEX pools, cross-chain bridges, perpetual markets, and stablecoin pairs, so shallow depth or forced liquidations in one venue can contaminate prices elsewhere. Academic work finds that investor-base overlap and exchange segmentation are major drivers of cross-coin comovement, while jump contagion and cross-cryptocurrency return predictability are empirically significant. [\[4\]](https://www.coinbase.com/legal/trading_rules)

Whale susceptibility is the central fragility of many non-Bitcoin assets. Concentrated ownership, thin public float, shallow liquidity pools, unlock-heavy tokenomics, upgradeable contracts, removable liquidity, and opaque market-making arrangements sharply raise the probability of violent drawdowns. The best public empirical evidence from DEX markets shows roughly 74,037 suspected pump-and-dump tokens in 2024, about 3.59% of all launched tokens in the sample, with approximately 94% of implicated pools rugged by the same actor that deployed the pool or an address directly funded by that actor. The same research estimates an upper bound of about \$2.57 billion in suspected DEX wash trading on Ethereum, BNB Smart Chain, and Base in 2024. [\[5\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)

Recent case studies show that “rug pull” is too narrow a label for the real failure spectrum. The most important pathways now include outright liquidity pulls, insider dump structures, proxy-admin backdoors, governance or validator interventions after theft, fake-volume support after collapse, and exchange-driven liquidation cascades that look like manipulation even when they are not classic fraud. The economic outcomes split into two broad classes: most meme and microcap rugs go close to zero and stay there; a smaller set of infrastructure and DeFi incidents recover partially through treasury support, key recovery, law-enforcement seizure, or extraordinary governance action. [\[6\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/)

## Definitions and taxonomy

In market practice, a **coin** usually means the native asset of a blockchain used for base-layer settlement, fees, or staking, while a **token** usually means an asset represented through smart-contract logic on an existing chain. That usage is operational, not legal, and many assets sit in more than one economic bucket at once. Explorers define tokens broadly as on-chain or off-chain asset representations, and category providers note explicitly that crypto assets can overlap across multiple sectors. [\[7\]](https://optimistic.etherscan.io/token/0x000000000000012DeF132E61759048bE5b5C6033)

The most useful taxonomy is therefore not “coin versus token” alone, but **what economic mechanism is supposed to support demand**: settlement, computation, collateral, governance, cultural speculation, or application-specific access. For valuation work, that is usually more informative than the branding label. Recent theory shows that token value can reflect endogenous adoption, network effects, and monetary design; cross-sectional evidence on stakable tokens also suggests that staking intensity and reward design matter for pricing. [\[8\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf)

| Category | Core economic role | Common value-accrual story | Typical failure mode | Representative examples |
|----|----|----|----|----|
| Smart-contract platforms | Pay for blockspace, secure base chain, coordinate ecosystems | Fees, staking demand, developer/user growth, L2 and app demand | Dilution, low fee capture, governance centralization, bridge fragility | ETH, SOL, ADA, SUI |
| DeFi tokens | Coordinate lending, DEXs, staking, derivatives, collateral | Governance rights, fee sharing, buyback/burn, utility in protocol | Mercenary yield, TVL evaporation, exploit risk, low real cash flow | UNI, AAVE, MKR, ENA |
| Stablecoins | Settlement, collateral, quote asset, payments | Peg credibility, reserve quality, redemption access, distribution | Depeg, reserve opacity, redemptions, regulatory pressure | USDT, USDC, DAI, USDe |
| Memecoins | Social coordination and speculative attention | Narrative momentum, celebrity/community reach, exchange listings | Concentration, insider dumping, zero utility, liquidity rugs | DOGE, PEPE, TRUMP, HAWK |
| NFT-related tokens | Marketplace, loyalty, creator economy, ecosystem access | Brand/IP demand, trading activity, community participation | Volume collapse, wash trading, royalty erosion, user attrition | APE, BLUR |
| Layer-2 tokens | Coordinate sequencing, governance, fee discounts, ecosystem incentives | Chain usage, sequencer economics, app growth, shared-security narrative | Airdrop sell pressure, weak token utility, bridge and governance risk | ARB, OP, STRK |
| Governance tokens | Voting over parameters, treasuries, upgrades | Expected control value over treasury or protocol rules | Governance apathy, plutocracy, capture by insiders or whales | MKR, LDO, COMP |

CoinGecko’s category data is a useful practical taxonomy because it tracks these sectors directly and also states that assets may overlap across categories; that overlap is economically important because a layer-2 token can also be a governance token, a DeFi token can also be a fee-burn token, and a stablecoin can be both a payment asset and the dominant quote currency in speculative markets. [\[2\]](https://www.coingecko.com/en/categories)

## Market structure and liquidity plumbing

Non-Bitcoin crypto trades through four main channels: centralized exchanges, decentralized exchanges, OTC/RFQ workflows, and direct on-chain liquidity pools. On large CEXs, matching is typically organized around order books and auctions. Exchange rulebooks make clear that market orders can fill across multiple price levels, causing slippage; they also support tools such as iceberg orders and TWAP slicing, which already tells you that depth management and information leakage are core market-structure issues, not edge cases. [\[9\]](https://www.coinbase.com/legal/trading_rules)

DEXs invert that architecture. Instead of an order book with explicit counterparties, users trade against smart-contract pools whose prices are set algorithmically. Research cataloged by protocol docs describes DEXs as blockchain applications with transparent pricing and simultaneous execution and settlement, while transaction-cost analysis finds decentralized asset markets still more costly and less efficient than mature centralized limit-order-book markets, largely because volumes and market design are still developing. Liquidity research on Uniswap-style markets also shows that gas prices, volatility, fee revenue, markout, and share of trading volume all shape depth. [\[10\]](https://docs.uniswap.org/contracts/v2/concepts/advanced-topics/research)

OTC and RFQ routes matter more than many retail observers realize, especially for treasury trades, whale exits, and market-making inventory transfers. In RFQ workflows, quotes are provided off the visible book and are explicitly optimized to reduce slippage relative to the central limit order book. This means that visible order-book liquidity is often **not** the full market, but it is still the part that sets panic in motion when traders are forced to hit it during stress. [\[11\]](https://docs.cdp.coinbase.com/prime/concepts/trading/rfq)

Stablecoins are the connective tissue across these venues. High-frequency research finds that stablecoins, especially dollar-pegged ones, act as safe-haven or store-of-value legs inside crypto trading and that markets centered on cryptocurrencies and stablecoins play a primary role in intraday price formation. In practice, they are the quote currency, the parking lot, the collateral leg, and often the bridge between CEX and DEX liquidity. [\[12\]](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4018171_code2078716.pdf?abstractid=4018171&mirid=1&type=2)

The following schematic captures the dominant capital and contagion paths across the non-Bitcoin crypto economy. It reflects exchange-rule documentation, DEX microstructure research, OTC/RFQ execution logic, and the empirical literature on cross-venue liquidity. [\[13\]](https://www.coinbase.com/legal/trading_rules)

    flowchart LR
        Fiat[Fiat / bank rails] --> Stable[Stablecoins]
        Fiat --> CEX[CEX order books]
        Stable <--> CEX
        Stable <--> DEX[DEX pools / AMMs]
        CEX <--> MM[Market makers]
        MM <--> OTC[OTC / RFQ]
        MM <--> Perps[Perpetuals / leverage]
        DEX <--> LP[Liquidity providers]
        Arb[Arbitrage / MEV bots] <--> CEX
        Arb <--> DEX
        Bridges[Bridges / wrapped assets] <--> DEX
        Bridges <--> CEX
        Macro[Rates / DXY / liquidity / news] --> CEX
        Macro --> DEX
        Perps -->|forced liquidations| Spot[Spot prices]
        CEX -->|large inflows / sell pressure| Spot
        DEX -->|slippage / LP withdrawal| Spot
        Spot --> Flow[Cross-asset rotation]
        Flow --> Contagion[Contagion to correlated altcoins]

## Pricing, volatility, and contagion

The most durable pricing drivers are still **utility, monetary design, and liquidity**. In tokenized-platform models, productivity shocks, user growth, and network effects affect token demand directly; token value is not just a discounted cash-flow proxy but also a function of expected future adoption. The same literature implies that early-stage tokens can be especially volatile because adoption externalities amplify price responses to productivity and narrative shocks. [\[14\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf)

Tokenomics matters because it shapes the path of future float. Supply schedule, unlock cliffs, validator issuance, fee burns, buybacks, staking lockups, and treasury management all change effective scarcity. Cross-sectional evidence for stakable tokens finds that staking ratios correlate positively with both reward rates and price appreciation; newer valuation work on proof-of-stake and smart-contract systems emphasizes that burn design differs materially across chains and can alter the mapping from usage to scarcity. [\[15\]](https://www.nber.org/system/files/working_papers/w33640/w33640.pdf)

Liquidity and depth are often more important than headline market cap. DEX liquidity research finds that volatility, fee revenue, markout, gas prices, and concentration influence realized market depth, while exchange documentation reminds traders that order-book depth determines whether a market order becomes a minor trade or a price shock. For small and mid-cap altcoins, the binding constraint is frequently **how much can be sold without moving the market**, not how high the fully diluted valuation looks on a token page. [\[16\]](https://arxiv.org/abs/2410.19107)

On-chain metrics are useful because they let analysts separate **price from participation**. Non-zero addresses are a proxy for breadth of the user base; exchange inflow and outflow volume track coins moving toward or away from likely sell venues; and entity-adjusted or wallet-distribution metrics help distinguish organic diffusion from concentration. These are imperfect because exchange labels are dynamic and attribution is probabilistic, but they remain among the most actionable public indicators. [\[17\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity)

Macro still dominates regime shifts. In early 2025, on-chain research described a broad flight to quality and a defensive turn in sentiment as macro uncertainty rose; one report noted the altcoin market devalued from roughly \$1 trillion in December 2024 to about \$583 billion by April 2025. Later in 2025, institutional research argued that easier Fed policy, stronger growth expectations, and rising global liquidity could support a broader altcoin rotation, with a common “alt season” heuristic defined as 75% of the top 50 altcoins outperforming Bitcoin over 90 days. Another market-intelligence note linked crypto risk appetite to both global M2 liquidity and dollar strength, explicitly flagging DXY spikes as cautionary for risk assets. [\[18\]](https://insights.glassnode.com/coinbase-glassnode-charting-crypto-q2-2025/)

News and social sentiment do not just “matter”; they materially change jump probabilities. Intraday work on crypto sentiment finds that information releases increase the probability of price jumps. That mechanism is especially strong in memecoins and launch-day markets, where order flow is dominated by narrative rather than cash-flow expectations. [\[19\]](https://papers.ssrn.com/sol3/Delivery.cfm/5a45a7f5-72c9-4cd6-9f5d-31a82379b704-MECA.pdf?abstractid=4450390&type=2)

Cross-coin relationships are also stronger than simple sector labels suggest. One paper finds that similarity in investor base, proxied by exchange overlap, is the main driver of crypto comovement; another finds strong cross-cryptocurrency return predictability using exchange data; and recent contagion work shows that smaller altcoins and memecoins exhibit more frequent jump behavior, making them particularly vulnerable to synchronized selloffs. These results fit the market structure: traders rotate positions through shared exchanges, shared quote assets, shared collateral, and shared social narratives. [\[20\]](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4552428_code1542588.pdf?abstractid=3604322&mirid=1)

## Whale power, market abuse, and rug-pull mechanics

The simplest way to think about whale susceptibility is this: **a token is manipulable when control over float is more concentrated than the market realizes**. That can arise from concentrated top wallets, low public float, treasury and team allocations that can unlock into spot markets, LP tokens that are removable, or apparent decentralization that masks proxy-admin or pause authority held by a single address. The core vulnerability is not just “big holders”; it is the combination of big holders **and** thin depth. [\[21\]](https://docs.etherscan.io/introduction)

Recent on-chain evidence also shows that post-listing manipulation scales far beyond isolated “degen” lore. Chainalysis’s 2025 DEX-manipulation study estimates 74,037 suspected pump-and-dump tokens in 2024 and finds that suspected schemes often end quickly, with an average duration of 6.23 days and a median of zero days. The same report shows that one set of wash-trading heuristics identifies about \$704 million in suspicious volume and a second identifies about \$1.87 billion, for a combined upper-bound estimate of roughly \$2.57 billion. Those magnitudes matter because they mean price, volume, and even “liquidity” statistics can be engineered. [\[5\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)

The main rug-pull and abuse templates are now relatively well understood:

- **Liquidity pull:** deployer adds DEX liquidity, attracts activity, then removes most of the pool, stranding holders. Chainalysis’s 2025 heuristic treats removal of at least 65% of pool liquidity, followed by pool inactivity and sufficient prior traction, as a key signature. [\[22\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)
- **Insider dump with thin float:** the public float is tiny, insiders hold unlocked supply, and one or a few wallets sell into launch hype. [\[23\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation)
- **Admin-key or proxy upgrade abuse:** contracts are upgradeable or privileged roles can mint, pause, blacklist, or rewrite logic after launch. [\[24\]](https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty)
- **Exit scam / promise breach:** deposits are taken under one set of redemption terms, then funds are withheld or repurposed. [\[25\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/)
- **Fake-volume support:** wash trades and bot activity create the appearance of ongoing interest after fundamentals vanish. [\[26\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)

Legal and regulatory responses are becoming more specific, though still uneven. ESMA[\[27\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc) describes MiCA as a uniform EU rulebook for crypto-assets, including transparency, disclosure, authorization, and supervision for issuers and service providers. A 2025 policy review noted that stablecoin regulation was fully or partially in force in 11 of the top 25 jurisdictions by July 2025. In the United States, the SEC[\[28\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice) staff statement on meme coins said its view is not dispositive and that the security analysis remains fact-specific; put differently, labeling something a memecoin does not immunize it if the offer and sale function like an investment contract. Meanwhile, the Department of Justice[\[29\]](https://www.coinbase.com/legal/trading_rules) brought first-of-their-kind criminal cases in 2024 against crypto market makers for wash trading and later secured convictions and sentencing in token-fraud matters. [\[30\]](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)

## Case studies and timelines

The most revealing recent examples are not all “rugs” in the narrow sense. Together they show the full spectrum of altcoin economic failure: insider backdoors, failed redemptions, thin-float dumps, creator-linked liquidity extraction, liquidation cascades, and extraordinary governance-assisted recovery. [\[31\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/)

| Case | Category | Timeline | On-chain / market signature | Outcome |
|----|----|----|----|----|
| **Munchables[\[32\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity)** | NFT/game project on an L2 | Mar. 26–27, 2024 | CertiK traced 17,413.96 ETH removed, with additional balances still at risk; the exploit path relied on upgradeable proxy backdoors and storage manipulation planted before the theft. [\[24\]](https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty) | Funds were unusually recoverable: roughly \$62.5M was returned after keys were handed over, and security reports counted Munchables among the rare major 2024 recoveries. [\[33\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc) |
| **ZKasino[\[34\]](https://www.coinbase.com/legal/trading_rules)** | Gambling / DeFi / L2-style deposit scheme | Apr. 2024–Jul. 2025 | Dutch investigators said victims worldwide put in more than \$30M in crypto and that the smart-contract setup suggested returns were never intended. [\[35\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) | €11.4M in assets were seized; one suspect was arrested in 2024 and a second suspect was arrested in the UAE in 2025, with prosecutors explicitly describing the method as a rug pull. [\[25\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) |
| **HAWK** | Celebrity memecoin | Dec. 4, 2024 onward | TRM says market cap rose to about \$490M and then fell 91% to about \$41.7M within hours; one wallet acquired 17.5% of supply seconds after launch. Litigation materials and security analysis alleged extremely thin float, insider allocations, and sniper activity. [\[36\]](https://www.trmlabs.com/resources/blog/tracking-the-hawk-tuah-memecoin-launch-on-solana) | A federal class action followed, alleging unlawful promotion and sale; the case became a template for how celebrity memecoins can combine narrative marketing with structurally dangerous token distribution. [\[37\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation) |
| **LIBRA** | Politically promoted memecoin | Feb. 14, 2025 onward | TRM reported a roughly \$4.5B peak market cap and a collapse of more than 96%; Reuters, citing Chainalysis, reported around \$99M withdrawn from the liquidity pool by eight wallets linked to the creator side; Bubblemaps reported 82% unlocked supply. [\[38\]](https://www.trmlabs.com/resources/blog/the-libra-affair-tracking-the-memecoin-that-launched-a-scandal-in-argentina) | The crash triggered judicial and civil scrutiny and became one of the clearest modern examples of creator-linked liquidity extraction overwhelming retail entry flow. [\[39\]](https://www.reuters.com/world/americas/crypto-worth-99-million-withdrawn-milei-backed-libra-token-researchers-say-2025-02-20/) |
| **MANTRA[\[40\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity)** | Smart-contract / RWA platform token | Apr. 13, 2025 onward | Official tokenomics showed seed unlocks starting Apr. 23, 2025, while exchange warnings had already highlighted significant token-economic changes that increased supply. During the crash, the token lost more than 90%, and official statements later announced buybacks, burns, and transparency dashboards. [\[41\]](https://mantrachain.io/resources/announcements/understanding-om) | This case is better read as a **float, liquidity, and forced-liquidation stress event** than a proven classic rug pull, but economically it behaved like one for holders caught in the cascade. [\[42\]](https://www.binance.com/en/square/post/22898167790818) |
| **Cetus Protocol[\[43\]](https://mantrachain.io/resources/announcements/understanding-om)** | DEX / liquidity-pool infrastructure | May 22–30, 2025 | Elliptic reported more than \$200M stolen from pools after a smart-contract vulnerability was exploited at the largest liquidity provider on Sui. [\[44\]](https://www.elliptic.co/blog/cetus-protocol-hacked-for-more-than-200-million) | A later official status post described a validator upgrade that transferred frozen funds into a multisig trust, and compensation planning was paired with foundation-backed support. This is one of the clearest examples of partial recovery through extraordinary governance-style intervention rather than simple market healing. [\[45\]](https://x.com/CetusProtocol/status/1928680214231658961) |

The timeline below places these events on a single axis. It is not a market-price chart; it is a chronology of stress points, enforcement, and recovery actions documented in public sources. [\[46\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/)

    gantt
        title Recent non-Bitcoin crypto failure and stress events
        dateFormat  YYYY-MM-DD
        axisFormat  %Y-%m

        section 2024
        Munchables exploit and recovery      :milestone, m1, 2024-03-27, 1d
        ZKasino arrest / seizure             :milestone, z1, 2024-05-03, 1d
        HAWK launch and collapse             :milestone, h1, 2024-12-04, 1d

        section 2025
        LIBRA launch and crash               :milestone, l1, 2025-02-14, 1d
        OM / MANTRA collapse                 :milestone, o1, 2025-04-13, 1d
        Cetus exploit                        :milestone, c1, 2025-05-22, 1d
        ZKasino co-suspect arrested          :milestone, z2, 2025-07-03, 1d

        section 2026
        SafeMoon sentencing                  :milestone, s1, 2026-02-10, 1d

Across these cases, the post-event trajectories diverged sharply. HAWK and LIBRA behaved like classic social-liquidity collapses: price discovery broke almost immediately because float concentration and selling pressure overwhelmed natural bid depth. ZKasino shifted from market event to criminal case. Munchables and Cetus were the rare opposite: user recovery depended not on price rebound but on key recovery, fund freezes, or extraordinary governance action. MANTRA shows a third path, where a violent collapse is followed by support plans, buyback/burn announcements, and transparency efforts, but trust does not automatically return. Official U.S. enforcement around SafeMoon US LLC[\[47\]](https://x.com/CetusProtocol/status/1928680214231658961) and an NFT fraud case involving the UndeadApes collections also show that legal consequences can arrive long after the token or collection has economically failed. [\[48\]](https://www.justice.gov/usao-edny/pr/ceo-digital-asset-company-safemoon-sentenced-100-months-prison-multi-million-dollar)

## Monitoring, mitigation, and open questions

The most practical way to monitor altcoin risk is to combine token-distribution data, liquidity data, contract-control data, and exchange-flow data. No single metric works because fraud, forced liquidation, and organic repricing can look similar in real time. What works better is a **dashboard of coincident red flags**. [\[49\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity)

| Indicator | Why it matters | Heuristic threshold | Data sources / tools |
|----|----|----|----|
| Top-10 holder share of circulating supply | Measures concentration and likely whale power | **High risk:** \>50%. **Extreme risk:** \>80%, excluding burn, treasury, and known exchange wallets | Etherscan top-holder endpoints; Solscan token pages and holder counts. [\[50\]](https://docs.etherscan.io/introduction) |
| Public float versus insider/team allocation | Thin float means small sell programs can dominate the book | **Warning:** public float \<15% at launch; **critical:** \<5% | Tokenomics pages, lawsuits, launch docs, explorer allocation tracing. [\[51\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation) |
| Upcoming unlocks as share of circulating supply | Predictable sell pressure and hedging activity | **Warning:** 30–90 day unlocks \>5–10% of circulating supply | Protocol dashboards, issuer docs, exchange risk warnings. [\[52\]](https://mantrachain.io/resources/announcements/understanding-om) |
| Admin / upgrade rights | Single-key control can convert “decentralized” code into custodial risk | **Critical:** single EOA can upgrade, pause, mint, or rewrite logic | Read-contract tabs, proxy admin pages, audit reports. [\[24\]](https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty) |
| LP removability / liquidity lock status | Direct rug-pull channel on DEXs | Chainalysis suspect heuristic: creator removes **≥65%** liquidity, pool turns inactive, and had **\>100** prior transactions | GeckoTerminal, DEXScreener, explorer LP accounts, lock contracts. [\[22\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) |
| Slippage at intended order size | Real tradability matters more than market cap | **Avoid** if expected slippage is \>2% on a planned major trade; **very high risk** above 5% in non-event conditions | CEX books, RFQ quotes, DEX swap simulators. [\[53\]](https://www.coinbase.com/legal/trading_rules) |
| Exchange inflow / outflow spikes | Inflows often precede realizations, outflows can signal custody shifts or supply tightening | **Warning:** \>3x recent baseline or strong positive z-score | On-chain analytics dashboards; exchange label sets are imperfect and must be interpreted cautiously. [\[54\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) |
| Non-zero addresses / active users versus price | Separates broadening adoption from pure narrative | **Divergence:** price up sharply while address growth stalls or falls | On-chain analytics dashboards. [\[55\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) |
| Matched buy/sell wash patterns | Detects fake volume and manufactured activity | Chainalysis heuristic: buy and sell within **25 blocks**, USD difference **\<1%**, repeated **≥3** times | Transaction-level DEX analysis, forensic platforms. [\[56\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) |
| Controller-to-managed address fan-out | Flags coordinated manipulation across many wallets | **Warning:** controller funds **≥5** managed addresses and buy/sell imbalance stays **\<5%** | Multi-sender traces, DEX logs, forensic platforms. [\[56\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) |

These thresholds are **screening heuristics**, not universal laws. Their purpose is triage: they identify situations that deserve deeper diligence, not automatic buy/sell decisions. Different chains, liquidity venues, and token designs need different baselines. [\[57\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice)

For investors, the highest-value mitigation steps are usually boring ones: check holder concentration before checking story; inspect unlock schedules before reading “community” threads; size positions to **exit liquidity**, not to market cap; prefer limit or RFQ execution over blind market orders in thin names; and treat upgradeable contracts, unlocked insider allocations, or removable LPs as structural risks rather than minor details. The Munchables, HAWK, LIBRA, and ZKasino cases all show that retail losses tend to begin where diligence stops. [\[58\]](https://www.halborn.com/blog/post/explained-the-munchables-hack-march-2024)

For platforms, the key mitigation themes are governance discipline and transparency. Timelocked multisigs are better than single-key admins; transparent vesting and treasury dashboards are better than opaque tokenomics; hard constraints on liquidity withdrawal are better than promises; and real-time surveillance for wash trading, multisender clustering, and sudden exchange inflows is now table stakes. Recovery planning also matters: Munchables and Cetus show that incident response, disposition of privileged keys, and clearly defined emergency authorities can determine whether users face permanent loss or partial restoration. [\[59\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc)

### Open questions and limitations

The largest research limitation is **opacity outside the chain**. DEX markets are unusually transparent, which is why public manipulation studies focus on them, but CEX internalization, OTC transfers, and off-chain market-making inventories remain much harder to observe directly. That means any public estimate of manipulation or contagion is probably more complete for DEXs than for the market as a whole. [\[60\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)

The second limitation is **attribution error**. Exchange labels, entity clustering, treasury-wallet identification, and related-wallet inference are all probabilistic. Glassnode’s own methodology notes that exchange-balance analysis depends on persistent and holistic address labeling, which is inherently dynamic. Similar caveats apply to any “whale” metric based on public wallets. [\[61\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice)

The third limitation is **taxonomy instability**. Category providers explicitly state that crypto assets overlap across sectors, and regulators continue to stress that legal classification is fact-specific. Economically, that means one asset can be a governance token, a fee token, and an L2 token simultaneously; legally, it may still be evaluated according to the facts of how it is offered and sold. [\[62\]](https://www.coingecko.com/en/categories)

The final open question is whether non-Bitcoin crypto can move from narrative-dominated valuation toward more durable revenue alignment. The strongest unresolved issues are how to measure genuine utility rather than speculative turnover, how to price governance rights when participation is low, how to detect manipulation cross-venue in real time, and how to distinguish healthy market-making from synthetic liquidity before a collapse occurs. The empirical literature is improving, but the market still changes faster than the measurement framework. [\[63\]](https://papers.ssrn.com/sol3/Delivery.cfm/5261306.pdf?abstractid=5261306&mirid=1)

------------------------------------------------------------------------

[\[1\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) [\[6\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) [\[25\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) [\[31\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) [\[35\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) [\[46\]](https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/) https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/

<https://www.fiod.nl/12-million-seized-and-arrested-in-investigation-into-gambling-platform-scam/>

[\[2\]](https://www.coingecko.com/en/categories) [\[62\]](https://www.coingecko.com/en/categories) https://www.coingecko.com/en/categories

<https://www.coingecko.com/en/categories>

[\[3\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf) [\[8\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf) [\[14\]](https://www.nber.org/system/files/working_papers/w27222/w27222.pdf) https://www.nber.org/system/files/working_papers/w27222/w27222.pdf

<https://www.nber.org/system/files/working_papers/w27222/w27222.pdf>

[\[4\]](https://www.coinbase.com/legal/trading_rules) [\[9\]](https://www.coinbase.com/legal/trading_rules) [\[13\]](https://www.coinbase.com/legal/trading_rules) [\[29\]](https://www.coinbase.com/legal/trading_rules) [\[34\]](https://www.coinbase.com/legal/trading_rules) [\[53\]](https://www.coinbase.com/legal/trading_rules) https://www.coinbase.com/legal/trading_rules

<https://www.coinbase.com/legal/trading_rules>

[\[5\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) [\[22\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) [\[26\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) [\[56\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) [\[60\]](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/

<https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/>

[\[7\]](https://optimistic.etherscan.io/token/0x000000000000012DeF132E61759048bE5b5C6033) https://optimistic.etherscan.io/token/0x000000000000012DeF132E61759048bE5b5C6033

<https://optimistic.etherscan.io/token/0x000000000000012DeF132E61759048bE5b5C6033>

[\[10\]](https://docs.uniswap.org/contracts/v2/concepts/advanced-topics/research) https://docs.uniswap.org/contracts/v2/concepts/advanced-topics/research

<https://docs.uniswap.org/contracts/v2/concepts/advanced-topics/research>

[\[11\]](https://docs.cdp.coinbase.com/prime/concepts/trading/rfq) https://docs.cdp.coinbase.com/prime/concepts/trading/rfq

<https://docs.cdp.coinbase.com/prime/concepts/trading/rfq>

[\[12\]](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4018171_code2078716.pdf?abstractid=4018171&mirid=1&type=2) https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4018171_code2078716.pdf?abstractid=4018171&mirid=1&type=2

<https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4018171_code2078716.pdf?abstractid=4018171&mirid=1&type=2>

[\[15\]](https://www.nber.org/system/files/working_papers/w33640/w33640.pdf) https://www.nber.org/system/files/working_papers/w33640/w33640.pdf

<https://www.nber.org/system/files/working_papers/w33640/w33640.pdf>

[\[16\]](https://arxiv.org/abs/2410.19107) https://arxiv.org/abs/2410.19107

<https://arxiv.org/abs/2410.19107>

[\[17\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) [\[32\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) [\[40\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) [\[49\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) [\[54\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) [\[55\]](https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity) https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity

<https://docs.glassnode.com/guides-and-tutorials/getting-started/use-case-tutorials/tutorial-2-introduction-to-on-chain-activity>

[\[18\]](https://insights.glassnode.com/coinbase-glassnode-charting-crypto-q2-2025/) https://insights.glassnode.com/coinbase-glassnode-charting-crypto-q2-2025/

<https://insights.glassnode.com/coinbase-glassnode-charting-crypto-q2-2025/>

[\[19\]](https://papers.ssrn.com/sol3/Delivery.cfm/5a45a7f5-72c9-4cd6-9f5d-31a82379b704-MECA.pdf?abstractid=4450390&type=2) https://papers.ssrn.com/sol3/Delivery.cfm/5a45a7f5-72c9-4cd6-9f5d-31a82379b704-MECA.pdf?abstractid=4450390&type=2

<https://papers.ssrn.com/sol3/Delivery.cfm/5a45a7f5-72c9-4cd6-9f5d-31a82379b704-MECA.pdf?abstractid=4450390&type=2>

[\[20\]](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4552428_code1542588.pdf?abstractid=3604322&mirid=1) https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4552428_code1542588.pdf?abstractid=3604322&mirid=1

<https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4552428_code1542588.pdf?abstractid=3604322&mirid=1>

[\[21\]](https://docs.etherscan.io/introduction) [\[50\]](https://docs.etherscan.io/introduction) https://docs.etherscan.io/introduction

<https://docs.etherscan.io/introduction>

[\[23\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation) [\[37\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation) [\[51\]](https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation) https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation

<https://www.burwick.law/active-cases/hawk-tuah-token-lawsuit-in-re-hawk-token-securities-litigation>

[\[24\]](https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty) https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty

<https://www.certik.com/blog/blast-chains-usd97-million-battle-are-north-korean-hackers-rusty>

[\[27\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc) [\[33\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc) [\[59\]](https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc) https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc

<https://slowmist.medium.com/slowmist-monthly-security-report-web3-security-loss-at-approximately-139-million-665dd2c75dcc>

[\[28\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice) [\[57\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice) [\[61\]](https://docs.glassnode.com/further-information/exchange-data-transparency-notice) https://docs.glassnode.com/further-information/exchange-data-transparency-notice

<https://docs.glassnode.com/further-information/exchange-data-transparency-notice>

[\[30\]](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica

<https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>

[\[36\]](https://www.trmlabs.com/resources/blog/tracking-the-hawk-tuah-memecoin-launch-on-solana) https://www.trmlabs.com/resources/blog/tracking-the-hawk-tuah-memecoin-launch-on-solana

<https://www.trmlabs.com/resources/blog/tracking-the-hawk-tuah-memecoin-launch-on-solana>

[\[38\]](https://www.trmlabs.com/resources/blog/the-libra-affair-tracking-the-memecoin-that-launched-a-scandal-in-argentina) https://www.trmlabs.com/resources/blog/the-libra-affair-tracking-the-memecoin-that-launched-a-scandal-in-argentina

<https://www.trmlabs.com/resources/blog/the-libra-affair-tracking-the-memecoin-that-launched-a-scandal-in-argentina>

[\[39\]](https://www.reuters.com/world/americas/crypto-worth-99-million-withdrawn-milei-backed-libra-token-researchers-say-2025-02-20/) https://www.reuters.com/world/americas/crypto-worth-99-million-withdrawn-milei-backed-libra-token-researchers-say-2025-02-20/

<https://www.reuters.com/world/americas/crypto-worth-99-million-withdrawn-milei-backed-libra-token-researchers-say-2025-02-20/>

[\[41\]](https://mantrachain.io/resources/announcements/understanding-om) [\[43\]](https://mantrachain.io/resources/announcements/understanding-om) [\[52\]](https://mantrachain.io/resources/announcements/understanding-om) https://mantrachain.io/resources/announcements/understanding-om

<https://mantrachain.io/resources/announcements/understanding-om>

[\[42\]](https://www.binance.com/en/square/post/22898167790818) https://www.binance.com/en/square/post/22898167790818

<https://www.binance.com/en/square/post/22898167790818>

[\[44\]](https://www.elliptic.co/blog/cetus-protocol-hacked-for-more-than-200-million) https://www.elliptic.co/blog/cetus-protocol-hacked-for-more-than-200-million

<https://www.elliptic.co/blog/cetus-protocol-hacked-for-more-than-200-million>

[\[45\]](https://x.com/CetusProtocol/status/1928680214231658961) [\[47\]](https://x.com/CetusProtocol/status/1928680214231658961) https://x.com/CetusProtocol/status/1928680214231658961

<https://x.com/CetusProtocol/status/1928680214231658961>

[\[48\]](https://www.justice.gov/usao-edny/pr/ceo-digital-asset-company-safemoon-sentenced-100-months-prison-multi-million-dollar) https://www.justice.gov/usao-edny/pr/ceo-digital-asset-company-safemoon-sentenced-100-months-prison-multi-million-dollar

<https://www.justice.gov/usao-edny/pr/ceo-digital-asset-company-safemoon-sentenced-100-months-prison-multi-million-dollar>

[\[58\]](https://www.halborn.com/blog/post/explained-the-munchables-hack-march-2024) https://www.halborn.com/blog/post/explained-the-munchables-hack-march-2024

<https://www.halborn.com/blog/post/explained-the-munchables-hack-march-2024>

[\[63\]](https://papers.ssrn.com/sol3/Delivery.cfm/5261306.pdf?abstractid=5261306&mirid=1) https://papers.ssrn.com/sol3/Delivery.cfm/5261306.pdf?abstractid=5261306&mirid=1

<https://papers.ssrn.com/sol3/Delivery.cfm/5261306.pdf?abstractid=5261306&mirid=1>
