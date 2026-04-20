# Electric Motor Design: Principles, Types, and Practices

**Executive Summary:** Electric motors – devices that convert electrical energy to mechanical torque – are ubiquitous in modern engineering. Their history stretches from Faraday’s 1821 demonstration of electromagnetic rotation[\[1\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/#:~:text=Self,current%20produces%20a%20magnetic%20field) through Tesla’s 1888 AC induction motor patents[\[2\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=It%20fell%20to%20Edison%E2%80%99s%20former,the%20requisite%20AC%20transformers%20and) to today’s high-efficiency drives. Designing a custom motor requires understanding electromagnetic fundamentals, machine types, performance trade-offs, materials, control electronics, and manufacturing. This guide reviews motor history and key inventors; explains Lorentz-force torque production and torque–speed–power relations (e.g. $`P = T\omega`$, \$T=9550\\P\_{\rm kW}/n\$[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as)); and surveys motor categories (DC brushed, BLDC/PMSM, induction/asynchronous, synchronous reluctance, switched reluctance, stepper, linear, homopolar, axial-flux, etc.). We examine losses (copper $`I^{2}R`$, iron (hysteresis/eddy), mechanical, stray)[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point) and efficiency (modern large motors often exceed 90–95%, enabling global standards IE1–IE4[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1)[\[6\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=IEC%20efficiency%20standards%20Standard%20IEC%2FEN,apply%20to%20synchronous%20and%20permanent)). Key materials (Cu windings, steel laminations, rare-earth magnets) and winding/slot topologies are covered, along with analytical vs. FEA design methods. Mechanical aspects (bearings, shafts, housing), manufacturing processes (lamination stamping, winding, assembly), prototyping and test methods, and instrumentation (torque sensors, thermography) are discussed. Control electronics (PWM inverters, vector/FOC drives, sensorless control) and sensors (optical encoders, resolvers, Hall) are described. Emerging trends (additive manufacturing, wide-bandgap GaN/SiC drives[\[7\]](https://www.ti.com/lit/pdf/slyt801#:~:text=instance%2C%20GaN%20offers%20a%20gate,%E2%84%A6)[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN), integrated motors, magnet-free SynRM motors[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency)) are summarized. A step-by-step design workflow and a worked example for sizing a motor are provided, along with key formulas and a bill-of-materials template. Comparison tables summarize motor types by attributes (efficiency, cost, torque density, speed range, control complexity, typical uses). References to major texts, IEEE/NEMA/IEC standards, and manufacturer notes underpin the discussion.

## History and Key Inventors

Electric motors evolved from early 19th-century discoveries. In 1821 Faraday built the first “homopolar” motor: a wire in mercury that rotated around a magnet[\[1\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/#:~:text=Self,current%20produces%20a%20magnetic%20field). By 1832–1834, Sturgeon and Jacobi developed the first practical rotary motors (Jacobi drove a small boat)[\[1\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/#:~:text=Self,current%20produces%20a%20magnetic%20field). In 1834 Thomas Davenport created a DC commutator motor and in 1837 obtained the first US electric-motor patent[\[10\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/davenport-motor-1834/#:~:text=battery%20provided%20the%20electricity,the%20machines%20in%20his%20workshop)[\[11\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/davenport-motor-1834/#:~:text=decided%20to%20try%20again%20after,after%20patent). Davenport’s motor used a battery, brushes and a commutator – essentially a primitive DC motor. Edison's later DC dynamos and motors (1870s–1880s) enabled DC distribution. The breakthrough for AC came in 1888, when Tesla (and independently Ferraris) invented polyphase AC induction motors[\[2\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=It%20fell%20to%20Edison%E2%80%99s%20former,the%20requisite%20AC%20transformers%20and). Westinghouse commercialized Tesla’s two-phase AC motor in 1888–89, and engineer Dolivo-Dobrovolsky built the first three-phase cage-rotor induction motor in 1889[\[12\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=George%20Westinghouse%20acquired%20Tesla%E2%80%99s%20AC,phase%20induction%20motor%20in%201889). Since then, inventors like Charles Brush, George Westinghouse, Frank Julian Sprague (DC motor with shunt/compound fields), Steinmetz, and many others improved motor technology. Modern innovators include Bose, Miller, Krause, Chapman, and manufacturers (Siemens, ABB, Bosch, Nidec) advancing specialized designs.

## Electromechanical Principles

All motors rely on the Lorentz force: a current-carrying conductor in a magnetic field experiences a force $`F = I\ell \times B`$. In practical machines, AC or DC currents in stator coils produce a rotating magnetic field which interacts with currents or magnets on the rotor to generate torque. Key quantities: flux linkage $`\psi`$ (Wb-turns), electromotive force $`e = d\psi/dt`$, torque $`T \propto i \times \psi`$. For example, a surface-mounted permanent-magnet synchronous (PMSM) motor yields electromagnetic torque $`T_{e} = \frac{3}{2}p\lambda_{M}i_{q}`$, where $`p`$ = pole pairs, $`\lambda_{M}`$ = rotor flux linkage and $`i_{q}`$ = q-axis current[\[13\]](https://ntrs.nasa.gov/api/citations/20210025115/downloads/PMSM_v6.pdf#:~:text=%F0%9D%91%87%F0%9D%91%92%20%3D%203%202%20%F0%9D%91%9B%F0%9D%91%9D%F0%9D%9C%86%F0%9D%91%80%F0%9D%91%96%F0%9D%91%9E,%F0%9D%91%91%F0%9D%9C%94%F0%9D%91%9F%20%F0%9D%91%91%F0%9D%91%A1%20%3D%20%F0%9D%91%9B%F0%9D%91%9D%20%F0%9D%90%BD). In DC machines (with fixed field flux), $`T = k_{t}I`$ (directly proportional to armature current). In an induction motor, torque arises from slip-induced currents: $`T \propto sE^{2}`$ (simplified). In all cases electrical power converts to mechanical power $`P = T\omega`$ (with $`\omega`$ in rad/s). Full-load torque for a motor rated \$P\_{\rm kW}\$ at speed \$n\_{\rm rpm}\$ is \$T = 9550\\P\_{\rm kW}/n\_{\rm rpm}\$[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as).

## Motor Types

**Brushed DC Motors:** The earliest practical motors. A rotor (armature) winding rotates inside a stationary magnetic field (from permanent magnets or a field winding). Brushes and a mechanical commutator switch the armature current each half-turn, keeping torque in one direction[\[14\]](https://en.wikipedia.org/wiki/Brushed_DC_electric_motor#:~:text=Brushed%20motors%20were%20the%20first,using%20%2082%20power%20electronic). Brushed DC motors offer simple construction and easy speed control via voltage, but brushes wear out. They were common in older appliances and vehicles, but many applications now use brushless designs[\[14\]](https://en.wikipedia.org/wiki/Brushed_DC_electric_motor#:~:text=Brushed%20motors%20were%20the%20first,using%20%2082%20power%20electronic). Series, shunt, and compound-wound configurations allow different torque-speed curves (series wound gives high starting torque; shunt wound gives almost constant speed vs load).

**Brushless DC / Permanent-Magnet Synchronous (BLDC/PMSM):** Modern equivalents of DC motors, but with no brushes. A permanent-magnet rotor provides a fixed flux; stationary three-phase (or multi-phase) stator windings are driven by an inverter. Electronic commutation (based on Hall sensors or sensorless algorithms) replaces brushes[\[15\]](https://maintexmotors.com/who-invented-bldc-motor/#:~:text=In%201962%2C%20T,problems%20of%20traditional%20brushed%20motors). Brushless motors have high efficiency, high speed capability, and long life. BLDC often refers to trapezoidal-back-EMF motors, while PMSM usually implies sinusoidal back-EMF (and thus amenable to field-oriented control). Key inventors: Wilson & Trickey built a practical brushless DC motor in 1962[\[15\]](https://maintexmotors.com/who-invented-bldc-motor/#:~:text=In%201962%2C%20T,problems%20of%20traditional%20brushed%20motors). Today PM motors are prevalent in EVs, robotics, and appliances thanks to rare-earth magnets and vector drives.

**Induction (Asynchronous) Motors:** Most common for industrial drives. The stator produces a rotating magnetic field at synchronous speed $`\omega_{s} = 2\pi f/p`$. A cage or wound rotor carries induced currents (from slip $`s`$) that interact with the stator field to produce torque. At full load, rotor spins slightly slower than synchronous speed. Induction motors are robust and inexpensive but generally less efficient than PM motors. Large induction motors can reach ~95% efficiency at rated load. Tesla and Ferraris’ AC induction concepts date to 1888[\[2\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=It%20fell%20to%20Edison%E2%80%99s%20former,the%20requisite%20AC%20transformers%20and), but commercial cage-rotor motors evolved into the 20th century. Induction motors require an AC drive (or fixed-frequency supply); modern VFDs allow precise control.

**Synchronous Reluctance Motors (SynRM):** A magnet-free synchronous motor whose rotor is laminated steel shaped with salient (anisotropic) poles. Torque is produced by the tendency of the rotor to align its least-reluctance axis with the stator field. SynRMs combine PM-motor efficiency with induction-motor simplicity. Recent advances enable ultra-efficient IE5+ motors without magnets[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency). ABB claims its IE5 SynRM has ~40% lower losses than an IE3 motor[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency). No rotor currents or magnets means maintenance similar to an induction motor, but requiring a sophisticated inverter for starting and synchronization.

**Switched Reluctance Motors (SRM):** Stator with salient poles and simple windings; rotor is just plain iron (no windings or magnets). Stator poles are energized in sequence; the rotor moves to minimize reluctance. Very rugged and cheap, but exhibit high torque ripple and acoustic noise unless carefully controlled. SRMs were researched in the 1970s–90s and find niche use (e.g. in automotive applications) due to their simplicity and magnet-free design.

**Stepper Motors:** Essentially a multi-phase brushless synchronous motor designed to move in discrete steps. Common types are permanent-magnet steppers and variable-reluctance steppers. They provide open-loop position control without feedback (each pulse moves the rotor one step). Widely used in printers, CNC, and robotics for precise position control. Modern “hybrid” steppers offer high torque, often driven with microstepping currents.

**Linear Motors:** Flat counterparts of rotary motors. For example, a linear synchronous motor has a slider (plunger) moving along a track with a travelling magnetic field. Voice-coil (Lorentz-type) motors and linear induction motors are special cases. Used in maglev trains, actuators, conveyors. These follow the same electromagnetic principles but produce linear force instead of torque.

**Homopolar Motors:** Simplest form: a conductor in a uniform magnetic field with DC current produces continuous torque (Faraday’s disk). Extremely low voltage, high current. Niche uses (e.g. motor-generators for high current applications). Faraday’s original 1821 experiment was essentially a homopolar motor[\[1\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/#:~:text=Self,current%20produces%20a%20magnetic%20field).

**Axial-Flux Motors:** The flux path is along the axis of rotation, yielding a pancake shape (flat rotor/stator discs). This geometry allows a large diameter and more magnetic length, giving very high torque density. Torque density can be *up to four times* that of similar-sized radial-flux motors[\[16\]](https://www.stanfordmagnets.com/advantages-and-disadvantages-of-axial-flux-motors.html#:~:text=Due%20to%20their%20geometry%2C%20axial,electric%20vehicles%20and%20aerospace%20applications). Axial-flux motors are used where space or weight savings are critical (e.g. EV wheel motors, aerospace). However, they can be harder to cool and more complex to manufacture.

\<div style="text-align:center"\>**Figure:** Typical torque and current vs. slip (speed) curves for a three-phase induction motor (with rated load at zero slip). The torque peaks at breakdown then falls to zero at synchronous speed[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as)[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point). \</div\> <img src="/win/linux/Code/Text/marginalia/tmp/ai-research-reports/data/md/electric-motor-design-principles-types-and-practices/assets/media/rId39.png" style="width:5.83333in;height:3.8in" />  
*Fig. 1. Induction motor torque-speed/current curves. Starting torque and current are high, followed by a pull-up and breakdown peak, then torque goes to zero at synchronous speed. (Data adapted from typical motor curves[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point)[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as).)*

## Torque, Speed, and Power Relationships

All motors obey \$P\_{\rm out} = T \omega\$, where $`T`$ is torque and $`\omega`$ is angular speed. In practical units, for power $`P`$ in kilowatts and speed $`n`$ in rpm, torque $`T`$ in Nm is

\$\$ T = \frac{9550\\P\_{\rm kW}}{n\_{\rm rpm}} \quad. \$\$

(E.g. a 7.5 kW motor at 1500 rpm yields $`T = 9550 \times 7.5/1500 \approx 47.8`$ Nm[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as).) At no load, torque is zero and speed is maximum (synchronous for AC motors). As load torque increases, speed drops (in induction motors) or the drive increases current (in synchronous/PMSM) to maintain speed. DC motor speed is roughly proportional to applied voltage (for fixed field); AC synchronous speed is fixed by supply frequency. Fig. 1 shows a typical induction-motor torque-speed curve: high starting torque and current, a dip (pull-up torque), then a peak (breakdown torque), and zero torque at no slip (synchronous speed)[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as). The torque–current relation is roughly linear for small loads: $`T = k_{t}I`$ (where $`k_{t}`$ \[Nm/A\] is the motor’s torque constant[\[17\]](https://solution.mabuchi-motor.com/en/blog/motor-performance-curves#:~:text=The%20slope%20of%20the%20T,expressed%20by%20the%20following%20equation)).

## Efficiency and Losses

Motor efficiency \$\eta=P\_{\rm out}/P\_{\rm in}\$ reflects unavoidable losses. The main loss categories are: **Copper (I²R) losses** in stator and rotor windings, **iron (core) losses** in laminations (hysteresis and eddy currents), **mechanical losses** (bearing friction, windage), and **stray losses** (harmonics, leakage, contact resistance)[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point). For example, a typical induction motor may see ~30–40% of its losses as stator copper, ~15–25% rotor copper, ~15–25% iron, ~5–15% friction/windage, and ~5–15% stray[\[18\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Category%20Percentage%20of%20Total%20Losses,harmonic%20effects%2C%20slot%20permeance%20variations). Copper losses scale with load² (since $`I`$ increases), whereas iron losses scale with frequency and flux (constant with load). Mechanical losses rise roughly as speed³[\[19\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Friction%20and%20Windage). Premium-efficiency designs reduce losses via more copper, thinner laminations, better steel, and tight air gaps. Large IEC “IE3” or NEMA Premium motors often exceed 94–96% efficiency under full load[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1)[\[6\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=IEC%20efficiency%20standards%20Standard%20IEC%2FEN,apply%20to%20synchronous%20and%20permanent). (Government and efficiency standards classify motors from IE1 up to IE4/IE5[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1)[\[6\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=IEC%20efficiency%20standards%20Standard%20IEC%2FEN,apply%20to%20synchronous%20and%20permanent), with IE4/5 being super-premium.) Table 1 (below) compares types: note BLDC/PMSMs generally have highest efficiency and torque density, while induction motors are cheapest and simplest.

Motor heat comes from these losses and must be managed. Continuous-duty ratings assume a temperature-rise limit (e.g. IEC class B or F insulation). Thermal design (air/water cooling) ensures winding and bearing temperatures stay safe under load; often using thermal equivalent circuits or FEA to predict temperature. Overheating can degrade insulation and magnets, so thermal margin is crucial.

## Materials

- **Conductors:** Copper is used for windings; it has high conductivity (low losses). Aluminum is cheaper/lighter but requires larger cross-section. Litz wire is used in some high-frequency motors. Insulation (varnish, epoxy, slot liners) prevents shorting; classes (A, B, F, H) specify max temperature.
- **Magnetic Steel:** Laminated silicon steel (thickness 0.35–0.5 mm) forms stator/rotor cores. Thin laminations reduce eddy losses. For high-speed or high-frequency, special steels (Hi-B, amorphous) or powder metals reduce losses.
- **Magnets:** Rare-earth NdFeB magnets offer highest flux for PM motors. SmCo is stable at high temperature. Ferrite magnets are cheaper but weaker (used in low-cost BLDCs). Magnet choice affects performance, cost, and demagnetization risk (requires guarding flux density).
- **Structural Materials:** Shafts are typically steel (e.g. 1045 steel). Housing can be cast iron or aluminum. Bearings (often deep-groove ball bearings) support the rotor; selection affects life and noise. Shafts and housings may need keyways, shrink fits, balancing.

## Windings and Topologies

Stators have either distributed (multiple coils per phase spread across slots) or concentrated (single coil per pole per phase) windings. Concentrated (e.g. one coil per pole per phase) reduces end-winding length and often suits fractional-horsepower motors. Distributed windings yield more sinusoidal magnetomotive force and lower cogging. Slot/pole combinations (e.g. 36-slot/4-pole) affect harmonics and torque ripple. Common winding types include lap and wave for DC armatures, and various concentrated or distributed patterns for AC.

## Electromagnetic Design Methods

Initial sizing often uses analytical formulas: Maxwell’s stress, flux density limits, and empirical “specific magnetic loading” and “specific electric loading” (forces per area). Classic design methods (magnetic circuit models) date to Chapman/Krause textbooks. However, complex slot geometries and saturation require Finite Element Analysis (FEA). Software like ANSYS Maxwell, JMAG, or FEMM allow 2D/3D magnetic simulation, capturing leakage and end-effects. Designers often iterate: use analytical design for a first estimate (stack length, turns, air-gap) then refine with FEA. For detailed thermal analysis, software like Motor-CAD couples electromagnetic losses with thermal circuits.

## Mechanical Design

Bearings (ball or roller) must handle radial/axial loads; sealed or grease-packed options vary life. Shaft diameter is set by torque and rotational speed (to avoid torsional deflection and critical speeds). Housings often add mounting flanges and vent openings for cooling. Mechanical balance (balancing rotor to ~2G or better) minimizes vibration. The air-gap uniformity between stator and rotor is critical; manufacturing tolerances (e.g. 0.1 mm) ensure even gap and reduce noise.

## Manufacturing Processes

Typical motor manufacturing includes: - **Laminate stamping:** Stator and rotor core lamination sets are punched from sheet steel. Tolerance and stacking affect performance. - **Core assembly:** Laminations are stacked (often with epoxy or welded edges) to form the stator/rotor. - **Rotor fabrication:** For squirrel-cage motors, rotor bars are inserted and end-rings brazed or die-cast. For permanent-magnet rotors, magnets are glued or mechanically retained in slots; sometimes inserted after assembly. SynRM rotors have salient steel poles. - **Winding:** Automatic coil winding machines thread enamelled wire around stator teeth. Coils are wound, insulated, and fitted into slots. End-turns are bound or resin-coated to resist movement/vibration. - **Insulation and impregnation:** Windings may be varnished or vacuum-pressure impregnated for durability and heat conduction. - **Assembly:** Rotor is press-fit onto the shaft, bearings and fan mounted, end-shields bolted to housing. Ventilation ducts or fans are added if needed. - **Balancing:** The assembled rotor is balanced (often in situ) to minimize vibration. - **Testing:** Each motor is tested for winding insulation resistance, no-load current, locked-rotor torque, and efficiency as per IEC/NEMA standards.

## Prototyping and Testing

Early prototypes may use 3D-printed parts (plastic cores or housings) to verify assembly. FEA models are validated by building a proof-of-concept motor. Testing includes dynamometer runs to measure torque, speed, efficiency, and thermal behavior. Instrumentation: torque transducers, tachometers, current/voltage sensors, thermal probes or cameras. Standard test setups (IEEE Std 112) segregate losses. Endurance tests check bearing heat and insulation class.

## Control Electronics and Drives

Most custom motors need a power electronic drive: - **Brushed DC drives:** simple PWM or linear control to vary voltage; feedback from tachometer or current.  
- **AC drives (VFDs):** Inverters (IGBT/MOSFET bridge) supply 3-phase motor with controlled voltage/frequency (V/Hz control) or vector control. Field-Oriented Control (FOC) rotates the current vector in the rotor reference frame, decoupling torque and flux control. For PMSM/BLDC, FOC or trapezoidal commutation is used. Sensorless methods infer rotor position from back-EMF or high-frequency injection.  
- **Switched reluctance drives:** Specialized controllers sequentially energize phases to shape current so as to reduce torque ripple. They often require customized power stages. - Modern drives include regenerative capability (feed energy back to the source). Drives also implement protection (overcurrent, overvoltage, thermal) and sometimes integrated sensors (current shunts, DC-bus voltage monitors).

GaN and SiC transistors are increasingly used in drives. Compared to silicon, GaN/SiC allow higher switching frequencies (50–100 kHz or more) and lower losses[\[7\]](https://www.ti.com/lit/pdf/slyt801#:~:text=instance%2C%20GaN%20offers%20a%20gate,%E2%84%A6)[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN). For example, GaN-based inverter stages can exceed 98% conversion efficiency (vs ~92% with silicon)[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN). This reduces inverter size and improves motor response, but requires attention to gate drive and EMI due to fast edges.

## Sensors

**Position sensors:** Encoders (optical or magnetic) and resolvers provide accurate rotor angle/speed feedback for vector control. Hall-effect sensors (on small BLDC motors) give coarse rotor position for commutation[\[15\]](https://maintexmotors.com/who-invented-bldc-motor/#:~:text=In%201962%2C%20T,problems%20of%20traditional%20brushed%20motors). Resolvers (rugged analog position sensors) are common in industrial drives. Low-cost BLDC motors often use 3 Hall sensors spaced 120°.  
**Current and voltage sensing:** For FOC, stator current is measured (shunts or Hall ICs) to regulate torque. DC-bus voltage monitors help control power flow.  
**Temperature sensors:** Thermistors or RTDs embedded in windings/bearings enable thermal protection/control. **Accelerometers:** For harsh-vibration environments, may trigger shutdown.

## Cooling Methods

Motors must shed heat to maintain ratings. Cooling schemes include: - **Air cooling:** Internal or external fans blow air over the frame (common TEFC or ODP motors). Fins on housing increase surface area.  
- **Liquid cooling:** Channels within stator housing circulate coolant (water/glycol). Used for high power-density motors (EVs, industrial).  
- **Oil-immersion:** Entire motor submerged in transformer oil or special coolant, transferring heat to an external radiator.  
Proper cooling extends life and allows higher continuous torque. Thermal analysis should ensure hotspot temperature (often at coil end-winding or winding root) stays within insulation limits.

## Noise and Vibration

Torque ripple and magnetic forces can cause vibration (acoustic noise). Skewing rotor/stator or using fractional-slot windings can reduce cogging torque and harmonics. Mechanical resonances are damped by stiff construction. EMI filters may also quiet electrical noise. Noise can be an issue at low torque speeds (audible hum) and in high-rpm drives.

## Reliability, Standards, and Safety

Industrial motors must meet standards (IEC 60034 series worldwide, NEMA MG1 in North America). For example, IEC 60034-1 defines thermal classes, duty types, and vibration limits, while IEC 60034-30-1 defines efficiency classes IE1–IE4[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1). NEMA MG1 ensures interchangeability and durability (NEMA B, C, D, etc. design codes define torque profiles). NEMA often uses a service factor (SF) of 1.15–1.25 for overload capability[\[20\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=Selecting%20IEC%20devices%20requires%20a,on%20space%20and%20cost%20savings). Safety standards (IEC/UL) require enclosures to protect users, and ground-fault protection for insulation. In hazardous areas, explosion-proof motors (IECEx, UL) use special enclosures.

Motors must also comply with environmental regulations (RoHS restricts certain materials; REACH concerns). Sustainable design includes using recyclable materials and high efficiency to reduce lifetime energy use (motors consume ~50% of industrial electricity[\[21\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=So%20why%20is%20efficiency%20such,to%20lowering%20greenhouse%20gasses%20and)).

## Materials Sourcing and Cost

Key cost drivers: copper (windings), steel (laminations), magnets (rare earths), and power electronics. Magnet supply volatility (neodymium) can affect PM motor cost. Induction motors avoid magnet cost but need more copper/steel. In practice, motor cost is a small fraction of lifecycle energy cost (premium efficiency pays off). Global suppliers (e.g. Nidec, Siemens) provide raw materials and components, while modular design (IEC frame sizes) allow off-the-shelf parts. Custom prototypes may source specialized laminations or windings from smaller vendors. For budgeting, motors are often priced by power: roughly \\X per kW depending on efficiency class and complexity.

## Future Trends

- **Advanced Materials:** New steels and magnets (e.g. Gen2 NdFeB, high-flux composites) push performance. Research into magnet-free designs (SynRM, SRM) and hybrid concepts continues.
- **Additive Manufacturing:** 3D printing of copper windings or complex cooling jackets may enable new designs (e.g. conformal cooling, interior permanent magnets).
- **Wide-Bandgap Drives:** As noted, GaN and SiC inverters shrink drive size and loss; e.g. SiC MOSFETs cut inverter losses by ~25%[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN).
- **Integrated Motors:** Integration of motor+drive into a single unit (e.g. in-wheel EV motors, “intelligent” servo motors with built-in controllers) is growing. This reduces wiring and improves packaging.
- **IoT and Smart Motors:** Embedded sensors and communications (EtherCAT, etc.) for predictive maintenance.
- **Efficiency Legislation:** Standards continue to tighten; IE5/6 motors (including SynRM and IPM motors) are being developed for ultra-low energy use[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency).
- **Noise and Vibration Mitigation:** Better modeling (FEA) and design for NVH.
- **Automotive Drive:** Electric vehicles drive innovation in high-speed PM motors, high-power SiC inverters, and new architectures (axial flux, integrated transmissions).

## Design Workflow

A typical design process flows through stages:

    flowchart TD
        A[Specifications: Torque, Speed, Voltage, Constraints] --> B[Preliminary Design]
        B --> C[Electromagnetic Design (analytical/FEA)]
        C --> D[Mechanical Design (shaft, bearings, housing)]
        D --> E[Cooling & Thermal Analysis]
        E --> F[Electrical Design (windings, insulation)]
        F --> G[Prototype Manufacturing]
        G --> H[Testing & Validation]
        H -->|Iterate if needed| C
        H --> I[Final Design & Documentation]
        I --> J[Production/Manufacturing]

Fig. 2: Design workflow for a custom motor. Starting from requirements (power, speed, voltage, ambient) we size the magnetic circuit (air-gap, poles, slots), then design the rotor/stator geometry (analytically and via FEA). Next mechanical and cooling details are fleshed out. A prototype is built for testing (torque-speed curve, thermal behavior) and iterated. Finally documentation and BOM are prepared for manufacture.

## Example: Sizing a Motor

*Problem:* Design a 5 kW motor for 1500 rpm (50 Hz, 4-pole) on 400 V line, continuous duty, ambient 40°C.

*Assumptions:* Aim for IE3 efficiency (≈93%). Laminations 0.35 mm steel, NdFeB PM rotor, water-cooled.

1.  **Torque requirement:** $`T = 9550 \times 5/1500 \approx 31.8`$ Nm.
2.  **Air-gap flux:** Choose Bδ ≈0.5 T in air-gap for saturation margin. Reluctance and mmf from magnet strength.
3.  **Stator size:** Empirical approach: for 4-pole, 50 Hz, per-phase flux per pole Φ ≈ 0.03 Wb; therefore stator cross-section ≈Φ/(B×l_eff).
4.  **Windings:** Assuming 3-phase Y, choose turns per phase using V=4.44fNΦ for one winding.
5.  **Preliminary losses:** Calculate I²R for chosen copper area and frequency, estimate core loss from steel grade.
6.  **Cooling:** Water channels sized for ~10 K rise at full load (requires ~50 W/K heat transfer).
7.  **Iteration:** Run 2D FEA to refine slot shape and end-windings, check flux saturation.
8.  **Check:** Ensure maximum temperature \<130°C (class F insulation).
9.  **BOM:** Lamination stack, copper (estimated by slot fill factor), magnets (mass from volume and ρ_NdFeB), bearings, shaft, housing.
10. **Example Equations:**
    - **Torque:** $`T = \frac{3}{2}p\lambda_{M}i_{q}`$ in PMSM[\[13\]](https://ntrs.nasa.gov/api/citations/20210025115/downloads/PMSM_v6.pdf#:~:text=%F0%9D%91%87%F0%9D%91%92%20%3D%203%202%20%F0%9D%91%9B%F0%9D%91%9D%F0%9D%9C%86%F0%9D%91%80%F0%9D%91%96%F0%9D%91%9E,%F0%9D%91%91%F0%9D%9C%94%F0%9D%91%9F%20%F0%9D%91%91%F0%9D%91%A1%20%3D%20%F0%9D%91%9B%F0%9D%91%9D%20%F0%9D%90%BD).
    - **Air-gap torque (est.):** $`T \approx (3/2)p\left( \Phi I/A_{g} \right)`$ (where $`A_{g}`$ is air-gap area).
    - **Output power:** $`P = 2\pi NT/60`$.
    - **Efficiency:** \$\eta=(P\_{\rm out})/(P\_{\rm in})\$; ensure $`\sum\text{losses}`$ gives ~7% of output to meet IE3.

*Worked Calculation:* For 5 kW and 1500 rpm, 32 Nm is needed. If we choose $`k_{t} = 0.1`$ Nm/A, then $`I_{rated} \approx 320`$ A (per phase). Copper loss per phase $`I^{2}R`$ must be sized (e.g. $`R_{ph} = 0.01\Omega`$ gives 320²×0.01=1024 W per phase, times 3→3 kW, too high; so more copper or parallel turns needed).

This demonstrates key steps. In practice a detailed FEA and loss calculation (including mechanical and stray) confirms values. Standards like IEEE 112 Method B can guide loss measurement[\[22\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=,efficiency%20classes%20for%20induction%20motors).

## Bill of Materials (Example Template)

- **Core:** Stator laminations (qty, stack length), rotor laminations.
- **Windings:** Copper wire (specify gauge, insulation class, length per coil), impregnating varnish.
- **Magnets:** NdFeB blocks/disks (dimensions, grade).
- **Shaft:** Steel rod (dimensions).
- **Bearings:** (size, type).
- **Housing:** Cast or machined housing.
- **Bearings:** (type, lubrication).
- **Fasteners:** Screws, end-cover.
- **Cooling:** (fans, water jackets).
- **Sensors:** (Hall/encoder, thermistors).
- **Connectors:** (terminal block, cables).
- **Drive electronics:** (inverter specs).
- **Tools/fixtures:** (winding machine time, test jig).

Cost estimation uses material quantities × unit costs (e.g. copper at \\X/kg, steel at \\Y/kg, magnets at \\Z/kg, plus labor/overhead). For a 5 kW prototype, raw materials might total a few hundred dollars; labor dominates for custom builds.

## Motor Type Comparison

| **Type** | **Efficiency** | **Cost** | **Complexity** | **Torque Density** | **Speed Range** | **Control Difficulty** | **Typical Uses** |
|----|:--:|:--:|:--:|:--:|:--:|:--:|----|
| **Brushed DC** | Moderate (80–90%) | Low | Low (mech comm.) | Low–Moderate | Low–Moderate | Simple (voltage control) | Basic actuators, toys |
| **BLDC/PMSM** | High (90–97%) | Moderate–High | Moderate (electronic) | High | Very high | FOC or Hall-based | EVs, drones, servo drives |
| **AC Induction** | High (90–96%) | Low–Moderate | Moderate | Moderate | High (with VFD) | Moderate (V/Hz or FOC) | Pumps, fans, conveyors |
| **Syn. Reluctance (SynRM)** | Very High (IE5–IE6) | Moderate | Moderate | High | High | High (vector drive needed) | Ultra-efficient industrial drives |
| **Switched Reluctance (SRM)** | Moderate–High | Low | Low (stator only) | Moderate | Wide (needs control) | High (nonlinear control) | High-speed tools, EVs (in development) |
| **Stepper (PM)** | Moderate (85–90%) | Low–Mod | Low (digital drive) | Low–Moderate | Low–Medium | Low (step pulses) | Printers, CNC, robotics |
| **Linear (LSM, VCM)** | High (90–95%) | High | High | High (per area) | N/A (linear) | Varies (servo drives) | Maglev, actuators |
| **Homopolar** | Low (60–80%) | Low | Very Low | Low | Low rpm/high torque | Moderate (commutator) | Niche (railgun, pulse power) |
| **Axial-Flux PM** | Very High (95%+) | High | High | Very High | Low–Moderate | Moderate (like PMSM) | EV hub motors, aerospace |

*(Values are indicative: actual performance depends on design and operating point.)*

## References

Key design resources include Chapman’s *Electric Machinery Fundamentals*, Krause’s *Analysis of Electric Machinery*, and industry notes (e.g. ABB, Siemens app guides). For example, IEC 60034-30-1 defines efficiency classes IE1–IE4[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1); ABB notes motors consume ~53% of global electricity[\[21\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=So%20why%20is%20efficiency%20such,to%20lowering%20greenhouse%20gasses%20and). Industry case studies and technical notes (e.g. ABB on SynRM[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency)) and IEEE standards (e.g. IEEE Std 112 method B for loss measurement[\[22\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=,efficiency%20classes%20for%20induction%20motors)) provide detailed guidelines. The above discussion synthesizes these sources to give a comprehensive motor-design overview.

**Sources:** Textbooks (Chapman, Krause, Boldea), IEEE/IEC/NEMA standards, manufacturer technical notes (ABB, Siemens, etc.), and peer-reviewed studies. Notable references: ABB IEC efficiency note[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1); IEEE Spectrum on motor history[\[2\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=It%20fell%20to%20Edison%E2%80%99s%20former,the%20requisite%20AC%20transformers%20and); industrial motor loss analysis[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point); BLDC invention history[\[15\]](https://maintexmotors.com/who-invented-bldc-motor/#:~:text=In%201962%2C%20T,problems%20of%20traditional%20brushed%20motors); StanfordMagnets on axial flux[\[16\]](https://www.stanfordmagnets.com/advantages-and-disadvantages-of-axial-flux-motors.html#:~:text=Due%20to%20their%20geometry%2C%20axial,electric%20vehicles%20and%20aerospace%20applications); ABB SynRM whitepaper[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency); TI and Newark papers on SiC/GaN[\[7\]](https://www.ti.com/lit/pdf/slyt801#:~:text=instance%2C%20GaN%20offers%20a%20gate,%E2%84%A6)[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN).

------------------------------------------------------------------------

[\[1\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/#:~:text=Self,current%20produces%20a%20magnetic%20field) Faraday Motor – 1821 - Magnet Academy

<https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/faraday-motor-1821/>

[\[2\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=It%20fell%20to%20Edison%E2%80%99s%20former,the%20requisite%20AC%20transformers%20and) [\[12\]](https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor#:~:text=George%20Westinghouse%20acquired%20Tesla%E2%80%99s%20AC,phase%20induction%20motor%20in%201889) May 1888: Tesla Files His Patents for the Electric Motor - IEEE Spectrum

<https://spectrum.ieee.org/may-1888-tesla-files-his-patents-for-electric-motor>

[\[3\]](https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html#:~:text=In%20metric%20units%20the%20rated,torque%20can%20be%20expressed%20as) Electrical Induction Motors - Torque vs. Speed

<https://www.engineeringtoolbox.com/electrical-motors-torques-d_651.html>

[\[4\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Three,speed%20rating%2C%20and%20operating%20point) [\[18\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Category%20Percentage%20of%20Total%20Losses,harmonic%20effects%2C%20slot%20permeance%20variations) [\[19\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=Friction%20and%20Windage) [\[22\]](https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd#:~:text=,efficiency%20classes%20for%20induction%20motors) Motor Loss Breakdown: Stator, Rotor, Core, Friction & Stray Losses – Industrial Monitor Direct

<https://industrialmonitordirect.com/blogs/knowledgebase/three-phase-induction-motor-loss-distribution-and-analysis?srsltid=AfmBOopvtIApj3kuoUKHAHmqMJKL6IJ1r3FLde19RhXSpYFLrkYFNLMd>

[\[5\]](https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf#:~:text=The%20standard%20defines%20four%20IE,efficiency%20IE2%20Standard%20efficiency%20IE1) library.e.abb.com

<https://library.e.abb.com/public/db64d153e3c346938e18916e66fb1d0d/9AKK107319%20EN%2005-2018_20848_ABB_Technical_note_IEC_60034_30_1.pdf>

[\[6\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=IEC%20efficiency%20standards%20Standard%20IEC%2FEN,apply%20to%20synchronous%20and%20permanent) [\[20\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=Selecting%20IEC%20devices%20requires%20a,on%20space%20and%20cost%20savings) [\[21\]](https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies#:~:text=So%20why%20is%20efficiency%20such,to%20lowering%20greenhouse%20gasses%20and) NEMA vs. IEC Efficiencies \| News center \| ABB

<https://new.abb.com/news/detail/70167/nema-vs-iec-efficiencies>

[\[7\]](https://www.ti.com/lit/pdf/slyt801#:~:text=instance%2C%20GaN%20offers%20a%20gate,%E2%84%A6) Wide-bandgap semiconductors: Performance and benefits of GaN versus SiC

<https://www.ti.com/lit/pdf/slyt801>

[\[8\]](https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology#:~:text=Benefits%20of%20high%20GaN%20efficiency,lower%20electricity%20usage%20with%20GaN) Enhancing Industrial Energy Efficiency with SiC and GaN Technology \| Newark Electronics

<https://www.newark.com/technical-resources/articles/enhancing-industrial-energy-efficiency-with-sic-and-gan-technology>

[\[9\]](https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors#:~:text=Energy%20efficiency) ABB Synchronous reluctance motors \| ABB

<https://www.abb.com/global/en/areas/motion/motors-generators/low-voltage-motors/iec-low-voltage-motors/synchronous-reluctance-motors>

[\[10\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/davenport-motor-1834/#:~:text=battery%20provided%20the%20electricity,the%20machines%20in%20his%20workshop) [\[11\]](https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/davenport-motor-1834/#:~:text=decided%20to%20try%20again%20after,after%20patent) Davenport Motor – 1834 - Magnet Academy

<https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/museum/davenport-motor-1834/>

[\[13\]](https://ntrs.nasa.gov/api/citations/20210025115/downloads/PMSM_v6.pdf#:~:text=%F0%9D%91%87%F0%9D%91%92%20%3D%203%202%20%F0%9D%91%9B%F0%9D%91%9D%F0%9D%9C%86%F0%9D%91%80%F0%9D%91%96%F0%9D%91%9E,%F0%9D%91%91%F0%9D%9C%94%F0%9D%91%9F%20%F0%9D%91%91%F0%9D%91%A1%20%3D%20%F0%9D%91%9B%F0%9D%91%9D%20%F0%9D%90%BD) ntrs.nasa.gov

<https://ntrs.nasa.gov/api/citations/20210025115/downloads/PMSM_v6.pdf>

[\[14\]](https://en.wikipedia.org/wiki/Brushed_DC_electric_motor#:~:text=Brushed%20motors%20were%20the%20first,using%20%2082%20power%20electronic) Brushed DC electric motor - Wikipedia

<https://en.wikipedia.org/wiki/Brushed_DC_electric_motor>

[\[15\]](https://maintexmotors.com/who-invented-bldc-motor/#:~:text=In%201962%2C%20T,problems%20of%20traditional%20brushed%20motors) Who Invented the BLDC Motor? - Maintex \| Motor Manufacturer

<https://maintexmotors.com/who-invented-bldc-motor/>

[\[16\]](https://www.stanfordmagnets.com/advantages-and-disadvantages-of-axial-flux-motors.html#:~:text=Due%20to%20their%20geometry%2C%20axial,electric%20vehicles%20and%20aerospace%20applications) Advantages and Disadvantages of Axial Flux Motors

<https://www.stanfordmagnets.com/advantages-and-disadvantages-of-axial-flux-motors.html>

[\[17\]](https://solution.mabuchi-motor.com/en/blog/motor-performance-curves#:~:text=The%20slope%20of%20the%20T,expressed%20by%20the%20following%20equation) Explanation of How to Read Motor Performance Curves and T-N Curves

<https://solution.mabuchi-motor.com/en/blog/motor-performance-curves>
