---
template: page.html
---

\begin{reviewer}
{Yanina Bellini Saibene}
{María Dermit y	Yuriko Sosa}
\end{reviewer}

> Si usas robots para enseñar, les enseñas a las personas a ser robots.<br/>
> --- atribuido a varias personas

La tecnología ha cambiado la enseñanza y el aprendizaje muchas veces.
Antes de que se introdujeran los pizarrones en las escuelas a principios del siglo XIX,
no había forma de que las/los docentes compartieran un ejemplo improvisado,
un diagrama
o que trabajaran en un ejercicio con toda la clase a la vez.
Barato,
de confianza,
fácil de usar
y flexible,
los pizarrones permitieron a las/los docentes hacer cosas rápidamente y a gran escala,
que antes solo habían podido hacer lentamente y poco a poco.
De forma similar,
las cámaras de video portátiles revolucionaron el entrenamiento atlético;
al igual que las grabadoras revolucionaron la enseñanza musical una década antes.

Muchas de las personas que introducen internet en las aulas no conocen esta historia
y no se dan cuenta de que el suyo es solo el último de
[una larga serie de intentos][k0081]
de utilizar máquinas para enseñar <cite>Watt2014</cite>.
Desde la imprenta, pasando por la radio y la televisión,
a computadoras de escritorio y dispositivos móviles,
cada nueva forma de compartir conocimientos ha producido una ola de optimistas agresivos
que creen que la educación no funciona y que la tecnología puede arreglarlo.

Sin embargo,
las/los defensoras/es más acérrimas/os de la tecnología de la educación a menudo han sabido menos sobre "educación" que sobre "tecnología".
Detrás de su retórica,
muchas de estas personas han sido impulsadas más por la perspectiva de ganancias
que por el deseo de empoderar a las/los estudiantes.

El debate actual a menudo se enturbia al confundir "en línea" con "automatizado".
Si se realiza bien,
una docena de personas resolviendo un problema en un chat de video
se siente como cualquier otra discusión en grupos pequeños.
Por el contrario,
un escuadrón de ayudantes de enseñanza que califican cientos de trabajos con una rúbrica inflexible
bien podría ser una colección de scripts de Perl.<span i="Perl (referencia despectiva a)"></span>
Por lo tanto, este capítulo comienza con la instrucción en línea totalmente automatizada,
usando videos grabados y ejercicios calificados automáticamente,
y luego explora algunos modelos híbridos alternativos.

## Cursos masivos en línea {#online-moocs}

El esfuerzo de más alto perfil para reinventar la educación usando internet
son los <span g="mooc">cursos masivos en línea</span>{curso masivo en línea} (en inglés *Massive Open Online Course*), o *MOOC*.
El término fue inventado por David Cormier en 2008<span i="Cormier, David"></span>
para describir un curso organizado por George Siemens<span i="Siemens, George"></span>
y Stephen Downes.<span i="Downes, Stephen"></span>
Ese curso se basó en una visión <span g="connectivism" i="conectivismo">conectivista</span> del aprendizaje,
que sostiene que el conocimiento se distribuye
y el aprendizaje es el proceso de encontrar, crear y podar conexiones.

El término "MOOC" fue rápidamente cooptado por las/los creadores de
cursos semejantes al modelo de disertación de un aula tradicional:
una/un docente como el centro definiendo los objetivos
y estudiantes que se conciben como recipientes o replicadores de conocimientos.
Las clases que utilizan el modelo conectivista original se suelen denominar "cMOOCs,"
mientras que las clases que centralizan el control se llaman "xMOOCs."
(A este último también se le llama a veces un " MESS " (la palabra *mess* significa *lío* en inglés),
por las siglas Sabio Masivamente Realzado en el Escenario (*Massively Enhanced Sage on the Stage*, en inglés.))

Cinco años atrás,
no se podía caminar por los campus de las universidades más grandes
sin escuchar a alguien hablando sobre cómo los MOOCs revolucionarían la educación,
la destruirían
o posiblemente ambas cosas.
Los MOOCs le darían a las/los estudiantes acceso a un gran abanico de cursos
y les permitirían trabajar cuando les fuera conveniente
en lugar de acomodar su aprendizaje a la agenda de otra persona.

