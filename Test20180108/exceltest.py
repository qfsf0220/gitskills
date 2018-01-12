#-*- coding:utf-8 -*-
import xlsxwriter

d1= {'职位': '资深Linux运维', '地区': '上海-徐汇区', '薪酬': '1.5-2万/月', '公司名字': '上海大岂网络科技有限公司', '公司性质': '外资（非欧美）', '公司规模': '50-150人', '公司地址': '上班地址： 宛平南路75号', '工作经验': '5-7年经验', '招聘人数': '本科', '发布时间': '招1人', '岗位职责': '1、负责公司业务系统、服务器、网络、数据库、应用、环境的日常搭建、监控、维护及管理等 2、大规模集群的系统运维、服务监控分析、故障排查，以及紧急情况下的应急处理 3、研究服务架构，发现潜在问题，制定系统调整和优化方案，提高系统的健壮性和效率 4、负责日常日志分析备份、数据备份、故障排除、性能优化等工作，确保备份数据可用性，对提高系统可用性提出建议 5、按照设计要求编写运维工具相关程序代码，对其质量、性能负责 6、负责撰写部署文档，运维手册等相关技术文档，积极配合其他部门人员，提供技术支持 7、提升运维工作自动化以及智能化程度。 职位要求： 任职要求： 1、计算机相关专业毕业，5年以上IT实施部署或运维支持等方面的工作经验，熟悉阿里云，有大型互联网企业运维经验者优先考虑 2、熟悉Linux操作系统的维护及日常管理工作，能够对服务进行性能调优、定位故障并处理 3、熟悉Shell、Python等编程脚本,熟练使用sed、awk、sort、uniq、grep等命令 4、熟练Nginx、Apache Http、tomcat、jenkins、git server等常用软件的安装、配置及管理，有大、中型系统维护实战经验者优先 5、熟练mysql数据库的管理，配置，优化。了解redis，mongodb等nosql数据库 6、熟悉常用运维监控软件的安装、配置及管理 7、熟悉虚拟化（xen/kvm）、sdn、网络、存储更佳 8、优先考虑具备ELK、qconf、disconf、zabbix、zookeeper、scribe、cobar、kvm、docker等系统应用能力 9、具有快速分析问题、沟通和解决能力 10、具备良好的团队合作精神和服务意识，强烈的责任心与主动性，工作积极严谨，耐心负责，勇于承担压力 11、能承担较大工作强度，有较强的学习能力。 职能类别： 信息技术专员 分享 微信 邮件'}
d2={'职位': '运维工程师', '地区': '上海', '薪酬': '0.8-2万/月', '公司名字': '上海赢量金融服务有限公司', '公司性质': '民营公司', '公司规模': '50-150人', '公司地址': '上班地址： 上海市浦东新区东三里桥路1018号上海数字产业园A座107', '工作经验': '3-4年经验', '招聘人数': '本科', '发布时间': '招1人', '岗位职责': '岗位职责： 1.负责公司应用系统部署架构规划和设计，保证系统的高可用性和扩展性； 2.负责公司应用系统性能分析与系统优化，不断提高系统运行效率； 3.负责系统优化和风险点梳理，主动发现生产环境的问题和隐患，提高系统的可用性； 4.推进自动化运维工具的使用，负责建设自动化监控、自动化发布部署体系，不断提高运维工作效率； 5.负责运维团队日常管理，能运用ITIL、ISO 20000和ISO 27001的思想不断优化运维规范、工作流程、风险控制，应急预案等； 6.充分利用公有云私有云资源，构建混合云架构，并实施应用的部署和日常公有云运维。 岗位要求 1.本科以上学历，计算机相关专业 2.3年以上系统工程师运维工作经验 3.精通F5,array等负载均衡技术 4.熟悉Java环境部署和维护 5.熟悉Apache/Nginx/IIS/Tomcat的配置及参数优化，有Redis/Memcached集群部署经验者优先 6.熟练使用任一脚本语言(PHP/Perl/Python/Shell)进行编程工作 7.熟悉前端接入技术及CDN技术 8.自动化构建部署系统、监控报警等自动化运维 9.对虚拟化技术kvm、x[en能够熟练进行自动化部署、迁移和监控等；熟悉Mesos、Docker等容器技术者优先 10.有强烈的团队协作意识，对工作严谨负责，对新技术和未知领域乐于探索 11.有大型互联网公司海量集群环境运维经验者优先 12.熟悉mySQL，能进行数据库调优者优先 13.熟悉Java语言，并能进行开发者优先 *薪酬可谈，诚邀优秀人才加入。 职能类别： 其他 分享 微信 邮件'}

workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()
# worksheet.write('A1',"aaaaaaaaa")
a=0
b=1
for i in range(1):
        for x,y in d1.items():
            worksheet.write(i,a,str(x))
            worksheet.write(b,a,str(y))
            a+=1
workbook.close()