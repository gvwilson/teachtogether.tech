---
template: page.html
---

<div class="reviewers" markdown="1">

Traductora: [Natalia Morandeira][morandeira-natalia].<br/>
Revisoras: [Yanina Bellini Saibene][bellini-saibene-yanina] y [Zulemma Bazurto][bazurto-zulemma].

</div>

En todo el mundo han surgido comunidades de práctica
para enseñar programación, diseño web, robótica y otras habilidades
a <span g="free-range-learner" i="estudiante free-range">estudiantes free-range</span>.<sup>Nota de la editora:
el autor inventó el término "free-range" por analogía con la crianza de pollos y vacas de campo:
estudiantes que son libres de deambular, estirar las piernas, etc.
que aprenden fuera de un aula institucional con un plan de estudios y tareas obligatorias.
El autor también se refiere a las/los estudiantes
que se sientan en escritorios y aulas como "battery-farmed"
(nuevamente por analogía con la crianza a animales de granja).</sup>
Estos grupos existen para que la gente no tenga que aprender estas cosas por su cuenta,
pero, irónicamente,
sus fundadoras/es y docentes están muchas veces enseñándose a sí mismas/os cómo enseñar.

Hay una forma más conveniente.
Así como conocer un par de cuestiones básicas sobre gérmenes y nutrición te puede ayudar a permanecer saludable,
conocer un par de cosas sobre psicología cognitiva,
diseño instruccional,
inclusión
y organización comunitaria
te puede ayudar a aumentar tu efectividad como docente.
Este libro presenta ideas clave que puedes usar inmediatamente,
explica por qué creemos que son ciertas
y te señala otros recursos que te ayudarán a profundizar tus conocimientos.

> ### Re-uso
>
> Algunas secciones de este libro fueron originalmente creadas para
> [el programa de entrenamiento de instructores/as de Software Carpentry][carpentries-instructor].
> Cualquier parte del libro puede ser libremente distribuida y re-utilizada
> bajo la licencia Creative Commons Atribución-NoComercial 4.0
> (<a section="license"/>).
> Puedes usar la versión online disponible en <http://teachtogether.tech/es/>
> en cualquier clase
> (gratuita o paga),
> y puedes citar pequeños extractos bajo el criterio de [uso justo][uso-justo],
> pero no puedes re-publicar largos fragmentos en trabajos comerciales sin permiso previo.
>
> Las contribuciones, correcciones y sugerencias son bienvenidas,
> y cada vez que una nueva versión del libro sea publicada se les agradecerá a quienes contribuyan.
> Por favor consulta el <a section="joining"/> para detalles sobre como contribuir
> y el <a section="conduct"/> para conocer nuestro código de conducta.

## Quién eres {#intro-audience}

La <a section="process-personas"/> explica cómo averiguar quiénes son tus estudiantes.
Los cuatro tipos de personas a las que está destinado este libro son docentes usuarias/os finales:
la enseñanza no es su ocupación primaria, tienen poco o ningún conocimiento sobre pedagogía y
posiblemente trabajan fuera de clases institucionales.

Emilia
: está entrenada como bibliotecaria
  y actualmente trabaja como diseñadora web y gestora de proyectos en una pequeña empresa consultora.
  En su tiempo libre, ayuda a impartir clases de diseño para mujeres que ingresan a la tecnología como una segunda carrera.
  Se encuentra reclutando colegas para dar más clases en su área
  y quiere saber cómo preparar lecciones que otras personas puedan usar,
  a la par de hacer crecer una organización de enseñanza voluntaria.

David
: es un programador profesional, cuyos dos hijos adolescentes
  asisten a una escuela que no ofrece clases de programación.
  Se ha ofrecido como voluntario para dirigir un club de programación mensual después del horario de clases.
  A pesar de que expone presentaciones frecuentemente a sus colegas,
  no tiene experiencia de enseñanza en el aula.
  Quiere aprender a enseñar cómo construir lecciones efectivas en un tiempo razonable,
  y le gustaría aprender más acerca de los pros y contras de las clases en línea en las que cada asistente cursa a su propio ritmo.

Samira
: es una estudiante de robótica, que está considerando ser docente luego de graduarse.
  Quiere ayudar a sus pares en los talleres de robótica de fin de semana,
  pero nunca ha enseñado en una clase antes,
  y en gran medida siente el <span g="impostor-syndrome">síndrome de la impostora</span>{síndrome del impostor/a}.
  Quiere aprender más acerca de educación en general para decidir si la enseñanza es para ella
  y también está buscando sugerencias específicas que la ayuden a dar lecciones
  de forma más efectiva.

René
: es docente de ciencias de la computación en una universidad.
  Ha estado enseñando cursos de grado sobre sistemas operativos por seis años
  y cada vez se convence más de que tiene que haber una mejor manera de enseñar.
  El único entrenamiento disponible a través del centro de enseñanza y aprendizaje de su universidad
  es sobre publicar tareas y enviar evaluaciones en el sistema en línea de gestión del aprendizaje,
  por lo que quiere descubrir qué otro entrenamiento podría pedir.

