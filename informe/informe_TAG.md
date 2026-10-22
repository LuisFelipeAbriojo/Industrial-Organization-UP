# ¿Eficiencia o poder de mercado? La integración de Porsche al Grupo Volkswagen vista con datos de ingresos, y su distribución en el Perú

**Trabajo Aplicativo Grupal (TAG) – Organización Industrial, sección C**
Universidad del Pacífico, semestre 2026-II. Profesor: José Nicanor Gonzales Quijano.
Grupo 2: Cruz · Alvarez · Baca · Abriojo.
Artículo de referencia: Hess, J. T. y Wang, X. (2026), *Measuring Merger Effects with Revenue Data*, Banco de España, Documento de Trabajo N.º 2631.

---

## a. Introducción y problema de investigación

### a.1 La pregunta del artículo

Hess y Wang (2026) se preguntan si las fusiones horizontales vuelven más **eficiente** a la empresa fusionada o si aumentan su **poder de mercado**. Para responderlo siguen la evolución de dos indicadores tras 3 759 fusiones horizontales en España (1997–2022):

- la productividad total de los factores medida con ingresos (TFPR);
- el *markup*, es decir, el margen de precio sobre el costo marginal.

Encuentran que, ocho años después de la fusión, la TFPR sube alrededor de 4 % y el markup entre 5 % y 6 % (resumen y sección 4). Las ganancias de TFPR aparecen en casi todos los sectores. Los aumentos de markup, en cambio, se concentran en pocas industrias, sobre todo en actividades sanitarias (sección 4.3).

### a.2 El aporte que usamos: un problema de medición

El aporte central del artículo es **metodológico**. Los estados financieros se reportan por entidad legal: cuando una empresa absorbe a otra, la adquirida deja de reportar y sus cuentas pasan a las del adquirente. Si comparamos al adquirente antes de la fusión con el grupo fusionado después, estamos comparando **dos objetos distintos**, y el cambio medido mezcla desempeño real con un cambio de perímetro (sección 3.1).

La solución que proponen es la **consolidación virtual**: sumar las cuentas de adquirente y adquirida antes de la fusión, de modo que la unidad de observación sea la misma antes y después. El hallazgo que motiva nuestro trabajo es que, sin esa corrección, **tanto el efecto sobre la TFPR como el efecto sobre el markup cambian de signo** (sección 4.4). Además, agregar los markups previos con pesos por ventas en lugar de pesos por costo también basta para invertir el resultado de markups (sección 4.5, Proposición 2).

### a.3 Nuestra pregunta y cómo la aplicamos

> **¿La integración de Porsche al Grupo Volkswagen elevó su eficiencia o su poder de mercado, y cambia la respuesta según cómo se mida el "antes"?**

El caso es ideal para la parte metodológica: es una fusión de fabricantes de automóviles con información pública de ambas partes antes y después. Volkswagen (VW) tomó el 49.9 % de Porsche el 7 de diciembre de 2009 y la consolidó por completo el **1 de agosto de 2012** (VW, 2010, p. 121; VW, 2013, p. 188 y 266).

Hay que decir desde el inicio lo que el caso **no** permite. Es una sola operación y no tiene grupo de control, así que no podemos estimar un efecto causal como el *event study* del artículo. Sí podemos medir con datos reales los **sesgos mecánicos** que el artículo formaliza (Proposiciones 1 y 2 y sección 3.3.2), porque esos sesgos dependen solo de las cuentas antes de la fusión.

Luego llevamos los conceptos al **Perú**. Aquí el Grupo VW no se fusiona con nadie: vende a través de un importador que representa casi todo su portafolio (Grupo Euromotors). Por eso en el Perú los conceptos relevantes son la estructura de mercado (participaciones y HHI) y las **relaciones verticales** entre fabricante e importador. La subpregunta es:

> **¿Cuánto poder de mercado tiene el Grupo VW en el Perú y cómo lo moldea su distribución a través de un importador?**

---

## b. Conceptos de Organización Industrial que sustentan el artículo

### b.1 Fusiones horizontales: el trade-off de Williamson

Una fusión horizontal tiene dos efectos opuestos (semana 4).

- **Efecto unilateral.** Desaparece un competidor y la empresa fusionada internaliza la competencia entre sus productos, lo que empuja el precio al alza.
- **Eficiencias.** Si la fusión reduce el costo marginal (economías de escala o de alcance, compras conjuntas, plataformas compartidas), el precio puede bajar.

Williamson (1968) mostró que basta una reducción de costos pequeña para compensar en **bienestar total** la pérdida de eficiencia asignativa. Para que el **consumidor** no pierda se necesita mucho más.

