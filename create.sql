create table AGENCY(
AGENCY  varchar2(10) not null primary key,
AGENCY_TYPE varchar2(15)
);
create table PRODUCT(
AGENCY_CODE varchar2(10) not null references AGENCY(AGENCY),
PRODUCT_NAME varchar2(40) not null ,
CONSTRAINT PK_PRODUCT PRIMARY KEY (AGENCY_CODE,PRODUCT_NAME)
);


create table DESTINATION(
DESTINATION varchar2(50) not null primary key
);



create table PRODUCT_DETAILS(
    AGENCY_CODE VARCHAR(10) NOT NULL,
    PRODUCT_CODE varchar2(40) NOT NULL,
    DISTRIBUTION_CHANNEL varchar2(15) not null ,
    CLAIM VARCHAR2(5) NOT  NULL CHECK( CLAIM IN ('No','Yes')),
    DURATION NUMBER(*) DEFAULT NULL,
    DESTINATION varchar2(50) DEFAULT null REFERENCES DESTINATION(DESTINATION),
    NET_SALES NUMBER(*,2) NOT NULL,
    COMMISION NUMBER(*,2) NOT NULL,
    GENDER VARCHAR2(1) DEFAULT NULL CHECK ( GENDER IN ('F','M',NULL)),
    AGE number(*) NOT NULL,
    CONSTRAINT fk_PRODUCT_DETAILS Foreign Key (AGENCY_CODE,PRODUCT_CODE) References PRODUCT(AGENCY_CODE, PRODUCT_NAME)
 );
