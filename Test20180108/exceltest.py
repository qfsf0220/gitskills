#-*- coding:utf-8 -*-
import xlsxwriter
d1={'职位': 'Linux高级运维工程师', '地区': '上海-静安区', '薪酬': '6-8千/月', '公司名字': '上海天好电子商务股份有限公司', '公司性质': '上市公司', '公司规模': '150-500人', '公司地址': '上班地址： 天好花苑', '工作经验': '3-4年经验', '招聘人数': '招若干人', '发布时间': '01-12发布', '岗位职责': '1，驻场工程师，为客户提供技术支持和维护 2，客户关系的维护及拓展 3，提供Linux相关服务器产品的售前支持 4，机房Linux服务器日常巡检 5，客户现场Linux服务器的运维 6，客户现场Linux相关问题的处理与协调 7，客户现场VMware 8，上级安排的其他工作 任职要求： 1，计算机相关专业大专以上学历，3年以上IT工作经验； 2，熟悉各大硬件厂商的主流产品 3，熟悉linux和windows操作系统的安装和维护 4，熟悉vmware等主流虚拟化产品符合以下条件者优先 5，谦虚好学，有上进心；工作踏实，有良好的客户服务意识； 6，抗压能力强、高度责任心、对工作有认同感，良好的服务意识，学习能力强，实操能力强。具有团队协作精神，良好的沟通交流能力。 7，取得RHCE证书的优先 职能类别： 系统工程师 分享 微信 邮件'}
d2={'职位': '运维工程师（国泰君安）', '地区': '上海', '薪酬': '4.5-6千/月', '公司名字': '深圳市鼎驰科技发展有限公司', '公司性质': '民营公司', '公司规模': '50-150人', '公司地址': '上班地址： 上海', '工作经验': '无工作经验', '招聘人数': '招2人', '发布时间': '01-12发布', '岗位职责': '岗位职责： 1、对所负责的各个系统进行日间检查和维护，如报盘系统、行情系统。 2、盘后操作检查，如数据报送、备份、应急处理。 3、检查系统初始化是否正常。 4、检查所负责的服务器运行状态是否正常。 5、夜间值班检查及巡检，每月1-2次。 任职要求： 1、计算机相关专业，全日制统招专科以上学历，具有较强的沟通和管理能力。 2、具有系统运维经验者优先 3、具有相关证券期货工作经验者优先 4、热情活泼开朗者优先，注重团队合作者优先 工作时间：8:30-17:00 工作地点：国泰证券-来安路（金海路、广兰路、世纪大道地铁站有班车） 职能类别： 软件工程师 分享 微信 邮件'}
d3={'职位': '运维工程师', '地区': '上海', '薪酬': '0.8-2万/月', '公司名字': '上海赢量金融服务有限公司', '公司性质': '民营公司', '公司规模': '50-150人', '公司地址': '上班地址： 上海市浦东新区东三里桥路1018号上海数字产业园A座107', '工作经验': '3-4年经验', '招聘人数': '招1人', '发布时间': '01-12发布', '岗位职责': '岗位职责： 1.负责公司应用系统部署架构规划和设计，保证系统的高可用性和扩展性； 2.负责公司应用系统性能分析与系统优化，不断提高系统运行效率； 3.负责系统优化和风险点梳理，主动发现生产环境的问题和隐患，提高系统的可用性； 4.推进自动化运维工具的使用，负责建设自动化监控、自动化发布部署体系，不断提高运维工作效率； 5.负责运维团队日常管理，能运用ITIL、ISO 20000和ISO 27001的思想不断优化运维规范、工作流程、风险控制，应急预案等； 6.充分利用公有云私有云资源，构建混合云架构，并实施应用的部署和日常公有云运维。 岗位要求 1.本科以上学历，计算机相关专业 2.3年以上系统工程师运维工作经验 3.精通F5,array等负载均衡技术 4.熟悉Java环境部署和维护 5.熟悉Apache/Nginx/IIS/Tomcat的配置及参数优化，有Redis/Memcached集群部署经验者优先 6.熟练使用任一脚本语言(PHP/Perl/Python/Shell)进行编程工作 7.熟悉前端接入技术及CDN技术 8.自动化构建部署系统、监控报警等自动化运维 9.对虚拟化技术kvm、xen能够熟练进行自动化部署、迁移和监控等；熟悉Mesos、Docker等容器技术者优先 10.有强烈的团队协作意识，对工作严谨负责，对新技术和未知领域乐于探索 11.有大型互联网公司海量集群环境运维经验者优先 12.熟悉mySQL，能进行数据库调优者优先 13.熟悉Java语言，并能进行开发者优先 *薪酬可谈，诚邀优秀人才加入。 职能类别： 其他 分享 微信 邮件'}
d4={'职位': '服务器运维工程师', '地区': '上海', '薪酬': '6-8千/月', '公司名字': '上海易雍健康信息咨询有限公司', '公司性质': '合资', '公司规模': '50-150人', '公司地址': '上班地址： 普陀区中江路879号25号楼', '工作经验': '3-4年经验', '招聘人数': '招1人', '发布时间': '01-12发布', '岗位职责': '工作职责: 1、负责系统故障的应急响应和问题处理；维护linux、windows服务器，监控服务器性能； 2、负责Linux操作系统的安装、配置，系统监控和维护，问题处理，以及软件升级，安全优化，保证其稳定、高效运行； 3、负责公司平台及应用系统维护工作； 4、负责Linux 平台下的系统维护，提高系统的可用率及可维护性； 5、负责Linux系统及应用程序进行性能分析，优化，问题跟踪； 6、负责Windows Server 2008/2012的运维技术支持； 7、负责Windows AD域搭建维护。。 任职资格: 1、三年以上系统配置、管理、维护经验。 2、精通Linux系统、精通MySQL、FTP、DNS、Squid等常用服务的安装、配置和维护； 3、熟悉linux负载均衡技术；能熟练利用各种工具进行系统状态监控（cacti、Nagios，bigsister等）； 4、熟悉Linux下不同数据库的安装和调试及简单优化； 5、熟悉AD域控； 6、有阿里云、腾讯云、百度云、亚马逊等云服务器运维经验优先； 7、熟悉VMware vSphere虚拟化操作平台； 8、需手机24小时开机，有问题能随时处理。 职能类别： 技术支持/维护工程师 网络维修 分享 微信 邮件'}
d5={'职位': '技术运维工程师(职位编号：003)', '地区': '上海-浦东新区', '薪酬': '0.6-1万/月', '公司名字': '上海澎博财经资讯有限公司', '公司性质': '民营公司', '公司规模': '150-500人', '公司地址': '上班地址： 浦东新区峨山路91弄101号陆家嘴软件园5号楼5楼', '工作经验': '1年经验', '招聘人数': '招5人', '发布时间': '01-12发布', '岗位职责': '职位描述： 1、为期货公司、证券公司等金融行业公司提供本公司产品的安装、调试及售后维护。 2、为期货公司、证券公司等金融行业公司提供技术支持支持及咨询服务。 岗位要求： 1、计算机及相关专业毕业，大学本科及以上学历； 2、精通计算机软硬件相关知识； 3、1年以上相关工作经验； 4、责任心强，较强的动手能力、语言及文字表达能力； 5、具备较好的人际交往能力、沟通能力、执行能力。 职能类别： 技术支持/维护工程师 售前/售后技术支持工程师 关键字： 技术支持 分享 微信 邮件'}
dlist=[d1,d2,d3,d4,d5]

workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()
a=0;b=0;c=0
for i in d1.keys():
    worksheet.write(a,b,i)
    b+=1

# worksheet.write('A1',"aaaaaaaaa")
for a,b in enumerate(dlist):
    for  c in   range(len(b.values())):
        worksheet.write(a+1, c,list(b.values())[c])
        c+=1

workbook.close()