Nuestro mini-modelo (Anexo C, figura 4) lo ilustra con la demanda de la semana 9 (P = 150 − Q). Con tres empresas en Cournot y costos (30, 30, 45), si se fusionan las dos de costo 30 el precio sube de 63.75 a 75 sin sinergias. La condición de Farrell y Shapiro (1990) para que el precio no suba es c_M ≤ c₁ + c₂ − P_pre = −3.75: un costo **negativo**, imposible de alcanzar. El bienestar total, en cambio, no cae si c_M ≤ 21.3 (una reducción de 29 %).

La conclusión de política es la misma de la semana 4. El criterio de bienestar del consumidor es mucho más exigente que el de bienestar total, y el artículo no puede decidir entre ambos porque solo observa ingresos y costos, no precios ni cantidades físicas.

En un segundo escenario, un socio grande y eficiente (c = 30) absorbe a uno pequeño e ineficiente (c = 50) en un mercado con cuatro empresas. Ahí el umbral sí es alcanzable (c_M ≤ 22, una reducción de 27 %), y el bienestar total sube incluso sin sinergias, porque la producción se reasigna hacia la planta eficiente. Lo que importa para el consumidor es **quién** se fusiona y **cuánto** baja el costo marginal.

### b.2 Poder de mercado: Lerner, markup y HHI

El markup es μ = P/CMg, y se relaciona con el índice de Lerner por L = (P − CMg)/P = 1 − 1/μ. En Cournot, el Lerner de cada empresa es sᵢ/ε, y el Lerner promedio del mercado es **L = HHI/ε** (semana 11). Esta igualdad es el puente entre las dos partes del trabajo:

- el artículo mide el poder de mercado por el lado de la **conducta** (el markup de la empresa);
- en el Perú solo podemos medirlo por el lado de la **estructura** (el HHI).

La semana 11 advierte que los indicadores estructurales son útiles pero predicen poco, y que los de conducta describen mejor el desempeño, aunque exigen conocer costos.

### b.3 Cómo mide el artículo el markup: el enfoque de producción

El artículo usa el enfoque de De Loecker y Warzynski (2012). Si la empresa minimiza costos y los materiales son un insumo flexible, el markup es igual a la elasticidad del producto respecto de los materiales dividida entre la participación del gasto en materiales en los ingresos (ecuación 3). Con una función **Cobb-Douglas** esa elasticidad es una constante β_m, así que:

> μ = β_m · Q/M (ecuación 7), donde Q son los ingresos y M el costo de materiales.

Esto tiene una consecuencia práctica clave: **Δ ln μ = Δ ln(Q/M)**. Para medir *cambios* del markup no hace falta estimar β_m; basta con la razón ingresos/costo de materiales (sección 4.2). Es lo que hacemos con VW y Porsche.

La Cobb-Douglas además anula el "canal de elasticidad" de la ecuación 4. Con una translog, la elasticidad cambiaría solo porque la fusión reordena los insumos, y eso contaminaría la comparación antes-después.

### b.4 TFPR no es TFPQ

La TFPR (ecuaciones 1 y 6) mide cuánto **ingreso** genera la empresa por unidad de insumos, así que mezcla eficiencia física con precios. Si una fusión sube precios sin mejorar la tecnología, la TFPR sube igual. El artículo reconoce que con datos de ingresos no se puede separar la eficiencia física (TFPQ) del precio (sección 6).

Su argumento indirecto es que, si las subidas de TFPR fueran puro precio, deberían ir de la mano con subidas de markup en cada industria, y en los datos no ocurre así. También recuerda que un markup más alto no excluye eficiencias: si el costo marginal cae más que el precio, el markup sube aunque el consumidor pague menos (sección 4.2, citando a Syverson, 2019).

### b.5 Los dos sesgos que formaliza el artículo

**Sesgo de frontera (Proposición 1 y sección 3.3.2).** Como ingresos y materiales se suman, el markup del grupo consolidado es exactamente el **promedio ponderado por costo** de los markups individuales:

> μ_pool = w_A μ_A + w_T μ_T, con w_i = M_i / M_pool, de modo que **μ_pool − μ_A = w_T (μ_T − μ_A)**.

Comparar al adquirente antes con el grupo después agrega este término mecánico. Su signo depende solo de cuál de las dos empresas tiene el markup más alto. En España las adquiridas suelen tener markups menores, así que el sesgo empuja hacia abajo. Para la TFPR, la Proposición 1 da Z_pool/Z_A = a + r·b, donde r es la productividad relativa de la adquirida y a, b dependen de cómo se reparten los insumos.

**Sesgo de agregación (Proposición 2).** Antes de la fusión hay que combinar dos markups. El grupo consolidado *después* pondera implícitamente por costo. Si *antes* se pondera por ventas, se obtiene un número más alto, por la desigualdad de Jensen: el markup es β_m/c, una función convexa del costo unitario c = M/Q. Ese exceso aparece después como una caída espuria del markup.