Estas personas tienen *una variedad de conocimientos técnicos previos*
y *alguna experiencia previa con la enseñanza*,
pero *carecen de entrenamiento formal en enseñanza, diseño de lecciones u organización comunitaria*.
La mayoría trabaja con *estudiantes free-range*
y están *enfocadas en adolescentes y personas adultas*
más que en niñas/os;
todas estas personas *tienen tiempo y recursos limitados*.
Esperamos que nuestro cuarteto use este material de la siguiente manera:

Emilia
: tomará parte de un grupo de lectura semanal en línea con sus voluntarias.

David
: va a abordar parte de este libro en un taller de un día durante un fin de semana y estudiará el resto por su cuenta.

Samira
: usará este libro en un curso de grado de un semestre que incluirá tareas, un proyecto y un examen final.

René
: leerá el libro por su cuenta en su oficina o mientras viaja en el transporte público,
  deseando entretanto que las universidades hagan más para apoyar la enseñanza de alta calidad.

## Qué otras cosas leer {#intro-instead}

Si tienes prisa o quieres tener una idea de lo que cubrirá este libro,
<cite>Brow2018</cite> presenta diez sugerencias basadas en evidencias para enseñar computación<sup>En inglés</sup>.
También puedes disfrutar<sup>Todos en inglés</sup>:

- [El entrenamiento para instructoras/es de The Carpentries (Las/los carpinteras/os)][carpentries-instructor],
  en el cual está basado este libro.

- <cite>Lang2016</cite> y <cite>Hust2012</cite>, que son textos cortos y accesibles, que conectan las cosas que puedes aplicar
  inmediatamente con la investigación que hay detrás de ellas y las fundamenta.

- <cite>Berg2012,Lemo2014,Majo2015,Broo2016,Rice2018,Wein2018b</cite>
  están repletos de sugerencias prácticas sobre cosas que puedes hacer en tu clase,
  pero pueden cobrar más sentido una vez que tengas un marco conceptual para entender por qué sus ideas funcionan.

- <cite>DeBr2015</cite>,
  quien plantea qué cosas son ciertas sobre la educación al explicar qué cosas no lo son y <cite>Dida2016</cite>,
  que fundamenta la teoría del aprendizaje en psicología cognitiva.

- <cite>Pape1993</cite>,
  que continúa siendo una visión inspiradora sobre cómo las computadoras pueden cambiar la educación.
  [La excelente descripción de Amy Ko][ko-mindstorms]
  es una síntesis de las ideas de Papert, mejor que la que podría hacer yo,
  y <cite>Craw2010</cite> es una compañía provocadora y estimulante a ambos textos.

- <cite>Gree2014,McMi2017,Watt2014</cite> explican por qué tantos intentos de reformas educativas
  han fallado a lo largo de los últimos cuarenta años, cómo colegas que trabajan solo por dinero han explotado
  y exacerbado la desigualdad en nuestra sociedad, y cómo la tecnología repetidamente ha fracasado en revolucionar la educación.

- <cite>Brow2007</cite> y <cite>Mann2015</cite>,
  porque no puedes enseñar bien sin cambiar el sistema en el que enseñamos
  y no puedes lograr este cambio trabajando de forma solitaria.

Quienes deseen material más académico pueden encontrar gratificante leer a <cite>Guzd2015a,Hazz2014,Sent2018,Finc2019,Hpl2018</cite>,
mientras que [el blog de Mark Guzdial][guzdial-blog] ha sido consistentemente informativo, sugerente y motivador.

## Agradecimientos {#intro-acknowledgments}

Este libro no existiría sin las contribuciones de
Laura Acion,
Jorge Aranda,
Mara Averick,
Erin Becker,
Yanina Bellini Saibene,
Azalee Bostroem,
Hugo Bowne-Anderson,
Neil Brown,
Gerard Capes,
Francis Castro,
Daniel Chen,
Dav Clark,
Warren Code,
Ben Cotton,
Richie Cotton,
Karen Cranston,
Katie Cunningham,
Natasha Danas,
Matt Davis,
Neal Davis,
Mark Degani,
Tim Dennis,
Paul Denny,
Michael Deutsch,
Brian Dillingham,
Grae Drake,
Kathi Fisler,
Denae Ford,
Auriel Fournier,
Bob Freeman,
Nathan Garrett,
Mark Guzdial,
Rayna Harris,
Ahmed Hasan,
Ian Hawke,
Felienne Hermans,
Kate Hertweck,
Toby Hodges,
Roel Hogervorst,
Mike Hoye,
Dan Katz,
Christina Koch,
Shriram Krishnamurthi,
Katrin Leinweber,
Colleen Lewis,
Dave Loyall,
Paweł Marczewski,
Lenny Markus,
Sue McClatchy,
Jessica McKellar,
Ian Milligan,
Ernesto Mirt,
Julie Moronuki,
Lex Nederbragt,
Aleksandra Nenadic,
Jeramia Ory,
Joel Ostblom,
Nicolás Palopoli,
Elizabeth Patitsas,
Aleksandra Pawlik,
Sorawee Porncharoenwase,
Emily Porta,
Alex Pounds,
Thomas Price,
Danielle Quinn,
Ian Ragsdale,
Erin Robinson,
Rosario Robinson,
Ariel Rokem,
Pat Schloss,
Malvika Sharan,
Florian Shkurti,
Dan Sholler,
Juha Sorva,
Igor Steinmacher,
Tracy Teal,
Tiffany Timbers,
Richard Tomsett,
Preston Tunnell Wilson,
Matt Turk,
Fiona Tweedie,
Martin Ukrop,
Anelda van der Walt,
Stéfan van der Walt,
Allegra Via,
Petr Viktorin,
Belinda Weaver,
Hadley Wickham,
Jason Williams,
Simon Willison,
Karen Word,
John Wrenn,
y Andromeda Yelton.
También estoy agradecido a Lukas Blakk por el logotipo,
a Shashi Kumar por la ayuda con LaTeX,
a Markku Rontu por hacer que los diagramas se vean mejor,
y a toda aquella persona que ha usado este material a lo largo de los años.
Cualquier error que permanezca es mío.

