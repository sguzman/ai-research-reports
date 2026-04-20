# Savonius Wind Turbines – Comprehensive Design & DIY Guide

**Executive Summary:** Savonius rotors are vertical-axis, drag-type wind turbines named for Sigurd J. Savonius (1920s)[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[2\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius). They spin with simple “S”-shaped or semi-cylindrical scoops that catch wind on the concave side and rotate (Fig. 1). Their chief virtues are **simplicity, ruggedness, and omni-directionality** – no yaw mechanism is needed, and they self-start at very low wind speeds[\[3\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=to%20rotate%20in%20the%20direction,wind%20turbines%20against%20the%20wind)[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3). However, this comes at the cost of low aerodynamic efficiency: typical power coefficients (Cp) for a plain two-blade Savonius are only ~0.10–0.25[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[6\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=focused%20on%20the%20optimization%20of,7), well below the Betz limit (0.59) for lift-based turbines[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593)[\[8\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=of%20zero%20when%20the%20TSR,wind%20velocity). In practice, Savonius designs excel at generating **high torque at low RPM** and working in turbulent, changeable winds (urban/rural), making them useful for small-scale pumping, battery charging, and on-site applications[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3)[\[9\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=than%20the%20free).

This report covers everything needed to design, build, and operate a small-to-medium DIY Savonius system. We delve into key theory (aerodynamics, Cp, Betz context, tip-speed ratios), scale laws (swept area, *v³* dependence), and performance data. We compare Savonius to other VAWTs (Darrieus/H-rotor) and HAWTs, highlighting trade-offs. Detailed design parameters are given – rotor geometry (scoop count, overlap, height/diameter), materials (sheet metal, composites, welding/bolting), bearings and support structures – along with practical fabrication methods. Electrical integration is explained: generator options (permanent-magnet alternator or BLDC motor), direct-drive vs gearbox, rectification, MPPT/inverters, charge controllers, wiring and protection, and battery storage sizing. We cover siting and wind resource assessment (turbulence, roughness, IEC classes), mounting (towers, roofs, foundations), noise, safety, and maintenance. Finally, we outline construction plans: step-by-step build instructions, a bill-of-materials (BOM) with cost estimates, CAD/drawing references, testing protocols, and troubleshooting. Wherever possible, data tables summarize options (Cp, TSR, RPM, outputs) and decisions (e.g. scoop count, overlap). Visual aids include diagrams (block diagram, timeline) and an embedded 3D schematic of a multi-stage Savonius turbine【37†】. Primary sources (academic papers, standards, and technical guides) are cited throughout for rigor and credibility.

## 1. Fundamentals of Savonius Turbines

### 1.1 Operating Principle

A Savonius rotor uses **drag differential** rather than lift. Typically two half-cylindrical scoops (buckets) are arranged around a vertical shaft, offset so that when wind hits, the concave side of one scoop “catches” more wind than the convex side of the opposing scoop[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[10\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=that%2C%20as%20the%20rotor%20blades,9). This unbalanced drag creates a torque that turns the rotor. Because the concave side always generates more drag in the wind direction, the turbine self-starts in any wind direction without yaw control[\[11\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[10\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=that%2C%20as%20the%20rotor%20blades,9). The basic geometry is illustrated in Fig. 1:

<img src="/win/linux/Code/Text/marginalia/tmp/ai-research-reports/data/md/savonius-wind-turbines-comprehensive-design-diy-guide/assets/media/rId31.png" style="width:5.83333in;height:3.28125in" />  
\*Figure 1: Savonius turbine concept. (Left) Cutaway schematic showing scoops, shaft, generator stator, and wiring (adapted from a DIY design[\[12\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius)). (Right) Model of a three-stage Savonius rotor (stacked buckets) on a stand. Vertical axis means no yaw needed. Bearings (radial and thrust) support the shaft, with a generator or alternator mounted to it.[\[12\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius)[\[13\]](https://hackaday.com/wp-content/uploads/2018/07/wind_feature.png?w=800#:~:text=)

The Savonius rotor is inherently omni-directional (omni-wind acceptance) and low-speed: blade tip speed never exceeds wind speed (Tip-Speed Ratio TSR ≲ 1)[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was)[\[8\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=of%20zero%20when%20the%20TSR,wind%20velocity). In contrast, lift-based turbines (Darrieus/HAWT) run at TSR~5–8 for maximum Cp. The Savonius’s physics impose TSR≲1 because once blade speed approaches wind speed, relative wind on the blades drops to zero and no more power is extracted[\[8\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=of%20zero%20when%20the%20TSR,wind%20velocity)[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was).

Savonius turbines produce **pulsating torque**: as one scoop moves into wind (concave side forward) it generates positive torque, but the other scoop moving downwind and showing its convex side produces some negative drag torque[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[10\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=that%2C%20as%20the%20rotor%20blades,9). Net torque per revolution is modest, and design features (overlap gap, curved transitions, end plates) can smooth torque and improve performance (see Section 3).

### 1.2 Aerodynamics & Performance

The theoretical power in the wind passing through the rotor *swept area* A is:

``` math
P_{\text{wind}} = \frac{1}{2}\rho Av^{3}
```

where ρ is air density and *v* is wind speed[\[15\]](https://kirkwood.pressbooks.pub/windenergy/chapter/theoretical-power-of-wind/#:~:text=Wind%20Energy)[\[16\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=Theoretical%20Wind%20Power). For a Savonius, the swept area A is simply blade height H times rotor diameter D (i.e. A = H·D)[\[17\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=where%C2%A0%C2%A0is%20the%20density%20of%20the,H%20is%20the%20turbine%20height)[\[18\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=The%20amount%20of%20power%20a,turbine%20facing%20into%20the%20wind). The *actual* mechanical power captured by the turbine is $`P = C_{p} \times P_{\text{wind}}`$, where $`C_{p}`$ is the power coefficient. Savonius rotors have much lower $`C_{p}`$ than lift turbines. Typical two-blade Savonius designs achieve **Cp ≈ 0.1–0.25**[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[6\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=focused%20on%20the%20optimization%20of,7). By comparison, ideal (Betz) lift turbine max is 0.593[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593) and practical HAWTs reach ~0.4–0.5 at peak. Thus, Savonius machines convert only a small fraction of available wind power into shaft power.

Researchers note that pure Savonius designs typically yield **Cp well under the Betz limit** and can be boosted somewhat by modifications. For instance, one review reports classical two-blade Savonius studies show $`C_{p}`$ up to ~0.25 (max) with no auxiliary devices[\[19\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414). With added flow-guiding structures (curtains, guide vanes, cones), some experiments show $`C_{p}`$ up to ~0.4 or even 0.52[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[20\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=e,258%20414). Table 1 (later) compares representative $`C_{p}`$ values. In practice, a well-built 2-blade Savonius might be assumed $`C_{p} \approx 0.15`$ nominal, and perhaps $`0.2`$ with moderate tuning[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[6\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=focused%20on%20the%20optimization%20of,7). It is **rare to exceed 0.3–0.4** without complex augmentations[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[21\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414).

The tip-speed ratio TSR of a Savonius is usually low. Experimental studies indicate Savonius are often designed for **TSR around 1**[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was). CFD results found optimum TSR ~0.8–0.9 with peak $`C_{p} \approx 0.21`$[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was). By contrast, 3-bladed horizontal turbines peak around TSR 6–8[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593). Savonius rotors run at slower angular speeds (to keep tips ~wind speed) and high torque. Typical RPM is roughly (v/D)*60/(2π). For example, a 1 m-diameter rotor in 5 m/s wind gives tip speed ~5 m/s, so RPM ≈ (5/(π*1))×60 ≈ 95 RPM (at TSR=1). The shaft speed scales roughly linearly with wind speed.

Because Savonius power ∝ $`v^{3}`$ (as with all turbines), power rises steeply with wind. A doubling of wind speed gives ~8× power (ignoring cut-out/regulation)[\[22\]](https://kirkwood.pressbooks.pub/windenergy/chapter/theoretical-power-of-wind/#:~:text=wind%20power%20%3D%20%C2%BD%20%CF%81Av)[\[23\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=being%20unable%20to%20increase%20power,proportional%20to%20the%20wind%20velocity). Table 1 illustrates power for a sample small rotor:

| Wind Speed (m/s) | Cp   | D=1 m, H=1 m (A=1 m²): Shaft Power (W) |
|------------------|------|----------------------------------------|
| 3                | 0.20 | 3.3 W (≈0.08 kWh/day)                  |
| 5                | 0.20 | 15.3 W (≈0.37 kWh/day)                 |
| 8                | 0.20 | 62.7 W (≈1.5 kWh/day)                  |
| 12               | 0.20 | 212 W (≈5.1 kWh/day)                   |

*Table 1: Example power of a 1×1 m Savonius (Cp=0.20) vs wind speed. Actual electrical output will be lower due to gearbox/inverter losses.*

These numbers show why Savonius turbines are generally **small-scale**: even 12 m/s wind on a 1 m Savonius yields only a couple hundred watts mechanical (often half as electrical). Doubling rotor size quadruples area (to 4 m²) and power, so output ~1 kW at 12 m/s. Realistic small systems (1–10 kW) require large rotors or multi-rotor arrays.

### 1.3 Comparison to Other Turbine Types

- **Horizontal-Axis (HAWT)**: Conventional windmills with 2–3 airfoil blades. They have high Cp (≈0.3–0.5 at rated speed) and operate at high tip-speed ratios (6–8). They require yaw control and produce more noise and complexity (pitch control, gearboxes) but excel at utility-scale generation. By contrast, a Savonius has no yaw or blade pitch, is simple, and quieter, but only a fraction of the efficiency[\[3\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=to%20rotate%20in%20the%20direction,wind%20turbines%20against%20the%20wind)[\[24\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=Why%20would%20the%20open,at%20various%20wind%20speeds).
- **Darrieus VAWT**: Vertical-axis “egg-beater” or straight-blade (H-rotor) turbines. These are lift-based with higher efficiency than Savonius (Cp up to ~0.4 in optimized designs), and can achieve higher TSR (several units). However, pure Darrieus often cannot self-start (needs external torque until speed builds), and blades endure high cyclic stresses. Savonius turbines will start in low winds and turbulent conditions where Darrieus cannot[\[25\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=ABSTRACT%20Since%20Savonius%20wind%20turbine,dimentional)[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3). A compromise is a *hybrid* Savonius–Darrieus turbine: the Savonius section provides starting torque, feeding flow to the Darrieus for efficiency at higher RPM[\[25\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=ABSTRACT%20Since%20Savonius%20wind%20turbine,dimentional)[\[26\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=,eggbeater%20is%20difficult%20in%20manufacturing).
- **H-Rotor (Straight Darrieus)**: A type of Darrieus with two or three straight blades. The “eggbeater” curvature helps structural loads, but an H-rotor (with uniform attack) is easier to model/manufacture[\[27\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=match%20at%20L69%20,eggbeater%20is%20difficult%20in%20manufacturing). Savonius, however, has only 2–4 scoops with no lift physics. Typical trade-off: a 3-blade Savonius has smoother torque but more drag losses than 2-blade[\[25\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=ABSTRACT%20Since%20Savonius%20wind%20turbine,dimentional)[\[28\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=attack%20which%20helps%20in%20distribution,the%20number%20of%20blades%20and).
- **Other VAWTs**: There exist many hybrids (e.g. Gorlov helical, Cycloturbine), but these usually involve more complex manufacture. Savonius remains the simplest drag-type VAWT[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3).

### 1.4 Betz Limit Context

All wind turbines are bounded by the Betz limit (59.3% of wind power), which assumes an ideal lift turbine[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593). Savonius turbines are *drag-based*, so their theoretical limit is even lower. In practice, as noted, $`C_{p}`$ for bare Savonius rarely exceeds ~0.25. Even with elaborate flow guides, reaching 0.5 is exceptional[\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the)[\[20\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=e,258%20414). Thus Savonius are best viewed as **low-efficiency, high-torque** generators. This tradeoff is acceptable when mechanical simplicity and low cut-in speed are priorities (e.g. rooftop micro-wind or off-grid pumps)[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3)[\[9\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=than%20the%20free).

## 2. Rotor Design & Geometry

### 2.1 Number of Blades (Scoops)

A classical Savonius has **two** scoops (half-cylinders) opposite each other. More scoops (3 or 4) can reduce torque ripple and increase swept area without changing planform. However, additional scoops also add weight and additional negative drag surfaces. Studies generally find **two-blade rotors have higher Cp than 3- or 4-blade versions** of the same area[\[29\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=7%20Mohammadi%20et%20al.%20,Validated%20numerical%20Porous%20deflector%200.249)[\[30\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=When%20the%20design%20models%20in,with%20the%20flow%20reaching%20the). A three-bladed Savonius will start more easily (more continuous torque) but each scoop shares less wind, so net efficiency often dips. Some DIY builds use **three pairs (six scoops) in stages** (see Fig. 1) to boost output smoothness[\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence). If space is limited or multistage stacking is desired, 3-blade (120° apart) is common. For simplicity, two blades (180° apart) is simplest and common in small DIY units[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3).

### 2.2 Overlap Ratio (OR)

The *overlap ratio* $`G/D`$ is the fraction of the rotor diameter by which the scoops overlap (Fig. 2). Some gap (overlap) between concave and convex sides can recycle flow, reducing negative torque on the trailing scoop[\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the). Typical OR values studied are around 0.0–0.3. Most sources suggest an **optimum around 0.10–0.20 (10–20%)** of D[\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the)[\[33\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Another%20study%20examining%20changing%20the,the%20optimum%20for%20better%20results). For example, one analysis found best Cp at OR ≈0.15–0.20[\[33\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Another%20study%20examining%20changing%20the,the%20optimum%20for%20better%20results). Too little overlap (OR=0) gives a simple rotor, but more negative torque; too much overlap (\>0.3) can trap a vortex and reduce torque[\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the). A moderate overlap (15–20% of D) often improves starting and raises Cp by ~10–50% compared to OR=0[\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the)[\[33\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Another%20study%20examining%20changing%20the,the%20optimum%20for%20better%20results). In practice, build an adjustable gap or target ~0.15 (i.e. gap = 0.15×D) and refine by experiment.

【60†Image】 *Figure 2: Key geometry of Savonius rotor. D = diameter, H = blade height, OR = overlap gap between scoops, AR = aspect ratio = H/D. End plates (not shown) may cover the top and bottom to reduce tip losses.*

### 2.3 Aspect Ratio (Height/Diameter)

The *aspect ratio* AR = H/D (blade height to diameter) affects torque smoothness and structural stability. Taller (high AR) turbines sweep more area (more power for given D) and have higher torque due to more blade area, but they require stronger supports and bearings. Most small Savonius turbines use AR between **0.5 and 1.5**. The literature suggests **diminishing returns above AR~1.0**: e.g., increasing AR from 1.0 to 1.5 with OR~0.1 gave ~10% more Cp[\[34\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=integrity%20of%20the%20Savonius%20wind,profile%20came%20from%20a%20batch). Higher AR can raise Cp slightly, but after ~1.0 the structure becomes slender and prone to vibration. Multi-stage (stacked) Savonius can effectively extend H without a single tall rotor, improving both Cp and stability[\[35\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=different%20setups%20as%20opposed%20to,tenths). For a DIY design, AR ≈1 (H≈D) is a good compromise between output and rigidity[\[34\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=integrity%20of%20the%20Savonius%20wind,profile%20came%20from%20a%20batch).

### 2.4 Blade Profile and Modifications

- **Curved scoops:** Standard Savonius scoops are perfect semicircles (batch rotor). Many studies optimize the curvature or use modifications (e.g. twisting the blades into helical shapes)[\[36\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=blade,13). A 45° helical twist can greatly reduce torque pulsation and improve self-start[\[36\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=blade,13). Twisted (helical) Savonius rotors have become popular in commercial small VAWTs, offering smoother torque and somewhat higher Cp (a ~10–20% gain reported)[\[36\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=blade,13). Fabricating a helical scoop is more complex (requires curved surfaces), so for DIY we usually stick to straight-half cylinders or segments from barrels.

- **End plates:** Adding circular end discs on top and bottom of the blades can reduce airflow spilling around blade edges, improving efficiency ~5–10% and mitigating vibrations[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3). In practice, cover the top and bottom of the rotor with plywood, metal, or rigid disks slightly larger than D.

- **Number of stages:** Stacking multiple Savonius sections (with gaps between) increases height (power) and smooths torque. For example, three 1ft-tall stages give AR=3 as a single rotor. However, each stage adds complexity and weight. See Fig. 1 for a 3-stage prototype[\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence).

In summary, basic design parameters: use 2 scoops (or 3 with offset for smoother torque), moderate overlap (10–20%), AR ~1.0, and consider end plates. Table 2 (below) compares variants.

| Design Parameter | Low (simple) | High (optimized) | Trade-offs |
|----|----|----|----|
| Blade count | 2 half-cylinders | 3 or more scoops (stacked) | More blades= smoother torque but added drag/cost[\[29\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=7%20Mohammadi%20et%20al.%20,Validated%20numerical%20Porous%20deflector%200.249). |
| Overlap (OR = G/D) | 0 (no overlap) | ~0.15–0.20 (10–20%) | Positive torque ↑ vs complexity; too high overlap causes vortex[\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the). |
| Aspect ratio (H/D) | ≈0.5–1.0 | ≈1.0–1.5 | Taller = more torque/power[\[34\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=integrity%20of%20the%20Savonius%20wind,profile%20came%20from%20a%20batch) vs structural demands. |
| Blade profile | Semicircle (batch) | Twisted/helical (45°) | Helical improves Cp & start[\[36\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=blade,13) but harder to build. |
| End plates | None | Rigid top/bottom plates | Plates cut tip losses, steadier operation. |

*Table 2: Savonius rotor geometry trade-offs (qualitative).*

### 2.5 Materials & Fabrication

**Blades:** Common materials are thin sheet metal (steel or aluminum) or composite. Many DIYers repurpose **55-gallon steel drums** or plastic barrels: cut the cylinder in half lengthwise for two scoops[\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence). Plastic (PVC) pipes can be slit and unrolled into segments. Metal sheets (e.g. 1–2 mm steel) can be bent into half-cylinders (using a former or manual bending). For durability, galvanized or aluminum avoids rust. Composite (fiberglass/carbon) yields lighter blades, but is costly and complex.

**Shaft:** Usually mild steel pipe or square tubing. Needs to be stiff (hollow or solid ~1-2″ diameter) to support blades and rotate freely in bearings. Attach blades via strong welds or bolted flanges. The shaft transmits torque to the generator.

**Bearings & Supports:** Vertical-axis requires bearings at top and bottom to handle radial and thrust loads. A typical setup uses two *radial bearings* and one thrust bearing. For DIY, ball bearings (2x) at top/bottom with a thrust ball bearing (needle or thrust ball) above lower bearing will work. See Fig. 1: lower radial bearing plus thrust plate at bottom; upper radial bearing fixes shaft laterally. Housings can be steel plates welded to base and cap, or flange mounts.

**End Plates:** Often cut from plywood or metal, fastened above and below the blades around the shaft. Ensure clearance from tower/tower supports.

**Frame & Tower:** - A robust frame holds the shaft and generator. For small turbines (~\<500 W), a simple stand of angle iron or welded steel can suffice. Larger ones (\>1 m dia) need a mast or tower. Towers can be fixed (guyed or free-standing) – see Site/Mounting below. - Base plate or foundation depends on mounting height and soil. Even a ground-mount Savonius (short mast \<5m) typically needs concrete footings or anchor bolts.

**Electrical (magnetic) rotor support:** In Fig. 1, a multi-stage design shows permanent magnets on a rotor with ~1 mm gap to a stationary stator【37†】. In small systems, one may use a bicycle hub motor (for instance) by lacing magnets to the shaft. Alternatively, attach a pulley or gearbox to drive a standard generator.

Fabrication: Weld or bolt steel parts; make sure rotating assembly is balanced. Use bolts + nuts with thread-lock or weld as needed. Ensure weather-proofing (paint/galvanize metal; seal wood/composite blades). All exposed wiring must be weather-protected.

## 3. Aerodynamic Theory (Detailed)

For the technically inclined, we summarize Savonius aerodynamics and power equations[\[37\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Figure%205%20%20shows%20the,112)[\[38\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=replaced%20in%20Equation%20,14)[\[39\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Drag,1%29%2C%20as%20follows):

- **Drag Force on Blade:** $`F = \frac{1}{2}\rho\, C_{D}\, A_{\text{proj}}\, v^{2}`$, where $`A_{\text{proj}}`$ is projected area (blade height × effective width), and $`C_{D}`$ depends on concave vs convex side[\[40\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=The%20force%20occurring%20on%20the,7). The concave side has a higher drag coefficient than the convex side.

- **Net Torque & Power:** At a given wind speed $`V`$ and blade tangential speed $`v_{t}`$, forces on advancing (downwind concave) and returning (upwind convex) blades differ[\[41\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Turbine%20power%20is%20equal%20to,11). Analytical models yield an expression for turbine power as a function of blade speed and drag coefficients[\[42\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=). Optimizing power (∂P/∂ω = 0) gives an optimal rotor speed. In an idealized two-blade Savonius, this results in an equilibrium TSR ~0.8–0.85[\[43\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=In%20Savonius%20wind%20turbines%20without,15).

- **Tip-Speed Ratio (TSR):** Defined $`\lambda = v_{\text{tip}}/V = \omega R/V`$[\[44\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=The%20performance%20of%20a%20Savonius,speed%2C%20and%20%CF%89%3A%20angular%20velocity). For drag turbines, $`\lambda < 1`$. At $`\lambda = 1`$, blade moves with wind, net force ≈ zero. The literature notes Cp falls to 0 at λ=0 or 1, with a peak at intermediate ~0.8[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was)[\[8\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=of%20zero%20when%20the%20TSR,wind%20velocity).

- **Power Coefficient:** Using measured torque $`T`$ and angular speed $`\omega`$, $`C_{p} = \frac{T\omega}{\frac{1}{2}\rho AV^{3}}`$[\[44\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=The%20performance%20of%20a%20Savonius,speed%2C%20and%20%CF%89%3A%20angular%20velocity). Experimental data generally show Savonius max $`C_{p}`$ ~0.2 (sometimes up to 0.25)[\[21\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414). Advanced modifications can push towards ~0.4 (e.g. guide vanes, deflectors)[\[45\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=e,258%20414).

*No single formula* yields an easy closed-form Cp vs TSR for Savonius due to its complex drag interactions. For design, empirical $`C_{p}`$ benchmarks from literature (as in Table 1 and Fig. 3) guide realistic expectations.

## 4. Electrical Integration

### 4.1 Generator/Alternator Options

Savonius turbines produce relatively low RPM and high torque. Generator choice depends on intended output and RPM:

- **Permanent-Magnet Alternator (PMA)/BLDC motors:** A common DIY solution is to use a small permanent-magnet DC generator or brushless DC motor (with external controller). These can generate voltage at low RPM (e.g. ~200–800 RPM) and are compact. For example, repurposed 12–24 V BLDC motors (e.g. from ebike or treadmill) or axial-flux PM alternators (aka PMA) are popular. The rotor of such generators is often bolted to the turbine shaft; the stator is fixed to the frame. Three-phase PM generators with a rectifier can directly charge batteries.

- **Automotive alternator:** Car alternators produce ~13.8 V at a few 1000 RPM. They are heavy and need gearing to reach their speed. Generally not ideal for low-speed Savonius unless a gearbox is used. (Some DIYers rebuild them with smaller pulleys/gears but careful slip-synchronization is needed.)

- **Asynchronous (induction) generators:** Not suitable for stand-alone without a grid or large capacitor bank for excitation.

- **Gearbox vs Direct Drive:** A gearbox can step up RPM but adds cost and friction. Small Savonius (up to ~200 RPM) can often directly drive a generator whose optimal speed is similar. For larger turbines, some use belts or gears. Direct drive (shaft directly coupling rotor to generator) is simplest and lowest maintenance if generator can produce sufficient voltage at the rotor’s speeds.

For example, a small PMA rated 12 V/100 W might need ~300 RPM to produce 12 V open-circuit, so the turbine must spin accordingly. Ensure generator’s "cut-in" speed (for voltage) matches typical turbine speeds. Some mechanical overspeed protection (clutches or slip couplings) can protect the generator.

### 4.2 Power Electronics

- **Rectification:** Most DIY Savonius systems charge batteries, so a diode bridge (3-phase if needed) rectifies AC to DC. Heavy-duty Schottky diodes (low drop) or an external rectifier board can be used.

- **MPPT/Inverter:** For grid-tie or optimizing battery charging, a Maximum Power Point Tracker (MPPT) can be used. Off-grid battery systems require a charge controller. MPPT controllers for wind (12/24 V) adjust the electrical load to maximize generator output. Many small wind charge controllers on the market include dump loads to stabilize voltage.

- **Battery Storage:** Standalone systems need deep-cycle batteries (e.g. lead-acid or LiFePO4) to store energy. Sizing: base on average daily kWh load. For example, if the Savonius averages 100 W in good wind (2.4 kWh/day), and you want 2 days autonomy, need ~5 kWh battery (~200 Ah at 24 V). Batteries require charge controllers to prevent overcharge. Automotive batteries (starting batteries) are **not suitable** due to shallow cycling damage[\[46\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Stand,cycling%20operations.%5B16).

- **Wiring and Protection:** Use appropriately gauged wires (low voltage/high current makes copper runs thick). Include fuses or breakers to protect from faults. A dump load resistor (or heater element) can absorb excess power when batteries are full. All outdoor wiring should be weather-proof (Glands, sealed boxes). Earthing/grounding the turbine frame is recommended for lightning/safety.

### 4.3 Expected Electrical Output

Given the low power from Savonius (Table 1), it's most practical for *off-grid battery charging* or modest AC loads (via inverter). For instance, a 1 m×1 m Savonius (Cp~0.2) in 5 m/s wind yields ~15 W shaft power【Table 1】. After generator (~70% eff.) and inverter (~90%), usable may be ~10 W. This can trickle-charge a battery, but won’t run a major appliance. At 12 m/s, same rotor gives ~200 W mechanical, maybe 120 W AC – enough for small lights or sensors. A larger unit (2×2 m) scales by area (4× area, ~1 kW mechanical at 12 m/s).

As an illustration, Table 3 shows approximate electrical power for two rotor sizes at given winds (assuming 50% overall system efficiency). Actual outputs vary widely with exact Cp, generator, and conditions.

| Wind (m/s) | 1×1 m rotor (≈20% eff, Pshaft: 3, 15, 63, 212 W) | 2×2 m rotor (~same Cp) |
|----|----|----|
| 3 | ~1.5 W (fully ~0.5 W to battery) | ~6 W (1.5 W) |
| 5 | ~7 W (3 W) | ~28 W (14 W) |
| 8 | ~30 W (15 W) | ~120 W (60 W) |
| 12 | ~100 W (50 W) | ~400 W (200 W) |

*Table 3: Example AC output (post-conversion) of two Savonius sizes. Values are rough.*

These small outputs mean Savonius are best used for low-power scenarios (battery charging, lights, sensors, micro-UPS). For significant household kWh, a horizontal wind turbine or solar array is more cost-effective. Nevertheless, in turbulent or harsh winds (urban areas, roof tops), Savonius can harvest wind where a propeller might stall.

## 5. Site Assessment & Energy Yield

### 5.1 Wind Resource Estimation

Even simple DIY projects require checking local wind. The *average wind speed* at hub height is the key predictor of energy (since power ∝ *v³*). Use data from meteorological stations, local weather or tools (MERRA, Wind Atlas, or DOE SWERA maps). Adjust wind speed for height (higher is better: Roughly, wind speed increases ~ (height)^(1/7) rule of thumb). Also account for terrain roughness: build an approximate site class (IEC classes A–D) or use a tool like \[16†L0\] suggests.

For a rudimentary estimate:  
- Identify nearby weather stations and note mean wind speed at e.g. 10 m. If unknown, assume 5–7 m/s average in open terrain.  
- Correct for height: a 10m measurement might be ~10% lower than 20m level.  
- Consider obstruction: buildings, trees can halve wind speed and cause turbulence. A Savonius tolerates turbulence better but yields drop off quickly if blocked. The guide of thumb is to place the rotor ≥9 m above any obstacle within 90 m[\[47\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Because%20wind%20speeds%20increase%20with,of%20return%20in%20power%20production).

Annual energy is hard to estimate manually; small wind calculators exist. However, one can do: AEP (kWh) ≈ 8760 h \* 0.5ρA Cp \* (v_avg)^3 \* system_efficiency. With a low Cp, even a high v_avg yields limited kWh. It’s often better to measure site wind with an anemometer for a few weeks if serious output is needed.

### 5.2 Siting & Mounting

- **Height:** Place the rotor as high as practical. Even small increases in height mean higher wind and steadier flow[\[47\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Because%20wind%20speeds%20increase%20with,of%20return%20in%20power%20production). For an urban DIY, that may mean rooftop mount or a tall pole. The DOE guide recommends rotor bottom at least 9 m above any obstacle within 90 m[\[47\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Because%20wind%20speeds%20increase%20with,of%20return%20in%20power%20production). Practically, many residential turbines use 10–20 ft poles. Savonius are less sensitive to height than HAWTs (due to low cut-in speed), but still benefit.
- **Mounting Options:**
- *Roof-Mount:* Quick installation if roof strong enough. Beware vibrations transferred to structure. The rotor will spin off-axis in gusts – ensure no interference with roof elements. Roof mounting saves a tower cost but may be noisy to inhabitants.
- *Pole or Tower:* Easier maintenance (tilt-down towers possible) and better wind exposure. Guyed towers (with wires) are inexpensive but need space; free-standing (self-supporting) need heavier steel. For small Savonius, even a 3–6 m pole is often enough. Concrete foundations or anchor bolts should secure the base.
- **Orientation:** None needed – Savonius is omnidirectional[\[3\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=to%20rotate%20in%20the%20direction,wind%20turbines%20against%20the%20wind). Just ensure clear ring of space (360°) around it (no gear box tail needed).
- **Site Class:** Use IEC 61400-2 guidelines for small wind (if planning performance claims). For DIY, be conservative: assume Class C/D (mean 5–6 m/s) unless data shows stronger winds.

### 5.3 Environmental & Safety Considerations

- **Noise:** Savonius turbines are generally quiet due to low tip speed and fewer tonal components[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3). At a few tens of RPM, they produce a low hum, less than HAWTs (which can produce whoosh at 300+ RPM). Neighbors are seldom troubled. However, unbalanced or “resonant” blades can squeal – ensure good bearings and balance.
- **Birds/Wildlife:** Vertical rotors are said to be slightly bird-friendly (blades move slower and are more visible). But bird strikes are still possible; treat it like any turbine.
- **Failure Modes:** Savonius has fewer moving parts. Still, overspeed in extreme gusts can stress shaft/bearings. Incorporate a simple **governor**: e.g. a centrifugal clutch or magnetic brake that engages above a threshold, or just design strong enough (overspeed rarely generates much extra torque if load capped by generator). Cutting out at very high winds may use a mechanical furling or a brake (some DIYs use a friction pad). Monitor generator current – if it spikes, disconnect it.
- **Lightning:** As with any mast, consider a lightning rod/grounding system if in a thunder-prone area. Ground the tower and metal parts.

### 5.4 Maintenance

Savonius turbines are low-maintenance, but still require checks: - **Bearings:** Grease or oil periodically (yearly or per 5000 h) with weather-resistant lubricant.  
- **Structure:** Inspect bolts, welds, and blade integrity (especially if made from used drums) at least annually.  
- **Electrical:** Check wiring insulation; ensure charge controller and inverter ventilated (batteries in temp-controlled area if lead-acid).  
- **Cleaning:** Dust and debris can accumulate on blades; clean to maintain aerodynamics. In winter, ice can halt the rotor – plan for de-icing or parking the turbine.

## 6. Step-by-Step Construction Plan

### 6.1 Design Phase

1.  **Define Objectives:** Estimate required power (or make it educational). Determine site conditions (wind, space, budget). For example, target 200 W average in 6 m/s wind.

2.  **Rotor Dimensions:** Choose D and H. Using Table 3 and desired output, back-calculate a needed swept area. E.g., for ~100 W at 6 m/s, maybe D=2 m, H=1.5 m (A=3).

3.  **Geometry:** Set OR ≈0.15D, AR=H/D≈0.75. 2 scoops (or 3 for balanced torque).

4.  **Materials & Parts List:**

5.  Scoops: e.g. two 55-gal steel drums (each yields 2 half-cylinders)[\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence).

6.  Shaft: 1.5″ steel pipe, 4–6 ft long.

7.  Bearings: e.g. two 1.5″ bore pillow-block ball bearings + one thrust bearing.

8.  Frame: steel tubing or angle iron for base.

9.  Generator: e.g. 12 V PMA or BLDC hub motor, approx. 300–500 W rated.

10. Charge controller, battery (e.g. 12V 100Ah), wires, diode bridge.

11. Misc: nuts/bolts, welding rod, paint.

12. Tools: welder, grinder, drill, bandsaw or torch, anemometer.

13. **3D Modeling:** If possible, model in CAD or draw to validate fit. Ensure shaft aligns through scoops, bearings, and generator. Check clearance.

### 6.2 Fabrication Steps

1.  **Cut Blades:**
2.  For drums: cut drum in half vertically to get two halves. Cut overlapping 120° cuts if needed for more blades. Remove ribs. Clean edges.
3.  Alternatively, cut sheet metal into strips, form into arcs (use a pipe or jig).
4.  **Form Scoops:** Bend cuts into 180° half-cylinders. Overlap edges by OR width or weld at ends. If needed, trim so final diameter = desired D.
5.  **Prepare Shaft:** Cut steel pipe. Weld a central plate (mounting hub) to shaft at blade mid-height; fasten scoops to this hub. Drill holes or weld flanges to bolt on scoops. Attach end plates above and below blades (bolt or weld around shaft).
6.  **Assemble Rotor:** Bolt or weld scoops to hub. Ensure evenly spaced (180° apart or 120° for 3-blade). Check balance: spin by hand and adjust weights if needed.
7.  **Frame & Bearings:** Weld or bolt frame including base plate. Mount lower bearing on base. Mount upper bearing on a cap plate (to be bolted at top of shaft location). Fit shaft through bearings, check smooth rotation. Insert thrust bearing under rotor if used (as in Fig. 1).
8.  **Generator Coupling:** At lower shaft end (below bottom bearing), attach coupling to generator. If using a hub motor, weld or bolt its hub to shaft. Ensure alignment to avoid wobble.
9.  **Wiring:** Install diode bridge on frame (weatherproof box). Connect generator outputs (AC) to rectifier, then to battery via controller. Ground the frame.
10. **Finish:** Paint rotor (to prevent rust), assemble tower or mount frame. Ensure rotating parts are clear of structure.

### 6.3 Testing & Tuning

- **No-load Spin Test:** Release rotor in light wind or blow with fan. Check rotation smoothness, bearing friction, and V rms from generator.
- **Load Test:** Connect to battery through charge controller. Monitor voltage/current vs wind speed. Use tachometer to find RPM at various winds. Calculate TSR.
- **Data Collection:** Use an anemometer to log wind, and a wattmeter/battery monitor for output. Verify predicted power (e.g. Table 1) roughly. Check that cut-in speed matches expectations (~2–3 m/s).
- **Safety Check:** Verify any overspeed device works; ensure rotor stops freely when power disconnected.

### 6.4 Troubleshooting

- **Not starting:** Check overlap is not too large; remove load to see if rotor can spin freely. Inspect balance and ensure low friction.
- **Low voltage output:** Confirm generator spec (some need higher RPM). Consider re-gearing or using a different generator.
- **Excess noise/vibration:** Balance blades, add end-plate braces, tighten bearings. Consider helical modification if oscillation persists.
- **Overcharging battery:** Use proper charge controller; if absent, add dump resistor.

## 7. Expected Performance & Output

Based on design and site wind, estimate energy yield:

- Use the power equation $`P = 0.5\rho Av^{3}C_{p} \times \eta`$ (η = overall system efficiency ~0.5–0.7).
- For simplicity, with Cp ≈0.20 and η≈0.5, P(W) ≈ 0.5*1.225*(A)*(v^3)*0.2\*0.5. For A=1 m²: P ≈0.06 v³ (W).
- Integrate over wind distribution or assume constant for rough estimates. E.g. average 5 m/s continuous yields ~24 Wh per hour → ~0.6 kWh/day.

#### Sample Site Yields (Estimates)

If average wind at hub is 4 m/s (mean), and we have a 2×2 m Savonius (A=4 m², Cp=0.2):  
Power ≈0.06 \* 4 \* 64 = 15.4 W on average. That is ~370 Wh/day (~135 kWh/yr) after system losses. At 6 m/s: P≈0.06*4*216=51.8 W → 1.2 kWh/day (~430 kWh/yr).

Compare to a small solar panel: 200 W PV at 5 peak sun-hours = 1 kWh/day. So the Savonius is very modest. This underscores that **Savonius turbines are supplementary**, not primary, sources in residential settings, unless wind is very high.

## 8. Comparison Tables and Figures

- **Table 1:** (above) Savonius power vs wind (Cp=0.20).
- **Table 2:** (above) Geometry trade-offs.
- **Table 3:** (above) Example output for 1×1 and 2×2 m rotors.
- **Mermaid block diagram:** The electrical system layout.

<!-- -->

    flowchart TD
        Wind[Wind] --> Turbine[Turbine (Savonius Rotor)];
        Turbine --> Shaft[Rotating Shaft];
        Shaft --> Generator[Generator (PMA/BLDC)];
        Generator --> Rectifier[Rectifier (AC→DC)];
        Rectifier --> ChargeCtrl[Charge Controller / MPPT];
        ChargeCtrl --> Battery[Battery Bank];
        Battery --> Inverter[Inverter (DC→AC)];
        Inverter --> Load[AC Loads/Grid];
        ChargeCtrl --> Dump[Dump Load (heater) - if needed];

- **Mermaid timeline:** Project timeline (example):

<!-- -->

    gantt
        title Build & Test Timeline
        dateFormat  YYYY-MM-DD
        section Planning
          Design Specs         :done,    des01, 2026-01-01,2026-01-05
          Sourcing materials   :done,    mat01, after des01, 2026-01-15
        section Fabrication
          Blade cutting/forming:done,    fab01, 2026-01-16,2026-01-25
          Shaft & frame build  :done,    fab02, 2026-01-20,2026-01-30
          Assembly             :done,    asb01, 2026-01-28,2026-02-05
        section Electrical
          Generator install    :active,  elec01, 2026-02-02,2026-02-07
          Wiring & controls    :         elec02, 2026-02-05,2026-02-12
        section Testing
          No-load spin test    :         test01, 2026-02-10,2026-02-15
          Load testing         :         test02, after test01, 2026-02-20
          Tuning & refine      :         test03, after test02, 2026-03-01

## 9. Bill of Materials (BOM) & Costs

Approximate costs (USD) for a small DIY Savonius (~200–500 W):

| Item | Qty | Material/Spec | Cost (ea) | Comments |
|----|----|----|----|----|
| Steel sheets/drums | 2 | 55-gal drum (steel) | \$20–50/drum | Many scrapyards sell used drums cheaply. |
| Shaft/piping | 1 | 2" steel pipe, 5–6 ft | \$30 |  |
| Bearings | 2 | 1.5" bore ball bearings | \$15–25 each | Pillow-blocks ~\$30; thrust bearing ~\$10 |
| End plates (plywood) | 2 | 1x D-diameter discs | \$10–20 total | Plywood or aluminum sheet. |
| Fasteners | lot | Bolts/nuts/washers | \$10 | Stainless or galvanized recommended. |
| Frame materials | as needed | Angle iron/pipe | \$30 | For base stand/tower flange. |
| Generator | 1 | 12V PMA or BLDC motor | \$100–200 | E.g. e-bike motor, car alternator conversion, etc. |
| Charge controller | 1 | 10–20A wind controller | \$50–100 | Or DIY regulator. |
| Battery | 1 | 12V deep-cycle (~100Ah) | \$100–150 | If off-grid use; optional if grid-tie. |
| Inverter (optional) | 1 | 12V→120VAC (300–500W) | \$100–200 | If AC loads or grid interface needed. |
| Misc electronics |  | Diodes, wires, connectors | \$20 | Fuses, diodes, conduit, etc. |
| **Total (approx)** |  |  | **\$450–800** | (Without labor or tower; can vary widely) |

*Note:* Costs vary by region and sources. Salvaged parts (drums, motors) can cut expenses. For example, some builds use old car alternators or recycled e-bike motors.

## 10. References

- Savonius fundamentals and performance reviews[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the)[\[6\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=focused%20on%20the%20optimization%20of,7).
- Wind power basics, Betz law[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593).
- DOE Small Wind Guidebook – small turbine siting, wiring, storage[\[47\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Because%20wind%20speeds%20increase%20with,of%20return%20in%20power%20production)[\[48\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Small%20wind%20turbines%20generate%20direct,code%20officials%2C%20and%20future%20homebuyers).
- Experimental Savonius data: power coefficients[\[21\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414).
- Hybrid & comparative VAWT studies[\[49\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=of%20Savonius%2C%20Darrieus%20and%20combination,of%20its%20drag%20type%20blades)[\[12\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius).
- DIY turbine examples[\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence).

*All inline references are from opened sources (scientific articles, gov documents, etc.) as detailed above.*

------------------------------------------------------------------------

[\[1\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the) [\[3\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=to%20rotate%20in%20the%20direction,wind%20turbines%20against%20the%20wind) [\[5\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=determined%20that%20the%20power%20coefficient,Thus%2C%20within%20the) [\[11\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Savonius%20wind%20turbines%20have%20a,Since%20the%20torque%20on%20the) [\[17\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=where%C2%A0%C2%A0is%20the%20density%20of%20the,H%20is%20the%20turbine%20height) [\[19\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414) [\[20\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=e,258%20414) [\[21\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=%28a%29%20E,258%20414) [\[29\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=7%20Mohammadi%20et%20al.%20,Validated%20numerical%20Porous%20deflector%200.249) [\[30\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=When%20the%20design%20models%20in,with%20the%20flow%20reaching%20the) [\[37\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Figure%205%20%20shows%20the,112) [\[38\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=replaced%20in%20Equation%20,14) [\[40\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=The%20force%20occurring%20on%20the,7) [\[41\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=Turbine%20power%20is%20equal%20to,11) [\[42\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=) [\[43\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=In%20Savonius%20wind%20turbines%20without,15) [\[44\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=The%20performance%20of%20a%20Savonius,speed%2C%20and%20%CF%89%3A%20angular%20velocity) [\[45\]](https://www.mdpi.com/2227-9717/11/5/1473#:~:text=e,258%20414) Investigation of Performance Enhancements of Savonius Wind Turbines through Additional Designs

<https://www.mdpi.com/2227-9717/11/5/1473>

[\[2\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius) [\[12\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=The%20wind%20turbine%20that%20,Finnish%20engineer%20Sigurd%20Johannes%20Savonius) [\[24\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=Why%20would%20the%20open,at%20various%20wind%20speeds) [\[31\]](https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/#:~:text=After%20doing%20some%20research%2C%20the,the%20testing%20can%20now%20commence) DIY Wind Turbine For Where The Sun Doesn’t Shine \| Hackaday

<https://hackaday.com/2018/08/14/diy-wind-turbine-for-where-the-sun-doesnt-shine/>

[\[4\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=3) [\[6\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=focused%20on%20the%20optimization%20of,7) [\[8\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=of%20zero%20when%20the%20TSR,wind%20velocity) [\[9\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=than%20the%20free) [\[10\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=that%2C%20as%20the%20rotor%20blades,9) [\[32\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=The%20overlap%20ratio%20,have%20been%20performed%20on%20the) [\[33\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Another%20study%20examining%20changing%20the,the%20optimum%20for%20better%20results) [\[34\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=integrity%20of%20the%20Savonius%20wind,profile%20came%20from%20a%20batch) [\[35\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=different%20setups%20as%20opposed%20to,tenths) [\[36\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=blade,13) [\[39\]](https://www.mdpi.com/1996-1073/17/15/3708#:~:text=Drag,1%29%2C%20as%20follows) Enhancing the Performance of Savonius Wind Turbines: A Review of Advances Using Multiple Parameters \| MDPI

<https://www.mdpi.com/1996-1073/17/15/3708>

[\[7\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=,593) [\[16\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=Theoretical%20Wind%20Power) [\[23\]](https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/#:~:text=being%20unable%20to%20increase%20power,proportional%20to%20the%20wind%20velocity) Power from Wind – Wind Energy

<https://kirkwood.pressbooks.pub/windenergy/chapter/chapter-4-power-from-wind/>

[\[13\]](https://hackaday.com/wp-content/uploads/2018/07/wind_feature.png?w=800#:~:text=) hackaday.com

<https://hackaday.com/wp-content/uploads/2018/07/wind_feature.png?w=800>

[\[14\]](https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023#:~:text=Cp%20in%20Fig,54%20was) Tip speed ratio depending on the power coefficient of the Savonious rotor. \| Download Scientific Diagram

<https://www.researchgate.net/figure/Tip-speed-ratio-depending-on-the-power-coefficient-of-the-Savonious-rotor_fig3_230606023>

[\[15\]](https://kirkwood.pressbooks.pub/windenergy/chapter/theoretical-power-of-wind/#:~:text=Wind%20Energy) [\[22\]](https://kirkwood.pressbooks.pub/windenergy/chapter/theoretical-power-of-wind/#:~:text=wind%20power%20%3D%20%C2%BD%20%CF%81Av) Theoretical Power of Wind – Wind Energy

<https://kirkwood.pressbooks.pub/windenergy/chapter/theoretical-power-of-wind/>

[\[18\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=The%20amount%20of%20power%20a,turbine%20facing%20into%20the%20wind) [\[46\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Stand,cycling%20operations.%5B16) [\[47\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Because%20wind%20speeds%20increase%20with,of%20return%20in%20power%20production) [\[48\]](https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook#:~:text=Small%20wind%20turbines%20generate%20direct,code%20officials%2C%20and%20future%20homebuyers) Small Wind Guidebook \| Department of Energy

<https://www.energy.gov/cmei/wind/windexchange/windexchange/small-wind-guidebook>

[\[25\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=ABSTRACT%20Since%20Savonius%20wind%20turbine,dimentional) [\[26\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=,eggbeater%20is%20difficult%20in%20manufacturing) [\[27\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=match%20at%20L69%20,eggbeater%20is%20difficult%20in%20manufacturing) [\[28\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=attack%20which%20helps%20in%20distribution,the%20number%20of%20blades%20and) [\[49\]](https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf#:~:text=of%20Savonius%2C%20Darrieus%20and%20combination,of%20its%20drag%20type%20blades) tfaws.nasa.gov

<https://tfaws.nasa.gov/wp-content/uploads/TFAWS2020-ID-512-El-Nenaey-Paper.pdf>