### b.6 Restricciones verticales (para el caso peruano)

La relación entre fabricante e importador es vertical (semana 6). Las restricciones verticales pueden ser **pro-competitivas**: evitan la doble marginalización, aseguran servicios como la posventa y protegen inversiones frente al *hold-up*. También pueden **debilitar la competencia**: la intra-marca, con territorios exclusivos, o la inter-marca, con contratos exclusivos que elevan barreras a la entrada. La diferenciación **vertical** (semana 3, Tirole) explica por qué un mismo grupo vende marcas de gama media y de lujo: así segmenta a consumidores con distinta disposición a pagar por calidad.

---

## c. Aplicación a un caso real

### c.1 Contexto: el Grupo VW como serie de adquisiciones

El Grupo VW es en buena parte el resultado de adquisiciones sucesivas: Audi, SEAT, Škoda, Bentley, Lamborghini y Bugatti (automóviles), Scania y MAN (camiones) y Ducati (motos). Esa historia genera justamente el problema que estudia el artículo: **el perímetro contable cambia casi todos los años**.

Entre 2011 y 2012 se produjeron cuatro cambios de perímetro (Anexo A, tabla A3):

- **Porsche Holding Salzburg**, un distribuidor, consolidado el 1-mar-2011;
- **MAN**, consolidada el 9-nov-2011, con unos €14 000 millones de ingresos anuales;
- **Ducati**, en julio de 2012;
- **Porsche AG**, el 1-ago-2012.

Un dato que debilita la lectura de "fusión que crea poder de mercado": desde 2009 la integración ya estaba en marcha. VW tenía el 49.9 % de Porsche, y Porsche SE, la holding de las familias Porsche y Piëch, controlaba el 50.73 % de los votos de VW (Porsche SE, 2012, p. 151). La competencia entre ambas ya estaba en buena medida internalizada antes de 2012, y compartían plataformas como Cayenne/Touareg. Lo que cambió en 2012 fue sobre todo la **forma contable**: Porsche pasó del método de participación a la consolidación plena. Por eso el caso sirve muy bien para estudiar el sesgo de medición, y no tanto para medir un aumento de poder de mercado.

### c.2 Datos

- **VW:** ingresos, costo de materiales, costo de ventas, empleados y activos de la revisión quinquenal de sus reportes anuales (VW, 2013; VW, 2015).
- **MAN SE:** ingresos y costo de materiales de sus reportes anuales 2011, 2013 y 2014 (MAN SE, 2012, 2014, 2015), para limpiar el perímetro.
- **Porsche AG:** las mismas cifras de su tabla de indicadores (Porsche AG, 2014; Porsche AG, 2015).

Entre diciembre de 2009 y julio de 2012 ninguna entidad consolidaba a Porsche AG ni publicaba su costo de materiales. La única cifra pública previa a la integración que encontramos es la de **2011**, en el reporte 2013 de Porsche AG. Por eso definimos:

- **antes = 2011**;
- **después = 2013 y 2014**, los primeros años completos dentro de VW. En 2012 Porsche solo está consolidada 5 meses.

Las cifras están en el Anexo A, con fuente y página en `data/fuentes.md`.

### c.3 Resultados del ejercicio de consolidación

**Antes de la fusión (2011):**

| | Q/M |
|---|---|
| VW (adquirente) | 1.5226 |
| Porsche AG (adquirida) | 1.6019 |
| Unidad virtual VW + Porsche, pesos por costo | 1.5275 |
| Unidad virtual VW + Porsche, pesos por ventas | 1.5277 |

Porsche pesa poco: w_T = 6.1 % por costo y π_T = 6.4 % por ventas. Su markup proxy es **5.2 % más alto** que el de VW (figura 1).

**Descomposición del sesgo de frontera (sección 3.3.2).** w_T(x_T − x_A) = 0.061 × (1.6019 − 1.5226) = **+0.0049** en unidades de Q/M. El script verifica que coincide exactamente con x_pool − x_A. En logaritmos, el sesgo es ln x_pool − ln x_A = **+0.32 puntos log**. El signo es **positivo**, al revés del promedio español del artículo, porque aquí la adquirida tiene el markup más alto. Es la misma fórmula del artículo con un signo distinto en este caso.

**Sesgo de agregación (Proposición 2).** ln x_pool − ln x_ventas = **−0.02 puntos log**. Se cumple la desigualdad (μ_ventas ≥ μ_pool), pero el efecto es despreciable: Porsche pesa poco y su costo unitario se parece al de VW. La convexidad de Jensen solo importa cuando los costos unitarios de las dos empresas difieren mucho.

**Cambio estimado del markup** (Δ ln(Q/M) × 100, figura 2):

