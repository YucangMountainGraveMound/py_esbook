/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1_3306
Source Server Version : 50553
Source Host           : 127.0.0.1:3306
Source Database       : esbook

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-06-27 22:09:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `book_no` varchar(255) DEFAULT NULL,
  `chapter` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of books
-- ----------------------------
INSERT INTO `books` VALUES ('4', '1', '123213', '111', '1');
INSERT INTO `books` VALUES ('5', '1', '帝霸', '8_8109', '第3230章自作孽');

-- ----------------------------
-- Table structure for mail
-- ----------------------------
DROP TABLE IF EXISTS `mail`;
CREATE TABLE `mail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `smtpHost` varchar(255) DEFAULT NULL,
  `smtpPort` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `pwd` varchar(255) DEFAULT NULL,
  `kindlEmail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mail
-- ----------------------------
INSERT INTO `mail` VALUES ('4', '1', 'smtp.qq.com', '465', '768215684@qq.com', 'chaiyuan619', 'chaiyuan619@KINDLE.CN');
