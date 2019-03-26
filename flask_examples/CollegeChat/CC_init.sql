BEGIN TRANSACTION;
DROP TABLE IF EXISTS `UserType`;
CREATE TABLE IF NOT EXISTS `UserType` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Description`	TEXT NOT NULL UNIQUE
);
INSERT INTO `UserType` (ID,Description) VALUES (1,'Admin'),
 (2,'StandardUser'),
 (3,'ArchivedUser');
DROP TABLE IF EXISTS `User`;
CREATE TABLE IF NOT EXISTS `User` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Username`	TEXT NOT NULL UNIQUE,
	`Email`	TEXT NOT NULL UNIQUE,
	`Password`	TEXT NOT NULL,
	`UserTypeID`	INTEGER NOT NULL DEFAULT 2,
	`JoinTS`	TEXT NOT NULL,
	`LastLoginTS`	TEXT,
	FOREIGN KEY(`UserTypeID`) REFERENCES `UserType`(`ID`)
);
INSERT INTO `User` (ID,Username,Email,Password,UserTypeID,JoinTS,LastLoginTS) VALUES (1,'bob','bob@cc.net','123456',1,'2019-03-26T09:34:12.876731','2019-03-26T09:34:12.876731'),
 (2,'jane','jane@hotmail.vom','ilovecats',2,'2019-03-26T09:36:09.517930','2019-03-26T09:36:09.517930');
DROP TABLE IF EXISTS `Message`;
CREATE TABLE IF NOT EXISTS `Message` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Contents`	TEXT NOT NULL,
	`SenderID`	INTEGER NOT NULL,
	`ChatroomID`	INTEGER NOT NULL,
	`TS`	TEXT NOT NULL,
	`SenderIP`	TEXT NOT NULL,
	`SenderUA`	TEXT NOT NULL
);
INSERT INTO `Message` (ID,Contents,SenderID,ChatroomID,TS,SenderIP,SenderUA) VALUES (1,'Hello World!',1,1,'2019-03-26T09:34:12.876731','127.0.0.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36');
DROP TABLE IF EXISTS `ChatRoomMembership`;
CREATE TABLE IF NOT EXISTS `ChatRoomMembership` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`UserID`	INTEGER NOT NULL,
	`ChatroomID`	INTEGER NOT NULL,
	`Owner`	INTEGER NOT NULL,
	`Confirmed`	INTEGER NOT NULL
);
INSERT INTO `ChatRoomMembership` (ID,UserID,ChatroomID,Owner,Confirmed) VALUES (1,1,1,1,1),
 (2,2,1,0,1);
DROP TABLE IF EXISTS `ChatRoom`;
CREATE TABLE IF NOT EXISTS `ChatRoom` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT NOT NULL UNIQUE,
	`isPrivate`	INTEGER NOT NULL,
	`DateCreated`	INTEGER NOT NULL,
	`Disabled`	INTEGER NOT NULL,
	PRIMARY KEY(`ID`)
);
INSERT INTO `ChatRoom` (ID,Name,isPrivate,DateCreated,Disabled) VALUES (1,'In The Beginning',0,'2019-03-26T09:34:12.876731',0);
DROP TABLE IF EXISTS `AttachmentType`;
CREATE TABLE IF NOT EXISTS `AttachmentType` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Description`	INTEGER
);
INSERT INTO `AttachmentType` (ID,Description) VALUES (1,'Image'),
 (2,'Video'),
 (3,'Audio'),
 (4,'Document');
DROP TABLE IF EXISTS `Attachment`;
CREATE TABLE IF NOT EXISTS `Attachment` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`MessageID`	INTEGER NOT NULL,
	`AttachmentTypeID`	INTEGER NOT NULL,
	`OriginalFilepath`	INTEGER NOT NULL,
	`ThumpnailFilepath`	INTEGER NOT NULL
);
COMMIT;