| Especificación | 2011→2013 | 2011→2014 |
|---|---|---|
| Solo adquirente (VW 2011 vs grupo) | +1.79 | +0.34 |
| Consolidación virtual (VW + Porsche 2011 vs grupo) | +1.48 | +0.02 |
| Virtual con pesos por ventas | +1.46 | +0.01 |

### c.4 Interpretación honesta

1. **El sesgo existe, tiene el signo que predice la teoría y es pequeño.** Medir solo al adquirente sobreestima el aumento del markup en unos 0.3 puntos log, porque se suma una adquirida de markup más alto. Es pequeño porque Porsche pesa 6 % del grupo. En la muestra española del artículo, las adquiridas pesan en promedio un tercio o la mitad de lo que pesan los adquirentes (Tabla 1), y por eso allí el sesgo alcanza para invertir el signo.

2. **No podemos atribuir a la fusión el +1.5 %.** Entre 2010 y 2011, sin fusión de por medio, el Q/M de VW cayó 4.8 puntos log, más de tres veces el cambio estimado. Además, en 2014 el efecto prácticamente desaparece. Sin grupo de control, la variación anual del costo de materiales, el tipo de cambio o la mezcla de modelos dominan cualquier efecto de la fusión.

3. **El perímetro contamina la comparación, y es el mismo sesgo del artículo causado por otra adquisición.** MAN estuvo unos 2 meses dentro de VW en 2011 y el año completo en 2013. VW no publica el costo de materiales por segmento, así que usamos los reportes de MAN SE: su Q/M es alto (1.77 en 2011, 1.80 en 2013). Al restar MAN de VW:
   - en 2013 y 2014 restamos sus ingresos y su costo de materiales propios;
   - en 2011 restamos los €2 652 M que aportó a VW, con la razón Q/M de MAN de ese año (aproximación).

   El resultado: la consolidación virtual cae de +1.48 % a **+0.50 %** (2011→2013) y de +0.02 % a **−0.93 %** (2011→2014) (figura 3). Una parte importante del "aumento" del markup del grupo solo reflejaba que entró al perímetro una empresa de markup alto, exactamente el término w_T(μ_T − μ_A) aplicado a MAN.

4. **Las ventas intragrupo mueven el resultado.** En 2013, el 8 % de los ingresos de Porsche fueron ventas a otras empresas del grupo, probablemente distribuidores propios como Porsche Holding Salzburg (VW, 2015, p. 55). Antes de 2012 esas ventas eran ingreso de Porsche y compra de VW; al consolidar se eliminan. Si eliminamos la misma proporción en 2011, el resultado virtual baja a **+1.2 %** (2013) y **−0.25 %** (2014). Con ambos ajustes (sin MAN y sin ventas intragrupo), el cambio es **+0.22 %** a 2013 y **−1.20 %** a 2014. Esto matiza una afirmación del artículo: el agregado combinado es invariante a la contabilidad *interna* (sección 3.1), pero sumar dos estados financieros que comercian entre sí no reproduce exactamente la consolidación, que elimina las transacciones internas.

5. **Solo el cambio del markup es interpretable, no su nivel.** Con β_m = 0.388 (Tabla B.1, fabricantes de vehículos españoles), el "markup" de VW saldría 0.59 < 1. Por eso solo usamos cambios en logaritmos, donde β_m se cancela.

6. **La TFPR también se mueve mecánicamente** (Anexo B, ilustrativo). La Proposición 1 da un sesgo de **+1.25 puntos log**, porque r = 0.83 supera el umbral r* = 0.67. Las elasticidades usadas suman 0.884 (rendimientos decrecientes), no los rendimientos casi constantes con los que razona el artículo, y los activos de VW incluyen su financiera. La cifra es frágil, pero muestra que el signo del sesgo no es universal.

7. **¿Eficiencia o poder de mercado?** Con datos de ingresos no podemos separar ambos. Lo que sí vemos es que el Q/M de Porsche subió de 1.60 (2011) a 1.73 (2013) dentro de VW. Eso es compatible con menores costos de materiales por compras conjuntas con VW (Porsche SE, 2012, p. 71), pero también con precios más altos y cambios en la mezcla de modelos (más Cayenne y la nueva generación de Boxster/Cayman; Porsche AG, 2014, p. 130). Es la misma ambigüedad TFPR/TFPQ que el artículo declara.

### c.5 El Grupo VW en el Perú: estructura de mercado

**Datos.** Usamos las inscripciones de vehículos nuevos en SUNARP que publica la AAP, en dos niveles: vehículos livianos (2020–2025) y el segmento de lujo (2022–2025). Según su web, el Grupo Euromotors representa a Volkswagen, Audi, Porsche, SEAT, Cupra, Bentley, Lamborghini, Ducati, VW Camiones y Buses y MAN; Škoda no figura.