Pero los MOOCs no han sido tan efectivos
como predijeron sus defensoras/es más entusiastas <cite>Ubel2017</cite>.
Una razón es que
el contenido grabado es ineficaz para muchas personas principiantes
porque no puede aclarar los conceptos erróneos individuales (<a section="models"/>):
si no entienden una explicación la primera vez,
por lo general, no hay una explicación alternativa para ofrecer.
Otra razón es que la evaluación automatizada necesaria para lograr lo "masivo" en este tipo de cursos
solo funciona bien en los niveles más bajos
de la taxonomía de Bloom (<a section="process-objectives"/>).<span i="taxonomía de Bloom"></span>
Ahora también está claro que
las/los estudiantes tienen que soportar mucho más la carga de mantenerse concentrados en un MOOC,
que la impersonalidad de trabajar en línea puede fomentar un comportamiento descortés y desmotivar a las personas
y que "disponible para todos" significa en realidad
"disponible para todo el mundo lo suficientemente pudiente como para tener internet de alta velocidad y mucho tiempo libre".

<cite>Marg2015</cite> examinaron 76 MOOCs sobre varios temas y descubrieron que,
si bien la organización y presentación del material fue buena,
la calidad del diseño de las lecciones fue deficiente.
Con temáticas más afines a las de este libro,
<cite>Kim2017</cite> estudió treinta tutoriales en línea populares sobre programación
y descubrió que en gran medida enseñaban el mismo contenido de la misma manera:
de abajo hacia arriba,
comenzando con conceptos de programación de bajo nivel y avanzando hacia metas de alto nivel.
La mayoría de los tutoriales requería que las/los estudiantes escribieran programas y proporcionaron algún tipo de retroalimentación inmediata,
pero esta retroalimentación fue típicamente muy superficial.
Pocos tutoriales explicaban cuándo y por qué los conceptos son útiles
(es decir, no mostraban cómo transferir conocimientos),
o proporcionaban orientación para errores comunes.
Más allá de una diferenciación rudimentaria basada en la edad,
ninguna lección se personalizaba en base a la experiencia previa en programación o en los objetivos de las/los estudiantes.

> ### Aprendizaje personalizado
>
> Pocos términos han sido utilizados y abusados de tantas formas
> como <span g="personalized-learning">aprendizaje personalizado</span>.
> Para la mayoría de las/los defensores de la educación con tecnología,
> significa ajustar dinámicamente el ritmo de las lecciones en función del rendimiento de cada estudiante,
> de modo que si alguien responde varias preguntas seguidas correctamente,
> la computadora omitirá algunas de las siguientes preguntas.
>
> Hacer esto puede producir
> [modestas mejoras][k0082],
> pero hay aproximaciones más convenientes.
> Por ejemplo,
> si muchas/os estudiantes encuentran difícil un tema en particular,
> la/el docente puede preparar múltiples explicaciones alternativas de ese punto
> en lugar de acelerar un solo camino.
> De esa manera,
> si una explicación no resuena,
> otras están disponibles.
> Sin embargo,
> esto requiere mucho más trabajo de diseño por parte de quien enseña,
> lo que puede ser la razón por la que no ha demostrado su popularidad.
> Incluso si funciona,
> es probable que los efectos sean mucho menores de lo que creen algunas/os de sus defensores.
> En la escuela primaria,
> puede haber diferencias de 0.1 a 0.15 desviaciones estándar en el desempeño de fin de año debido a buenas/os docentes.
> <cite>Chet2014</cite>
> (ver [este artículo][k0083] para un breve resumen).
> No es realista creer que esto puede ser superado en el corto plazo por cualquier tipo de automatización.

Entonces, ¿cómo se *debe* usar internet para enseñar y aprender habilidades tecnológicas?
Sus pros y contras son:<span i="aprendizaje en línea!pros y contras de"></span>

Las/los estudiantes pueden acceder a más lecciones y más rápido que nunca antes
: Obviamente,
  suponiendo
  que un motor de búsqueda considere que vale la pena indexar esas lecciones,
  que su proveedor de servicios de internet y el gobierno no lo bloqueen,
  y que la verdad no se ahogue en un mar de desinformación que agota la atención.

Las/los estudiantes pueden acceder a *mejores* lecciones que nunca antes,
: a menos que estén siendo dirigidas/os hacia material de segunda categoría,
  para redistribuir la riqueza de las personas que no tienen, a las personas que sí tienen <cite>McMi2017</cite>.
  También vale la pena recordar que la escasez aumenta el valor percibido,
  por lo que a medida que la educación en línea sea más barata
  se convertirá cada vez más en lo que todo el mundo quiere para las/los hijas/os de otra persona.

