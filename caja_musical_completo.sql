-- =========================================================
-- Script completo: esquema + datos de prueba
-- caja_musical
-- Incluye: CREATE SCHEMA/TABLE y luego los INSERT de datos
-- =========================================================

-- 1. Creación del esquema
CREATE SCHEMA IF NOT EXISTS caja_musical;

-- =========================================================
-- Tabla: ttipo
-- =========================================================
CREATE TABLE caja_musical.ttipo (
    id_tipo      SERIAL       NOT NULL,
    nombre_tipo  VARCHAR(128) NOT NULL,
    CONSTRAINT pk_ttipo PRIMARY KEY (id_tipo)
);

-- =========================================================
-- Tabla: tgenero
-- =========================================================
CREATE TABLE caja_musical.tgenero (
    id_genero      SERIAL       NOT NULL,
    nombre_genero  VARCHAR(128) NOT NULL,
    CONSTRAINT pk_tgenero PRIMARY KEY (id_genero)
);

-- =========================================================
-- Tabla: tartista
-- =========================================================
CREATE TABLE caja_musical.tartista (
    id_artista  SERIAL       NOT NULL,
    nombre      VARCHAR(128) NOT NULL,
    id_tipo     INTEGER      NOT NULL,
    CONSTRAINT pk_tartista PRIMARY KEY (id_artista),
    CONSTRAINT fk_tartista_ttipo FOREIGN KEY (id_tipo)
        REFERENCES caja_musical.ttipo (id_tipo)
);

-- =========================================================
-- Tabla: talbum
-- =========================================================
CREATE TABLE caja_musical.talbum (
    id_album           SERIAL       NOT NULL,
    titulo             VARCHAR(128) NOT NULL,
    anio_lanzamiento   NUMERIC      NOT NULL,
    id_artista         INTEGER      NOT NULL,
    CONSTRAINT pk_talbum PRIMARY KEY (id_album),
    CONSTRAINT fk_talbum_tartista FOREIGN KEY (id_artista)
        REFERENCES caja_musical.tartista (id_artista)
);

-- =========================================================
-- Tabla: tcancion
-- =========================================================
CREATE TABLE caja_musical.tcancion (
    id_cancion         SERIAL        NOT NULL,
    nombre_cancion     VARCHAR(64)   NOT NULL,
    duracion           TIME          NOT NULL,
    fecha_lanzamiento  DATE          NOT NULL,
    id_album           INTEGER       NOT NULL,
    id_genero          INTEGER       NOT NULL,
    CONSTRAINT pk_tcancion PRIMARY KEY (id_cancion),
    CONSTRAINT fk_tcancion_talbum FOREIGN KEY (id_album)
        REFERENCES caja_musical.talbum (id_album),
    CONSTRAINT fk_tcancion_tgenero FOREIGN KEY (id_genero)
        REFERENCES caja_musical.tgenero (id_genero)
);

-- =========================================================
-- Tabla: tcantante
-- =========================================================
CREATE TABLE caja_musical.tcantante (
    id_cantante      SERIAL       NOT NULL,
    nombre           VARCHAR(36)  NOT NULL,
    primer_apellido  VARCHAR(36)  NOT NULL,
    edad             NUMERIC      NOT NULL,
    CONSTRAINT pk_tcantante PRIMARY KEY (id_cantante),
    CONSTRAINT uk_tcantante_edad UNIQUE (edad)
);

-- =========================================================
-- Tabla: tintegrante
-- =========================================================
CREATE TABLE caja_musical.tintegrante (
    id_integrante  SERIAL   NOT NULL,
    id_artista     INTEGER  NOT NULL,
    id_cantante    INTEGER  NOT NULL,
    CONSTRAINT pk_tintegrante PRIMARY KEY (id_integrante),
    CONSTRAINT fk_tintegrante_tartista FOREIGN KEY (id_artista)
        REFERENCES caja_musical.tartista (id_artista),
    CONSTRAINT fk_tintegrante_tcantante FOREIGN KEY (id_cantante)
        REFERENCES caja_musical.tcantante (id_cantante)
);

-- =========================================================
-- Fin del script
-- =========================================================
-- =========================================================
-- Script de datos de prueba: caja_musical
-- Requiere haber ejecutado antes: caja_musical_schema.sql
--
-- NOTA: los nombres de artistas/bandas y sus integrantes son
-- reales y de conocimiento público. Las EDADES en tcantante
-- son valores de EJEMPLO (no verificados/actualizados), ya
-- que la columna exige un valor numérico único por persona.
-- =========================================================