**Livianos (figura 5).**
- La participación de la **marca** Volkswagen cayó de 4.0 % (2021) a 2.0 % (2025), en un mercado de 186 981 unidades en 2025.
- Sumando Audi, Porsche, Lamborghini y Bentley, el **Grupo VW** pasa de 3.9 % (2022) a 2.4 % (2025).
- No incluimos SEAT y Cupra porque la AAP los agrupa en "Otros".
- El mercado es **poco concentrado**: el HHI por marca está entre 770 y 775 en 2025, y por grupo propietario (Toyota + Lexus, Hyundai + Kia, etc.) entre 948 y 951 (figura 7). Las cuatro primeras marcas suman 45 %.
- La competencia de marcas chinas (Changan, Jetour, Geely, JAC) creció con fuerza. En gama media, el Grupo VW es un competidor marginal sin poder de mercado estructural.

**Lujo (figura 6).** El cuadro cambia en 2025 (3 930 unidades):
- BMW 29.6 %, Mercedes-Benz 19.6 %, **Audi 17.7 %**, Volvo 10.5 %, Lexus 8.5 %, Mini 5.5 %, **Porsche 4.2 %**.
- El Grupo VW suma **22.2 %**, detrás de BMW Group (35.0 % con Mini).
- El HHI por marca es 1 815 y por grupo **2 302**.

**Ejercicio contrafactual.** Si Audi y Porsche fueran empresas independientes que se fusionan hoy en el Perú, el aumento del HHI sería 2 × 17.7 × 4.2 ≈ **148**. Con un HHI posterior de 2 302 > 1 800 y ΔHHI > 100, se superarían los umbrales de presunción estructural de las Merger Guidelines 2023 vistas en la semana 11. Hay que leerlo con tres cautelas:

- el "segmento de lujo" de la AAP no es necesariamente un mercado relevante en el sentido de la prueba SSNIP;
- Porsche y Audi compiten poco en precio: un 911 y un Audi Q3 no son sustitutos cercanos;
- en el Perú no hay ninguna operación que evaluar, porque ambas marcas pertenecen al mismo grupo y llegan por el mismo importador.

La Ley 31112 excluye expresamente del control previo el crecimiento "al interior del mismo grupo económico" (art. 6.2.a). Además, solo exige notificar si las ventas o activos **en el país** superan 118 000 UIT en conjunto y 18 000 UIT para al menos dos partes (art. 6.1). Una integración como la de 2012 se decidió en Alemania y, en el Perú, se reflejaría solo a través del importador.

**Lerner implícito (ilustrativo).** Con L = HHI/ε y elasticidades supuestas entre 1.5 y 5, el Lerner promedio del segmento de lujo estaría entre 0.05 y 0.15, y el de livianos entre 0.02 y 0.06. No estimamos ε. El ejercicio solo muestra que la misma estructura implica márgenes muy distintos según la elasticidad, y que el segmento de lujo, más concentrado y con demanda probablemente menos elástica, es donde cabe esperar márgenes mayores.

### c.6 Relaciones verticales: fabricante–importador–concesionario

En el Perú el Grupo VW no fabrica: exporta a un importador independiente que distribuye la mayor parte de su portafolio. Cuatro ideas de la semana 6 ayudan a entender este arreglo.

1. **Integrar o contratar.** En algunos mercados VW compró a sus importadores. Adquirió Porsche Holding Salzburg en 2011 y, en 2012, KPI Polska, que su reporte describe como "importador y distribuidor exclusivo" de varias marcas del grupo en Polonia (VW, 2013, p. 269). En el Perú mantiene un distribuidor independiente. La teoría lo explica así: integrarse elimina la doble marginalización y el riesgo de *hold-up*. Cuando el mercado es pequeño, como el peruano (2.4 % de livianos para el grupo), es más barato delegar en un socio local que conoce la regulación, el financiamiento y la red de talleres.

2. **Economías de alcance.** Un solo importador para varias marcas comparte homologación, logística de puerto, almacenes de repuestos, sistemas de garantía, financiamiento y personal técnico. Es la misma lógica de costos compartidos de la semana 9, aplicada a la distribución. El portafolio multimarca permite también cubrir todo el espectro de calidad, de VW a Lamborghini.

3. **Segmentación (diferenciación vertical).** El mismo distribuidor vende la marca de gama media (VW, con 2 % de livianos) y marcas de lujo (22 % del segmento de lujo). Es la diferenciación vertical de Tirole: separar consumidores por disposición a pagar con productos de calidad distinta, sin que las marcas propias se canibalicen en precio.

