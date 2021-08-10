-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: us-cdbr-east-04.cleardb.com    Database: heroku_849b96c415420e5
-- ------------------------------------------------------
-- Server version	5.6.50-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_name` varchar(45) NOT NULL,
  `admin_email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (5,'adminPrincipal','v2001.ferman@gmail.com','123456');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idUsuario_idx` (`idUsuario`),
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (5,'Romance',5),(15,'Aventura',5),(25,'Fantasía',5),(35,'Terror',5);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `highlight`
--

DROP TABLE IF EXISTS `highlight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `highlight` (
  `idhighlight` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(70) NOT NULL,
  `texto` varchar(3000) NOT NULL,
  `notas` varchar(200) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  PRIMARY KEY (`idhighlight`),
  KEY `idUsuariox_idx` (`idUsuario`),
  CONSTRAINT `idUsuarioh` FOREIGN KEY (`idUsuario`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `highlight`
--

LOCK TABLES `highlight` WRITE;
/*!40000 ALTER TABLE `highlight` DISABLE KEYS */;
INSERT INTO `highlight` VALUES (5,'Los 7 hábitos de la gente altamente efectiva','Comenzar con un fin en mente','Primer hábito',5),(15,'Los 7 hábitos de la gente altamente efectiva','Poner primero lo primero','Segundo hábito',5),(25,'Los 7 hábitos de la gente altamente efectiva','Los 7 hábitos no son un conjunto de partes independientes o fórmulas fragmentadas','Conclusion del libro',5);
/*!40000 ALTER TABLE `highlight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria`
--

DROP TABLE IF EXISTS `libreria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libreria` (
  `idlibreria` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(70) NOT NULL,
  `sinopsis` varchar(155) NOT NULL,
  `recomendacion` varchar(155) NOT NULL,
  `informacionDelAutor` varchar(155) NOT NULL,
  `contenido` varchar(3000) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `idCategoria` int(11) NOT NULL,
  `idResumen` int(11) NOT NULL,
  PRIMARY KEY (`idlibreria`),
  KEY `idCategoria_idx` (`idCategoria`),
  KEY `idResumen_idx` (`idResumen`),
  KEY `idUsuario_idx` (`idUsuario`),
  CONSTRAINT `idCategoriax` FOREIGN KEY (`idCategoria`) REFERENCES `resumen` (`idCategoria`),
  CONSTRAINT `idResumenx` FOREIGN KEY (`idResumen`) REFERENCES `resumen` (`id`),
  CONSTRAINT `idUsuariox` FOREIGN KEY (`idUsuario`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria`
--

LOCK TABLES `libreria` WRITE;
/*!40000 ALTER TABLE `libreria` DISABLE KEYS */;
INSERT INTO `libreria` VALUES (75,'Los 7 hábitos de la gente altamente efectiva','Nuestro carácter está compuesto por hábitos que son factores poderosos en nuestras vidas. Estos son pautas consistentes que crean efectividad.','Para todos aquellos en busca de crecimiento personal','Stephen Richards Covey fue un licenciado en administración de empresas, escritor, conferenciante, religioso y profesor estadounidense.','Los 7 hábitos de la gente altamente efectiva son los siguientes:\r\nEl hábito de la proactividad nos da la libertad para poder escoger nuestra respuesta a los estímulos del medioambiente. Nos faculta para responder de acuerdo con nuestros principios y valores. En esencia, es lo que nos hace humanos y nos permite afirmar que somos los arquitectos de nuestro propio destino.\r\nComenzar con un fin en mente hace posible que nuestra vida tenga razón de ser, pues la creación de una visión de lo que queremos lograr permite que nuestras acciones estén dirigidas a lo que verdaderamente es significativo en nuestras vidas.\r\nPoner primero lo primero nos permite liberarnos de la tiranía de lo urgente para dedicar tiempo a las actividades que en verdad dan sentido a nuestras vidas. Es la disciplina de llevar a cabo lo importante, lo cual nos permite convertir en realidad la visión que forjamos en el hábito 2.\r\nPensar en Ganar-Ganar nos permite desarrollar una mentalidad de abundancia material y espiritual, pues nos cuestiona la premisa de que la vida es un “juego de suma cero” donde para que yo gane alguien tiene que perder.\r\nBuscar entender primero y ser entendido después es la esencia del respeto a los demás. La necesidad que tenemos de ser entendidos es uno de los sentimientos más intensos de todos los seres humanos. Este hábito es la clave de las relaciones humanas efectivas y posibilita llegar a acuerdos de tipo Ganar-Ganar.\r\nSinergizar es el resultado de cultivar la habilidad y la actitud de valorar la diversidad. La síntesis de ideas divergentes produce ideas mejores y superiores a las ideas individuales. El logro del trabajo en equipo y la innovación son el resultado de este hábito.\r\nAfilar la sierra es usar la capacidad que tenemos para renovarnos física, mental y espiritualmente. Es lo que nos permite establecer un equilibrio entre todas las dimensiones de nuestro ser, a fin de ser efectivos en los diferentes papeles (roles) que desempeñamos en nuestras vidas.\r\nLos 7 hábitos no son un conjunto de partes independientes o fórmulas fragmentadas. En armonía con las leyes naturales del crecimiento, proporcionan un enfoque gradual, secuencial y altamente integrado del desarrollo de la efectividad personal e interpersonal.',5,15,5),(85,'Yo antes de ti','Will Traynor es un empresario exitoso que queda tetrapléjico luego de un accidente de moto. Tras perder su empleo, Louisa es contratada por los padres del ','Para todos aquellos amantes del romance y la tragedia.','Paulie Sarah Jo Moyes, mejor conocida como Jojó Moyes, es una periodista y escritora londinense, nacida en el año 1969.','La vida cambia de golpe\r\nEs el año 2007. Will Traynor se ha vestido para salir con su moto, pero debido a la lluvia decide tomar un taxi. Con el apuro para alcanzarlo, corre y se produce un accidente que lo deja cuadrapléjico. Apenas tiene movilidad muy limitada en las extremidades superiores.\r\n\r\nWill había sido hasta ese momento un empresario rico, joven, atractivo y aventurero. Le gustaba ir en moto, practicar deportes que le llenaban de adrenalina, como el submarinismo, por ejemplo. El accidente se lleva su movilidad y también sus ganas de vivir.\r\n\r\nEn 2009, Louisa Clark se queda desempleada. Tiene 26 años y no es particularmente ambiciosa. Su hermana es más joven, madre soltera, pero también está más preparada y ha tenido más éxito, económicamente. Viven con sus padres y la noticia del trabajo perdido no ayuda en absoluto. No obstante, en un centro de empleo consiguen una opción para ella: cuidar a un hombre que va en silla de ruedas.\r\n\r\nTiempo para un intento\r\nLouisa obtiene el empleo. La madre de Will, Camilla Traynor, no solo busca a alguien que cuide de su hijo, sino también a una persona que le ayude a recuperar la alegría. La mansión Traynor tampoco es un ejemplo perfecto, precisamente, ya que el matrimonio está pasando por un mal momento: el padre de Will tiene una aventura.\r\n\r\nCuando Louisa se da cuenta de que Will tiene cicatrices en las muñecas, comprende mejor su misión. Will ha intentado suicidarse. Ahora manifiesta su deseo de practicarse la eutanasia en Suiza, país en el que es posible realizar ese procedimiento, al que llaman “morir con dignidad”.\r\n\r\nLa señora Camilla y otros familiares consiguen negociar con Will un período de seis meses antes de que se vaya a Suiza; durante ese tiempo esperan poder convencerlo de reconsiderar su decisión. Louisa se entera de las intenciones de Will al escuchar, accidentalmente, una conversación familiar-\r\n\r\nEntonces se dedica a buscar la manera de que Will abandone la idea. Le corta el cabello y le afeita la barba, detalles que él había descuidado durante largo tiempo. Lo saca de paseo y lo llena de estímulos, para hacer su día a día agradable y lleno de sorpresas.\r\n\r\nSin embargo, esto no es suficiente para Will. Por lo tanto, poco antes de que se cumpla el tiempo señalado, Louisa renuncia. La señora Traynor la convence para que vuelva y entonces planifican un viaje a la Isla Mauricio, con el fin de alejarlo definitivamente de la idea del suicidio.\r\n\r\nLa noche antes de regresar, se besan. Louisa le confiesa que lo ama e intenta convencerlo de ser felices juntos. Sin embargo, él se muestra inflexible. No quiere vivir así.\r\n\r\nLa generosidad de Will\r\nDurante el tiempo en que interactúan como paciente y asistente, Will nota que, debido a su condición económica y su timidez, el mundo de Louisa es bastante limitado. Sus perspectivas de crecimiento son muy estrechas y apenas ha salido nunca de la ciudad. Ella es opuesta a lo que él había sido.\r\n\r\nFinalmente, antes de su viaje a Suiza, Louisa y Will ',15,5,25),(95,'Lazarillo de Tormes','Esta novela gira en torno a Lázaro, un niño ingenuo que, debido a las adversidades que vive, se convierte en un joven pícaro que lucha por sobrevivir.','Para aquellos en busca de un historia de superación y amor propio. Además de ser un clásico de la literatura española.','Este considerado anónimo. Sin embargo, Mercedes Agulló presentó un trabajo donde defendía que el autor del Lazarillo es Diego Hurtado de Mendoza.','Sus padres fueron encarcelados por varios crímenes. Lázaro, al verse huérfano, buscó la compañía de algún amo y se hizo mozo de un ciego pero no duró mucho tiempo con él . El ciego ganaba mucho dinero, pero a él no le daba nada de comer y lo tenía muerto de hambre . Así que lo dejó y fue a buscar otro. \r\nUn día, que iba mendigando, se encontró a un clérigo que le preguntó que si buscaba amo . Lázaro le dijo que sí . El clérigo tenía un arca y en el arca tenía la comida: pan , agua , arroz … Lázaro aprovechó que llegó a su casa un calderero y pidió la llave el arca para coger cosas para comer . Como el arca era vieja y tenía agujeros el clérigo pensó que eran los ratones los que mordisqueaban el pan. Cierto día, el clérigo se dio cuenta y le dijo que no se merecía un criado tan listo. Lo echó y le dijo que buscara amo. \r\nLázaro tuvo suerte de llegar a la gran ciudad de Toledo, pues allí encontró de nuevo un amo. Este fue un escudero. El escudero tenía pinta de ser muy rico pero era pobre . Al escudero le perseguía la justicia porque no pagaba sus deudas . Y Lázaro no quiso estar con él. \r\nUnas mujeres que cuidaban a Lázaro le dijeron que se fuera con un fraile amigo de ellas. Pero Lázaro solo duró ocho días con él pues andaba mucho y a él no le gustaba andar. \r\nA los pocos días sirvió a un buldero. El buldero tenía mucha experiencia para mentir y siempre , siempre se estaba peleando con un alguacil . Estuvo cuatro años con él pero como era muy mentiroso Lázaro decidió dejarlo. \r\nUn día que entró en la catedral uno de sus capellanes decidió contratarlo. Le hizo cargo de un burro, cuatro cántaros y un látigo y empezó a vender agua por el pueblo. Y cuando reunió el dinero suficiente, se compró ropa nueva y dejó al capellán. \r\nDespués de esto sirvió a un alguacil con el que no duró mucho y tiempo porque tenía un oficio muy peligroso. Un día unos delincuentes cogieron al alguacil y lo maltrataron, pero a Lázaro no lo pillaron . Y Lázaro siguió buscando amo. \r\nLázaro consiguió por último un oficio real. Y a los pocos días un cura lo casó con una de sus criadas y le alquiló una casa al lado de la suya. Vivieron felices.',5,15,55);
/*!40000 ALTER TABLE `libreria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil` (
  `idperfil` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `edad` int(11) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `iduser` int(11) NOT NULL,
  PRIMARY KEY (`idperfil`),
  KEY `iduserx_idx` (`iduser`),
  CONSTRAINT `iduserx` FOREIGN KEY (`iduser`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil`
--

LOCK TABLES `perfil` WRITE;
/*!40000 ALTER TABLE `perfil` DISABLE KEYS */;
INSERT INTO `perfil` VALUES (5,'Jason',19,'El Salvador',15),(45,'Lola',20,'Guatemala',5);
/*!40000 ALTER TABLE `perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `idrequest` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(45) NOT NULL,
  `User_email` varchar(45) NOT NULL,
  `Book_name` varchar(45) NOT NULL,
  `Book_year` int(11) NOT NULL,
  `Book_author` varchar(45) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`idrequest`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` VALUES (5,'testUser','bal@bal.com','Harry Potter',1999,'J. K. Rowling','Muy buen libro'),(15,'Verónica Fermán','v@gmail.com','El arte de ser un desastre',2016,'Jennifer McCartney','Muy buen libro ');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resumen`
--

DROP TABLE IF EXISTS `resumen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resumen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(70) NOT NULL,
  `sinopsis` varchar(155) NOT NULL,
  `recomendación` varchar(155) NOT NULL,
  `informacionDelAutor` varchar(155) NOT NULL,
  `contenido` varchar(3000) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `idCategoria` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idCategoria_idx` (`idCategoria`),
  KEY `idUsuarios_idx` (`idUsuario`),
  CONSTRAINT `idCategoria` FOREIGN KEY (`idCategoria`) REFERENCES `categories` (`id`),
  CONSTRAINT `idUsuarios` FOREIGN KEY (`idUsuario`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resumen`
--

LOCK TABLES `resumen` WRITE;
/*!40000 ALTER TABLE `resumen` DISABLE KEYS */;
INSERT INTO `resumen` VALUES (5,'Los 7 hábitos de la gente altamente efectiva','Nuestro carácter está compuesto por hábitos que son factores poderosos en nuestras vidas. Estos son pautas consistentes que crean efectividad.','Para todos aquellos en busca de crecimiento personal','Stephen Richards Covey fue un licenciado en administración de empresas, escritor, conferenciante, religioso y profesor estadounidense.','Los 7 hábitos de la gente altamente efectiva son los siguientes:\r\nEl hábito de la proactividad nos da la libertad para poder escoger nuestra respuesta a los estímulos del medioambiente. Nos faculta para responder de acuerdo con nuestros principios y valores. En esencia, es lo que nos hace humanos y nos permite afirmar que somos los arquitectos de nuestro propio destino.\r\nComenzar con un fin en mente hace posible que nuestra vida tenga razón de ser, pues la creación de una visión de lo que queremos lograr permite que nuestras acciones estén dirigidas a lo que verdaderamente es significativo en nuestras vidas.\r\nPoner primero lo primero nos permite liberarnos de la tiranía de lo urgente para dedicar tiempo a las actividades que en verdad dan sentido a nuestras vidas. Es la disciplina de llevar a cabo lo importante, lo cual nos permite convertir en realidad la visión que forjamos en el hábito 2.\r\nPensar en Ganar-Ganar nos permite desarrollar una mentalidad de abundancia material y espiritual, pues nos cuestiona la premisa de que la vida es un “juego de suma cero” donde para que yo gane alguien tiene que perder.\r\nBuscar entender primero y ser entendido después es la esencia del respeto a los demás. La necesidad que tenemos de ser entendidos es uno de los sentimientos más intensos de todos los seres humanos. Este hábito es la clave de las relaciones humanas efectivas y posibilita llegar a acuerdos de tipo Ganar-Ganar.\r\nSinergizar es el resultado de cultivar la habilidad y la actitud de valorar la diversidad. La síntesis de ideas divergentes produce ideas mejores y superiores a las ideas individuales. El logro del trabajo en equipo y la innovación son el resultado de este hábito.\r\nAfilar la sierra es usar la capacidad que tenemos para renovarnos física, mental y espiritualmente. Es lo que nos permite establecer un equilibrio entre todas las dimensiones de nuestro ser, a fin de ser efectivos en los diferentes papeles (roles) que desempeñamos en nuestras vidas.\r\nLos 7 hábitos no son un conjunto de partes independientes o fórmulas fragmentadas. En armonía con las leyes naturales del crecimiento, proporcionan un enfoque gradual, secuencial y altamente integrado del desarrollo de la efectividad personal e interpersonal.',5,15),(15,'Alicia en el país de las maravillas','En este libro se cuenta la historia de la joven Alicia quien cae en un mundo de fantasía a través de un agujero, donde encontrará criaturas y aventuras mág','Para todos aquellos amantes de la aventura y el misterio.','Lewis carroll escritor inglés de ficción infantil.','Todo comienza cuando Alicia está descansando a la orilla del río en verano, cuando un Conejo vestido igual a ella. El Conejo saca un reloj de bolsillo y baja por una madriguera. Alicia sigue al Conejo y se encontrará con un excelente pasillo forrado de puertas. Ella encuentra una pequeña entrada quela lleva a una mesa cercana.\r\n\r\nAquí Alicia, ve un hermoso jardín, y comienza a llorar porque se da cuenta que no cabe por la entrada. Ella encuentra una botella y se toma el contenido. Se encoge hasta caber por la entrada. Luego Alicia descubre un pastel de bodas que la hace crecer de tamaño. Alicia comienza a llorar una vez más, y sus enormes lágrimas forman una piscina a sus pies. Mientras llora, se encoge y cae en la piscina de lágrimas.\r\nLa piscina de lágrimas se convierte en un mar, donde luego aparece el ratón que acompaña a Alice a la orilla, en la que una cantidad de animales se reúnen en la orilla.\r\n\r\nConociendo a la duquesa\r\nLuego de un rato de paseo, Alicia come una planta que la hace volver a su tamaño normal, entonces se encuentra con una propiedad. Ella entra y encuentra a la duquesa, que está amamantando a un bebé chillón, y un gato de Cheshire sonriente, así como un cocinero que arroja niveles masivos de pimienta directamente en un caldero de sopa.\r\n\r\nLa duquesa se comporta groseramente con Alicia y se va para prepararse para encuentro con la Reina. El Gato de Cheshire le explica a Alicia que todos en el País de las Maravillas están locos, incluida la misma Alicia. El gato Cheshire da indicaciones para la propiedad de la Liebre de Marzo y se desvanece a sólo una sonrisa flotante.\r\n\r\nLa liebre de marzo y el sobrero loco\r\nAlicia viaja a la propiedad de la Liebre de Marzo. Una vez aquí fue maltratada y descubre que han hecho daño al Tiempo y por lo tanto están atrapados en la hora del té perpetuo. Después de una descortesía final, Alicia viaja al bosque y encuentra un árbol que usa para moverse a través de él para conseguir la fantástica sala de nuevo.\r\n\r\nDespués de salvar a muchos jardineros, Alicia se une a la Reina en una actividad muy extraña de croquet. El patio de croquet es montañoso, las bolas y mazos resultan ser son flamencos vivos y erizos, así como las lágrimas de la Reina. En medio de esta locura, Alicia se topa con el Gato de Cheshire una vez más, quien le pregunta cómo está realmente. El Gobernante de Corazones interrumpe su discurso y se esfuerza por intimidar al Felino de Cheshire, quien despide al gobernante descaradamente.\r\nEl Rey se ofende y se arregla con la ejecución del Gato de Cheshire, pero debido a que el Gato de Cheshire es una cabeza flotando en el aire ahora, nadie puede ponerse de acuerdo sobre cómo decapitarlo exactamente.\r\n\r\nEl desenlace final\r\nLa duquesa se acerca a Alicia y se esfuerza por hacerse amiga de ella, pero esta última no está segura. La Reina de Corazones persigue a la duquesa y le muestra a Alicia que debe ir a la Falsa Tortuga para escuchar su relato. Alicia tiene extraños encuentros con toda',5,25),(25,'Yo antes de ti','Will Traynor es un empresario exitoso que queda tetrapléjico luego de un accidente de moto. Tras perder su empleo, Louisa es contratada por los padres del ','Para todos aquellos amantes del romance y la tragedia.','Paulie Sarah Jo Moyes, mejor conocida como Jojó Moyes, es una periodista y escritora londinense, nacida en el año 1969.','La vida cambia de golpe\r\nEs el año 2007. Will Traynor se ha vestido para salir con su moto, pero debido a la lluvia decide tomar un taxi. Con el apuro para alcanzarlo, corre y se produce un accidente que lo deja cuadrapléjico. Apenas tiene movilidad muy limitada en las extremidades superiores.\r\n\r\nWill había sido hasta ese momento un empresario rico, joven, atractivo y aventurero. Le gustaba ir en moto, practicar deportes que le llenaban de adrenalina, como el submarinismo, por ejemplo. El accidente se lleva su movilidad y también sus ganas de vivir.\r\n\r\nEn 2009, Louisa Clark se queda desempleada. Tiene 26 años y no es particularmente ambiciosa. Su hermana es más joven, madre soltera, pero también está más preparada y ha tenido más éxito, económicamente. Viven con sus padres y la noticia del trabajo perdido no ayuda en absoluto. No obstante, en un centro de empleo consiguen una opción para ella: cuidar a un hombre que va en silla de ruedas.\r\n\r\nTiempo para un intento\r\nLouisa obtiene el empleo. La madre de Will, Camilla Traynor, no solo busca a alguien que cuide de su hijo, sino también a una persona que le ayude a recuperar la alegría. La mansión Traynor tampoco es un ejemplo perfecto, precisamente, ya que el matrimonio está pasando por un mal momento: el padre de Will tiene una aventura.\r\n\r\nCuando Louisa se da cuenta de que Will tiene cicatrices en las muñecas, comprende mejor su misión. Will ha intentado suicidarse. Ahora manifiesta su deseo de practicarse la eutanasia en Suiza, país en el que es posible realizar ese procedimiento, al que llaman “morir con dignidad”.\r\n\r\nLa señora Camilla y otros familiares consiguen negociar con Will un período de seis meses antes de que se vaya a Suiza; durante ese tiempo esperan poder convencerlo de reconsiderar su decisión. Louisa se entera de las intenciones de Will al escuchar, accidentalmente, una conversación familiar-\r\n\r\nEntonces se dedica a buscar la manera de que Will abandone la idea. Le corta el cabello y le afeita la barba, detalles que él había descuidado durante largo tiempo. Lo saca de paseo y lo llena de estímulos, para hacer su día a día agradable y lleno de sorpresas.\r\n\r\nSin embargo, esto no es suficiente para Will. Por lo tanto, poco antes de que se cumpla el tiempo señalado, Louisa renuncia. La señora Traynor la convence para que vuelva y entonces planifican un viaje a la Isla Mauricio, con el fin de alejarlo definitivamente de la idea del suicidio.\r\n\r\nLa noche antes de regresar, se besan. Louisa le confiesa que lo ama e intenta convencerlo de ser felices juntos. Sin embargo, él se muestra inflexible. No quiere vivir así.\r\n\r\nLa generosidad de Will\r\nDurante el tiempo en que interactúan como paciente y asistente, Will nota que, debido a su condición económica y su timidez, el mundo de Louisa es bastante limitado. Sus perspectivas de crecimiento son muy estrechas y apenas ha salido nunca de la ciudad. Ella es opuesta a lo que él había sido.\r\n\r\nFinalmente, antes de su viaje a Suiza, Louisa y Will ',5,5),(35,'Harry Potter','ggg','ggg','ggg','gggg',5,15),(45,'Harry Potter','ggg','gggx','gggx','ggggx',5,15),(55,'Lazarillo de Tormes','Esta novela gira en torno a Lázaro, un niño ingenuo que, debido a las adversidades que vive, se convierte en un joven pícaro que lucha por sobrevivir.','Para aquellos en busca de un historia de superación y amor propio. Además de ser un clásico de la literatura española.','Este considerado anónimo. Sin embargo, Mercedes Agulló presentó un trabajo donde defendía que el autor del Lazarillo es Diego Hurtado de Mendoza.','Sus padres fueron encarcelados por varios crímenes. Lázaro, al verse huérfano, buscó la compañía de algún amo y se hizo mozo de un ciego pero no duró mucho tiempo con él . El ciego ganaba mucho dinero, pero a él no le daba nada de comer y lo tenía muerto de hambre . Así que lo dejó y fue a buscar otro. \r\nUn día, que iba mendigando, se encontró a un clérigo que le preguntó que si buscaba amo . Lázaro le dijo que sí . El clérigo tenía un arca y en el arca tenía la comida: pan , agua , arroz … Lázaro aprovechó que llegó a su casa un calderero y pidió la llave el arca para coger cosas para comer . Como el arca era vieja y tenía agujeros el clérigo pensó que eran los ratones los que mordisqueaban el pan. Cierto día, el clérigo se dio cuenta y le dijo que no se merecía un criado tan listo. Lo echó y le dijo que buscara amo. \r\nLázaro tuvo suerte de llegar a la gran ciudad de Toledo, pues allí encontró de nuevo un amo. Este fue un escudero. El escudero tenía pinta de ser muy rico pero era pobre . Al escudero le perseguía la justicia porque no pagaba sus deudas . Y Lázaro no quiso estar con él. \r\nUnas mujeres que cuidaban a Lázaro le dijeron que se fuera con un fraile amigo de ellas. Pero Lázaro solo duró ocho días con él pues andaba mucho y a él no le gustaba andar. \r\nA los pocos días sirvió a un buldero. El buldero tenía mucha experiencia para mentir y siempre , siempre se estaba peleando con un alguacil . Estuvo cuatro años con él pero como era muy mentiroso Lázaro decidió dejarlo. \r\nUn día que entró en la catedral uno de sus capellanes decidió contratarlo. Le hizo cargo de un burro, cuatro cántaros y un látigo y empezó a vender agua por el pueblo. Y cuando reunió el dinero suficiente, se compró ropa nueva y dejó al capellán. \r\nDespués de esto sirvió a un alguacil con el que no duró mucho y tiempo porque tenía un oficio muy peligroso. Un día unos delincuentes cogieron al alguacil y lo maltrataron, pero a Lázaro no lo pillaron . Y Lázaro siguió buscando amo. \r\nLázaro consiguió por último un oficio real. Y a los pocos días un cura lo casó con una de sus criadas y le alquiló una casa al lado de la suya. Vivieron felices.',5,15);
/*!40000 ALTER TABLE `resumen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `salt` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (5,'logTestUser','bal@bal.com','$2b$14$EYVgUbJyZBhV3Ze6GNklvuMjzFO3cfXDmSOi0QXuOj.Vgh5tUU3BS','$2b$14$EYVgUbJyZBhV3Ze6GNklvu'),(15,'stanley','stanley@gmail.com','$2b$14$WrmGWEOQQdNzJwphTDQ2R.v5tNyDV4fA/23IG5sBRe09WatdSdMl2','$2b$14$WrmGWEOQQdNzJwphTDQ2R.'),(25,'aaa','aaa@gmail.com','$2b$14$4O2M6/HOjXSq0OVgs74AvOdEuD6GYwDiNRzapi4UK05dOFrgqiANy','$2b$14$4O2M6/HOjXSq0OVgs74AvO'),(35,'js','js@gmail.com','$2b$14$KOREkHpMQ1RAd76AmaeXre.EEeT8BBwR9EagDaXisguDKi5ueJi4e','$2b$14$KOREkHpMQ1RAd76AmaeXre');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-09 21:23:11