## Ejercicios {#intro-exercises}

Cada capítulo finaliza con una variedad de ejercicios que incluyen un formato sugerido y cuánto tiempo toma usualmente hacerlos en persona.
Muchos pueden ser usados en otros formatos ---en particular,
si estás avanzando en este libro por tu cuenta,
puedes hacer muchos de los ejercicios que son destinados a grupos--- y siempre
puedes dedicar más tiempo a un ejercicio que el que sugiero.

Si estás usando este material en un taller de formación docente,
puedes darles los siguientes ejercicios a quienes participen, con uno o dos días de anticipación,
para que tengan una idea de quiénes son y cuál es la mejor manera en que les puedes ayudar.
Por favor lee las advertencias en la <a section="classroom-prior"/> antes de hacer estos ejercicios.

### Altos y bajos (clase completa/5') {.exercise}

Escribe respuestas breves a las siguientes preguntas y compártelas con tus pares.
(Si estás tomando notas colaborativas en línea como se describe en la <a section="classroom-notetaking"/>, puedes escribir tus respuestas allí.)

1. ¿Cuál es la mejor clase o taller que alguna vez hayas tomado?
  ¿Qué la hacía tan buena?

1. ¿Cuál fue la peor?
  ¿Qué la hacía tan mala?

### Conócete (clase completa/5') {.exercise}

Comparte respuestas breves a las siguientes preguntas con tus pares.
Guarda tus respuestas para que puedas regresar a ellas como referencia
a la par que avanzas en el estudio de este libro.

1. ¿Qué es lo que más quieres enseñar?

1. ¿A quiénes tienes más ganas de enseñarles?

1. ¿Por qué quieres enseñar?

1. ¿Cómo sabrás si estás enseñando bien?

1. ¿Qué es lo que más ansías aprender acerca de enseñanza y aprendizaje?

1. ¿Qué cosa específica crees que es cierta acerca de enseñanza y aprendizaje?

### ¿Por qué aprender a programar? (individual/20') {.exercise}

Las/los políticas/os, líderes de negocios y educadoras/es usualmente dicen que
la gente debe aprender a programar porque los trabajos del futuro lo requerirán.
Sin embargo,
como Benjamin Doxtdator
[ha señalado][jobs-that-dont-exist],
muchas de estas afirmaciones están construidas sobre cimientos débiles.
Incluso si las afirmaciones fueran reales, la educación no debería preparar a la gente para los trabajos del futuro:
les debería dar el poder de decidir qué tipos de trabajos hay y asegurarles que vale la pena hacer esos trabajos.
Además, como [señala Mark Guzdial][guzdial-why-teach-programming],
hay realmente muchas razones para aprender a programar:

1. Para entender nuestro mundo.

1. Para estudiar y entender procesos.

1. Para ser capaz de hacer preguntas sobre las cosas que influyen en nuestras vidas.

1. Para usar una importante nueva forma de alfabetización.

1. Para tener una nueva manera de aprender arte, música, ciencia y matemática.

1. Como una habilidad laboral.

1. Para usar mejor las computadoras.

1. Como un medio en el cual aprender resolución de problemas.

Dibuja una grilla de 3x3 cuyos ejes estén etiquetados: "baja," "media," y "alta"
y coloca cada razón en un sector
de acuerdo a la importancia que tienen para ti (el eje X)
y para la gente a la que planeas enseñar (el eje Y).

1. ¿Qué puntos están estrechamente alineados en importancia
  (es decir, en la diagonal de tu grilla)?

1. ¿Qué puntos están desalineados
  (es decir, en las esquinas por fuera de la diagonal)?

1. ¿Cómo debería afectar esto lo que tú enseñas?