#coding=utf8
import itchat
#import math
import PIL.Image as Image
import os
#from pandas import Series,DataFrame

itchat.auto_login(hotReload=True)   #设置为自动 登录

friends = itchat.get_friends(update=True)[0:]
maps=itchat.get_mps(update=True)[0:]
chatrooms=itchat.get_chatrooms(update=True)[0:]

# ff=DataFrame(friends)              #好友列表
# fmaps=DataFrame(maps)              #公众号列表
# fchatrooms=DataFrame(chatrooms)      #群聊列表


#print fchatrooms
#print fchatrooms.columns

#将数据写入文件保存，编码格式设置为utf-8
# fchatrooms.to_csv('itchat_chatrooms.csv',encoding='utf-8') 
#fmaps.to_csv('itchat_maps.csv',encoding='utf-8')
# ff.to_csv('itchat_data.csv',encoding='utf-8')


#**********获取好友头像**********#

os.mkdir('headImg') #创建目录，保存微信好友头像
num = 0
for i in friends:
     img = itchat.get_head_img(userName=i["UserName"])	
     with open('./headImg/'+str(num) + ".jpg",'wb') as f:
	 f.write(img)
	 f.close()
	 num += 1

#**********获取所有聊天群头像**********#
for k1 in range(len(chatrooms)):
   num1 = 0
   memberList = itchat.update_chatroom(chatrooms[k1]['UserName'], detailedMember=True)
   # path='Image'+str(k1)
   path=str(chatrooms[k1][u'NickName'].encode('gbk'))
   os.mkdir(path)       #创建目录，保存群好友头像
   for k2 in range(memberList[u'MemberCount']):
     img1 = itchat.get_head_img(
	                             userName=memberList[u'MemberList'][k2]['UserName'],
								 chatroomUserName=memberList['UserName']
							    )	
     with open(path+'/'+str(num1) + ".jpg",'wb') as f2:
	 f2.write(img1)
	 f2.close()
	 num1 += 1

   
print 'ALL is Done'





















