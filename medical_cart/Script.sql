CREATE DATABASE medical;

CREATE TABLE medical.users (
id SERIAL PRIMARY KEY,
FirstName VARCHAR(100) NOT NULL,
MiddlName VARCHAR(100),
SacondName VARCHAR(100),
Birthday date,
ProfSpacial varchar(255),
Doctor BOOLEAN,
Admin BOOLEAN,
off BOOLEAN,
created_at datetime default now(),
updated_at datetime default now() on update now()
);


CREATE TABLE pacient (
id SERIAL PRIMARY KEY,
Doctor_id BIGINT unsigned NOT NULL,
FirstName VARCHAR(100) NOT NULL,
MiddlName VARCHAR(100),
SacondName VARCHAR(100),
Birthday date,
Sex BOOLEAN Not NULL,
Adres VARCHAR(255),
Phone VARCHAR(25),
Anamnes TEXT,
Diagnos TEXT,
PersDastaSoglasie BOOLEAN not NULL DEFAULT 1,
SoglasieMed BOOLEAN not NULL DEFAULT 1,
created_at datetime default now(),
updated_at datetime default now() on update now(),
FOREIGN KEY (Doctor_id) REFERENCES medical.users(id)
);


CREATE table access_keys (
id SERIAL PRIMARY KEY,
Doctor_id BIGINT unsigned NOT NULL,
created_at datetime default now(),
valid_until datetime default DATE_ADD(now(),INTERVAL 5 DAY),
FOREIGN KEY (Doctor_id) REFERENCES medical.users(id) );


DROP table access_keys ;

SELECT DATE_ADD(now(),INTERVAL 5 DAY);

insert into users (FirstName,password,Username) VALUES ('Иванов',MD5('user1'),'user1');

SELECT COUNT(*) FROM users WHERE Username = 'Администратор' AND password = MD5('Администратор') AND Admin = 1 AND off = 0;

INSERT INTO access_keys (Doctor_id,my_key) 
SELECT id,MD5(NOW()+id) FROM users WHERE Username = 'Администратор' AND password = MD5('Администратор') AND Admin = 1 AND off = 0;

SELECT MD5(NOW());
SELECT Doctor_id , my_key FROM access_keys ak join users u ON ak.Doctor_id = u.id WHERE u.Username = 'user1' ORDER by ak.id DESC limit 1;


SELECT now()+1;

SELECT IF (now()>valid_until , 0,1) FROM access_keys where my_key = '0aa89e56becdccf0e1f1f1b281feca95';

SELECT * FROM users;

SELECT md5('пароль');

INSERT INTO users ( Username,password,FirstName,MiddlName,SacondName,'Birthday','ProfSpacial','Doctor','Admin','off')
VALUES ('user2', '7e58d63b60197ceb55a1c487989a3720', 'Петр', 'Иванович', 'Петров', Null, 'Врач онколог', 1, 0, 0);

TRUNCATE access_keys ;


UPDATE users SET FirstName = 'Иванов', MiddlName = 'Сергеевич', SacondName = 'Сидоров',Birthday ='1979-11-22',ProfSpacial = '',Doctor = 1, Admin = 0, off = 0 WHERE id = 2;

SELECT date_format(Birthday,'%m-%d-%Y') FROM users u ;


SELECT id, Username, Doctor, Admin FROM users WHERE Username = 'user2' AND password = 'e242f36f4f95f12966da8fa2efd59992'  AND off = 0;


SELECT * from  users ;


ALTER TABLE users 
ADD CONSTRAINT username_long_check
CHECK (
   LENGTH(Username)>4 and LENGTH(Username)<=30
);


ALTER TABLE users 
ADD  CHECK ( Username>4 and Username<=30);


select id, LENGTH(Username) from users u ;

ALTER TABLE medical.users MODIFY COLUMN Birthday date Not NULL;




