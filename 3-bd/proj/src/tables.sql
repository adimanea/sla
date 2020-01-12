create table bibliotecar (
	   id_bib bigserial not null primary key,
	   -- bigserial = increments itself
	   -- primary key = uniquely identifies the person
	   nume varchar(20) not null,
	   prenume varchar(20) not null,
	   id_spec varchar(20) not null
)

create table edu (
	   id_edu bigserial not null primary key,
	   nume varchar(20) not null,
	   prenume varchar(20) not null,
	   email varchar(20),
	   newsletter boolean,
	   ab_activ boolean not null,
	   foreign key (id_carte_edu) references carte(id_carte),
	   foreign key (id_rev_edu) references revista(id_rev),
	   foreign key (id_spec_edu) references specializare(id_spec)
)

create table nedu (
	   id_cit bigserial not null primary key,
	   nume varchar(20) not null,
	   prenume varchar(20) not null,
	   email varchar(20),
	   newsletter boolean,
	   ab_activ boolean not null,
  	   foreign key (id_carte_nedu) references carte(id_carte),
   	   foreign key (id_spec_nedu) references specializare(id_spec)
)

create table restul (
	   id_pub bigserial not null primary key,
	   email varchar(20),
	   pw varchar(20),
	   wishlist text[],		-- array of strings
	   newsletter boolean
)

create table carte (
	   id_carte bigserial not null primary key,
	   autor_n varchar(20) not null,
	   autor_p varchar(20) not null,
	   titlu varchar(30) not null,
	   an smallserial,	-- from 1 to 32767
	   stoc smallint,	-- from -32768 to 32767
   	   foreign key (id_spec_carte) references specializare(id_spec)
)

create table revista (
	   id_rev bigserial not null primary key,
	   autor_n varchar(20) not null,
	   autor_p varchar(20) not null,
	   titlu varchar(30) not null,
	   numar smallserial,
	   stoc smallint,
   	   foreign key (id_spec_rev) references specializare(id_spec)
)

create table specializare (
	   id_spec bigserial not null primary key,
	   descriere text
)

create table feedback (
	   id_fb bigserial not null primary key,
	   rating smallserial,
	   continut text,
	   datafb date,
	   foreign key (id_bib_fb) references bibliotecar(id_bib),
	   foreign key (id_cit_fb) references nedu(id_cit),
	   foreign key (id_edu_fb) references edu(id_edu),
	   foreign key (id_spec_fb) references specializare(id_spec),
)

create table bib_spec (
	   foreign key (id_bib_bs) references bibliotecar(id_bib) on delete restrict,
	   -- don't delete referenced table until all references are deleted
	   foreign key (id_spec_bs) references specializare(id_spec) on delete restrict,
)

create table bib_cit (
	   foreign key (id_bib_bc) references bibliotecar(id_bib),
	   foreign key (id_cit_bc) references nedu(id_cit)
)

create table pub_carte (
	   foreign key (id_pub_pc) references restul(id_pub),
	   foreign key (id_carte_pc) references carte(id_carte)
)
	   
	   