-- =========================================================
-- 1. TTIPO (Solista, Agrupación)
-- =========================================================
INSERT INTO caja_musical.ttipo (id_tipo, nombre_tipo) VALUES
(1, 'Solista'),
(2, 'Agrupación');

-- =========================================================
-- 2. TARTISTA (15: 10 solistas, 5 agrupaciones)
-- =========================================================
INSERT INTO caja_musical.tartista (id_artista, nombre, id_tipo) VALUES
-- Solistas (id_tipo = 1)
(1,  'Shakira',           1),
(2,  'Bad Bunny',         1),
(3,  'Karol G',           1),
(4,  'Rosalía',           1),
(5,  'Natalia Lafourcade',1),
(6,  'Aleks Syntek',      1),
(7,  'Ely Guerra',        1),
(8,  'Alejandra Guzmán',  1),
(9,  'Enrique Iglesias',  1),
(10, 'Ricky Martin',      1),
-- Agrupaciones (id_tipo = 2)
(11, 'Zoé',               2),
(12, 'Fobia',             2),
(13, 'Kinky',             2),
(14, 'Caifanes',          2),
(15, 'Café Tacvba',       2);

-- =========================================================
-- 3. TCANTANTE (30: 10 solistas + 20 integrantes de bandas)
-- Nombres reales; edades = valores de ejemplo (no verificados)
-- =========================================================
INSERT INTO caja_musical.tcantante (id_cantante, nombre, primer_apellido, edad) VALUES
-- Solistas
(1,  'Shakira Isabel',     'Mebarak Ripoll',    20),
(2,  'Benito Antonio',     'Martínez Ocasio',   21),
(3,  'Carolina',           'Giraldo Navarro',   22),
(4,  'Rosalía',            'Vila Tobella',      23),
(5,  'Natalia',            'Lafourcade',        24),
(6,  'Aleks',              'Syntek',            25),
(7,  'Ely',                'Guerra',            26),
(8,  'Alejandra Antonieta','Guzmán Pinal',      27),
(9,  'Enrique Miguel',     'Iglesias Preysler', 28),
(10, 'Enrique Martín',     'Morales',           29),
-- Integrantes de Zoé
(11, 'León',               'Larregui',          30),
(12, 'Sergio',             'Acosta',            31),
(13, 'Ángel',              'Mosqueda',          32),
(14, 'Jesús',              'Báez',              33),
-- Integrantes de Fobia
(15, 'Leonardo',           'de Lozanne',        34),
(16, 'Jay',                'de la Cueva',       35),
(17, 'Vicente',            'Gayo',              36),
(18, 'Iñaki',              'Vázquez',           37),
-- Integrantes de Kinky
(19, 'Gilberto',           'Cerezo',            38),
(20, 'Omar',               'Gongora',           39),
(21, 'Ulises',             'Lozano',            40),
(22, 'Carlos',             'Chairez',           41),
-- Integrantes de Caifanes
(23, 'Saúl',               'Hernández',         42),
(24, 'Alejandro',          'Marcovich',         43),
(25, 'Sabo',               'Romo',              44),
(26, 'Alfonso',            'André',             45),
-- Integrantes de Café Tacvba
(27, 'Rubén',              'Albarrán',          46),
(28, 'Emmanuel',           'del Real',          47),
(29, 'José Alberto',       'Rangel',            48),
(30, 'Enrique',            'Rangel',            49);

-- =========================================================
-- 4. TINTEGRANTE (30: 10 solistas [1 c/u] + 5 agrupaciones [4 c/u])
-- =========================================================
INSERT INTO caja_musical.tintegrante (id_integrante, id_artista, id_cantante) VALUES
-- Solistas (el propio artista es su único integrante)
(1,  1,  1),
(2,  2,  2),
(3,  3,  3),
(4,  4,  4),
(5,  5,  5),
(6,  6,  6),
(7,  7,  7),
(8,  8,  8),
(9,  9,  9),
(10, 10, 10),
-- Zoé (artista 11)
(11, 11, 11),
(12, 11, 12),
(13, 11, 13),
(14, 11, 14),
-- Fobia (artista 12)
(15, 12, 15),
(16, 12, 16),
(17, 12, 17),
(18, 12, 18),
-- Kinky (artista 13)
(19, 13, 19),
(20, 13, 20),
(21, 13, 21),
(22, 13, 22),
-- Caifanes (artista 14)
(23, 14, 23),
(24, 14, 24),
(25, 14, 25),
(26, 14, 26),
-- Café Tacvba (artista 15)
(27, 15, 27),
(28, 15, 28),
(29, 15, 29),
(30, 15, 30);