Las/los estudiantes también pueden acceder a muchos más contactos que nunca.
: Pero solo si esas/os estudiantes realmente tienen acceso a la tecnología requerida,
  pueden permitirse usarla
  y no son excluidas/os por acoso o marginadas/os
  por no ajustarse a las normas sociales del grupo que lleve la voz cantante.
  En la práctica,
  la mayoría de las/los usuarias/os de MOOC proviene de entornos seguros y de buen nivel adquisitivo <cite>Hans2015</cite>.

Las/los docentes pueden obtener información mucho más detallada sobre cómo trabajan sus estudiantes.
: Siempre que las/los estudiantes hagan cosas que sean susceptibles de análisis automatizado a gran escala
  y no se opongan a la vigilancia en el aula
  o no sean lo suficientemente poderosas/os como para que sus objeciones importen.

<cite>Marg2015,Mill2016a,Nils2017</cite> describen formas de acentuar los aspectos positivos en la lista anterior
evitando los negativos:

Haz que los plazos sean frecuentes y bien publicitados,
: y aplícalos para que tus estudiantes entren en ritmo de trabajo.

Manten al mínimo las actividades sincronizadas de todas las clases, como conferencias en vivo
: para que las personas no se pierdan cosas debido a conflictos de agenda.

Haz que tus estudiantes contribuyan al conocimiento colectivo,
: p. ej. tomar notas compartidas (<a section="classroom-notetaking"/>),
  servir como escribas en el aula
  o contribuir con problemas a conjuntos de problemas compartidos (<a section="individual-peer"/>).

Anima o solicita a tus estudiantes que realicen parte de su trabajo en grupos pequeños,
: los cuales *sí* tienen actividades sincrónicas en línea, como por ejemplo una discusión semanal.
  Esto ayuda a las/los estudiantes a mantener su compromiso y motivación sin crear demasiados problemas de agenda.
  (Ver el <a section="meetings"/> para obtener algunos consejos sobre cómo hacer que estas discusiones sean justas y productivas.)

Crea, publicita y haz cumplir un código de conducta.
: para que toda la clase pueda participar en los debates en línea (<a section="classroom-coc"/>).

Utiliza muchas lecciones breves en lugar de pocos fragmentos largos al estilo conferencias
: para minimizar la carga cognitiva
  y brindar muchas oportunidades para la evaluación formativa.
  Esto también ayuda con el mantenimiento de las lecciones:
  si todos tus videos son cortos,
  simplemente puedes volver a grabar cualquiera que necesite actualización,
  lo que a menudo es más barato que intentar arreglar videos largos.

Usa videos para fomentar la participación en lugar de instruir.
: Dejando de lado las discapacidades (<a section="motivation-accessibility"/>),
  las/los estudiantes pueden leer más rápido de lo que tú puedes hablar.
  La excepción a esta regla es que
  el video es la mejor manera de enseñar verbos (acciones):
  grabaciones breves de tu pantalla que muestran cómo usar un editor,
  cómo recorrer el código en un depurador,
  y así sucesivamente, son más eficaces que las capturas de pantalla con texto.

Identifica y aclara tempranamente conceptos erróneos.
: Si los datos muestran que las/los estudiantes tienen dificultades con algunas partes de una lección,
  crea explicaciones alternativas de esas partes
  y ejercicios adicionales para que practiquen.

Todo esto tiene que ser implementado de alguna manera,<span i="aprendizaje en línea!implementación de"></span>
lo que significa que necesitas alguna clase de plataforma de enseñanza.
Puedes utilizar tanto un <span g="lms">sistema de gestión del aprendizaje</span> (*learning management system*, en inglés) todo en uno
como [Moodle][k0084] o [Sakai][k0085],
o generar uno por tu cuenta
usando [Slack][k0086] o [Zulip][k0087] para el chat,
[Google Hangouts][k0088]
o [appear.in][k0089] para videoconferencias,
y [WordPress][k0090],
[Google Docs][k0120],
o cualquier número de sistemas wiki para la autoría colaborativa.
Si recién estás comenzando,
elige lo que sea más fácil de configurar y administrar
y lo que sea más familiar para tus estudiantes.
Si te enfrentas a una elección,
la segunda consideración es más importante que la primera:
esperas que las personas aprendan mucho en tu clase,
por lo que es justo que tú aprendas a manejar las herramientas con las que se sientan más cómodas.

Montar una plataforma para el aprendizaje es necesario pero no suficiente:
si quieres que tus estudiantes prosperen,
necesitas crear una comunidad.
Cientos de libros y presentaciones hablan sobre cómo hacer esto,
pero la mayoría se basan en las experiencias personales de sus autores.
<cite>Krau2016</cite> es una excepción bienvenida:
si bien es anterior al descenso acelerado de Twitter y Facebook hacia el abuso y la desinformación,
la mayoría de sus hallazgos siguen siendo relevantes.
<cite>Foge2005</cite> también está lleno de consejos útiles
sobre comunidades de práctica a las que las/los estudiantes pueden desear unirse;
exploramos algunas de sus ideas en el <a section="community"/>.

