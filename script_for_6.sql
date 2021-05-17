CREATE DATABASE IF NOT EXISTS `db_campaign`;

CREATE USER IF NOT EXISTS 'admin_campaign' IDENTIFIED BY '4dm1n_c4mp41gn';

GRANT ALL ON db_campaign.* TO 'admin_campaign';

show databases;

select user, host from mysql.user;

show grants for admin_campaign;