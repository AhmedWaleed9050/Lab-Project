use lab;

create table diagnosis
(
gross varchar(MAX) not null,
microscope varchar(MAX) not null,
conclusion varchar(MAX) not null,
nature varchar(MAX) not null,
code varchar(5) not null

constraint code_pk primary key(code)
);

create table patients
(
name nvarchar(50) not null,
age int not null,
sex varchar(7) not null,
rc_date date not null,
rp_date date not null,
lr_ref int identity not null,
pre_ref int not null,
s_name nvarchar(30) not null,
shareeha int not null,
code varchar(5) not null

constraint lr_ref_pk primary key (lr_ref),
constraint code_fk foreign key (code) references diagnosis(code)
);