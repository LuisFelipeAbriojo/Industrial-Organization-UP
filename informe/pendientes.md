# Pendientes y verificaciones abiertas

Última actualización: Fase 4 (22-oct-2026). Todos los scripts se volvieron a correr desde cero (`bash analisis/correr_todo.sh`) y las **110 cifras** que revisa `analisis/verificar_informe.py` coinciden con el informe, el guion y las preguntas.

## 1. Lo que no pudimos verificar o es aproximado (decirlo si preguntan)

| Tema | Situación | Dónde se usa |
|---|---|---|
| Costo de materiales de **MAN para nov–dic 2011** | VW no lo publica. Se aproxima aplicando a los ingresos de MAN dentro de VW en 2011 (€2 652 M) la razón Q/M anual de MAN SE en 2011 (1.77). | Informe c.4 (3); figura 3 |
| **Ventas intragrupo de Porsche en 2011** | No se publican. Se asume la misma proporción observada en 2013 (8.0 % de los ingresos de Porsche). Es una sensibilidad, no un dato. | Informe c.4 (4); figura 3 |
| **Costo de materiales de Porsche AG 2009–2010 y costo de ventas 2011** | No encontramos fuente pública: Porsche AG estuvo en método de participación entre dic-2009 y jul-2012. Por eso el "antes" es solo 2011. | Informe c.2 |
| **Empleados** | VW reporta promedio anual; Porsche AG reporta empleados al 31 de diciembre. Solo afecta la ilustración de TFPR (Anexo B). | Anexo B |
| **Elasticidades β** | Son las de NACE 29 estimadas por Hess y Wang para España (Tabla B.1), no para VW. Solo se usan como ilustración (TFPR) y para mostrar que el nivel del markup no es interpretable. | c.4 (5) y (6); Anexo B |
| **Grupos propietarios fuera de VW** (Hyundai–Kia, Toyota–Lexus, BMW–Mini, Geely–Volvo, Stellantis, JLR) | Se tomaron de conocimiento general y no se verificaron en fuente primaria (ver `data/grupos_propietarios.csv`, columna `verificado`). Afectan el HHI "por grupo". El HHI por marca no depende de esto. | Tabla A2; figuras 6–7 |
| **Definición de "segmento de lujo" de la AAP** | La AAP no explica qué marcas incluye ni con qué criterio. No es un mercado relevante en sentido antimonopolio. | c.5 |
| **SEAT y Cupra en el Perú** | Están dentro de "Otros" en livianos, así que la participación del Grupo VW en livianos es una **cota inferior**. | c.5; Tabla A2 |
| **Contratos de Euromotors** (exclusividad, territorios, precios) | No hay información pública. La sección c.6 es interpretación teórica, y el informe lo dice. | c.6 |
| **Inicio del régimen de la Ley 31112** (14-jun-2021, D.S. 039-2021-PCM) | Viene de fuentes secundarias; el texto de la ley solo dice "15 días calendario después de la adecuación normativa". No se usa en el informe. | `data/fuentes.md` |
| **ARAPER** | El sitio no respondió (error 502). Se usó solo la AAP, con los mismos datos de SUNARP. | — |
| **Referencias académicas de la bibliografía** (Williamson 1968; Farrell y Shapiro 1990; Salant, Switzer y Reynolds 1983; De Loecker y Warzynski 2012; Syverson 2019; Tirole 1988; Merger Guidelines 2023) | Citadas de memoria: revisar volumen y páginas antes de entregar. Los datos del paper de Hess y Wang sí se verificaron contra el PDF. | Bibliografía |

## 2. Antes de entregar (grupo)

1. **Extensión.** El cuerpo del informe (secciones a–d, con las tablas de c.3) tiene unas 4 200 palabras. En Word, con Calibri 11 e interlineado sencillo, debería quedar en unas 7.5–8 páginas. Si se pasa, recortar primero c.4 (6) (TFPR) y el detalle de c.6. El Anexo B y el C ya están fuera del cuerpo.
2. **Pasar a Word/PDF** e insertar las figuras de `analisis/figuras/` donde el texto las menciona, o como anexo.
3. **Armar el PowerPoint** con `informe/slides_outline.md` (6 slides).
4. **Repartir y ensayar** `informe/preguntas_probables.md`: cada integrante debe poder responder todas.
5. **GitHub:** el push a `claude/youthful-brahmagupta-bwtxf8` falló con error 403 (la app de Claude no tiene acceso al repositorio). Los commits están hechos localmente. Hay que reconectar GitHub en https://claude.ai/connect-github y volver a hacer push. El repositorio es **público**: el material del curso (slides y lineamientos) está excluido en `.gitignore`.
