# Preguntas probables y respuestas breves

Cada integrante debe poder responder **todas**. Las cifras provienen de `analisis/resultados/` y las secciones citadas son de Hess y Wang (2026).

---

**1. ¿Cuál es la pregunta del artículo y cuál es su aporte principal?**
La pregunta es si las fusiones elevan la eficiencia (TFPR) o el poder de mercado (markups) de la empresa fusionada. El aporte es de medición: con estados financieros, la adquirida deja de reportar, así que comparar al adquirente antes con el grupo después mezcla desempeño con un cambio de perímetro. La consolidación virtual suma ambas empresas antes de la fusión. Sin esa corrección, los dos efectos cambian de signo (sección 4.4).

**2. ¿Por qué basta Q/M para medir cambios del markup sin estimar la función de producción?**
Con Cobb-Douglas, la elasticidad de los materiales es una constante β_m, y μ = β_m · Q/M (ec. 7). Al tomar logaritmos, ln μ = ln β_m + ln(Q/M), así que la constante desaparece al restar: Δ ln μ = Δ ln(Q/M). El nivel sí depende de β_m. Con la β_m que el artículo estima para fabricantes españoles (0.388), VW tendría un "markup" de 0.59 < 1, señal de que el nivel no es interpretable en nuestro caso.

**3. ¿Qué diferencia hay entre TFPR y TFPQ y por qué importa?**
La TFPQ mide cuántas unidades físicas se producen por unidad de insumos; la TFPR mide cuánto ingreso. Si una fusión sube precios sin mejorar la tecnología, la TFPR sube igual. Por eso el artículo admite que no puede separar eficiencia de poder de mercado con datos de ingresos (sección 6). Solo argumenta indirectamente: si la TFPR subiera por puro precio, debería moverse junto con el markup en cada industria, y no lo hace.

**4. Expliquen el sesgo de frontera con una fórmula.**
El markup del grupo consolidado es el promedio de los markups individuales ponderado por costo de materiales: μ_pool = w_A μ_A + w_T μ_T. Por tanto, μ_pool − μ_A = w_T (μ_T − μ_A) (sección 3.3.2). En VW–Porsche: w_T = 6.1 % y x_T − x_A = 1.602 − 1.523, de modo que el término vale +0.0049 en Q/M, o +0.32 puntos log.

**5. ¿Por qué en su caso el sesgo es positivo y en el artículo negativo?**
Porque su signo depende solo de quién tiene el markup más alto. En España las adquiridas suelen tener markup menor que el adquirente. Porsche, como marca premium, tenía un Q/M más alto que VW. Es la misma fórmula con un signo distinto en este caso.

**6. ¿Qué dice la Proposición 2 y por qué el efecto es tan pequeño en su caso?**
Ponderar los markups previos por ventas da un número mayor que ponderar por costo, por la desigualdad de Jensen: μ = β_m/c es convexa en el costo unitario c = M/Q. Si el "antes" se arma con pesos por ventas y el "después" (consolidado) pondera implícitamente por costo, aparece una caída espuria. En nuestro caso es −0.02 puntos log, porque Porsche pesa poco y los costos unitarios de ambas empresas se parecen (0.62 frente a 0.66). Jensen solo importa cuando los costos unitarios difieren mucho.

**7. ¿Por qué usan 2011 como "antes" y no 2012?**
VW consolidó Porsche el 1-ago-2012, así que 2012 incluye solo 5 meses de Porsche y mezcla los dos regímenes. Entre dic-2009 y jul-2012, Porsche AG se registraba por el método de participación tanto en VW como en Porsche SE, y su costo de materiales solo aparece públicamente para 2011, en el reporte 2013 de Porsche AG. Por eso: antes = 2011, después = 2013–2014.

**8. ¿Cómo afecta MAN a la comparación?**
MAN se consolidó el 9-nov-2011 (unos 2 meses en 2011, el año completo en 2013) y tiene un Q/M alto, alrededor de 1.8. Al entrar, sube mecánicamente el Q/M del grupo: es el mismo sesgo de frontera, causado por otra adquisición. Al restarla, el cambio virtual pasa de +1.48 % a +0.50 % (2013) y de +0.02 % a −0.93 % (2014). Para 2011 aproximamos los 2 meses de MAN con su razón Q/M anual: es una limitación declarada.

**9. ¿Por qué no usaron la división Automotive o Passenger Cars?**
VW publica por segmento los ingresos y el resultado operativo, pero **no el costo de materiales**, así que no podemos calcular Q/M por división. Por eso restamos MAN usando los reportes de MAN SE.

