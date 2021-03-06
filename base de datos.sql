drop database universidad;
create database universidad;
use universidad;

-- -----------------------------
-- Creacion de Tablas
-- -----------------------------

Create table Estudiante (
  Est_Nommbre varchar(30) not null,
  Est_Apellido varchar(30) not null,
  Est_Matricula int not null auto_increment primary key,
  Est_Documento varchar(13) not null ,
  Est_TipoDocumento varchar(50) not null,
  Est_Direccion varchar(40),
  Est_Carrera int not null,
  Est_Estatus   varchar(1) not null
) ;


-- Tabla Docentes
Create table Docentes (
  Doc_Nommbre varchar(30) not null,
  Doc_Apellido varchar(30) not null,
  Doc_Matricula int not null auto_increment primary key, 
  Doc_Documento varchar(13) not null ,
  Doc_TipoDocumento varchar(50) not null,
  Doc_Direccion varchar(40),
  Doc_Secciones int not null, 
  Doc_Estatus   varchar(1) not null
) ;

-- Tabla Carrera
Create table Carrera (
  Car_Nombre_CD int not null auto_increment primary key,
  Car_Nombre_DESC varchar(40) not null
  
);

-- Tabla Materias
Create table Materias (
  Mat_Nombre_CD int not null auto_increment primary key, 
  Mat_Nombre_DESC varchar(40) not null,
  Mat_Nombre_seciones_CD varchar(10) not null
  
);


-- Tabla Estudiantes x Materia
Create table Est_Materia (
  Periodo varchar(50) not null, 
  Est_Matricula int not null,
  Materia_CD int not null
 
);

-- ---------------------------------------------------------
-- CREACION DE LAS LLAVES PRIMARIAS Y SECUNDARIAS 
-- ---------------------------------------------------------

-- tabla Estudiante 
alter table Estudiante add Foreign Key (Est_Carrera)  REFERENCES Carrera (Car_Nombre_CD);

-- tabla Docentes 
alter table Docentes add Foreign Key (Doc_Secciones)  REFERENCES Materias (Mat_Nombre_CD);

-- tabla Estudiantes x Materia 
alter table Est_Materia add Foreign Key (Est_Matricula)  REFERENCES Estudiante (Est_Matricula);

-- tabla Estudiantes x Materia 

alter table Est_Materia add Foreign Key (Materia_CD)  REFERENCES Materias (Mat_Nombre_CD) ;

-- ---------------------------------------------------------
-- insert valores
-- ---------------------------------------------------------

-- tabla Materias
insert into  Materias values (default, 'MATEMATICA BASICA','MAT_01');
insert into  Materias values ( default, 'CONTABILIDAD GENERAL','CONT_01');
insert into  Materias values ( default, 'QUIMICA GENERAL',	'QUI_01');
insert into  Materias values ( default, 'CALCULO 1','CAL_01');
insert into  Materias values ( default, 'CONTABILIDAD GENERAL','CONT_01');
insert into  Materias values ( default, 'INGLES BASICO','LEX_01');
insert into  Materias values ( default, 'ORIENTACION UNIVERSITARIA','EDU_01');
insert into  Materias values ( default, 'SOCIOLOGIA','SOC_01');
insert into  Materias values ( default, 'TECNICA DE ESTUDIO','EDU_02');
insert into  Materias values ( default, 'LITERATURA','EDU_03');
insert into  Materias values ( default, 'FISICA GENERAL','FIS_01');

-- tabla carreras

insert into  Carrera values (default, 'Ing sistemas');
insert into  Carrera values (default, 'Administacion de Empresa');
insert into  Carrera values (default, 'Contabilidad');
insert into  Carrera values (default, 'Medicina');
insert into  Carrera values (default, 'Odontologia');
insert into  Carrera values (default, 'ing Civil');
insert into  Carrera values (default, 'ing Quimica');
insert into  Carrera values (default, 'economia');
insert into  Carrera values (default, 'sociologia');
insert into  Carrera values (default, 'ing industrial');

-- tabla Estudiante

insert into  Estudiante values ('Jose Antonio', 'Ramirez', default, '0010866714', 'Cedula','25 de ??Febrero No. ??15', 1 ,'A');
insert into  Estudiante values ('Miguel??','Carrasco ',default,'02106587843','Cedula','Villa Faro, ??Calle 10, No. ??100',2 , 'A' );
insert into  Estudiante values ('Maria????Celeste','Fernandez',default,'VE156214','Pasaporte??','Ensanche Julieta No. ??66',3,'A');
insert into  Estudiante values ('Yulissa','Rosado',default,'0018521324','Cedula','Evaristo ??Morales, Calle 33 No. ??200',4,'A');
insert into  Estudiante values ('Marleny','Perez',default,'US325874??','Seguro Social??','Arroyo Hondo, Calle ??7ma. No. 25',5	,'A');
insert into  Estudiante values ('Carlos??','Lara	',default,'210841321','Cedula??','Los Mina, ??Calle 3D, ??No. 50',6,'A');
insert into  Estudiante values ('Andrea ','Gonzales',default,'10866716','Cedula','25 de ??Febrero No. ??20',7	,'A');
insert into  Estudiante values ('Felipe	','Alvarez',default,'02106515843','Cedula','Villa Faro, ??Calle 10, No. ??150	',8	,'A');
insert into  Estudiante values ('Gabriel','Luna	',default,'VE157214	','Pasaporte','Ensanche Julieta No. ??78	',9,'A');
insert into  Estudiante values ('Teresa	','Fuentes',default,'0018121324','Cedula','Evaristo ??Morales, ??Calle 40 No. ??200',10,'A');