4. **Competencia intra-marca e inter-marca.** Un importador único por marca elimina la competencia intra-marca en la importación. La competencia relevante para el consumidor pasa a ser la **inter-marca** (Audi frente a BMW y Mercedes; VW frente a Toyota, Hyundai o Changan) y, aguas abajo, la que exista entre concesionarios. En livianos la competencia inter-marca es intensa (HHI < 1 000). En lujo es más débil, y ahí cobran importancia los servicios de posventa y la reputación de marca que la exclusividad ayuda a sostener. No tenemos información pública sobre los contratos (exclusividad territorial, precios sugeridos), así que esto es una interpretación teórica y no una afirmación sobre Euromotors.

---

## d. Conclusiones y recomendaciones

### d.1 Principales resultados

1. **El artículo aporta una lección de medición.** Con datos contables, comparar al adquirente antes con el grupo después mezcla desempeño con un cambio de perímetro. La consolidación virtual corrige ese sesgo y la forma de agregar importa (pesos por costo, no por ventas).

2. **En el caso VW–Porsche, el sesgo tiene el signo opuesto al promedio español.** Porsche tenía un markup proxy 5 % mayor que VW, así que medir solo al adquirente **sobreestima** el aumento del markup, aunque poco (+0.3 puntos log), porque Porsche pesaba 6 % del grupo. El sesgo de agregación es despreciable aquí.

3. **No encontramos evidencia de que la integración elevara el markup del grupo.** El cambio con consolidación virtual es +1.5 % a 2013 y ≈0 % a 2014. Al quitar MAN, otra adquisición de markup alto que entró al perímetro en el mismo periodo, cae a +0.5 % y −0.9 %, y con el ajuste intragrupo a +0.2 % y −1.2 %. Todas estas cifras son menores que la variación anual normal de VW (−4.8 % entre 2010 y 2011). La pregunta "¿eficiencia o poder de mercado?" queda abierta, como reconoce el propio artículo para datos de ingresos.

4. **En el Perú**, el Grupo VW no tiene poder de mercado estructural en livianos (2.4 %, mercado poco concentrado), pero sí una posición relevante en lujo (22 %, HHI por grupo de 2 302). Su presencia se organiza mediante un importador multimarca, un arreglo vertical que aprovecha economías de alcance y segmentación.

### d.2 Fortalezas y limitaciones del enfoque

- **Fortalezas.** La consolidación virtual solo exige estados financieros públicos y no requiere estimar la función de producción para medir cambios de markup. Además, el sesgo de frontera se calcula con una fórmula simple, w_T(μ_T − μ_A), que cualquier analista de competencia puede aplicar.
- **Limitaciones generales.** Los datos de ingresos no separan precio de eficiencia (TFPR ≠ TFPQ). El markup en nivel depende de β_m.
- **Limitaciones de nuestra aplicación.** Es una sola fusión sin grupo de control. Los perímetros cambian casi cada año (MAN, Porsche Holding Salzburg, Ducati). Hay ventas intragrupo previas. La integración ya estaba avanzada desde 2009. Y en el Perú solo observamos unidades inscritas, no precios ni márgenes.

### d.3 Utilidad y aplicabilidad

El enfoque es útil para evaluar fusiones *ex post* con estados financieros, por ejemplo para que Indecopi revise operaciones aprobadas bajo la Ley 31112. Para el caso peruano recomendamos:

- medir el HHI por **grupo propietario** y no por marca;
- definir el mercado relevante del segmento de lujo con criterios de sustitución, no con la etiqueta "lujo";
- si se quisiera estudiar el margen del distribuidor, aplicar la misma lógica Q/M a estados financieros auditados. Euromotors, como empresa privada no listada, no los publica.

---

## Bibliografía

Asociación Automotriz del Perú. (2022). *Informe del sector automotor: a diciembre 2021*. https://aap.org.pe/storage/estadisticas/2021/Diciembre.pdf

Asociación Automotriz del Perú. (2024). *Informe del sector automotor: diciembre 2023*. https://aap.org.pe/storage/estadisticas/2023/Diciembre.pdf

Asociación Automotriz del Perú. (2026). *Informe del sector automotor: diciembre 2025*. https://aap.org.pe/storage/estadisticas/informes-mensuales/1768240598052.pdf

De Loecker, J. y Warzynski, F. (2012). Markups and firm-level export status. *American Economic Review, 102*(6), 2437–2471.

Dr. Ing. h.c. F. Porsche AG. (2014). *Annual report 2013*. https://newsroom.porsche.com/

Dr. Ing. h.c. F. Porsche AG. (2015). *Annual report 2014*. https://newsroom.porsche.com/

Farrell, J. y Shapiro, C. (1990). Horizontal mergers: An equilibrium analysis. *American Economic Review, 80*(1), 107–126.

Gonzales Quijano, J. N. (2026). *Organización Industrial: sesiones semanas 2, 3, 4, 6, 9, 10 y 11* [Diapositivas]. Universidad del Pacífico.

Hess, J. T. y Wang, X. (2026). *Measuring merger effects with revenue data* (Documentos de Trabajo N.º 2631). Banco de España. https://doi.org/10.53479/44445

