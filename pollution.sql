-- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pollution-db` ;

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` DEFAULT CHARACTER SET utf8 ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `pollution-db`.`location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`location` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`location` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `geo_point` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`reading`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`reading` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`reading` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location_id` INT NULL,
  `date_time` VARCHAR(45) NULL,
  `nox` FLOAT NULL,
  `no` FLOAT NULL,
  `pm10` FLOAT NULL,
  `nvpm10` FLOAT NULL,
  `vpm10` FLOAT NULL,
  `nvpm2.5` FLOAT NULL,
  `pm2.5` FLOAT NULL,
  `vpm2.5` FLOAT NULL,
  `co` FLOAT NULL,
  `o3` FLOAT NULL,
  `so2` FLOAT NULL,
  `temperature` FLOAT NULL,
  `rh` FLOAT NULL,
  `air_pressure` FLOAT NULL,
  `date_start` DATETIME NULL,
  `date_end` DATETIME NULL,
  `current` VARCHAR(45) NULL,
  `instrument_type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `location_foreign_key_idx` (`location_id` ASC) VISIBLE,
  CONSTRAINT `location_foreign_key`
    FOREIGN KEY (`location_id`)
    REFERENCES `pollution-db`.`location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`schema`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`schema` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`schema` (
  `id` INT NULL AUTO_INCREMENT,
  `measure` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `unit` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