-- tabla Docentes

insert into  Docentes values ('laura','bonilla',default,'0014166714??','Cedula??','25 de ??Febrero No. ??20', 1,'A');
insert into  Docentes values ('jose manuel','Carrasco',default,'02106457843??','Cedula??','Villa Faro, ??Calle 10, No. 110',2,'A');
insert into  Docentes values ('gabriel','villalona',default,'VE156210','Pasaporte??','Ensanche Julieta No. ??02',3,'A');
insert into  Docentes values ('hugo','parada',default,'0018521244','Cedula','Evaristo ??Morales, ??Calle 52 No. ??200',4,'A');
insert into  Docentes values ('beatriz','Perez ',default,'US325814','Seguro Social??','Arroyo Hondo, Calle ??7ma. No. 10',5,'A');
insert into  Docentes values ('cecilia','moncada',default,'210841302','Cedula','Los Mina, ??Calle 3D, ??No. 52',6	,'A');
insert into  Docentes values ('jorge felix','herrera',default,'10866703','Cedula??','25 de ??Febrero No. ??30',7,'A');
insert into  Docentes values ('heleodoro','comuna',default,'02106515453','Cedula','Villa Faro, ??Calle 10, No. ??158',8,'A');
insert into  Docentes values ('addys','montero',default,'VE157207','Pasaporte??','Ensanche Julieta No. ??80',9,'A');
insert into  Docentes values ('brenda','parra',default,'18121312','Cedula??','Evaristo ??Morales, ??Calle 40 No. ??250',10,'A');

-- tabla Est_Materia
insert into Est_Materia values ('MAY_AGO-2021',	1	,1 );
insert into Est_Materia values ('MAY_AGO-2021',	2	,1 );
insert into Est_Materia values ('MAY_AGO-2021',	3	,1 );
insert into Est_Materia values ('MAY_AGO-2021',	4	,1 );
insert into Est_Materia values ('MAY_AGO-2021',	5	,1 );
insert into Est_Materia values ('MAY_AGO-2021',	6	,2 );
insert into Est_Materia values ('MAY_AGO-2021',	2	,2 );
insert into Est_Materia values ('MAY_AGO-2021',	1	,2 );
insert into Est_Materia values ('MAY_AGO-2021',	4	,2 );
insert into Est_Materia values ('MAY_AGO-2021',	5	,2 );
insert into Est_Materia values ('MAY_AGO-2021',	7	,3 );
insert into Est_Materia values ('MAY_AGO-2021',	8	,3 );
insert into Est_Materia values ('MAY_AGO-2021',	9	,3 );
insert into Est_Materia values ('MAY_AGO-2021',	10	,3 );
insert into Est_Materia values ('MAY_AGO-2021',	1	,4 );
insert into Est_Materia values ('MAY_AGO-2021',	2	,4 );
insert into Est_Materia values ('MAY_AGO-2021',	3	,4 );
insert into Est_Materia values ('MAY_AGO-2021',	4	,4 );
insert into Est_Materia values ('MAY_AGO-2021',	8	,4 );
insert into Est_Materia values ('MAY_AGO-2021',	10	,5 );
insert into Est_Materia values ('MAY_AGO-2021',	9	,5 );
insert into Est_Materia values ('MAY_AGO-2021',	8	,5 );
insert into Est_Materia values ('MAY_AGO-2021',	7	,5 );
insert into Est_Materia values ('MAY_AGO-2021',	2	,6 );
insert into Est_Materia values ('MAY_AGO-2021',	4	,6 );
insert into Est_Materia values ('MAY_AGO-2021',	6	,6 );
insert into Est_Materia values ('MAY_AGO-2021',	3	,7 );
insert into Est_Materia values ('MAY_AGO-2021',	6	,7 );
insert into Est_Materia values ('MAY_AGO-2021',	9	,7 );
insert into Est_Materia values ('MAY_AGO-2021',	4	,8 );
insert into Est_Materia values ('MAY_AGO-2021',	8	,8 );
insert into Est_Materia values ('MAY_AGO-2021',	10	,8 );
insert into Est_Materia values ('MAY_AGO-2021',	1	,8 );
insert into Est_Materia values ('MAY_AGO-2021',	1	,9 );
insert into Est_Materia values ('MAY_AGO-2021',	5	,9 );
insert into Est_Materia values ('MAY_AGO-2021',	10	,9 );
insert into Est_Materia values ('MAY_AGO-2021',	1	,10 );
insert into Est_Materia values ('MAY_AGO-2021',	3	,10 );
insert into Est_Materia values ('MAY_AGO-2021',	6	,10 );
insert into Est_Materia values ('MAY_AGO-2021',	9	,10 );