> ### Libertad para, libertad de
>
> El ensayo de 1958 de Isaiah Berlin<span i="Berlin, Isaiah"></span>
> ["Dos conceptos de libertad"][k0092]
> hizo una distinción entre [libertad positiva][k0093],
> que es la capacidad de hacer algo,
> y [libertad negativa][k0094],
> que es la ausencia de reglas que digan que no puedes hacerlo.
> Las discusiones en línea generalmente ofrecen libertad negativa
> (nadie te impide decir lo que piensas),
> pero no libertad positiva
> (muchas personas no pueden ser escuchadas, en realidad).
> Una forma de abordar esto es introducir algún tipo de limitación,
> como permitir que cada estudiante contribuya con un mensaje por hilo de discusión al día.
> Hacer esto les da a aquellas/los que tienen algo que decir la oportunidad de decirlo,
> mientras deja espacio para que otras/os también digan cosas.

Otra preocupación que se tiene sobre la enseñanza en línea es la posibilidad de que las/los estudiantes hagan trampa.
La deshonestidad del día a día no es más común en las clases en línea que en los entornos presenciales <cite>Beck2014</cite>,
pero la tentación de que otra persona escriba el examen final
y la dificultad de comprobar si esto realmente sucedió,
es una de las razones por las que las instituciones educativas se han mostrado reacias a ofrecer créditos para las clases solamente en línea.
Es posible supervisar el examen a distancia,
pero antes de invertir en esto,
lee <cite>Lang2013</cite>:
explora por qué y cómo las/los estudiantes hacen trampa,
y cómo se pueden estructurar los cursos para evitar darles una razón para hacerlo.

## Video {#online-video}

Una característica destacada de la mayoría de los MOOC es el uso de clases grabadas en video.
Estos videos pueden ser efectivos:
como se menciona en el <a section="performance"/>,
una técnica de enseñanza llamada instrucción directa<span i="instrucción directa"></span>
basada en la entrega precisa de un guión bien diseñado ha demostrado repetidamente su eficacia <cite>Stoc2018</cite>.
Sin embargo,
los guiones para la instrucción directa deben diseñarse,
probarse
y perfeccionarse con mucho cuidado,
lo que es una inversión que muchos MOOC no han querido o no han podido hacer.
Hacer un pequeño cambio en una página web o en una plataforma de diapositivas solo toma unos minutos;
hacer incluso un pequeño cambio en un video corto lleva una hora o más,
por lo que el costo de actuar en base a los comentarios puede ser insoportable para la/el docente.
Incluso cuando están bien hechos,
los videos deben combinarse con actividades para que sean beneficiosos:
<cite>Koed2015</cite> estimaron que
"… hacer tareas extra tiene un beneficio sobre el aprendizaje … seis veces mayor que mirar o leer extra."

Si estás enseñando programación,
puedes usar grabaciones de pantallas en lugar de diapositivas,<span i="grabación de pantalla"></span>
ya que ofrecen algunas de las mismas ventajas que la programación en vivo (<a section="performance-live"/>).
<cite>Chen2009</cite> ofrecen consejos útiles para crear y criticar grabaciones de pantallas y otros videos; la
<a figure="f:online-screencasting"/> (de <cite>Chen2009</cite>) reproduce los patrones que presenta el papel
y las relaciones entre ellos.
(También es un buen ejemplo de mapa conceptual (<a section="memory-concept-maps"/>).)

<figure id="f:online-screencasting">
  <img src="screencast.svg" alt="Patrones para grabaciones de pantalla"/>
  <figcaption>Patrones para grabaciones de pantalla</figcaption>
</figure>

Entonces, ¿qué hace que un video instructivo sea efectivo?
<cite>Guo2014</cite> midieron el compromiso y participación, observando cuánto tiempo las/los estudiantes vieron los videos de MOOCs,
y encontraron que:

- Los videos más cortos son mucho más atractivos; los videos no deben durar más de seis minutos.

- Una cabeza parlante superpuesta a las diapositivas es más atractiva que solo una voz en off.

- Los videos que se sienten personales pueden ser más atractivos que las grabaciones de estudio de alta calidad,
  por lo que filmar en entornos informales podría funcionar mejor que filmar en un estudio profesional por un costo menor.