**10. ¿Por qué no usaron la capitalización de mercado o la reacción de las acciones?**
Porque responde otra pregunta: mide cuánto valor *esperan* los accionistas, no si el markup o la productividad cambiaron. Además mezcla poder de mercado, sinergias, expectativas y condiciones financieras. En este caso estaba contaminada por la toma de control: Porsche SE llegó a la mayoría de los votos de VW el 5-ene-2009 (Porsche SE, reporte 2008/09) y la ley VW (VW-Gesetz) limitaba los derechos de voto (VW, reporte 2008). El artículo trabaja con estados financieros de la empresa, y nosotros seguimos su método.

**11. ¿Qué son las ventas intragrupo y por qué importan?**
En 2013, el 8 % de los ingresos de Porsche fueron ventas a otras empresas de VW, probablemente distribuidores propios. Antes de 2012 ese monto era ingreso de Porsche y compra de VW; al consolidar se elimina. Si eliminamos la misma proporción en 2011, el cambio virtual baja a +1.2 % (2013). Esto matiza el artículo: sumar dos estados financieros que comercian entre sí no reproduce exactamente la consolidación.

**12. Entonces, ¿la integración de Porsche generó eficiencia o poder de mercado?**
Con estos datos no podemos afirmar ninguna de las dos. Una vez limpio el perímetro, el markup del grupo no cambió de forma distinguible de su variación anual normal, y la TFPR no separa precio de eficiencia. El Q/M de Porsche sí subió de 1.60 a 1.73 entre 2011 y 2013, lo que es compatible con compras conjuntas con VW (menor costo; Porsche SE, reporte 2011) o con precios y mezcla de modelos (más Cayenne y la nueva Boxster/Cayman). Además la integración venía desde 2009, cuando Porsche SE ya tenía el 50.73 % de los votos de VW.

**13. ¿Qué dice el modelo de Cournot sobre cuánta eficiencia hace falta?**
La condición de Farrell-Shapiro para que el precio no suba es c_M ≤ c₁ + c₂ − P_pre. Con los datos de la semana 9 (P = 150 − Q; costos 30, 30, 45), el umbral es −3.75: imposible, el precio sube siempre (de 63.75 a 75 sin sinergias). El bienestar total no cae si c_M ≤ 21.3, el trade-off de Williamson. Si un socio grande y eficiente absorbe a uno pequeño (costos 30 y 50), basta c_M ≤ 22, una reducción de 27 %. Lo que importa es quién se fusiona.

**14. ¿El Grupo VW tiene poder de mercado en el Perú?**
En livianos, no en términos estructurales: tiene 2.4 % en 2025 y el HHI por grupo es ≈950 (poco concentrado). En el segmento de lujo sí tiene una posición relevante: 22.2 %, con HHI por grupo de 2 302, segundo detrás de BMW Group (35 %). Con L = HHI/ε el Lerner implícito del segmento de lujo estaría entre 0.05 y 0.15 si ε va de 5 a 1.5, pero no estimamos ε: es ilustrativo.

**15. Si Audi y Porsche se fusionaran hoy en el Perú, ¿Indecopi tendría que revisarlo?**
No. Pertenecen al mismo grupo y la Ley 31112 excluye las operaciones "al interior del mismo grupo económico" (art. 6.2.a). Además, el control previo solo aplica si las ventas o activos **en el país** superan 118 000 UIT en conjunto y 18 000 UIT para al menos dos partes (art. 6.1). Como ejercicio contrafactual con empresas independientes, el ΔHHI sería ≈148 y el HHI 2 302, por encima de los umbrales de presunción de las Merger Guidelines 2023, siempre que el "segmento de lujo" fuera el mercado relevante, lo cual es dudoso.

**16. ¿Por qué VW usa un importador independiente en el Perú si en otros países compró a sus distribuidores?**
Integrarse verticalmente elimina la doble marginalización y el riesgo de *hold-up*, pero tiene costos fijos y exige conocimiento local. VW compró Porsche Holding Salzburg (2011) y KPI Polska (2012, "importador y distribuidor exclusivo"), que operan en mercados grandes. En un mercado pequeño como el peruano (unas 4 500 unidades del grupo en 2025), un importador multimarca reparte los costos fijos entre varias marcas (economías de alcance). No conocemos los contratos de Euromotors, así que esto es una interpretación teórica.

---

### Preguntas "trampa" a tener presentes

- **"Su resultado contradice el artículo."** No. El artículo mide un promedio sobre 3 759 fusiones españolas. Nosotros aplicamos sus fórmulas a un caso con una adquirida de markup alto, y el signo distinto es justamente lo que la fórmula predice.
- **"¿Su +1.5 % es el efecto de la fusión?"** No. Es un antes-después sin grupo de control y, una vez limpio el perímetro, prácticamente desaparece.
- **"¿El HHI prueba poder de mercado?"** No. Es un indicador estructural de baja capacidad predictiva (semana 11). Además depende de la definición de mercado y de medir por grupo y no por marca.
