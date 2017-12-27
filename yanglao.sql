/*
Navicat MySQL Data Transfer

Source Server         : 213
Source Server Version : 50638
Source Host           : 192.168.10.213:3306
Source Database       : yanglao

Target Server Type    : MYSQL
Target Server Version : 50638
File Encoding         : 65001

Date: 2017-12-27 08:10:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for image
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `info` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT '0',
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_image_1_idx` (`info`),
  CONSTRAINT `fk_image_1` FOREIGN KEY (`info`) REFERENCES `info` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=65058 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for info
-- ----------------------------
DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL COMMENT '养老院名称',
  `tel` varchar(50) DEFAULT NULL COMMENT '联系电话',
  `province` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `county` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL COMMENT '机构类型',
  `nature` varchar(50) DEFAULT NULL COMMENT '机构性质',
  `corporation` varchar(50) DEFAULT NULL COMMENT '公司负责人/法人',
  `founding_time` varchar(50) DEFAULT NULL COMMENT '成立时间',
  `area` varchar(50) DEFAULT NULL COMMENT '占地面积',
  `bed_number` varchar(50) DEFAULT NULL COMMENT '床位数',
  `collect_object` varchar(50) DEFAULT NULL COMMENT '收住对象',
  `toll_range` varchar(50) DEFAULT NULL COMMENT '收费区间',
  `special_service` varchar(2000) DEFAULT NULL COMMENT '特色服务',
  `contacts` varchar(50) DEFAULT NULL COMMENT '联系人',
  `address` varchar(200) DEFAULT NULL COMMENT '地址',
  `website` varchar(200) DEFAULT NULL COMMENT '网址',
  `traffic` varchar(2000) DEFAULT NULL COMMENT '交通',
  `introduction` text COMMENT '机构介绍',
  `charge_standard` text COMMENT '收费标准',
  `facilities` text COMMENT '设施',
  `service` text COMMENT '服务内容',
  `notice` text COMMENT '入住须知',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29276 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for url
-- ----------------------------
DROP TABLE IF EXISTS `url`;
CREATE TABLE `url` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50494 DEFAULT CHARSET=utf8;