MAN SE. (2012). *Annual report 2011*. https://irpages2.eqs.com/Download/Companies/MAN/Annual%20Reports/DE0005937007-JA-2011-EQ-E-00.pdf

MAN SE. (2014). *Annual report 2013*. https://irpages2.eqs.com/Download/Companies/MAN/Annual%20Reports/DE0005937007-JA-2013-EQ-E-00.pdf

MAN SE. (2015). *Annual report 2014*. https://irpages2.eqs.com/Download/Companies/MAN/Annual%20Reports/DE0005937007-JA-2014-EQ-E-00.pdf

Ley N.º 31112. Ley que establece el control previo de operaciones de concentración empresarial. *El Peruano*, 7 de enero de 2021.

Porsche Automobil Holding SE. (2012). *Annual report fiscal year 2011*. https://www.porsche-se.com/en/investor-relations/financial-publications

Salant, S. W., Switzer, S. y Reynolds, R. J. (1983). Losses from horizontal merger: The effects of an exogenous change in industry structure on Cournot-Nash equilibrium. *Quarterly Journal of Economics, 98*(2), 185–199.

Syverson, C. (2019). Macroeconomics and market power: Context, implications, and open questions. *Journal of Economic Perspectives, 33*(3), 23–43.

Tirole, J. (1988). *The theory of industrial organization*. MIT Press.

U.S. Department of Justice y Federal Trade Commission. (2023). *Merger guidelines*.

Volkswagen AG. (2009). *Annual report 2008*. https://www.volkswagen-group.com/en/publications/corporate/annual-report-2008-2326

Volkswagen AG. (2010). *Annual report 2009*. https://www.volkswagen-group.com/en/publications/corporate/annual-report-2009-2327

Volkswagen AG. (2012). *Annual report 2011*. https://www.volkswagen-group.com/en/publications/corporate/annual-report-2011-2329

Volkswagen AG. (2013). *Annual report 2012*. https://www.volkswagen-group.com/en/publications/corporate/annual-report-2012-2330

Volkswagen AG. (2015). *Annual report 2014*. https://www.volkswagen-group.com/en/publications/corporate/annual-report-2014-2332

Williamson, O. E. (1968). Economies as an antitrust defense: The welfare tradeoffs. *American Economic Review, 58*(1), 18–36.

---

## Anexos

### Anexo A. Datos

**Tabla A1. Grupo VW y Porsche AG (millones de euros, salvo indicación)**

| Entidad | Año | Ingresos | Costo de materiales | Costo de ventas | Empleados | Activos | Q/M |
|---|---|---|---|---|---|---|---|
| VW | 2009 | 105 187 | 67 925 | 91 608 | 367 000 | 177 178 | 1.549 |
| VW | 2010 | 126 875 | 79 394 | 105 431 | 389 000 | 199 393 | 1.598 |
| VW | 2011 | 159 337 | 104 648 | 131 371 | 454 000 | 253 769 | 1.523 |
| VW | 2012 | 192 676 | 122 450 | 157 522 | 533 000 | 309 518 | 1.574 |
| VW | 2013 | 197 007 | 127 089 | 161 407 | 563 000 | 324 333 | 1.550 |
| VW | 2014 | 202 458 | 132 514 | 165 934 | 583 000 | 351 209 | 1.528 |
| Porsche AG | 2011 | 10 928 | 6 822 | n.d. | 15 307 | 21 556 | 1.602 |
| Porsche AG | 2012 | 13 865 | 8 124 | 9 755 | 17 502 | 22 747 | 1.707 |
| Porsche AG | 2013 | 14 326 | 8 282 | 10 139 | 19 456 | 24 560 | 1.730 |
| Porsche AG | 2014 | 17 205 | 10 405 | 12 885 | 22 401 | 26 060 | 1.654 |

Fuentes: VW (2013, p. 189; 2015, p. 143); Porsche AG (2014, p. 117 y 130; 2015, p. 60 y 65). Empleados de VW: promedio anual; de Porsche: al 31 de diciembre. n.d.: no disponible.

**Tabla A2. Perú: participación y HHI en vehículos livianos nuevos (inscripciones SUNARP)**

| Año | Total | Marca VW | Grupo VW | HHI por marca | HHI por grupo |
|---|---|---|---|---|---|
| 2020 | 112 181 | 3.70 % | n.d. | 785–788 | 974–977 |
| 2021 | 157 100 | 4.02 % | n.d. | 760–765 | 918–923 |
| 2022 | 159 814 | 3.44 % | 3.89 % | 791–795 | 978–982 |
| 2023 | 164 485 | 2.58 % | 3.21 % | 833–839 | 1 009–1 013 |
| 2024 | 151 062 | 1.94 % | 2.54 % | 798–804 | 980–983 |
| 2025 | 186 981 | 1.97 % | 2.43 % | 770–775 | 948–951 |

