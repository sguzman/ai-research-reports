# Structure and Layout of the Cryptocurrency Ecosystem

## Executive summary

The cryptocurrency ecosystem is best understood as a layered system rather than as a single “market.” At the top are users, wallets, funds, brokers, exchanges, and applications. Beneath that sits market structure: spot venues, derivatives venues, OTC desks, prime services, market makers, liquidity providers, arbitrageurs, and—in onchain environments—searchers and block builders. Under those layers is the protocol substrate: consensus, block production, state representation, virtual machines, data availability, and peer-to-peer networking. Around all of it sits a service perimeter of custody, RPC providers, indexers, explorers, analytics, monitoring, and compliance. The practical result is that “crypto” is simultaneously a financial market, a distributed systems stack, and an operational security problem. [\[1\]](https://www.coinbase.com/exchange)

A useful first distinction is between **coins** and **tokens**. A coin is the native asset of a blockchain and is usually tied to paying transaction fees, incentivizing security, or both—for example, BTC on Bitcoin, ETH on Ethereum, SOL on Solana, and SUI on Sui. A token is typically issued or represented by smart-contract or protocol logic on top of a base chain, often under a standard such as ERC-20, and can represent utility, governance rights, stable value, wrapped assets, or claims on some offchain/onchain resource. In practice, the terminology is market convention rather than a universally binding legal or protocol definition, so edge cases exist. [\[2\]](https://bitcoin.org/)

Market structure splits sharply between centralized and onchain venues. Centralized exchanges combine custody, matching, margining, and surveillance inside one operator-controlled system, while decentralized exchanges move matching and settlement into smart contracts or related protocols. OTC desks exist for negotiated, large-size execution with less order-book impact; prime brokers combine custody, trading access, financing, and sometimes staking; futures and perpetuals create leveraged exposure without spot ownership; and ETFs/ETPs move some crypto exposure into conventional securities-market rails. Those financial layers are inseparable from the underlying infrastructure because execution quality depends on custody design, node access, transaction propagation, oracle freshness, data indexing, and bridge security. [\[3\]](https://www.coinbase.com/exchange)

The technological foundation is equally heterogeneous. Bitcoin is organized around a UTXO ledger and proof-of-work mining. Ethereum and many smart-contract chains use account/state models and proof-of-stake plus smart-contract runtimes. Solana uses an account-based runtime optimized for parallel execution and a different transaction-forwarding model. Cosmos-style chains use BFT consensus and interoperable modules, with IBC providing a light-client-based approach to cross-chain communication. Meanwhile, rollups, validiums, sidechains, and data-availability systems add another layer of specialization around scaling and interoperability. [\[4\]](https://developer.bitcoin.org/devguide/transactions.html)

From a risk perspective, the most important truth is that crypto’s trust assumptions move around rather than disappear. Self-custody removes exchange default risk but makes key management existential. DEXs remove some intermediaries but add smart-contract, oracle, and MEV risk. Bridges increase capital mobility but often create some of the highest-concentration technical risk in the stack. RPC and indexing providers improve developer productivity but can centralize operational dependencies. Regulations also attach unevenly: typically much more directly to exchanges, custodians, brokers, issuers, and ETF structures than to decentralized protocols themselves. [\[5\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0)

## Layered architecture

A rigorous way to visualize the ecosystem is as a stack in which **assets and orders** move downward into execution and settlement, while **data, proofs, prices, and analytics** move upward to applications, traders, and institutions. The diagram below is intentionally architectural rather than chain-specific; the exact implementation differs by protocol and jurisdiction. [\[6\]](https://www.coinbase.com/exchange)

    flowchart TB
      subgraph A[User and access layer]
        W[Wallets and signers<br/>self-custody, hardware, multisig, MPC]
        App[Apps, brokers, funds, exchanges]
      end

      subgraph B[Market layer]
        CEX[CEXs<br/>order books and custody]
        DEX[DEXs<br/>AMMs and onchain settlement]
        OTC[OTC desks and prime brokers]
        Deriv[Futures, perpetuals, ETFs and ETPs]
        MM[Market makers, LPs,<br/>arbitrageurs, searchers]
      end

      subgraph C[Middleware and services]
        RPC[RPC gateways and node providers]
        Oracle[Oracles and external data]
        Bridge[Bridges, wrapped assets,<br/>cross-chain messaging, IBC]
        Index[Indexers, explorers,<br/>analytics, monitoring]
      end

      subgraph D[Protocol layer]
        L2[Rollups, sidechains, validiums]
        L1[L1 blockchains]
        RT[Execution runtimes<br/>EVM, Solana runtime, Move, WASM]
        State[State and data structures<br/>UTXO, accounts, Merkle structures]
        Cons[Consensus<br/>PoW, PoS, BFT]
      end

      subgraph E[Node and network layer]
        Nodes[Full, archive, light, pruned,<br/>validator and RPC nodes]
        P2P[P2P overlay, gossip,<br/>mempool, propagation]
      end

      W --> App
      App --> CEX
      App --> DEX
      App --> OTC
      App --> Deriv

      CEX --- MM
      DEX --- MM
      OTC --- MM
      Deriv --- MM

      CEX --> RPC
      DEX --> RPC
      OTC --> RPC
      Deriv --> RPC
      MM --> RPC

      Oracle --> DEX
      Oracle --> Deriv
      Bridge --> App
      Bridge --> L2
      Index --> App

      RPC --> Nodes
      Nodes --> P2P
      P2P --> L1
      Cons --> L1
      L1 --> RT
      RT --> State
      L2 --> L1
      L2 --> Bridge
      L2 --> Oracle
      Nodes --> Index

The key design insight is that settlement, security, and observability are distributed across this whole stack. A user may trade on a venue front end, but execution may depend on an API gateway, which depends on one or more RPC nodes, which depend on peer connectivity, consensus clients, and timely block propagation. At the same time, asset pricing may depend on external oracle networks, and cross-chain asset movement may depend on bridge contracts or light-client verification. This is why outages or exploits in “infrastructure” often propagate directly into market failures. [\[7\]](https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/)

A compact definition table for native versus issued assets is helpful:

| Asset type | What it is | Typical roles | Representative examples |
|----|----|----|----|
| Coin | Native asset of a blockchain protocol | Pays fees, secures consensus, staking/mining rewards, base settlement asset | BTC, ETH, SOL, SUI |
| Token | Asset represented by protocol or smart-contract logic on top of a chain | Stablecoins, governance, utility, wrapped assets, claims on offchain/onchain resources | ERC-20 tokens such as USDC, wrapped assets such as WETH |

This distinction is synthesized from Bitcoin, Ethereum, Solana, Sui/Aptos-style documentation, and the ERC-20 standard. [\[8\]](https://bitcoin.org/)

## Market and liquidity layer

### Venues and intermediation

Centralized exchanges are the most recognizable crypto venues because they look closest to traditional electronic markets: they operate order books, hold customer assets or balances, and provide market data, matching, margining, and sometimes futures access through one operator. Coinbase describes direct exchange access in terms of high-throughput APIs, deep spot liquidity, and integrated futures and market-data access. Binance presents a similarly broad product surface spanning spot, futures, and P2P markets, though exact availability varies by entity and jurisdiction. [\[9\]](https://www.coinbase.com/exchange)

Decentralized exchanges do not all work the same way, but the most economically important design has been the AMM. Uniswap’s official documentation describes its protocol family as centered on liquidity pools and AMM contracts rather than traditional order books. In an AMM venue, liquidity providers contribute assets into pools, and pricing comes from contract logic plus arbitrage pressure rather than a centralized matching engine. The result is that execution and settlement happen onchain, with transparency and composability as major advantages, but with smart-contract, oracle, and MEV tradeoffs. [\[10\]](https://developers.uniswap.org/docs/protocols/overview?utm_source=chatgpt.com)

OTC desks exist because large trades can move visible market prices if they hit a public order book directly. Binance’s spot-market material explicitly notes that OTC execution can be useful for large-volume trades when exchange-book execution would create slippage. Crypto prime brokerage then sits one level above pure OTC: a prime platform typically bundles trading, custody, financing, reporting, and operational workflows for institutions. Coinbase Prime describes itself as an integrated platform for custody, trading, financing, and staking, which is the right mental model for how crypto “prime” fits into the ecosystem. [\[11\]](https://academy.binance.com/lt/articles/what-is-a-spot-market-and-how-to-do-spot-trading)

Derivatives add another parallel market structure. Traditional-dated futures are widely available on regulated infrastructures such as CME Group[\[12\]](https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures), while perpetual futures are crypto-native derivatives that provide continuous exposure without an expiry date. Coinbase’s perpetuals materials emphasize the no-expiration structure and margin-based exposure; its current international specifications show perpetual products settled in USDC on a recurring basis. ETFs and ETPs are another wrapper layer: the Securities and Exchange Commission[\[13\]](https://www.coinbase.com/prime/custody) describes crypto asset ETPs as exchange-listed investment products, and in the United States it approved the listing and trading of spot bitcoin ETPs in January 2024 and later permitted in-kind creations and redemptions for crypto ETPs in 2025. [\[14\]](https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures)

### Trading primitives

A **trading pair** is the market expression of one asset against another—typically a base and quote asset such as BTC/USD, ETH/USDC, or SOL/USDT. On CEXs this pair usually corresponds to an order book; on DEXs it often corresponds to an AMM pool or routing path. Coinbase’s documentation on supported pairs and advanced-trade interfaces shows how venues enumerate these markets, while Uniswap’s protocol docs show how token pairs sit inside pooled-liquidity structures. [\[15\]](https://help.coinbase.com/en/prime/trading-and-funding/supported-cryptocurrencies-and-trading-pairs)

An **order book** is the live ladder of bids and asks for a market. Coinbase’s advanced-trade documentation describes the order book and depth chart as the live set of open buy and sell interest, while Binance Academy explains that makers add liquidity by resting orders on that book and takers remove it by immediately crossing existing quotes. This is the mechanical basis for maker-taker fees, market depth, and quoted spreads. [\[16\]](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview)

In AMMs, the key primitives are the liquidity pool, the pricing function, and routing logic. Uniswap’s official material states plainly that the protocol uses an automated market maker model with liquidity pools rather than order books. Because AMMs quote prices from pool state, large trades move the pool price directly; in both AMM and order-book markets this execution-price drift is what traders experience as **slippage**. Binance’s liquidity and market-order materials make the order-book side of the same point: shallow liquidity means bigger price movement for large or urgent orders. [\[17\]](https://developers.uniswap.org/docs/get-started/concepts/how-uniswap-works?utm_source=chatgpt.com)

**Liquidity** is therefore not just “volume”; it is the market’s capacity to absorb size without large price movement. In order-book markets it shows up as book depth; in AMMs it shows up as pool depth and curve shape; and in multi-venue crypto it is also a routing problem because capital is fragmented across exchanges, chains, and quote assets. Arbitrageurs connect those fragments by buying where an asset is cheap and selling where it is rich, helping keep CEX and DEX prices aligned. Onchain, that same transaction-ordering race becomes part of the block-production economy itself. [\[18\]](https://academy.binance.com/ka-GE/articles/liquidity-explained)

**MEV** is the clearest example of crypto’s market microstructure collapsing into protocol infrastructure. Ethereum’s official docs explain that validators are the parties who can guarantee inclusion, but that searchers run algorithms to find arbitrage, liquidation, and ordering opportunities and submit them into the block-building supply chain. Flashbots’ MEV-Boost documentation describes today’s proposer-builder separation model on Ethereum, in which validators can outsource block construction to a builder market via relays. That means current Ethereum market structure is not just traders versus venues; it is also users, wallets, searchers, builders, relays, and validators competing over transaction ordering. [\[19\]](https://ethereum.org/developers/docs/mev/)

The venue comparison below synthesizes official exchange and protocol documentation:

| Choice | Core execution model | Main strengths | Main tradeoffs | Typical fit |
|----|----|----|----|----|
| CEX | Operator-run order book and internal custody | High throughput, deep books, familiar UX, margining and surveillance | Counterparty/custody dependence, jurisdiction-specific access, opaque internal controls relative to onchain settlement | High-frequency spot and derivatives trading, institutional routing |
| DEX | Smart-contract execution, usually AMMs or related routing models | Self-custody, transparent settlement, composability, permissionless access where available | Smart-contract risk, oracle dependence, MEV exposure, chain congestion and gas costs | Onchain asset exchange, long-tail pairs, composable DeFi workflows |

Comparison basis: Coinbase Exchange and Advanced Trade documentation, plus Uniswap protocol documentation and Ethereum MEV documentation. [\[20\]](https://www.coinbase.com/exchange)

## Protocol and execution foundation

### Consensus, finality, and block production

Consensus mechanisms answer a narrower question than people often assume: how a distributed network decides who may propose the next block, how other nodes verify it, and when users should treat the result as final. Bitcoin’s model is proof-of-work: miners expend energy to satisfy a hash target, and the chain with the greatest accumulated work becomes canonical. Ethereum’s current model is proof-of-stake: validators post stake, propose and attest to blocks, and face penalties or slashing for certain invalid or malicious behaviors. Cosmos-style systems such as CometBFT and Solana’s Tower BFT sit in the broader BFT family, where the protocol is designed to remain safe under bounded Byzantine faults, though the exact safety and liveness machinery differs. [\[21\]](https://bitcoin.org/en/how-it-works)

Finality also differs by design. Bitcoin-style PoW gives **probabilistic finality**: confidence rises as more work accumulates on top of a block, but reorgs remain theoretically possible. Ethereum’s PoS docs describe **crypto-economic finality**, where reversing finalized history would require burning a large share of staked ETH under consensus failure. CometBFT describes a system designed to remain secure and consistent as long as fewer than one-third of machines fail arbitrarily, which is the classic BFT threshold intuition. [\[22\]](https://developer.bitcoin.org/devguide/block_chain.html)

| Choice | Security resource | Finality style | Main advantages | Main tradeoffs | Examples |
|----|----|----|----|----|----|
| PoW | Hash power, electricity, specialized hardware | Probabilistic | Simple and battle-tested block-production economics; no slashing machinery required | High energy cost; ASIC and pool concentration concerns; slower confirmation certainty | Bitcoin |
| PoS | Staked native asset plus penalties/slashing | Economic finality, often faster | Lower energy cost; capital-based security; supports richer validator incentives | Requires staking system design, slashing, and careful validator/client coordination | Ethereum |
| BFT-style PoS variants | Staked validators with Byzantine-fault thresholds | Often stronger deterministic/economic finality properties at low latency | Fast agreement and strong consistency assumptions for application chains | Can be more sensitive to validator-set quality, networking assumptions, or governance concentration | CometBFT/Cosmos, Solana Tower BFT |

Comparison basis: Bitcoin and Ethereum documentation, CometBFT docs, and Solana Tower BFT materials. [\[23\]](https://bitcoin.org/en/how-it-works)

### Miners, validators, pools, ASICs, and rewards

In proof-of-work systems, miners select candidate transactions, build blocks, and race to find valid proofs of work. Bitcoin’s mining guide explains pool mechanics directly: individual miners submit “shares” to a pool to smooth payout variance, and when a pool finds a valid block it distributes block reward plus fees according to its payout method. Bitcoin.org also states that miners use specialized hardware and compete in an environment where profitability depends on efficiency as difficulty rises. This is why ASIC supply chains, energy prices, and pool concentration are not peripheral—they are part of the protocol’s lived security model. [\[24\]](https://developer.bitcoin.org/devguide/mining.html)

In proof-of-stake networks, validators replace miners as block producers and attestors. Ethereum’s documentation explains that validators stake ETH, verify blocks, and may be penalized or slashed for equivocation-like offenses. Solana similarly frames validators as the operators that keep the network secure and enable staking-based participation, albeit inside a different runtime and networking architecture. Economically, validator revenue mixes issuance, fees, and sometimes MEV or related ordering revenue; the downside risk is downtime, missed rewards, or active penalties. [\[25\]](https://ethereum.org/developers/docs/consensus-mechanisms/pos/?utm_source=chatgpt.com)

### State, blocks, headers, and Merkle structures

Bitcoin and Ethereum differ fundamentally in how they model state. Bitcoin transactions consume prior outputs and create new outputs, producing a UTXO set that wallets and nodes track. Ethereum organizes its world state as accounts containing balances, nonces, code, and storage, with state transitions applied directly to account objects. Neither model is universally “better”; they optimize for different implementation and application tradeoffs. [\[26\]](https://developer.bitcoin.org/devguide/transactions.html)

Blocks are the onchain packaging unit, but their internal meaning differs across chains. Bitcoin’s blockchain guide describes the chain as the public ledger that protects against double-spending and modification of previous records. Ethereum’s account/state system stores a state root in block headers, and its Merkle Patricia Trie documentation explains how balances, contracts, and storage are encoded into verifiable root values. Rollups then reuse the same idea, often posting commitments to compressed L2 state on an L1. [\[27\]](https://developer.bitcoin.org/devguide/block_chain.html)

| Choice | Core object | Strengths | Tradeoffs | Common consequences | Examples |
|----|----|----|----|----|----|
| UTXO model | Spendable outputs | Good auditability of coin lineage, natural parallelism across independent UTXOs, simpler coin-selection semantics | More awkward generalized stateful apps, wallet UX complexity, fragmented balances | Transactions explicitly consume and create outputs; “balance” is a wallet abstraction over many UTXOs | Bitcoin |
| Account/state model | Accounts with balances, nonce, code, storage | Better fit for general-purpose smart contracts and persistent application state | More complex shared-state execution, more care required around state contention and ordering | Applications look like stateful programs mutating shared objects/accounts | Ethereum, Solana-style accounts, many smart-contract chains |

Comparison basis: Bitcoin transaction and glossary docs, plus Ethereum whitepaper and account/state documentation. [\[28\]](https://developer.bitcoin.org/devguide/transactions.html)

### Smart contracts, runtimes, and fee models

The **EVM** is the canonical example of a smart-contract runtime: a replicated virtual machine where transactions execute code and mutate shared state under metered resource consumption. Ethereum’s documentation frames the EVM as the state-transition engine for smart contracts and transactions. Solidity’s official security docs are still the clearest concise source on classic EVM risks: external calls can enable reentrancy if state is not updated before control is handed off, and proxy-based upgrade patterns separate logic from storage to allow post-deployment changes. [\[29\]](https://ethereum.org/developers/docs/evm/)

Solana’s runtime is architecturally different. Official Solana docs describe state as living in accounts, with programs themselves being stateless executable accounts. The Sealevel material explains the key performance idea: because transactions declare the accounts they read and write, non-overlapping operations can run in parallel. Solana also meters execution in **compute units** and allows optional prioritization fees, a different fee model from EVM gas even though the economic purpose—pricing scarce execution and ordering priority—is analogous. [\[30\]](https://solana.com/docs/core/accounts)

The **Move** family shifts emphasis toward resource safety. Aptos documentation describes Move as a language centered on scarcity and access control, with resources that cannot be accidentally copied or dropped unless explicitly allowed. Sui extends that design into an object model where onchain state is built from objects as the primary units of interaction. By contrast, **WASM-based** smart-contract environments such as CosmWasm and parts of the Polkadot stack emphasize modular, sandboxed execution compiled to WebAssembly. [\[31\]](https://aptos.dev/network/blockchain/move)

Fee models are not uniform across crypto. EVM chains meter execution and storage-like effects with gas. Solana meters computation with compute units and optional priority fees. ZKsync’s protocol docs describe fee accounting that includes execution and pubdata considerations, including refunds in some cases. The analytical takeaway is that “gas model” really means **how a chain prices scarce state transition resources**—compute, storage, bandwidth, proof costs, or some combination—not just one universal tariff mechanism. [\[32\]](https://ethereum.org/developers/docs/evm/)

### Scaling, data availability, interoperability, and oracles

Rollups are now central to Ethereum’s scaling approach. Ethereum’s documentation distinguishes **optimistic rollups**, which assume correctness unless challenged with fault/fraud proofs, from **ZK rollups**, which submit validity proofs. Optimism’s current docs describe permissionless fault proofs for OP Stack withdrawals, while Arbitrum’s BoLD documentation describes a dispute protocol for permissionless validation. ZKsync frames itself explicitly as a network of interoperable ZK rollups and validiums. [\[33\]](https://ethereum.org/developers/docs/scaling/optimistic-rollups/)

Data availability is the other half of scaling. Ethereum’s danksharding and proto-danksharding materials explain blob-based DA: rollups can publish data blobs to Ethereum more cheaply than permanent calldata, and future designs such as data-availability sampling and PeerDAS increase DA capacity further. This is crucial because a rollup is only safely reconstructable if its users and validators can access the transaction data needed to verify state transitions. [\[34\]](https://ethereum.org/roadmap/danksharding/)

Sidechains and validiums should not be confused with rollups. Ethereum’s scaling docs state clearly that sidechains are independent blockchains connected by bridges and **do not inherit Ethereum’s security properties**. Validiums use validity proofs but keep transaction data offchain, trading off some data-availability assumptions for throughput. That distinction matters because “L2” is often used loosely in marketing, while security inheritance, settlement path, and DA assumptions are the real technical differentiators. [\[35\]](https://ethereum.org/developers/docs/scaling/sidechains/)

Interoperability ranges from relatively trust-minimized designs to more trust-assuming bridge systems. Cosmos IBC is explicitly based on light clients, proofs, and channels between sovereign chains. Wormhole’s docs describe a Guardian network and a message-passing layer used for wrapped-token transfers and other cross-chain operations. Hop describes itself as a rollup-to-rollup token bridge that avoids waiting for the full challenge period in some workflows. Wrapped assets are exactly what they sound like: a tokenized representation of an asset on another network, typically produced via lock-and-mint or burn-and-release mechanisms. [\[36\]](https://docs.cosmos.network/ibc/latest/intro?utm_source=chatgpt.com)

Oracles bridge the onchain/offchain boundary. Chainlink documents its data feeds as decentralized oracle networks connecting smart contracts to external data such as prices, reserve balances, and L2 sequencer health. This makes oracles essential infrastructure for lending, derivatives, synthetics, and many stable-value systems—but it also means oracle design is one of the crypto stack’s most important hidden trust boundaries. [\[37\]](https://docs.chain.link/data-feeds)

| Choice | Security model | Latency / withdrawal pattern | Main strengths | Main tradeoffs | Examples |
|----|----|----|----|----|----|
| Optimistic rollups | Assume validity unless challenged; rely on dispute/fault proofs | Typically challenge window for certain final exits | Mature EVM compatibility, simpler proving stack, strong L1 anchoring when properly designed | Withdrawal delays and proof/dispute complexity | Arbitrum, Optimism |
| ZK rollups | Validity proofs prove state transitions | Usually faster final settlement once proof accepted | Strong cryptographic correctness guarantees, potentially faster finality, compression benefits | More complex proving systems, specialized tooling and prover costs | zkSync and other ZK rollups |

Comparison basis: Ethereum scaling docs plus Arbitrum, Optimism, and ZKsync official documentation. [\[33\]](https://ethereum.org/developers/docs/scaling/optimistic-rollups/)

## Infrastructure, custody, and operations

### Nodes, networking, propagation, and indexing

A blockchain is not one server; it is a federation of node types with different trust and performance profiles. Bitcoin’s operating-modes documentation distinguishes full nodes from SPV clients, while Ethereum’s docs distinguish full, archive, and light nodes and explain that archive nodes retain all historical state. Solana’s own materials distinguish consensus validators from dedicated RPC infrastructure and note that poor RPC performance is user-visible even if consensus itself is healthy. Taken together, this gives a practical taxonomy: **full nodes** validate the chain directly; **archive nodes** keep complete historical state; **light clients** use headers plus proofs; **RPC nodes** expose API access for applications; and **indexers** transform raw chain data into queryable datasets. Exact **pruned** modes are client-specific, but the general idea is full validation with reduced retained history. [\[38\]](https://developer.bitcoin.org/devguide/operating_modes.html)

The network layer is equally important. Bitcoin’s P2P guide describes the protocol for collaborative block and transaction exchange, and the Ethereum networking-layer docs describe gossip and request-response protocols between thousands of peers. Pending transactions usually wait in a **mempool** or analogous queue until a block producer selects them. Solana is a notable architectural deviation: its Gulf Stream design pushes transaction forwarding toward expected future leaders, which is why Solana is often described as “mempool-less” in the conventional public-mempool sense. [\[39\]](https://developer.bitcoin.org/devguide/p2p_network.html)

Latency and bandwidth are not secondary operational details; they shape security and UX. Bitcoin’s blockchain guide explains how simultaneous block production can create competing chains and stale blocks, so slower propagation directly affects orphan/stale-block risk. On Ethereum, network propagation and client coordination affect block/attestation timing and application responsiveness. On Solana, dedicated RPC architecture and stake-weighted QoS reflect the fact that high-throughput networks need differentiated handling for read access, write submission, and transaction landing. [\[40\]](https://developer.bitcoin.org/devguide/block_chain.html)

Indexers and explorers convert raw ledgers into usable operational data. The Graph describes subgraphs as open APIs that extract, process, and expose blockchain data, with indexers staking GRT to serve queries. Etherscan[\[41\]](https://developer.bitcoin.org/devguide/mining.html) describes itself as an explorer, search, API, and analytics platform, while Blockscout[\[42\]](https://academy.binance.com/ka-GE/articles/liquidity-explained) frames an explorer as a frontend that indexes and organizes blocks, transactions, addresses, and contract metadata. This observability layer is what makes dashboards, compliance systems, analytics products, and application backends viable at scale. [\[43\]](https://thegraph.com/docs/en/indexing/overview/)

### Custody and signing models

Custody is the most economically important trust boundary in the ecosystem. The U.S. investor bulletin on crypto custody defines **self-custody** as the model where the user controls the private keys and also bears the full consequence of loss or compromise. That is the purest form of digital bearer ownership, but it converts operational mistakes into permanent asset loss. [\[44\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0)

A **hardware wallet** pushes keys into an isolated signing environment. Ledger[\[45\]](https://developer.bitcoin.org/devguide/p2p_network.html) defines a hardware wallet as a physical device that stores private keys separately from an internet connection and signs transactions without exposing those keys directly to online systems. This generally reduces remote attack surface, but not phishing, seed compromise, or poor backup practices. [\[46\]](https://www.ledger.com/academy/crypto-hardware-wallet)

**Multisig** and **MPC** are the two dominant institutional design patterns for distributing signing authority. BitGo’s materials define multisig as requiring multiple keys to authorize a transaction, while its developer docs explain that BitGo supports both multisignature and threshold-signature MPC approaches. Fireblocks[\[47\]](https://www.ledger.com/academy/crypto-hardware-wallet) defines MPC as key sharing in which the full private key is never assembled in one place. The tradeoff is straightforward: multisig offers more explicit onchain auditability where natively supported, while MPC offers chain-agnostic signing flexibility and policy-rich institutional workflows. [\[48\]](https://www.bitgo.com/resources/blog/what-is-a-multi-signature-wallet/)

Third-party custodians then add legal, operational, and compliance wrappers around those cryptographic models. Coinbase Prime states that Coinbase Custody Trust Company is a fiduciary under New York banking law and a qualified custodian, while BitGo markets regulated and qualified custody alongside self-custody, cold storage, and hot-wallet options. In other words: custody is not just about cryptography; it is also about bankruptcy remoteness, segregation, insurance, reporting, and the legal identity of the service provider. [\[49\]](https://www.coinbase.com/prime/custody)

### Tooling, clients, and developer experience

Developer productivity in crypto depends heavily on prebuilt clients, SDKs, local development environments, and hosted infrastructure. Ethereum’s docs provide extensive material on development networks, testnets, smart-contract toolchains, IDEs, and node operation. Solana’s docs now provide installation flows, local development tooling, public RPC endpoints, and cookbook references. Aptos provides a similarly explicit stack: CLI, localnet, SDKs, indexer APIs, and faucet-backed testing flows. The consistent pattern is that modern crypto development is impossible without a layered toolchain that spans signing, RPC, compiling, deployment, indexing, and simulation. [\[50\]](https://ethereum.org/developers/docs/)

Managed node access reduces the operational burden of running this stack yourself. Infura describes itself as providing scalable API access to Ethereum and IPFS; Alchemy emphasizes high-availability node RPC and real-time data; QuickNode[\[51\]](https://bitcoin.org/) emphasizes globally distributed low-latency RPC infrastructure. These services do not change consensus rules, but they do change operational risk by concentrating application connectivity into a small set of infrastructure providers. [\[52\]](https://www.infura.io/)

Monitoring completes the loop. Geth exposes a metrics system and dashboards for node observability; Ethstats provides real-time and historical node/network statistics; and application-specific explorers or indexers expose contract verification, tracing, and query APIs. The operational lesson is that crypto stacks require SRE-style monitoring every bit as much as traditional distributed systems. [\[53\]](https://geth.ethereum.org/docs/monitoring/metrics)

## Risks, compliance, and ecosystem map

### Risk matrix

The main ecosystem threats and primary mitigations can be organized as follows:

| Threat | Where it sits | Typical impact | Main mitigations | Responsible actors |
|----|----|----|----|----|
| Private-key loss or theft | Wallet / custody layer | Irrecoverable loss of assets | Hardware isolation, backup discipline, multisig, MPC, policy controls, segregation of duties | Users, custodians, wallet providers |
| Smart-contract bugs and reentrancy | Runtime / application layer | Drained funds, frozen funds, broken invariants | Secure patterns such as checks-effects-interactions, audits, formal tools, conservative upgrade governance, pause controls | Protocol teams, auditors, governance bodies |
| 51% attacks and deep reorgs | Consensus layer | Double spending, settlement failure, chain instability | Decentralized hash/stake distribution, finality waiting, client diversity, monitoring | Miners, validators, node operators, protocol communities |
| MEV abuse, frontrunning, sandwiching | Mempool / block-building layer | User-price harm, liquidation extraction, unfair ordering | Slippage limits, private transaction relays, improved auction design, protocol-level PBS or encrypted-mempool approaches | Wallets, dApps, builders, validators, protocols |
| Oracle manipulation | Data / DeFi layer | Bad liquidations, bad pricing, insolvency | Multi-source feeds, robust oracle networks, circuit breakers, TWAPs, sequencer health checks | Oracle providers, protocol teams |
| Bridge compromise or wrapped-asset failure | Interoperability layer | Cross-chain asset theft, systemic wrapped-asset contagion | Minimize trust, prefer strong verification models, rate limits, monitoring, bug bounties, native transfer models where possible | Bridge operators, guardians/validators, app integrators |
| RPC or indexer outage | Infrastructure layer | App downtime, stale reads, failed submissions | Multi-provider failover, self-hosted redundancy, health checks, cached state, replay-safe logic | App operators, infra providers |
| Stablecoin reserve or redemption stress | Issuer / offchain financial layer | Peg breaks, redemption delays, collateral mismatch | Reserve transparency, attestations, segregated reserve management, legal clarity on redeemability | Issuers, custodians, regulators, users |
| AML / sanctions / travel-rule failures | Exchange / custodian / issuer layer | Enforcement, account freezes, access loss, jurisdictional barriers | KYC/CDD, sanctions screening, transaction monitoring, travel-rule workflows, recordkeeping | Exchanges, custodians, issuers, regulated intermediaries |

This matrix is synthesized from official custody, Solidity, Ethereum, Chainlink, Wormhole, bridge, stablecoin, and AML materials. [\[54\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0)

### Regulatory and compliance touchpoints

Because jurisdiction was unspecified, the most accurate framing is global and modular: rules attach most directly to **fiat interfaces, custody, issuance, and organized venues**, and much less uniformly to open-source protocol code itself. The Financial Action Task Force[\[55\]](https://ethereum.org/developers/docs/scaling/optimistic-rollups/) defines virtual assets broadly and has extended AML/CFT expectations to virtual asset service providers, including Travel Rule workflows. That is why KYC, sanctions screening, suspicious-activity processes, and counterparty information exchange are now core operational requirements for many exchanges and custodians. [\[56\]](https://www.fatf-gafi.org/en/topics/virtual-assets.html)

Exchange compliance surfaces are explicit in operator documentation. Coinbase’s identity-verification materials state that KYC is part of its regulatory-compliance program and linked to local AML laws. Binance’s support materials likewise describe identity verification as a fraud, money-laundering, and terrorist-financing control tied to service access. The implication is simple: centralized venue usability and legal access are inseparable from compliance architecture. [\[57\]](https://www.coinbase.com/blog/identity-verification-and-financial-compliance)

Custody regulation is similarly layered. Coinbase Custody describes itself as a fiduciary and qualified custodian under New York law; BitGo emphasizes qualified custody but also notes jurisdictional and regulatory restrictions on digital-asset services. Those examples should not be generalized into a single global rule, but they do show the main pattern: crypto custody sits at the intersection of cryptography, trust law, market regulation, and operational controls. [\[58\]](https://www.coinbase.com/prime/custody)

Stablecoin regulation and market trust turn on reserve transparency, redeemability, and issuer structure. Circle[\[59\]](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview) states that USDC and EURC are fully backed by highly liquid reserves held separately from operating funds and that reserve reporting is published regularly. Tether[\[60\]](https://thegraph.com/docs/en/indexing/overview/) states that its tokens are pegged 1:1 to their reference fiat currencies and backed by reserves, with transparency pages and reports. Those are issuer statements rather than a single harmonized regulatory standard, which is why stablecoin credit, liquidity, disclosure, and legal-claim analysis cannot be collapsed into “onchain” risk alone. [\[61\]](https://www.circle.com/transparency)

### Taxonomy of essential infrastructure providers and representative projects

The table below is intentionally representative rather than exhaustive. It includes a mix of protocol-native projects and service providers that are commonly treated as core ecosystem infrastructure.

| Category | What it does | Representative providers / projects |
|----|----|----|
| Spot and derivatives venues | Matching, custody, margining, data feeds, and settlement workflows | Binance, Coinbase, Coinbase International Exchange, CME futures infrastructure |
| DEX / liquidity protocols | Onchain swapping, liquidity routing, composable market structure | Uniswap |
| Prime brokerage / institutional access | Trade, custody, financing, reporting, and operational workflows | Coinbase Prime, BitGo |
| Custody and signing infrastructure | Self-custody, institutional custody, cold/hot storage, multisig, MPC | Coinbase Custody, BitGo, Fireblocks[\[47\]](https://www.ledger.com/academy/crypto-hardware-wallet), Ledger[\[45\]](https://developer.bitcoin.org/devguide/p2p_network.html) |
| Node and RPC access | Managed JSON-RPC, archive/full-node access, developer APIs | Infura, Alchemy, QuickNode[\[51\]](https://bitcoin.org/) |
| L2 scaling | Cheaper/faster execution with L1 settlement or proof anchoring | Arbitrum, Optimism, zkSync |
| Bridges and interoperability | Asset transfer, wrapped assets, cross-chain messaging, chain-to-chain verification | Wormhole, Hop, Cosmos IBC |
| Oracles | External prices, reserve data, sequencer health, message delivery | Chainlink |
| Indexing and querying | Structured access to chain data for apps and analytics | The Graph |
| Explorers and operations visibility | Human-readable chain state, contract verification, APIs | Etherscan[\[41\]](https://developer.bitcoin.org/devguide/mining.html), Blockscout[\[42\]](https://academy.binance.com/ka-GE/articles/liquidity-explained) |
| Core clients and protocol software | Actual consensus and execution implementations | Bitcoin Core, Geth, Ethereum consensus clients, Solana validator / RPC software, CometBFT |

Representative basis: official product and protocol documentation for exchanges, prime platforms, custody providers, RPC providers, rollups, bridges, oracle systems, explorers, and indexers. [\[62\]](https://www.coinbase.com/exchange)

### Suggested further reading

For authoritative follow-up, the best next documents are the original protocol and infrastructure references rather than secondary explainers:

1.  **Bitcoin Developer Guide** for the blockchain, transactions, mining, and P2P network. [\[63\]](https://developer.bitcoin.org/devguide/block_chain.html)
2.  **Ethereum developer documentation** for accounts, the EVM, consensus, rollups, data availability, nodes, and networking. [\[64\]](https://ethereum.org/whitepaper/)
3.  **Solana core docs** for accounts, programs, fees, RPC infrastructure, and validator/RPC separation. [\[65\]](https://solana.com/docs/core/accounts)
4.  **Cosmos / CometBFT / IBC docs** for BFT consensus and light-client-based interoperability. [\[66\]](https://docs.cosmos.network/cometbft/latest/docs/introduction/intro?utm_source=chatgpt.com)
5.  **Uniswap docs and Flashbots / Ethereum MEV docs** for AMMs and onchain market microstructure. [\[67\]](https://developers.uniswap.org/docs/protocols/overview?utm_source=chatgpt.com)
6.  **Arbitrum, Optimism, zkSync, and Ethereum scaling docs** for rollup security and proof models. [\[68\]](https://docs.arbitrum.io/get-started/arbitrum-introduction)
7.  **Chainlink and Wormhole docs** for oracle and cross-chain system architecture. [\[69\]](https://docs.chain.link/architecture-overview/architecture-overview)
8.  **Investor.gov, FATF, Coinbase Custody, Circle, and Tether materials** for custody, AML, Travel Rule, and stablecoin reserve/compliance touchpoints. [\[70\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0)

### Open questions and limitations

This report is intentionally architectural. It does **not** attempt to quantify current market-share concentration across venues, current bridge TVL, exact current fee schedules, or jurisdiction-by-jurisdiction legal treatment of specific assets, because those details are highly changeable and were unspecified. It also treats some families—such as “PoS chains,” “DEXs,” and “custodians”—at the design-pattern level rather than as full case studies of every major implementation. The goal here is to map the ecosystem’s structure and technical foundation faithfully, not to imply that all chains or providers have equivalent trust assumptions or operational quality.

------------------------------------------------------------------------

[\[1\]](https://www.coinbase.com/exchange) [\[3\]](https://www.coinbase.com/exchange) [\[6\]](https://www.coinbase.com/exchange) [\[9\]](https://www.coinbase.com/exchange) [\[20\]](https://www.coinbase.com/exchange) [\[62\]](https://www.coinbase.com/exchange) https://www.coinbase.com/exchange

<https://www.coinbase.com/exchange>

[\[2\]](https://bitcoin.org/) [\[8\]](https://bitcoin.org/) [\[51\]](https://bitcoin.org/) https://bitcoin.org/

<https://bitcoin.org/>

[\[4\]](https://developer.bitcoin.org/devguide/transactions.html) [\[26\]](https://developer.bitcoin.org/devguide/transactions.html) [\[28\]](https://developer.bitcoin.org/devguide/transactions.html) https://developer.bitcoin.org/devguide/transactions.html

<https://developer.bitcoin.org/devguide/transactions.html>

[\[5\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) [\[44\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) [\[54\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) [\[70\]](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0

<https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0>

[\[7\]](https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/) https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/

<https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/>

[\[10\]](https://developers.uniswap.org/docs/protocols/overview?utm_source=chatgpt.com) [\[67\]](https://developers.uniswap.org/docs/protocols/overview?utm_source=chatgpt.com) Protocols Overview \| Uniswap Developers

<https://developers.uniswap.org/docs/protocols/overview?utm_source=chatgpt.com>

[\[11\]](https://academy.binance.com/lt/articles/what-is-a-spot-market-and-how-to-do-spot-trading) https://academy.binance.com/lt/articles/what-is-a-spot-market-and-how-to-do-spot-trading

<https://academy.binance.com/lt/articles/what-is-a-spot-market-and-how-to-do-spot-trading>

[\[12\]](https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures) [\[14\]](https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures) https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures

<https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures>

[\[13\]](https://www.coinbase.com/prime/custody) [\[49\]](https://www.coinbase.com/prime/custody) [\[58\]](https://www.coinbase.com/prime/custody) https://www.coinbase.com/prime/custody

<https://www.coinbase.com/prime/custody>

[\[15\]](https://help.coinbase.com/en/prime/trading-and-funding/supported-cryptocurrencies-and-trading-pairs) https://help.coinbase.com/en/prime/trading-and-funding/supported-cryptocurrencies-and-trading-pairs

<https://help.coinbase.com/en/prime/trading-and-funding/supported-cryptocurrencies-and-trading-pairs>

[\[16\]](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview) [\[59\]](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview) https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview

<https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/dashboard-overview>

[\[17\]](https://developers.uniswap.org/docs/get-started/concepts/how-uniswap-works?utm_source=chatgpt.com) How Uniswap Works

<https://developers.uniswap.org/docs/get-started/concepts/how-uniswap-works?utm_source=chatgpt.com>

[\[18\]](https://academy.binance.com/ka-GE/articles/liquidity-explained) [\[42\]](https://academy.binance.com/ka-GE/articles/liquidity-explained) https://academy.binance.com/ka-GE/articles/liquidity-explained

<https://academy.binance.com/ka-GE/articles/liquidity-explained>

[\[19\]](https://ethereum.org/developers/docs/mev/) https://ethereum.org/developers/docs/mev/

<https://ethereum.org/developers/docs/mev/>

[\[21\]](https://bitcoin.org/en/how-it-works) [\[23\]](https://bitcoin.org/en/how-it-works) https://bitcoin.org/en/how-it-works

<https://bitcoin.org/en/how-it-works>

[\[22\]](https://developer.bitcoin.org/devguide/block_chain.html) [\[27\]](https://developer.bitcoin.org/devguide/block_chain.html) [\[40\]](https://developer.bitcoin.org/devguide/block_chain.html) [\[63\]](https://developer.bitcoin.org/devguide/block_chain.html) https://developer.bitcoin.org/devguide/block_chain.html

<https://developer.bitcoin.org/devguide/block_chain.html>

[\[24\]](https://developer.bitcoin.org/devguide/mining.html) [\[41\]](https://developer.bitcoin.org/devguide/mining.html) https://developer.bitcoin.org/devguide/mining.html

<https://developer.bitcoin.org/devguide/mining.html>

[\[25\]](https://ethereum.org/developers/docs/consensus-mechanisms/pos/?utm_source=chatgpt.com) Proof-of-stake (PoS)

<https://ethereum.org/developers/docs/consensus-mechanisms/pos/?utm_source=chatgpt.com>

[\[29\]](https://ethereum.org/developers/docs/evm/) [\[32\]](https://ethereum.org/developers/docs/evm/) https://ethereum.org/developers/docs/evm/

<https://ethereum.org/developers/docs/evm/>

[\[30\]](https://solana.com/docs/core/accounts) [\[65\]](https://solana.com/docs/core/accounts) https://solana.com/docs/core/accounts

<https://solana.com/docs/core/accounts>

[\[31\]](https://aptos.dev/network/blockchain/move) https://aptos.dev/network/blockchain/move

<https://aptos.dev/network/blockchain/move>

[\[33\]](https://ethereum.org/developers/docs/scaling/optimistic-rollups/) [\[55\]](https://ethereum.org/developers/docs/scaling/optimistic-rollups/) https://ethereum.org/developers/docs/scaling/optimistic-rollups/

<https://ethereum.org/developers/docs/scaling/optimistic-rollups/>

[\[34\]](https://ethereum.org/roadmap/danksharding/) https://ethereum.org/roadmap/danksharding/

<https://ethereum.org/roadmap/danksharding/>

[\[35\]](https://ethereum.org/developers/docs/scaling/sidechains/) https://ethereum.org/developers/docs/scaling/sidechains/

<https://ethereum.org/developers/docs/scaling/sidechains/>

[\[36\]](https://docs.cosmos.network/ibc/latest/intro?utm_source=chatgpt.com) IBC-Go Documentation - Cosmos Docs

<https://docs.cosmos.network/ibc/latest/intro?utm_source=chatgpt.com>

[\[37\]](https://docs.chain.link/data-feeds) https://docs.chain.link/data-feeds

<https://docs.chain.link/data-feeds>

[\[38\]](https://developer.bitcoin.org/devguide/operating_modes.html) https://developer.bitcoin.org/devguide/operating_modes.html

<https://developer.bitcoin.org/devguide/operating_modes.html>

[\[39\]](https://developer.bitcoin.org/devguide/p2p_network.html) [\[45\]](https://developer.bitcoin.org/devguide/p2p_network.html) https://developer.bitcoin.org/devguide/p2p_network.html

<https://developer.bitcoin.org/devguide/p2p_network.html>

[\[43\]](https://thegraph.com/docs/en/indexing/overview/) [\[60\]](https://thegraph.com/docs/en/indexing/overview/) https://thegraph.com/docs/en/indexing/overview/

<https://thegraph.com/docs/en/indexing/overview/>

[\[46\]](https://www.ledger.com/academy/crypto-hardware-wallet) [\[47\]](https://www.ledger.com/academy/crypto-hardware-wallet) https://www.ledger.com/academy/crypto-hardware-wallet

<https://www.ledger.com/academy/crypto-hardware-wallet>

[\[48\]](https://www.bitgo.com/resources/blog/what-is-a-multi-signature-wallet/) https://www.bitgo.com/resources/blog/what-is-a-multi-signature-wallet/

<https://www.bitgo.com/resources/blog/what-is-a-multi-signature-wallet/>

[\[50\]](https://ethereum.org/developers/docs/) https://ethereum.org/developers/docs/

<https://ethereum.org/developers/docs/>

[\[52\]](https://www.infura.io/) https://www.infura.io/

<https://www.infura.io/>

[\[53\]](https://geth.ethereum.org/docs/monitoring/metrics) https://geth.ethereum.org/docs/monitoring/metrics

<https://geth.ethereum.org/docs/monitoring/metrics>

[\[56\]](https://www.fatf-gafi.org/en/topics/virtual-assets.html) https://www.fatf-gafi.org/en/topics/virtual-assets.html

<https://www.fatf-gafi.org/en/topics/virtual-assets.html>

[\[57\]](https://www.coinbase.com/blog/identity-verification-and-financial-compliance) https://www.coinbase.com/blog/identity-verification-and-financial-compliance

<https://www.coinbase.com/blog/identity-verification-and-financial-compliance>

[\[61\]](https://www.circle.com/transparency) https://www.circle.com/transparency

<https://www.circle.com/transparency>

[\[64\]](https://ethereum.org/whitepaper/) https://ethereum.org/whitepaper/

<https://ethereum.org/whitepaper/>

[\[66\]](https://docs.cosmos.network/cometbft/latest/docs/introduction/intro?utm_source=chatgpt.com) Intro

<https://docs.cosmos.network/cometbft/latest/docs/introduction/intro?utm_source=chatgpt.com>

[\[68\]](https://docs.arbitrum.io/get-started/arbitrum-introduction) https://docs.arbitrum.io/get-started/arbitrum-introduction

<https://docs.arbitrum.io/get-started/arbitrum-introduction>

[\[69\]](https://docs.chain.link/architecture-overview/architecture-overview) https://docs.chain.link/architecture-overview/architecture-overview

<https://docs.chain.link/architecture-overview/architecture-overview>
