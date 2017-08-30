#coding=utf8
import itchat
from pandas import Series,DataFrame

itchat.auto_login(hotReload=True)   #设置为自动 登录

friends = itchat.get_friends(update=True)[0:]
maps=itchat.get_mps(update=True)[0:]
chatroms=itchat.get_chatrooms(update=True)[0:]

#print maps
#print type(friends)

ff=DataFrame(friends)              #好友列表
fmaps=DataFrame(maps)              #公众号列表
fchatroms=DataFrame(chatroms)      #群聊列表


obj1=ff.reindex([1])
print  obj1



#print fchatroms
#print fchatroms.columns

#将数据写入文件保存，编码格式设置为utf-8
fchatroms.to_csv('itchat_chatroms.csv',encoding='utf-8')
fmaps.to_csv('itchat_maps.csv',encoding='utf-8')
ff.to_csv('itchat_data.csv',encoding='utf-8')

#print friends[0:100]
#ac=['sss','sasasas']
#values = ','.join(str(v) for v in value_list)
#frid=''.join(str(v) for v in friends)  #list类型转换成str类型
#file_frd=open('frd.txt','w')
#f.writelines(frid)  
#file_frd.write(frid)
#file_frd.close()  

#a=['1','2','3','4','33']
#b=['dd','ddd','d']
#cf={a:b}
#