Segmento de lujo:

| Año | Total | Grupo VW | Audi | Porsche | HHI por marca | HHI por grupo | ΔHHI por propiedad común VW |
|---|---|---|---|---|---|---|---|
| 2022 | 3 059 | 23.6 % | 21.4 % | 1.9 % | 1 991 | 2 334 | 96 |
| 2023 | 3 770 | 27.2 % | 23.2 % | 3.8 % | 1 888 | 2 482 | 188 |
| 2024 | 3 848 | 23.5 % | 19.2 % | 4.1 % | 1 807 | 2 254 | 169 |
| 2025 | 3 930 | 22.2 % | 17.7 % | 4.2 % | 1 815 | 2 302 | 163 |

Fuente: AAP (2022, 2024, 2026). El Grupo VW incluye Volkswagen, Audi, Porsche, Lamborghini y Bentley (sin SEAT ni Cupra, que la AAP agrupa en "Otros"). El HHI de livianos es un rango porque la AAP agrupa el resto de marcas en "Otros".

**Tabla A3. Cambios de perímetro del Grupo VW**

| Fecha | Evento | Fuente |
|---|---|---|
| 22-jul-2008 | Consolidación de Scania | VW (2009), p. 136 |
| 7-dic-2009 | VW toma el 49.9 % de Porsche (método de participación) | VW (2010), p. 121 |
| 1-mar-2011 | Consolidación de Porsche Holding Salzburg (distribuidor) | VW (2012), p. 261 |
| 9-nov-2011 | Consolidación de MAN | VW (2012), p. 264 |
| 19-jul-2012 | Adquisición de Ducati | VW (2013), p. 268 |
| 1-ago-2012 | Consolidación plena de Porsche AG | VW (2013), p. 266 |

### Anexo B. Ilustración de la Proposición 1 (TFPR)

Usamos las elasticidades de producción bruta para NACE 29 de Hess y Wang (2026, Tabla B.1): β_k = 0.267, β_l = 0.229, β_m = 0.388. Los datos son de 2011, con K = activos totales, L = empleados y M = costo de materiales.

| Variable | Valor |
|---|---|
| Participación de VW en el capital (s_K) | 0.922 |
| Participación de VW en el trabajo (s_L) | 0.967 |
| Participación de VW en los materiales (s_M) | 0.939 |
| a | 0.948 |
| b | 0.078 |
| a + b | 1.026 |
| r = Z_T/Z_A | 0.831 |
| Umbral r* = (1 − a)/b | 0.670 |
| Sesgo ln(a + r·b) | +0.0125 |

Como r > r*, el sesgo es positivo. Los resultados son ilustrativos: las elasticidades se estimaron para empresas españolas y los activos de VW incluyen su negocio financiero.

### Anexo C. Mini-modelo de Cournot (detalle)

La demanda es P = 150 − Q y los costos marginales son constantes. Las fórmulas de equilibrio son las de la semana 9: qᵢ = [a + Σc − (n + 1)cᵢ]/(n + 1).

| | Escenario A: costos (30, 30, 45); se fusionan 1 y 2 | Escenario B: costos (30, 50, 30, 30); se fusionan 1 y 2 |
|---|---|---|
| Precio pre-fusión | 63.75 | 58.00 |
| Precio post sin sinergias | 75.00 | 60.00 |
| ¿Rentable sin sinergias? | No: 2 025 < 2 278.13 (paradoja de Salant, Switzer y Reynolds) | Sí: 900 > 848 |
| Umbral de precio (Farrell-Shapiro) | c_M ≤ −3.75 (inalcanzable) | c_M ≤ 22 (−27 %) |
| Umbral de bienestar total (Williamson) | c_M ≤ 21.30 (−29 %) | No cae aun sin sinergias |
| Umbral de rentabilidad | c_M ≤ 25.91 | Rentable aun sin sinergias |

### Anexo D. Figuras y reproducibilidad

Figuras en `analisis/figuras/`:

1. Proxy de markup Q/M de VW y Porsche (2009–2014).
2. Cambio estimado del markup según especificación.
3. Consolidación virtual con ajustes de perímetro (sin MAN; sin MAN ni ventas intragrupo).
4. Umbrales de Cournot.
5. Participación del Grupo VW en livianos en el Perú.
6. Segmento de lujo 2025.
7. HHI en el tiempo.

Para reproducir todo: `bash analisis/correr_todo.sh`. El ajuste por MAN usa las cifras de MAN SE. Para 2011 aproxima los dos meses de MAN dentro de VW con la razón Q/M de MAN de ese año. Los escenarios con razones Q/M hipotéticas para MAN están en `analisis/resultados/porsche_sens_man.csv`.
