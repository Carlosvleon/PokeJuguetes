-- BORRAR CONTENIDO DE LAS TABLAS
DELETE FROM `Tipo de productos`;
DELETE FROM `Productos`;


-- POBLADO DE TIPOS
INSERT INTO `Tipo de productos` VALUES (01, '--');																		
INSERT INTO `Tipo de productos` VALUES (02, 'Planta');																		
INSERT INTO `Tipo de productos` VALUES (03, 'Veneno');																		
INSERT INTO `Tipo de productos` VALUES (04, 'Fuego');																		
INSERT INTO `Tipo de productos` VALUES (05, 'Volador');																		
INSERT INTO `Tipo de productos` VALUES (06, 'Agua');																		
INSERT INTO `Tipo de productos` VALUES (07, 'Bicho');																		
INSERT INTO `Tipo de productos` VALUES (08, 'Normal');																		
INSERT INTO `Tipo de productos` VALUES (09, 'Electrico');																		
INSERT INTO `Tipo de productos` VALUES (10, 'Tierra');		

--POBLADO DE POKEMONS
INSERT INTO `Productos` VALUES (	1	, 'Bulbasaur', 'descripcion de producto',	9	,	10000	,	2	,	3	, 'fotos_pkm/Bulbasaur.webp')	;
INSERT INTO `Productos` VALUES (	2	, 'Ivysaur', 'descripcion de producto',	    9	,	10000	,	2	,	3	, 'fotos_pkm/Ivysaur.webp')	;
INSERT INTO `Productos` VALUES (	3	, 'Venusaur', 'descripcion de producto',	9	,	10000	,	2	,	3	, 'fotos_pkm/Venusaur.webp')	;
INSERT INTO `Productos` VALUES (	4	, 'Charmander', 'descripcion de producto',	9	,	10000	,	4	,	1	, 'fotos_pkm/Charmander.webp')	;
INSERT INTO `Productos` VALUES (	5	, 'Charmeleon', 'descripcion de producto',	9	,	10000	,	4	,	1	, 'fotos_pkm/Charmeleon.webp')	;
INSERT INTO `Productos` VALUES (	6	, 'Charizard', 'descripcion de producto',	9	,	10000	,	4	,	5	, 'fotos_pkm/Charizard.webp')	;
INSERT INTO `Productos` VALUES (	7	, 'Squirtle', 'descripcion de producto',	9	,	10000	,	6	,	1	, 'fotos_pkm/Squirtle.webp')	;
INSERT INTO `Productos` VALUES (	8	, 'Wartortle', 'descripcion de producto',	9	,	10000	,	6	,	1	, 'fotos_pkm/Wartortle.webp')	;
INSERT INTO `Productos` VALUES (	9	, 'Blastoise', 'descripcion de producto',	9	,	10000	,	6	,	1	, 'fotos_pkm/Blastoise.webp')	;
INSERT INTO `Productos` VALUES (	10	, 'Caterpie', 'descripcion de producto',	9	,	10000	,	7	,	1	, 'fotos_pkm/Caterpie.webp')	;
INSERT INTO `Productos` VALUES (	11	, 'Metapod', 'descripcion de producto',	    9	,	10000	,	7	,	1	, 'fotos_pkm/Metapod.webp')	;
INSERT INTO `Productos` VALUES (	12	, 'Butterfree', 'descripcion de producto',	9	,	10000	,	7	,	5	, 'fotos_pkm/Butterfree.webp')	;
INSERT INTO `Productos` VALUES (	13	, 'Weedle', 'descripcion de producto',	    9	,	10000	,	7	,	3	, 'fotos_pkm/Weedle.webp')	;
INSERT INTO `Productos` VALUES (	14	, 'Kakuna', 'descripcion de producto',	    9	,	10000	,	7	,	3	, 'fotos_pkm/Kakuna.webp')	;
INSERT INTO `Productos` VALUES (	15	, 'Beedrill', 'descripcion de producto',	9	,	10000	,	7	,	3	, 'fotos_pkm/Beedrill.webp')	;
INSERT INTO `Productos` VALUES (	16	, 'Pidgey', 'descripcion de producto',	    9	,	10000	,	8	,	5	, 'fotos_pkm/Pidgey.webp')	;
INSERT INTO `Productos` VALUES (	17	, 'Pidgeotto', 'descripcion de producto',	9	,	10000	,	8	,	5	, 'fotos_pkm/Pidgeotto.webp')	;
INSERT INTO `Productos` VALUES (	18	, 'Pidgeot', 'descripcion de producto',	    9	,	10000	,	8	,	5	, 'fotos_pkm/Pidgeot.webp')	;
INSERT INTO `Productos` VALUES (	19	, 'Rattata', 'descripcion de producto',	    9	,	10000	,	8	,	1	, 'fotos_pkm/Rattata.webp')	;
INSERT INTO `Productos` VALUES (	20	, 'Raticate', 'descripcion de producto',	9	,	10000	,	8	,	1	, 'fotos_pkm/Raticate.webp')	;
INSERT INTO `Productos` VALUES (	21	, 'Spearow', 'descripcion de producto',	    9	,	10000	,	8	,	5	, 'fotos_pkm/Spearow.webp')	;
INSERT INTO `Productos` VALUES (	22	, 'Fearow', 'descripcion de producto',	    9	,	10000	,	8	,	5	, 'fotos_pkm/Fearow.webp')	;
INSERT INTO `Productos` VALUES (	23	, 'Ekans', 'descripcion de producto',	    9	,	10000	,	3	,	1	, 'fotos_pkm/Ekans.webp')	;
INSERT INTO `Productos` VALUES (	24	, 'Arbok', 'descripcion de producto',	    9	,	10000	,	3	,	1	, 'fotos_pkm/Arbok.webp')	;
INSERT INTO `Productos` VALUES (	25	, 'Pikachu', 'descripcion de producto',	    9	,	10000	,	9	,	1	, 'fotos_pkm/Pikachu.webp')	;
INSERT INTO `Productos` VALUES (	26	, 'Raichu', 'descripcion de producto',	    9	,	10000	,	9	,	1	, 'fotos_pkm/Raichu.webp')	;
INSERT INTO `Productos` VALUES (	27	, 'Sandshrew', 'descripcion de producto',	9	,	10000	,	10	,	1	, 'fotos_pkm/Sandshrew.webp')	;
INSERT INTO `Productos` VALUES (	28	, 'Sandslash', 'descripcion de producto',	9	,	10000	,	10	,	1	, 'fotos_pkm/Sandslash.webp')	;
INSERT INTO `Productos` VALUES (	29	, 'NidoranF', 'descripcion de producto',	9	,	10000	,	3	,	1	, 'fotos_pkm/NidoranF.webp')	;
INSERT INTO `Productos` VALUES (	30	, 'Nidorina', 'descripcion de producto',	9	,	10000	,	3	,	1	, 'fotos_pkm/Nidorina.webp')	;
INSERT INTO `Productos` VALUES (	31	, 'Nidoqueen', 'descripcion de producto',	9	,	10000	,	3	,	10	, 'fotos_pkm/Nidoqueen.webp')	;
INSERT INTO `Productos` VALUES (	32	, 'NidoranM', 'descripcion de producto',	9	,	10000	,	3	,	1	, 'fotos_pkm/NidoranM.webp')	;
INSERT INTO `Productos` VALUES (	33	, 'Nidorino', 'descripcion de producto',	9	,	10000	,	3	,	1	, 'fotos_pkm/Nidorino.webp')	;
INSERT INTO `Productos` VALUES (	34	, 'Nidoking', 'descripcion de producto',	9	,	10000	,	3	,	10	, 'fotos_pkm/Nidoking.webp')	;