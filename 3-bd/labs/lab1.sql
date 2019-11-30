--Laborator 1
--1
create or replace procedure criptare1(textclar in varchar2, textcriptat out varchar2)
as
    raw_sir raw(100);
    raw_cheie raw(100);
    rezultat raw(100);
    cheie varchar2(100) := '12345678';
    mod_operare number;
begin
    mod_operare := dbms_crypto.encrypt_des + dbms_crypto.pad_zero
                    + dbms_crypto.chain_ecb;

    raw_sir := utl_i18n.string_to_raw(textclar, 'AL32UTF8');
    raw_cheie := utl_i18n.string_to_raw(cheie, 'AL32UTF8');

    rezultat := dbms_crypto.encrypt(raw_sir, mod_operare, raw_cheie);

    dbms_output.put_line(rezultat);

    textcriptat := rawtohex(rezultat);
end;
/

variable rez_criptare varchar2(200)
execute criptare1('Text in clar', :rez_criptare);
print rez_criptare

set serveroutput on
declare
tmp varchar2(100);
begin
    criptare1('Text in clar', tmp);
    dbms_output.put_line(tmp);
end;
/

--2
create or replace procedure decriptare1 (textcriptat in varchar2,
                                        textdecriptat out varchar2)
as
    raw_sir raw(100);
    raw_cheie raw(100);
    rezultat raw(100);
    cheie varchar2(100) := '12345678';
    mod_operare number;
begin
    mod_operare := dbms_crypto.encrypt_des + dbms_crypto.pad_zero
                    + dbms_crypto.chain_ecb;
    raw_cheie := utl_i18n.string_to_raw(cheie, 'AL32UTF8');
    raw_sir := hextoraw(textcriptat);
    rezultat := dbms_crypto.decrypt(raw_sir, mod_operare, raw_cheie);
    dbms_output.put_line(rezultat);
    textdecriptat := utl_i18n.raw_to_char(rezultat, 'AL32UTF8');
end;
/

variable rez_decriptare varchar2(200)
execute decriptare1(:rez_criptare, :rez_decriptare);
print rez_decriptare
