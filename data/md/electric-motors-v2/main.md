# Executive Summary

Electric motors have evolved from 19th-century experiments to today’s high-performance drives. Pioneers like Volta, Faraday, Tesla and Dolivo-Dobrovolsky laid the foundation[\[1\]](https://www.eti.kit.edu/english/1376.php#:~:text=The%20first%20rotating%20device%20driven,Barlow%27s%20Wheel)[\[2\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1871%E2%80%931873%2C%C2%A0Z%C3%A9nobe%20Th%C3%A9ophile%20Gramme%20%20,laminated%20magnetic%20cores%20of%20insulated). Motors operate on basic electromagnetic laws (Lorentz force and Faraday’s law), yielding torque \$τ=K_t I\$ and back‐EMF \$E=K_e \omega\$[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque)[\[4\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=V%20%3D%20Rw%20I%20%2B,It%20is%20a%20proportionality%20constant). Today’s motors span brushed DC, BLDC/PMSM, induction, synchronous, stepper, switched/synchronous-reluctance, and axial-flux designs. Each has trade-offs in torque/power density, efficiency, cost, and control. For example, PM motors (BLDC/PMSM) achieve very high torque and efficiency (~95–98%), but require expensive magnets[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[6\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20offer%20much,as%20electric%20vehicles%20and%20robotics); induction motors are cheaper and robust but slightly lower-efficiency (~90–93%)[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[7\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20deliver%20higher,efficiency%20and%20energy%20efficiency%20goals). Design involves material choices (copper vs. aluminum windings, silicon steel laminations[\[8\]](https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2#:~:text=What%20is%20Electrical%20Steel%3F%20%E2%80%A2,silicon%20%E2%80%A2%20Very%20efficient%20at), NdFeB/SmCo/ferrite magnets), cooling, bearings, and precise tolerances. Manufacturing techniques include lamination stamping, winding (hairpin or distributed), rotor assembly (gluing or mechanical retention of magnets), and balancing. Modern drives use PWM inverters, vector (FOC) control, and sensors (encoders/Hall) or sensorless methods[\[9\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=Figure%205%3A%20In%20a%20BLDC,sensors%20to%20determine%20rotor%20position)[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque). Testing covers torque-speed curves, efficiency maps, and thermal/vibration analysis under standards (IEC/NEMA). Optimization often employs finite-element (Maxwell) simulation for electromagnetic and thermal design. Future trends feature axial-flux machines (even higher torque density[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density)), wide-bandgap (SiC/GaN) drives, magnet-free designs (syn-reluctance), and demands from EV/robotics. In practice, one follows a step-by-step design checklist (specs → topology → electromagnetic and thermal design → control system → prototyping/testing). Two example projects are included: a high-speed BLDC drone motor and a medium-power axial-flux hub motor, with BOM, rough sizing, and expected performance.

    timeline
        title Electric Motor Invention Timeline
        section 1800s
          1800 : Alessandro Volta invents the voltaic pile (first battery)[1]
          1820 : H.C. Ørsted discovers electric current creates magnetic field[1]
          1821 : Michael Faraday demonstrates first electromagnetic rotation (early motor)[1]
          1822 : Peter Barlow invents “Barlow’s Wheel” (first continuous rotation)[1]
          1825 : W. Sturgeon invents the electromagnet (crucial for motors)[1]
          1828 : Ányos Jedlik builds a commutator-type rotary machine (proto-motor)[1][11]
          1834 : Moritz Jacobi builds practical DC motor (powered a boat)[1]
          1837 : Thomas Davenport obtains US patent on electric motor (first commercial use)[1][2]
          1873 : Z.T. Gramme invents the ring-armature DC motor (improves smooth output)[2]
          1879 : Walter Baily’s four-coil induction motor prototype[12]
          1888 : Galileo Ferraris (Italy) publishes rotating magnetic field (AC motor)[13]; Nikola Tesla (USA) independently patents 2φ/3φ AC induction motors[13].  
          1889 : M. Dolivo-Dobrovolsky (Germany) develops 3φ cage/wound-rotor induction motors; first industrial AC drives[14].
          1935 : Eric Laithwaite demonstrates the linear induction motor[15].
          1970s-90s : Rise of power electronics (IGBT, DSP) enables modern FOC/BLDC drives.
        section 1900s–2000s
          2000 : Widespread use of rare-earth magnets (NdFeB) greatly raises motor performance[16].
          2010s: Emergence of axial-flux designs (YASA/Magtec motors) and wide-bandgap inverters.

## Fundamentals of Motor Physics

Electric motors convert electrical energy to torque via electromagnetic forces. The **Lorentz force law** (\$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})\$) implies that a current-carrying conductor in a magnetic field experiences force perpendicular to both current and field[\[17\]](https://www.monolithicpower.com/en/learning/mpscholar/electric-motors/introduction-to-motors/basic-principles-of-motor-operation?srsltid=AfmBOorqWckN0CDZgAy0wy_k4WKdoYsEWRcTvgumUG9GJ3gLS-eGWsWN#:~:text=Consider%20a%20scenario%20where%20there,this%20fundamental%20principle%20of%20rotation). In practice, for a wire length \$L\$ carrying current \$I\$ in field \$B\$, \$F = I\\L\times B\$ (right-hand rule). Motors exploit this by arranging coils in magnetic fields so forces produce rotation. **Faraday’s law of induction** governs back-EMF: \$\mathcal{E}=-N\\d\Phi/dt\$[\[18\]](https://www.monolithicpower.com/en/learning/mpscholar/electric-motors/introduction-to-motors/basic-principles-of-motor-operation?srsltid=AfmBOorqWckN0CDZgAy0wy_k4WKdoYsEWRcTvgumUG9GJ3gLS-eGWsWN#:~:text=The%20ruling%20equation%20is%3A), meaning that a rotating coil in flux generates a voltage opposing the supply (this back-EMF limits current as speed rises). From these principles one derives the familiar motor equations:

- **Torque** \$τ\$ is proportional to current: \$τ=K_t I\$, where \$K_t\$ (N·m/A) is the torque constant[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque).
- **Back-EMF (Voltage Constant)**: \$V=R_w I + K_e \omega\$, with \$K_e\$ the back-EMF constant[\[4\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=V%20%3D%20Rw%20I%20%2B,It%20is%20a%20proportionality%20constant). Here \$K_t\$ and \$K_e\$ share the same units (N·m/A = V·s/rad), so numerically \$K_e=K_t\$ in SI. In short, “current produces torque, speed produces back-EMF.”

Maxwell’s equations (formulated 1861–64[\[19\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1861%E2%80%931864%2C%C2%A0James%20Clerk%20Maxwell%20%20,pulsating%20DC%20problem%3B%20at%20Vienna)) underpin these laws, tying together fields and currents. Together, these relations mean a motor is reversibly a generator: mechanical power \$τω\$ plus losses equals electrical power \$VI\$.

**Control of torque** in practical motors is done by varying coil currents (via commutation or inverter PWM) while keeping fields orthogonal for maximum torque. In DC machines this was mechanical (brushes); in AC/BLDC it is electronic, either open-loop BEMF-based or closed-loop FOC (vector control) that aligns stator current with rotor field.

## Motor Types and Performance

Electric motors can be categorized broadly (see taxonomy diagram below). Major classes include:

- **Brushed DC (BDC)**: Simple permanent-magnet or wound-field stator with an armature and mechanical brush/commutator. **Pros:** low control complexity, direct torque control, high low-speed torque. **Cons:** lower torque/power density (heavy iron/brush assembly), brush wear (maintenance), limited top speed (brush friction)[\[20\]](https://www.orientalmotor.com/brushless-dc-motors-gear-motors/technology/AC-brushless-brushed-motors.html#:~:text=Service%20and%20Maintenance%3A%20DC%20vs,BLDC). Typical efficiency ~70–85%. Used in low-cost tools, toys, vehicles (starter motors).
- **Brushless DC (BLDC/PMSM)**: 3-phase permanent magnets on the rotor, wound stator. Electronic commutation (six-step or sinusoidal PWM). If trapezoidal BEMF and six-step drive, often called BLDC; with sinusoidal drive and vector control, it’s a permanent-magnet synchronous motor (PMSM). **Pros:** very high torque density and efficiency (~90–98%), compact size (no brushes)[\[21\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=As%20always%2C%20there%20are%20trade,these%20losses%2C%20which%20limits%20performance)[\[9\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=Figure%205%3A%20In%20a%20BLDC,sensors%20to%20determine%20rotor%20position), high speed, low maintenance. **Cons:** needs electronic drive (more cost/complexity), requires rotor sensing or sensorless control. Sensitive to demagnetization/heat (magnet design). Widely used in drones, EVs, servos, appliances.
- **Induction (Asynchronous)**: Stator winding creates rotating field; rotor (squirrel cage or wound) has no magnets but induced currents. **Pros:** rugged, inexpensive (no magnets), inherently self-protecting, low maintenance[\[22\]](https://eshop.se.com/in/blog/post/induction-motor-working-principles-and-types.html?srsltid=AfmBOorNetYzPh6Bc6hS1COwb9e4E0eydf3YAFuTZbQuZbZ0h9C_BE6Y#:~:text=Some%20of%20the%20advantages%20of,induction%20motors%20are%20listed%20below), widely used in fixed-speed/industrial. **Cons:** slightly lower peak efficiency (up to 93%[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[7\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20deliver%20higher,efficiency%20and%20energy%20efficiency%20goals)), moderate torque density, requires VFD for efficient speed control (increases complexity). Slip limits top speed and efficiency. Found in pumps, fans, conveyors, and some EVs (e.g. Tesla’s early motors).
- **AC Synchronous (wound-rotor)**: Like induction but rotor has DC-excited coils (or permanent magnets). Runs exactly at synchronous speed. **Pros:** stable speed, good power factor control, high torque. **Cons:** bulky field winding or slip rings needed, brushes or exciter, maintenance. Used in large generators, synchronous condensers, specialized drives.
- **Stepper (Variable Reluctance or PM)**: Multi-pole poles and phases allow open-loop micro/macro-stepping to precise angles. **Pros:** very precise position control without encoder, simple open-loop drive. **Cons:** low efficiency (coils must hold position constantly[\[23\]](https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8#:~:text=remain%20energized%20at%20all%20times,even%20when%20not%20in%20motion)), torque drops with speed[\[24\]](https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8#:~:text=Disadvantages%3A), limited speed, possible resonance/step loss. Used in printers, CNC, cameras.
- **Switched Reluctance (SRM)**: Stator with concentrated coils, plain toothed rotor (no magnets). Phases are energized sequentially to pull rotor poles into alignment. **Pros:** very simple rotor (no magnets/coils), high speed and temperature capability, low cost, inherently rugged/fault-tolerant[\[25\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=To%20form%20the%20phase%20of,and%20hence%20more%20fault%20tolerant)[\[26\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=As%20compared%20to%20induction%20motors%2C,demand%20for%20switched%20reluctance%20motors). **Cons:** complex drive (non-linear, requires current control and position feedback), high torque ripple and acoustic noise[\[27\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=Disadvantages%20of%20the%20switched%20reluctance,current%20and%20bus%20voltage%20speed), requiring sensors or predictive control. Niche uses (e.g. low-cost EV drives, appliances).
- **Synchronous Reluctance (SynRM)**: Rotor has anisotropic iron (no windings, no magnets) arranged to favor reluctance torque. **Pros:** magnet-free, high efficiency (no rotor copper losses)[\[28\]](https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm#:~:text=The%20core%20idea%20of%20a,combination%20of%20simplicity%20and%20efficiency), inherently quiet, no rotor heating[\[29\]](https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm#:~:text=drive,heat%20losses%20from%20the%20motor). **Cons:** sophisticated drive required, torque density typically lower than PM motors, rotor design complex. Gaining use in IE4 (premium-efficiency) motors.

<!-- -->

    graph TD
        A[Electric Motors] --> DC[DC Motors]
        A --> AC[AC Motors]
        DC --> BrushedDC[Brushed DC]
        DC --> BrushlessDC[Brushless DC (BLDC/PMSM)]
        AC --> Induction[Induction (Asynchronous)]
        AC --> Synchronous[Synchronous (Wound Rotor or PWM-Sync)]
        AC --> Stepper[Stepper]
        AC --> SwRel[Switched Reluctance]
        Synchronous --> PMSM[Permanent Magnet Synchronous]
        Synchronous --> SynRel[Synchronous Reluctance]
        Stepper --> [Stepper (2-Phase, 5-Phase, etc)]

### Comparison Table

Key attributes of motor types are summarized below (relative: Low/Med/High, or descriptors).

| **Type** | **Torque Density** | **Power Density** | **Efficiency** | **Cost** | **Complexity (Mech/Elec)** | **Maintenance** | **Control Difficulty** | **Magnets?** | **Typical Uses** | **Manufacturability** |
|----|----|----|----|----|----|----|----|----|----|----|
| *Brushed DC* | Low–Med | Low–Med | Moderate (~60–85%) | Low | Low (simple mech, no drive) | **High** (brush wear) | Low (just source DC) | No | Toys, tools, lead-acid pumps | Easy (no electronics) |
| *BLDC (PM AC)* | **High** | **High** | **High** (up to 95–98%) | Med–High (PMs) | High (electronic commutation) | Low | Med (sensorless possible) | Yes (rare-earth) | Drones, EV traction, HVAC, robotics | Moderate (PM assembly) |
| *Induction AC* | Med | Med–High | Med–High (90–93%) | Low (no magnets) | Med (simple rotor, VFD for speed) | Very Low | Med (requires VFD) | No | Industry (pumps, fans), appliances | Easy (stamp+wire) |
| *Synchronous AC* | Med–High | High | High (\>90%) | High (exciter) | High (exciter/slip rings) | High (brushes) | Med–High (excitation) | Rotor coil (or PM) | Power gen, heavy drives | Hard (precision) |
| *Stepper* | Low–Med | Low–Med | Low (~30–70%) | Low–Med | Low (simple construction) | Low | Med (step control logic) | Some (PM or none) | 3D printers, CNC, camera autofocus | Easy (simple coils) |
| *Switched Reluct.* | **High** | High | High (equal or \>IM) | Very Low | High (complex control) | Very Low | High (cogging, ripple) | No | Appliances (pumps), EV (niche) | Moderate (simple parts) |
| *Syn Reluct.* | Med–High | High | High (\>90%) | Med (no PM cost) | Med (needs vector drive) | Very Low | Med (like induction) | No | Premium industrial, retrofits | Moderate (special rotor) |
| *Axial-Flux (PM)* | **Very High** | Very High | **Very High** (\>96%) | **High** | High (double-sided, cooling) | Low | High (sensor + cooling) | Yes (PM) | EV hub, aerospace, robotics | Difficult (novel design) |

- **Torque/Power Density:** PM and reluctance designs excel (per unit volume)[\[30\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Remember%20when%20we%20mentioned%20a,has%20a%20multiplying%20effect%20on)[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density). Axial-flux PM motors achieve extremely high torque density via large diameter rotors[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density).
- **Efficiency:** PM machines (BLDC/PMSM) lead (~95–98%), followed by SynRM; induction motors peak ~90–93%[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[7\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20deliver%20higher,efficiency%20and%20energy%20efficiency%20goals). Brushed/stepper are lower due to brush losses or continuous coil current[\[23\]](https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8#:~:text=remain%20energized%20at%20all%20times,even%20when%20not%20in%20motion).
- **Cost:** Magnet machines incur magnet cost (NdFeB/SmCo). Cheap ferrite or magnet-free (induction, SRM, SynRM) have lower material cost.
- **Complexity/Maintenance:** BLDC/PM need electronic drives (higher up-front complexity) but minimal mechanical maintenance. Brushed DC and wound rotor require periodic brush/commutator service. SR and SynRM eliminate magnets but demand sophisticated control.
- **Control:** Sensorless BLDC/induction control is possible at expense of some performance; encoders/Hall sensors simplify vector control (with added cost). SRM control (torque ripple mitigation) is challenging.[\[27\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=Disadvantages%20of%20the%20switched%20reluctance,current%20and%20bus%20voltage%20speed)[\[31\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=good%20starting%20torque%20and%20low,and%20complexity%20of%20the%20system)

## Design Considerations

### Materials & Components

- **Conductors:** Copper is preferred for windings due to highest conductivity (carrying more current for a given size). Aluminum (60% conductivity of copper but ~1/3 weight) may be used for cost/weight trade-offs in very large machines[\[8\]](https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2#:~:text=What%20is%20Electrical%20Steel%3F%20%E2%80%A2,silicon%20%E2%80%A2%20Very%20efficient%20at). Windings can be enamelled wire or hairpin/AWV for high-power stators.
- **Laminations:** Use high-grade electrical steel (CRGO) with ~3–6% Si to reduce eddy (core) losses[\[8\]](https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2#:~:text=What%20is%20Electrical%20Steel%3F%20%E2%80%A2,silicon%20%E2%80%A2%20Very%20efficient%20at). Thinner laminations (\<0.5 mm) lower losses at higher frequencies. Amorphous or nanocrystalline alloys or soft-magnetic composites (SMC) are options for special high-speed or 3D-core designs[\[32\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=One%20major%20consideration%20in%20permanent,material%20only%20compounds%20the%20problem).
- **Magnets:** Rare-earth (NdFeB, SmCo) offer strongest flux (enabling compact design) but cost and demag risk increase. High-temp grades or SmCo are chosen for \>150°C or very stable fields. Ferrite magnets (cheaper, lower energy) are used in low-cost motors. Magnet grade, coating (to protect from corrosion/heat) and placement (buried vs surface) affect performance. Supply chain is a concern (rare-earth price volatility[\[32\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=One%20major%20consideration%20in%20permanent,material%20only%20compounds%20the%20problem)).
- **Insulation:** Class B (130°C) or Class F (155°C) is common[\[33\]](https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html#:~:text=A%20105%20221%2060%2070,H%20180%20356%20125); higher classes (H=180°C) enable more compact/warmer operation. Windings are insulated by varnish, mica, or Class-H wire. Insulation class sets max operating temp; exceeding it (e.g. +10°C) roughly halves lifetime[\[34\]](https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html#:~:text=In%20general%20a%20motor%20should,are%20directly%20related%20to%20motor).
- **Bearings:** Choose ball or roller based on load and speed. Preload and lubrication (grease or oil) are critical for life, especially in high-speed or high-vibration applications. Consider bearing type (deep-groove, angular-contact) for radial/axial loads.
- **Mechanical Tolerances:** Tight airgap (\<1 mm) improves flux but risks rub. Rotor balance (ISO G2.5 or better) is needed to avoid vibration at speed. Shaft and housing tolerances affect bearing life and noise.

### Thermal Management

Heat arises from copper losses, core losses, friction. Cooling options: open-air (blowers), enclosed with forced air (motor fan), liquid jackets, or potting. Use thermal simulation or testing to size heat sinks. Allow appropriate IP rating (outdoor use, moisture).

### Winding Design

- **Distributed vs Concentrated:** Distributed windings (coils spanning several slots) yield smoother torque (higher winding factor) and lower cogging, but longer end-turns and more complex manufacturing. Concentrated (single tooth/phase) reduce copper length and size, used in SRM and axial designs.
- **Slot/Pole Combinations:** Co-prime slot-to-pole (e.g. 9 slots, 10 poles) minimize cogging. More poles give lower speed/higher torque per amp-turn. Slot fill (copper packing) should be maximized for given wire.

## Manufacturing & Prototyping

- **Stator & Rotor Cores:** Fabricate via stamping lamination sheets (steel) for stators and rotors. Vacuum pressure bonding or stacking is common. For prototypes or low-volume, CNC-milling of laminated stacks or even 3D-printing plastic cores is possible (with higher losses).
- **Winding Methods:** Hand-winding on winding jig for small motors; machine winding for high volume. Hairpin windings allow high-copper fill and automated assembly (often in EV motors). End-turns may be impregnated/varnished to secure and insulate.
- **Rotor Fabrication:** For PM rotors, insert magnets into milled pockets or glue them onto rotor surface (ensure mechanical retention plates or adhesives). For wound rotors (synchronous), wind coils on rotor and connect slip rings or brushes. For SRM/SynRM, rotor is usually a single-piece steel (machined/laminated).
- **Balancing:** Dynamically balance assembled rotors (with magnets installed) to grade (e.g. G2.5) to prevent vibration. Laser or mechanical methods measure imbalance.
- **Coating:** Stator windings are typically varnished/potted to improve insulation and heat conduction. Anti-corrosion coatings protect magnets and steel.
- **Prototyping Tips:** Use 3D printing for housings, end-caps, prototyping stator molds. CNC mills can cut laminations from steel sheets (low volume). Winding prototypes can use AWG wire or magnet wire. “Coke bottle” motor tests (hand-held stator with rotor attached) can be done for basic validation.

## Power Electronics & Control

- **Inverter Topologies:** Three-phase motors usually use a 6-switch bridge (three half-bridges) powered by DC bus. For multi-phase (stepper, SRM), use H-bridge per phase or custom bridge. MOSFET or IGBT (or SiC/GaN for high-frequency/high-speed).
- **PWM Techniques:** Sinusoidal PWM or Space-Vector PWM (SVPWM) for smooth control. BLDC often uses 6-step (square-wave commutation) for trapezoidal motors. Overcurrent and shoot-through protection is critical.
- **FOC / Vector Control:** Maintain stator current vector in quadrature with rotor field. Involves Clarke/Park transforms and PI controllers. Provides precise torque/speed control and is used for BLDC (sinusoidal) and AC motors.
- **Sensorless Methods:** BEMF zero-crossing detection (6-step) for BLDC when spinning; or full-state observers (flux estimation) for FOC. Provide position estimation without physical sensors, but typically need injection or movement at low speeds.
- **Position Feedback:** Hall sensors (simple, 60° resolution) or encoders (optical/magnetic, high-resolution) feed the controller. Resolvers (sin/cos signals) are robust industrial sensors.
- **Current Sensing:** Shunt resistors or Hall-effect sensors on each phase measure current for torque control and protection. Precise sensing (Kelvin connections) needed for accurate FOC.
- **Protection:** Include overcurrent, overvoltage (TVS diodes), under-voltage lockout, and thermal shutdown. Soft-start and braking circuits (regen resistors or choppers) for safety.

<!-- -->

    flowchart LR
        Battery["Battery / DC Supply"] -->|DC| Inverter["Inverter (3Φ Bridge)"]
        Inverter -->|AC| Motor["Electric Motor"]
        Motor -->|Mechanical Torque| Load["Mechanical Load"]
        Motor -->|Rotor Position (θ)| Encoder["Encoder / Hall Sensor"]
        Encoder --> Controller["Motor Controller (FOC)"]
        Controller -->|PWM Gate Signals| Inverter
        Inverter -.->|Current Feedback| Controller

## Testing & Instrumentation

- **Dynamometer Testing:** Use a torque meter or brake (eddy current, hysteresis, or mechanical) to load the motor. Measure speed, torque, input electrical power to plot torque-speed curves and calculate efficiency across operating points.
- **Efficiency Measurement:** Compare mechanical output (torque×ω) vs electrical input (V·I minus losses). Follow IEC 60034-2 standards for loss components if high precision is needed.
- **Thermal Testing:** Attach thermocouples to windings, magnets, bearings to monitor rise under load. Use winding resistance method or back-EMF to estimate temperature. Define cooling needs.
- **Vibration/Noise:** Accelerometers or microphone measure NVH (noise, vibration harshness). Identify mechanical resonances or unbalance.
- **Electrical Tests:** Insulation resistance (Megger), winding resistance/inductance (LCR meter). Back-EMF waveform (by spinning motor with known speed) checks consistency.
- **Safety/Regulatory:** Ensure compliance with relevant standards: NEMA or IEC frame and mounting standards, IEEE or UL safety (windings, earth-leakage), CE marking for EMC. Enclosures per IP (ingress protection). Motors often follow IEC 60034 series (rotating machines) for ratings and testing.

## Optimization & Reliability

- **FEA Simulation:** Use finite-element tools (e.g. Ansys Maxwell, Comsol, FEMM) to optimize magnetic design (flux density, cogging, torque, losses) and thermal analysis (heat paths). Multi-physics simulation can couple EM and thermal.
- **Thermal Simulation:** Simulate airflow and heat conduction to refine cooling (fins, jackets, fans). Consider resin potting or thermal pad materials.
- **Multi-Objective Optimization:** Explore trade-offs (e.g. minimize torque ripple vs maximize torque) via algorithms or design of experiments (DOE). Pareto fronts often guide PM size vs copper fill.
- **Common Failure Modes:** Bearing wear, insulation breakdown (overheat), demagnetization (excess heat or fault current), mechanical fatigue (wind-up), and commutator/brush failure (for brushed). Mitigations include oversize bearings, thermal cutouts, soft-start limits, and surge suppression.
- **Cost & Supply:** Source from reputable suppliers: standard lamination stacks, magnet vendors, custom windings. For prototypes, off-the-shelf rotor/stator cores or kits can save time. Rare-earth sourcing may require lead time. Factor economies-of-scale: complex custom stators or rotors get expensive in low volume.

## Future Trends

- **Axial-Flux Machines:** “Pancake” motors with axial flux (e.g. YASA, Magnax designs) achieve 2–4× higher torque density over radial designs[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density) and better cooling[\[35\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Cooling%20is%20one%20place%20where,saving%20cooling%20systems). Ideal for space-limited EV hubs, eVTOL, robotics. Challenges: manufacturing complexity and cost[\[36\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Although%20having%20the%20technical%20advantages%2C,manufacture%2C%20especially%20in%20large%20quantities).
- **Wide-Bandgap Drives:** SiC/GaN transistors in inverters allow higher switching speeds (smaller passive components), higher efficiency and power density, especially at high voltage. They enable higher-speed motors and faster FOC loops.
- **Magnet-Free Designs:** Synchronous reluctance and new high-speed switched-reluctance topologies remove rare-earth magnets, responding to supply concerns[\[32\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=One%20major%20consideration%20in%20permanent,material%20only%20compounds%20the%20problem). Improved materials (e.g. SMC, new laminations) enhance these motors.
- **Advanced Materials:** Grain-oriented electrical steels, better insulations (polyimide, new varnishes), and novel composites will reduce losses and increase thermal limits. Rare-earth recycling and new magnet alloys (e.g. low-RE magnets) are active research areas.
- **Application Drivers:** Electric vehicles, drones, and robotics demand ever-higher torque/power density and efficiency. Integration (e.g. integrated gearheads, motor-controllers), functional safety (e.g. diagnostics, fault-tolerant designs) and miniaturization are focal points.

## Step-by-Step Design Checklist

1.  **Specifications:** Define power, speed, torque, voltage, and application constraints (size, environment). Establish duty cycle, continuous vs peak torque.
2.  **Topology Selection:** Choose motor type (from table), decide on winding (star/∆), slot/pole count, axial vs radial design. Consider bearing and shaft size for mechanical loads.
3.  **Preliminary Sizing:** Use empirical formulas (e.g. \$P\approx Tω\$, \$T\approx kI\$, BEMF constant estimates) to estimate dimensions. Select lamination size (inner/outer diameter, stack length) to meet flux density \<1.6T, airgap \>0.3× slot pitch.
4.  **Electromagnetic Design:** Compute number of turns per coil for desired torque constant. Optimize magnet strength and pole arc for flux. Check winding factors and cogging.
5.  **Thermal Design:** Estimate losses (copper, core, friction). Choose cooling method. Pick insulation class and wire gauge to handle temperature rise.
6.  **Mechanical Design:** Finalize rotor dynamics (inertia), balance, and structural support. Design housings and end-caps. Verify bearing specs for load/speed.
7.  **Drive Design:** Select inverter switching devices (current and voltage ratings), microcontroller/DSP for FOC. Plan sensors (Hall vs encoder) and protection circuits.
8.  **Prototype Manufacture:** Order/custom-make laminations; procure wire and magnets. Wind stator, assemble rotor, insert magnets, glue or mechanically secure. Balance the rotor. Assemble motor and integrate with driver.
9.  **Testing & Iteration:** Perform no-load and loaded tests. Measure back-EMF constant, torque curve, efficiency. Validate thermal behavior. Compare against simulations. Refine design if needed (e.g. more cooling, different winding).
10. **Validation:** Ensure it meets performance, efficiency, and safety requirements. Iterate to final design.

## Case Study: Small High-Speed BLDC (Drone Motor)

- **Requirements:** ~300W mechanical power at 40,000 rpm (e.g. 10-inch prop), 11.1 V battery. Torque needed ~0.36 N·m.
- **Preliminary:** Choose outrunner BLDC (magnets on rotating outer can) for good cooling and torque. Target KV ≈ 3600 rpm/V (11.1 V → ~40k rpm no-load) so low-speed torque constant \$K_t≈0.055\$ N·m/A (SI). At 0.36 N·m, current ~6.5 A.
- **Stator:** Use 12-slot, 14-pole configuration (7 pole pairs) common in hobby motors. Winding: 3-phase, wye, 14 turns per phase (calculations via motor constant). Gauge: ~AWG20 to handle 6–10 A. Lamination: thin (0.35 mm) silicon steel for high speed. Outer stator diameter ~60 mm.
- **Rotor:** NdFeB magnets (Grade N35) on rotor can, 14 poles. Magnets arcs cover ~60% of pole-pitch for high flux. Airgap ~0.5 mm. Rotor inertia kept low (alloy can, light support).
- **Assembly:** Glue magnets with epoxy and add retaining steel rings. Bearings: 688ZZ (6×19×6 mm) rated \>20krpm. Enclosure: aluminum shell for rigidity.
- **Controller:** 3-phase 30A ESC with six MOSFETs (≥30V, 60A) and microcontroller for FOC. Hall sensors on stator for rotor position.
- **BOM Highlights:** Silicon steel stack (~\$10), 150g copper wire, 30 g NdFeB magnets (~\$20), bearings, shaft, aluminum can. ESC & battery separate. Total ~500g.
- **Performance:** Expected ~80% efficiency (≈250W out). No-load speed ~40k RPM, KV ~3600 RPM/V. Torque constant \$K_t≈0.055\$N·m/A, so 6.5A→0.36N·m. Thrust ~1.5 kg with 10″ prop.
- **References:** Typical hobby BLDC data (Motor constants and charts[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque)) and efficiency comparisons[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart). See *e.g.* Scorpion or T-Motor drone motors.

## Case Study: Medium-Power Axial-Flux PMSM (Hub Motor)

- **Requirements:** ~10 kW peak at 300 rpm for an e-scooter hub. Torque needed ~320 N·m.
- **Topology:** Axial-flux outer-rotor (rotor discs on either side of stator). Use high-strength NdFeB ring magnets on a dual-rotor. 12 stator teeth per side, 12 rotor poles.
- **Stator:** Thin steel laminations (0.3 mm) stacked as two annular stators. Concentrated winding (one tooth-per-phase) with 6 coils per stator (double-layer multi-turn). Large-diameter stators (~200 mm) for torque. Copper foil windings (hairpin style) to handle ~50 A continuous (peak ~100 A). Insulation class F (155°C).
- **Magnets:** 24 ring segments per rotor, N48H grade (180°C, high coercivity). Axial airgap ~1.5 mm (for cooling gap).
- **Cooling:** Liquid jacket around stator outer edge (common in hub motors) to remove ~500 W losses.
- **Electronics:** 800 V battery DC-DC to 400 V bus (for compact inverter). 6-phase inverter (2× 3-phase to reduce current per leg) with SiC MOSFETs, torque control via field-oriented control. Resolver for rotor position sensing (rugged).
- **Mechanical:** 6306 ball bearings (30×72×19 mm) for rotor. Hub housing integrated. Precision alignment needed for axial airgaps.
- **BOM Highlights:** ~30 kg stator+rotor, ~10 kg magnets (~\$200), ~10 kg copper, cooling system, bearings, 6-phase inverter (~\$500).
- **Expected Performance:** Peak torque 320 N·m, continuous ~150 N·m. Efficiency ~96% peak (Axial PMSM can exceed 96%[\[37\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Axial%20flux%20motors%2C%20nevertheless%2C%20have,range%20applications)). Motor ~40 cm diameter, 10 cm stack. Power density ~3.5 kW/kg (high).
- **References:** Data from EV hub motor trends and axial-flux studies[\[30\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Remember%20when%20we%20mentioned%20a,has%20a%20multiplying%20effect%20on)[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density).

**Sources:** Authoritative texts and articles, motor handbooks, and vendor documents were referenced throughout (e.g. Bodine Handbook[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque), NEMA guides[\[8\]](https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2#:~:text=What%20is%20Electrical%20Steel%3F%20%E2%80%A2,silicon%20%E2%80%A2%20Very%20efficient%20at)[\[34\]](https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html#:~:text=In%20general%20a%20motor%20should,are%20directly%20related%20to%20motor), industry whitepapers[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[28\]](https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm#:~:text=The%20core%20idea%20of%20a,combination%20of%20simplicity%20and%20efficiency)). Performance comparisons derive from published benchmarks[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart)[\[6\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20offer%20much,as%20electric%20vehicles%20and%20robotics) and vendor material[\[21\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=As%20always%2C%20there%20are%20trade,these%20losses%2C%20which%20limits%20performance)[\[38\]](https://www.orientalmotor.com/brushless-dc-motors-gear-motors/technology/AC-brushless-brushed-motors.html#:~:text=load%20and%20low,the%20motor%27s%20performance%20curve). (Standards: IEC 60034, NEMA MG1 for machine design.)

------------------------------------------------------------------------

[\[1\]](https://www.eti.kit.edu/english/1376.php#:~:text=The%20first%20rotating%20device%20driven,Barlow%27s%20Wheel) Institute - History - The invention of the electric motor 1800-1854

<https://www.eti.kit.edu/english/1376.php>

[\[2\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1871%E2%80%931873%2C%C2%A0Z%C3%A9nobe%20Th%C3%A9ophile%20Gramme%20%20,laminated%20magnetic%20cores%20of%20insulated) [\[11\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1828%2C%C2%A0%C3%81nyos%20Jedlik%20%20%20Hungarian%2C,18) [\[12\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1873%2C%C2%A0Auguste%20Pellerin%20%20French%3B%20introduced,25) [\[13\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1885%2C%C2%A0Galileo%20Ferraris%20%20%20Italian%2C,phase%20current.%5B%2030) [\[14\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1889%E2%80%9390%2C%C2%A0Mikhail%20Dolivo,10) [\[15\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1935%2C%20Hermann%20Kemper%20%20,model%20of%20linear%20induction%20motor) [\[19\]](https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor#:~:text=1861%E2%80%931864%2C%C2%A0James%20Clerk%20Maxwell%20%20,pulsating%20DC%20problem%3B%20at%20Vienna) Timeline of the electric motor - Wikipedia

<https://en.wikipedia.org/wiki/Timeline_of_the_electric_motor>

[\[3\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=T%20%3D%20Kt%20I%20where,relates%20current%20to%20developed%20torque) [\[4\]](https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX#:~:text=V%20%3D%20Rw%20I%20%2B,It%20is%20a%20proportionality%20constant) bodine-electric.com

<https://www.bodine-electric.com/blog/wp-content/uploads/2021/11/bodine-gearmotors-introduction-to-motor-constants-for-fractional-horsepower-07470050.pdf?srsltid=AfmBOoo1pUx34XnGbZMz9gUi4YrdssXAbm945dv6iOl-CerC2QrU0gLX>

[\[5\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Motor%20Efficiency%20Auto%20Electrification%20,torque%20chart) [\[16\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Permanent%20Magnet%20Motor%20Efficiency) [\[30\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=Remember%20when%20we%20mentioned%20a,has%20a%20multiplying%20effect%20on) [\[32\]](https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification#:~:text=One%20major%20consideration%20in%20permanent,material%20only%20compounds%20the%20problem) Permanent Magnet vs Induction Motor: Torque, Losses, Material

<https://www.horizontechnology.biz/blog/induction-vs-permanent-magnet-motor-efficiency-auto-electrification>

[\[6\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20offer%20much,as%20electric%20vehicles%20and%20robotics) [\[7\]](https://osenc.com/motor-and-permanent-magnet/#:~:text=Permanent%20magnet%20motors%20deliver%20higher,efficiency%20and%20energy%20efficiency%20goals) Permanent Magnet Motor Vs Induction Motor - Osenc

<https://osenc.com/motor-and-permanent-magnet/>

[\[8\]](https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2#:~:text=What%20is%20Electrical%20Steel%3F%20%E2%80%A2,silicon%20%E2%80%A2%20Very%20efficient%20at) PowerPoint Presentation

<https://www.nema.org/docs/default-source/motor-and-generator-guides-and-resources-library/2-1-ac-motor-components-detailed-v2.pdf?sfvrsn=947aee6f_2>

[\[9\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=Figure%205%3A%20In%20a%20BLDC,sensors%20to%20determine%20rotor%20position) [\[21\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=As%20always%2C%20there%20are%20trade,these%20losses%2C%20which%20limits%20performance) [\[31\]](https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/#:~:text=good%20starting%20torque%20and%20low,and%20complexity%20of%20the%20system) Choosing Between Brush and Brushless DC Motors - Allied Motion

<https://www.alliedmotion.com/choosing-between-brush-and-brushless-dc-motors/>

[\[10\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Torque%20and%20Power%20Density) [\[35\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Cooling%20is%20one%20place%20where,saving%20cooling%20systems) [\[36\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Although%20having%20the%20technical%20advantages%2C,manufacture%2C%20especially%20in%20large%20quantities) [\[37\]](https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html#:~:text=Axial%20flux%20motors%2C%20nevertheless%2C%20have,range%20applications) Radial vs Axial Flux Motor: Which is Suitable for the Future of Electric Machines?

<https://www.stanfordmagnets.com/radial-vs-axial-flux-motor-which-is-suitable-for-the-future-of-electric-machines.html>

[\[17\]](https://www.monolithicpower.com/en/learning/mpscholar/electric-motors/introduction-to-motors/basic-principles-of-motor-operation?srsltid=AfmBOorqWckN0CDZgAy0wy_k4WKdoYsEWRcTvgumUG9GJ3gLS-eGWsWN#:~:text=Consider%20a%20scenario%20where%20there,this%20fundamental%20principle%20of%20rotation) [\[18\]](https://www.monolithicpower.com/en/learning/mpscholar/electric-motors/introduction-to-motors/basic-principles-of-motor-operation?srsltid=AfmBOorqWckN0CDZgAy0wy_k4WKdoYsEWRcTvgumUG9GJ3gLS-eGWsWN#:~:text=The%20ruling%20equation%20is%3A) Basic Principles of Motor Operation

<https://www.monolithicpower.com/en/learning/mpscholar/electric-motors/introduction-to-motors/basic-principles-of-motor-operation?srsltid=AfmBOorqWckN0CDZgAy0wy_k4WKdoYsEWRcTvgumUG9GJ3gLS-eGWsWN>

[\[20\]](https://www.orientalmotor.com/brushless-dc-motors-gear-motors/technology/AC-brushless-brushed-motors.html#:~:text=Service%20and%20Maintenance%3A%20DC%20vs,BLDC) [\[38\]](https://www.orientalmotor.com/brushless-dc-motors-gear-motors/technology/AC-brushless-brushed-motors.html#:~:text=load%20and%20low,the%20motor%27s%20performance%20curve) Brushless DC Motor vs. AC Motor vs. Brushed Motor

<https://www.orientalmotor.com/brushless-dc-motors-gear-motors/technology/AC-brushless-brushed-motors.html>

[\[22\]](https://eshop.se.com/in/blog/post/induction-motor-working-principles-and-types.html?srsltid=AfmBOorNetYzPh6Bc6hS1COwb9e4E0eydf3YAFuTZbQuZbZ0h9C_BE6Y#:~:text=Some%20of%20the%20advantages%20of,induction%20motors%20are%20listed%20below) Induction Motor: Working Principle & Their Types - Schneider Electric

<https://eshop.se.com/in/blog/post/induction-motor-working-principles-and-types.html?srsltid=AfmBOorNetYzPh6Bc6hS1COwb9e4E0eydf3YAFuTZbQuZbZ0h9C_BE6Y>

[\[23\]](https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8#:~:text=remain%20energized%20at%20all%20times,even%20when%20not%20in%20motion) [\[24\]](https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8#:~:text=Disadvantages%3A) Stepper Motors vs. Servo Motors: What Are The Differences?

<https://www.actuonix.com/stepper-motors-vs-servo-motors?srsltid=AfmBOorSYwf4QvioSbDvlcbwmCcqtfhoDRTEyelFL1h7BR0O_PCG_lQ8>

[\[25\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=To%20form%20the%20phase%20of,and%20hence%20more%20fault%20tolerant) [\[26\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=As%20compared%20to%20induction%20motors%2C,demand%20for%20switched%20reluctance%20motors) [\[27\]](https://www.nide-group.com/Emobile/news_1/id/150.html#:~:text=Disadvantages%20of%20the%20switched%20reluctance,current%20and%20bus%20voltage%20speed) Ningbo Nide Tech Co.,Ltd

<https://www.nide-group.com/Emobile/news_1/id/150.html>

[\[28\]](https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm#:~:text=The%20core%20idea%20of%20a,combination%20of%20simplicity%20and%20efficiency) [\[29\]](https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm#:~:text=drive,heat%20losses%20from%20the%20motor) 6 Reasons to Choose SynRM - Inverter Drive Systems Ltd

<https://www.inverterdrivesystems.com/6-reasons-to-choose-synrm>

[\[33\]](https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html#:~:text=A%20105%20221%2060%2070,H%20180%20356%20125) [\[34\]](https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html#:~:text=In%20general%20a%20motor%20should,are%20directly%20related%20to%20motor) NEMA Insulation Classes

<https://www.engineeringtoolbox.com/nema-insulation-classes-d_734.html>