- Dibujar en una tableta es más atractivo que las diapositivas de PowerPoint o las grabaciones de pantalla con código,
  aunque no está claro si esto se debe al movimiento y la informalidad
  o porque reduce la cantidad de texto en la pantalla.

- Está bien que las/los docentes hablen bastante rápido siempre que estén entusiasmados.

Una cosa que  <cite>Guo2014</cite> no abordaron es el problema del huevo y la gallina:
¿las/los estudiantes encuentran cierto tipo de video atractivo porque están acostumbrados?
Entonces, ¿producir más videos de ese tipo aumentará la participación simplemente debido a un ciclo de retroalimentación?
¿O estas recomendaciones reflejan algunos procesos cognitivos más profundos?
Otra cosa que este documento no analizó son los resultados del aprendizaje:
sabemos que las evaluaciones de las/los estudiantes de los cursos no se correlacionan con el aprendizaje <cite>Star2014,Uttl2017</cite>,
y si bien es plausible que las/los estudiantes no aprendan de las cosas que no ven,
queda por demostrar que *aprenden* de las cosas que *ven*.

> ### Estoy un poco incómoda/o
>
> La investigación de <cite>Guo2014</cite> fue aprobada por una junta universitaria de ética en investigación,
> las/los estudiantes cuyos hábitos de visualización fueron monitoreados casi con certeza hicieron clic en "aceptar"
> en un acuerdo de términos de servicio en algún momento,
> y me alegra tener estos nuevos conocimientos.
> Por otra parte,
> la palabra "privacidad" no apareció en el título o en el resumen
> de *ninguna* de las decenas de artículos o posters en la conferencia donde se presentaron estos resultados.
> Si pudiera elegir,
> preferiría no saber qué tanto compromiso tenían los estudiantes en vez de fomentar la vigilancia ubicua en el aula.

Hay muchas formas diferentes de grabar lecciones en video;
para saber cuáles son más eficaces,
<cite>Mull2007a</cite> asignó 364 estudiantes de física de primer año
a los tratamientos multimedia en línea de la Primera y Segunda Ley de Newton en uno de cuatro estilos:

Exposición:
: presentación concisa al estilo de una clase magistral.

Exposición extendida:
: igual que la anterior, pero con información adicional interesante.

Refutación:
: Exposición con conceptos erróneos comunes explícitamente declarados y refutados.

Diálogo:
: Discusión estudiante-docente del mismo material que en la Refutación.

Refutación y diálogo produjeron los mayores beneficios de aprendizaje en comparación con la exposición;
las/los estudiantes con pocos conocimientos previos se beneficiaron más
y quienes tenían un alto conocimiento previo no estuvieron en desventaja.
De nuevo,
esto destaca la importancia de abordar directamente los conceptos erróneos de tus estudiantes.
No solo le digas a las personas lo que *es*:
diles también qué *no es* y por qué no.

## Modelos híbridos {#online-hybrid}
<span i="enseñanza híbrida"></span>

La enseñanza totalmente automatizada es solo una forma de utilizar la web en la enseñanza.
En la práctica,
casi todo el aprendizaje en las sociedades prósperas tiene actualmente un componente en línea,
ya sea oficialmente
o a través de canales de comunicación persona a persona y búsquedas encubiertas de respuestas a preguntas sobre la tarea.
La combinación de instrucción en vivo y automatizada permite a las/los docentes usar las fortalezas de ambas modalidades.
En un aula tradicional,
la/el docente puede responder preguntas de inmediato,
pero sus estudiantes necesitan días o semanas para recibir comentarios sobre sus ejercicios de programación.
En línea,
una/un estudiante puede tardar más en obtener una respuesta,
pero puede obtener comentarios inmediatos sobre el código que programó
(y al menos para ese tipo de ejercicios podemos calificar automáticamente).

Otra diferencia es que
los ejercicios en línea deben ser más detallados
porque tienen que anticiparse a las preguntas de las/los estudiantes.
Encuentro que las lecciones en persona comienzan con la intersección de lo que todo el curso necesita saber y se expanden a pedido,
mientras que las lecciones en línea deben incluir la unión de lo que todas las personas necesitan saber
porque la/el docente no está ahí para hacer esta expansión.

En realidad,
la distinción entre en línea y presencial ahora es menos importante para la mayoría de las personas
que la distinción entre sincrónico y asincrónico:
¿docentes y estudiantes interactúan en tiempo real?
¿O su comunicación se extiende e intercala con otras actividades?
En persona casi siempre la interacción será sincrónica,
pero en línea es, cada vez más, una mezcla de ambas:

> Creo que nuestras/os nietas/os probablemente considerarán la distinción que hacemos
> entre lo que llamamos el mundo real y lo que ellas/os consideran simplemente el mundo
> como la cosa más pintoresca e incomprensible sobre nosotras/os.<br/>
> --- William Gibson<span i="Gibson, William"></span>

La implementación más popular de este futuro combinado hoy
es el <span g="flipped-classroom">aula invertida</span>,
en el que las/los estudiantes ven lecciones grabadas por su cuenta
y el tiempo de la clase se utiliza para discutir y resolver conjuntos de problemas.
Descripto originalmente en <cite>King1993</cite>,
la idea se popularizó como parte de la instrucción entre pares (<a section="classroom-peer"/>)
y se ha estudiado intensamente durante la última década.
Por ejemplo,
<cite>Camp2016</cite> comparó a estudiantes que tomaron una clase de introducción a la informática en línea
con quienes la tomaron en un aula invertida.
La finalización de ejercicios de práctica (sin marcar) se correlacionó con los puntajes de los exámenes para ambos grupos,
pero la tasa de finalización de los ejercicios de ensayo por parte de las/los estudiantes en línea
fue significativamente más baja que las tasas de asistencia a clase para las/los estudiantes presenciales.

Pero si hay grabaciones disponibles,
¿seguirán asistiendo las/los estudiantes a las clases para hacer ejercicios de práctica?
<cite>Nord2017</cite> examinó el impacto de las grabaciones en la asistencia a las clases
y al desempeño de las/los estudiantes en diferentes niveles.
En la mayoría de los casos, el estudio no encontró consecuencias negativas al hecho de hacer disponibles las grabaciones;
en particular,
las/los estudiantes no se saltaron las clases cuando las grabaciones estaban disponibles
(al menos, no más de lo que suelen faltar).
Los beneficios de proporcionar grabaciones fueron mayores para las/los estudiantes al principio de sus carreras,
pero disminuyeron a medida que las/los estudiantes avanzaban.

Otro modelo híbrido es aquel que lleva al aula la vida en línea.
Tomar notas en conjunto es un primer paso (<a section="classroom-notetaking"/>);
agrupando respuestas a preguntas de opción múltiple en tiempo real
con herramientas como [Pear Deck][k0095]
y [Socrative][k0096].
Si la clase es pequeña --- digamos, de una docena a quince personas ---
y si hay posibilidades de conectarse a internet en el aula,
también puedes
hacer que todas las personas del curso se unan a una videoconferencia
para que puedan compartir la pantalla con la/el docente.
Esto les permite mostrar su trabajo (o sus problemas) a toda la clase.
sin tener que conectar su computadora portátil al proyector.
Las/los estudiantes también pueden usar el chat en la videollamada para hacer preguntas para la/el docente;
en mi experiencia,
la mayoría de las preguntas serán respondidas por sus compañeras/os,
y la/el docente puede encargarse del resto cuando lleguen a un momento natural de descanso.
Este modelo ayuda a nivelar "la cancha´´ para las/los estudiantes remotos:
si alguien no puede asistir a clase por razones de salud
o por compromisos familiares o laborales,
todavía puede participar casi en pie de igualdad
si todo el curso está acostumbrado a colaborar en línea y en tiempo real.

También he impartido clases utilizando instrucción remota en tiempo real,
modalidad en la que las/los estudiantes comparten la ubicación en 2 a 6 sitios diferentes, con ayudantes presentes,
mientras yo enseñaba vía videoconferencia (<a section="joining-using"/>).
Esto escala bien,
ahorra en gastos de viaje,
y permite el uso de técnicas como la programación en parejas (<a section="classroom-pair"/>).
Lo que *no* funciona, es tener un grupo en persona y uno o más grupos de forma remota:
aún con la mejor voluntad del mundo,
quienes participan en persona reciben mucha más atención.

## Participación en línea {#online-engagement}

<cite>Nuth2007</cite> descubrió que hay tres mundos superpuestos en cada aula:
lo público (lo que dice y hace la/el docente),
lo social (interacciones entre pares, entre estudiantes),
y lo privado (dentro de la cabeza de cada estudiante).
De estos,
el más importante suele ser el social:
las/los estudiantes captan tanto a través de las señales de sus compañeras/os como de la instrucción formal.

Por lo tanto, la clave para hacer efectiva cualquier forma de enseñanza en línea es
facilitar las interacciones entre pares.
Para ayudar a lograr esto,
los cursos casi siempre tienen algún tipo de foro de discusión.
<cite>Mill2016a</cite> observaron que las/los estudiantes los utilizan de formas muy diferentes:

> …es muy poco probable que las personas procrastinadoras participen en foros de discusión en línea
> y esta participación reducida,
> a su vez,
> se correlaciona con peores calificaciones.
> Una posible explicación de esta correlación es que
> las personas procrastinadoras son especialmente reacias a unirse una vez que la discusión está en curso,
> quizás porque les preocupa ser percibidas como recién llegadas en una conversación establecida.
> Esta aversión a participar tarde
> provoca que se pierdan los beneficios importantes de aprendizaje y motivación de la interacción entre pares.

<cite>Vell2017</cite> analiza publicaciones en foros de discusión de 395 estudiantes de CS2 en dos universidades
dividiéndo a las publicaciones en cuatro categorías:

Activa:
: solicitud de ayuda que no muestra razonamiento
  y no muestra lo que la/el estudiante ya ha intentado o ya sabe.

Constructiva:
: refleja el razonamiento de las/los estudiantes
  o intenta construir una solución al problema.

Logística:
: políticas del curso, horarios, envío de tareas, etc.

Aclaración de contenido:
: solicitud de información adicional
  que no revela el propio pensamiento de la estudiante.

Descubrieron que dominaban las preguntas constructivas y logísticas,
y que las preguntas constructivas se correlacionaban con las calificaciones.
También encontraron que las/los estudiantes rara vez hacen más de una pregunta activa en un curso,
y que estas *no* se correlacionan con las calificaciones.
Si bien esto es decepcionante,
saberlo ayuda a establecer las expectativas de las docentes:
si bien es posible que deseemos que nuestros cursos tengan comunidades en línea animadas,
tenemos que aceptar que la mayoría no lo hará,
o que la mayor parte de la discusión de estudiante a estudiante se llevará a cabo
a través de canales que ya están usando
y en los que no podemos ser parte.

> ### Cooperación
>
> <cite>Gull2004</cite> describe un concurso de programación en línea que combina colaboración y competencia.
> El concurso comienza cuando se publica una descripción del problema junto con una solución correcta pero ineficiente.
> Cuando acaba,
> la persona ganadora es quien ha hecho la mayor contribución global
> para mejorar el rendimiento de la solución global.
> Todas las presentaciones están abiertas,
> para que los participantes puedan ver el trabajo de los demás y tomar prestadas ideas entre ellos.
> Como muestra el trabajo,
> la solución final es casi siempre un híbrido que utiliza ideas de muchas personas.
>
> <cite>Batt2018</cite> describió una variación a pequeña escala de esto en una clase de introducción a la informática.
> En la etapa uno,
> cada estudiante presentó un proyecto de programación de forma individual.
> En la etapa dos,
> las/los estudiantes trabajaron en parejas para crear una solución mejorada al mismo problema.
> La evaluación indica que los proyectos de dos etapas tienden a mejorar la comprensión de las/los estudiantes
> y que ellas/os disfrutaron del proceso.
> Proyectos como estos no solo mejoran la participación:
> también brindan a las/los estudiantes más experiencia sobre la base del código de otra persona.

La discusión no es la única forma de lograr que las/los estudiantes trabajen juntos en línea.
<cite>Pare2008</cite> y <cite>Kulk2013</cite> reportan experimentos
en el que las/los estudiantes califican el trabajo del resto del curso
y las calificaciones que asignan se comparan con
las calificaciones otorgadas por docentes auxiliares ya graduadas/os u otras personas expertas.
Ambos trabajos encontraron que las calificaciones asignadas por las/los estudiantes coincidían con las calificaciones asignadas por las personas expertas
con tanta frecuencia como las calificaciones de las personas expertas coincidían entre sí.
También encontraron que unos sencillos pasos
(como filtrar respuestas obviamente no consideradas o estructurar rúbricas)
disminuyeron aún más el desacuerdo.
Como se discute en la <a section="individual-peer"/>,
la colusión y el sesgo *no* son factores importantes en la calificación de pares.

> ### Confía, pero educa
>
> La forma más común de medir la validez de los comentarios
> es comparar las calificaciones de las/los estudiantes con las calificaciones de personas expertas,
> pero la revisión por pares calibrada (<a section="individual-peer"/>) puede ser igualmente efectiva.
> <span i="revisión por pares calibrada"></span>
> Antes de pedirles a estudiantes que califiquen el trabajo del resto del curso,
> se les pide que califiquen muestras y se comparan sus resultados con las calificaciones asignadas por la/el docente.
> Una vez que ambas calificaciones se alinean,
> se permite que cada estudiante comience a calificar a sus pares.
> Dado que la lectura crítica es una forma eficaz de aprender,
> este resultado puede apuntar a un futuro en el que las/los estudiantes utilicen la tecnología para emitir juicios,
> en lugar de ser juzgadas/os por la tecnología.