-- =========================================================
-- 5. TGENERO (soporte para TCANCION)
-- =========================================================
INSERT INTO caja_musical.tgenero (id_genero, nombre_genero) VALUES
(1, 'Pop'),
(2, 'Rock'),
(3, 'Reggaetón'),
(4, 'Balada'),
(5, 'Electrónica');

-- =========================================================
-- 6. TALBUM (soporte para TCANCION: 1 álbum por artista)
-- =========================================================
INSERT INTO caja_musical.talbum (id_album, titulo, anio_lanzamiento, id_artista) VALUES
(1,  'Horizonte',          2019, 1),
(2,  'Cristal',            2020, 2),
(3,  'Caminos',            2018, 3),
(4,  'Reflejos',           2021, 4),
(5,  'Nocturno',           2017, 5),
(6,  'Latidos',            2022, 6),
(7,  'Origen',             2016, 7),
(8,  'Distancias',         2020, 8),
(9,  'Al Vuelo',           2019, 9),
(10, 'Marea',              2023, 10),
(11, 'Fronteras',          2018, 11),
(12, 'Cordillera',         2021, 12),
(13, 'Voltaje',            2022, 13),
(14, 'Concreto',           2019, 14),
(15, 'Ritual',             2020, 15);

-- =========================================================
-- 7. TCANCION (15 canciones, una por álbum)
-- =========================================================
INSERT INTO caja_musical.tcancion (id_cancion, nombre_cancion, duracion, fecha_lanzamiento, id_album, id_genero) VALUES
(1,  'Amanecer',        '00:03:20', '2019-03-15', 1,  1),
(2,  'Espejismo',       '00:03:45', '2020-06-01', 2,  2),
(3,  'Sendero',         '00:04:10', '2018-09-22', 3,  3),
(4,  'Ecos de Ti',      '00:03:30', '2021-02-14', 4,  4),
(5,  'Medianoche',      '00:04:00', '2017-11-05', 5,  5),
(6,  'Pulso',           '00:03:15', '2022-07-19', 6,  1),
(7,  'Raíz',            '00:03:50', '2016-05-30', 7,  2),
(8,  'Kilómetros',      '00:04:20', '2020-01-10', 8,  3),
(9,  'Instante',        '00:03:05', '2019-08-08', 9,  4),
(10, 'Marejada',        '00:03:40', '2023-04-25', 10, 5),
(11, 'Sin Fronteras',   '00:03:55', '2018-12-01', 11, 1),
(12, 'Altura',          '00:04:05', '2021-10-17', 12, 2),
(13, 'Corriente',       '00:03:25', '2022-03-03', 13, 3),
(14, 'Hormigón',        '00:03:35', '2019-06-12', 14, 4),
(15, 'Ceremonia',       '00:04:15', '2020-09-09', 15, 5);

-- =========================================================
-- 8. Ajuste de secuencias
-- =========================================================
SELECT setval(pg_get_serial_sequence('caja_musical.ttipo', 'id_tipo'), (SELECT MAX(id_tipo) FROM caja_musical.ttipo));
SELECT setval(pg_get_serial_sequence('caja_musical.tartista', 'id_artista'), (SELECT MAX(id_artista) FROM caja_musical.tartista));
SELECT setval(pg_get_serial_sequence('caja_musical.tcantante', 'id_cantante'), (SELECT MAX(id_cantante) FROM caja_musical.tcantante));
SELECT setval(pg_get_serial_sequence('caja_musical.tintegrante', 'id_integrante'), (SELECT MAX(id_integrante) FROM caja_musical.tintegrante));
SELECT setval(pg_get_serial_sequence('caja_musical.tgenero', 'id_genero'), (SELECT MAX(id_genero) FROM caja_musical.tgenero));
SELECT setval(pg_get_serial_sequence('caja_musical.talbum', 'id_album'), (SELECT MAX(id_album) FROM caja_musical.talbum));
SELECT setval(pg_get_serial_sequence('caja_musical.tcancion', 'id_cancion'), (SELECT MAX(id_cancion) FROM caja_musical.tcancion));

-- =========================================================
-- Fin del script
-- =========================================================
