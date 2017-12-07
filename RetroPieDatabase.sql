DROP DATABASE RetroPie;

CREATE DATABASE RetroPie;

USE RetroPie;


CREATE TABLE CurrentGame(
  game_name         VARCHAR(100) NOT NULL,
  system_name       VARCHAR(70) NOT NULL,
  game_start_time   VARCHAR(20) NOT NULL,
  PRIMARY KEY (game_name)
);


CREATE TABLE GamesPlayed(
  game_name         VARCHAR(100) NOT NULL,
  system_name       VARCHAR(70) NOT NULL,
  PRIMARY KEY (game_name)
);











CREATE TABLE Hospitals (
    ProviderID              INT NOT NULL,
    ProviderName            VARCHAR(100) NOT NULL,
    ProviderStreetAddress   VARCHAR(50) NOT NULL,
    ProviderCity            VARCHAR(40) NOT NULL,
    ProviderState           VARCHAR(2) NOT NULL,
    ProviderZip             INT NOT NULL,
    ReferralRegionState     VARCHAR(2) NOT NULL,
    ReferralRegionCity      VARCHAR(35) NOT NULL,
    PRIMARY KEY (ProviderID)
);