Una técnica que definitivamente vamos a ver más en los próximos años es
la transmisión en línea de sesiones de programación en vivo <cite>Raj2018,Haar2017</cite>.
Esto tiene la mayoría de los beneficios discutidos en la <a section="performance-live"/>,
y cuando se combina con la toma de notas colaborativa (<a section="classroom-notetaking"/>)
puede ser una aproximación cercana a una experiencia en clase.

Si pensamos en unos años más,
<cite>Ijss2000</cite> identificaron cuatro niveles de presencia en línea,
desde el realismo (no podemos notar la diferencia),
la inmersión (nos olvidamos de la diferencia),
la participación (tenemos compromiso con la clase, pero somos conscientes de la diferencia)
a la suspensión de la incredulidad (estamos haciendo la mayor parte del trabajo).
La diferencia crucial que distinguen es
la presencia física, como
la sensación de estar en algún lugar,
y la presencia social, que es la sensación de estar con las demás personas.
Esta última es más importante en la mayoría de situaciones de aprendizaje
y, otra vez,
podemos fomentarla utilizando la tecnología diaria de las/los estudiantes en el aula.
Por ejemplo,
<cite>Deb2018</cite> descubrieron que la retroalimentación en tiempo real sobre los ejercicios en clase,
usando los dispositivos móviles de las/los estudiantes, mejoró la retención de conceptos y
la participación de las/los estudiantes, al tiempo que redujo las tasas de fracaso.

La enseñanza en línea y asincrónica aún está en pañales.
Los MOOCs centralizados pueden llegar a ser un callejón evolutivo sin salida,
pero aún quedan muchos otros modelos prometedores por explorar.
En particular,
<cite>Broo2016</cite> describe cincuenta formas en que los grupos pueden discutir cosas de manera productiva,
y solo unas pocas son ampliamente conocidas o implementadas en línea.
Si vamos a donde están tecnológicamente nuestras/os estudiantes,
en lugar de pedirles que vengan a nosotros,
podemos terminar aprendiendo tanto como ellas/los.

## Ejercicios {#online-exercises}

### Video bidireccional (parejas/10') {.exercise}

Grábate en un video de 2 a 3 minutos haciendo algo,
luego intercambia el video con tu colega
para que cada una/o pueda ver el video de la otra persona a una velocidad 4x.
¿Qué tan fácil es seguir lo que está pasando?
¿Te perdiste de algo?

### Puntos de vista (individual/10') {.exercise}

De acuerdo a <cite>Irib2009</cite>,
diferentes disciplinas se centran en diferentes factores
que afectan el éxito o no de las comunidades en línea:

Negocios:
: fidelización de clientes, gestión de marca, motivación extrínseca.

Psicología:
: sentido de comunidad, motivación intrínseca.

Sociología:
: identidad de grupo, comunidad física, capital social, acción colectiva.

Ciencias de la computación:
: implementación tecnológica.

¿Cuál de estas perspectivas se corresponde más con la tuya?
¿Con cuál estás menos alineada/o?

### Ayudar o dañar (grupos pequeños/30') {.exercise}

[Este artículo de Susan Dynarski en *New York Times*][k0097]
explica cómo y por qué las escuelas asignan a cursos en línea a aquellas/os estudiantes que no aprueban los cursos presenciales,
y cómo esto configura las condiciones para un fracaso aún mayor.
Lee el artículo y luego:

1. En grupos pequeños,
   piensen en dos o tres cosas que las escuelas podrían hacer para compensar estos efectos negativos
   y crear estimaciones aproximadas de sus costos por estudiante.

1. Compara tus sugerencias y costos con los de otros grupos.
   ¿Cuántos puestos de enseñanza a tiempo completo crees que deberían eliminarse
   con el fin de liberar recursos para implementar las ideas más populares para un centenar de estudiantes?

1. Finalmente, discutan en toda la clase:
   ¿creen que sería un beneficio real para las/los estudiantes o no?

Los ejercicios de presupuestación como este son una buena manera de saber quién se toma en serio el cambio educativo.
Todas las personas pueden pensar en cosas que les gustaría hacer;
pero muchas menos están dispuestas a hablar sobre las compensaciones necesarias para que suceda el cambio.