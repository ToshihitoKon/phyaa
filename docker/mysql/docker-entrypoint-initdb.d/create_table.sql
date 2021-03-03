create database phyaa_dev;
use phyaa_dev;

create table files (
  id mediumint not null auto_increment,
  filepath varchar(192),
  primary key (id)
);
