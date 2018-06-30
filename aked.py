# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys, codecs
from gtts import gTTS
from googletrans import Translator

#===================SELF========================
try:
    client = LineClient(authToken='auth_')
except:
    client = LineClient()
channel = LineChannel(client)
poll = LinePoll(client)
#===================ASSIST========================
try:
    assist = LineClient(authToken='auth_')
except:
    assist = LineClient()
assistchannel = LineChannel(assist)
assistpoll = LinePoll(assist)
#==================BOT LOGIN SUCCESS===============
try:
    assist1 = LineClient(authToken='auth_')
except:
    assist1 = LineClient()
assistchannel = LineChannel(assist1)
assistpoll = LinePoll(assist1)
#==================BOT LOGIN SUCCESS===============

#=================   BOT SETUP  ==================
clientMid = client.getProfile().mid
assistMid = assist.getProfile().mid
assist1Mid = assist1.getProfile().mid
akedBOT = [clientMid,assistMid,assist1Mid]
Bot = [client,assist,assist1]

vol = """
[-Menu Help-[Asisst]

-Respon
-Speed
-Tagall
-Masuk
-Keluar
-Sider On
-Sider Off

[-Aktif Protect Grup-]
- Pkick:[on/off] <- Protectkick
- ! @tag <- Kick with tag

[-Info Assist-[Login]
.. Status : On
.. Type : Kick Protect
.. Cooming : FiturNew!

.CreatorID
https://bit.ly/2J3ywc3
"""

protect = {
    "kick":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
            if op.type == 19:
                if op.param1 in protect["kick"]:
                    if op.param2 in akedBOT:
                        pass
                    else:
                        try:
                            random.choice(Bot).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            client.kickoutFromGroup(op.param1, [op.param2])
                else:
                    pass
            if op.type == 19:
                if op.param3 in clientMid:
                    if op.param2 not in akedBOT:
                        random.choice(Bot).kickoutFromGroup(op.param1, [op.param2])
                        P = random.choice(Bot).getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(P)
                        invsend = 0
                        Ticket = random.choice(Bot).reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = random.choice(Bot).getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(A)
                if op.param3 in assistMid:
                    if op.param2 not in akedBOT:
                        random.choice(Bot).kickoutFromGroup(op.param1, [op.param2])
                        P = random.choice(Bot).getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(P)
                        invsend = 0
                        Ticket = random.choice(Bot).reissueGroupTicket(op.param1)
                        assist.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = random.choice(Bot).getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(A)
                if op.param3 in assist1Mid:
                    if op.param2 not in akedBOT:
                        random.choice(Bot).kickoutFromGroup(op.param1, [op.param2])
                        P = random.choice(Bot).getGroup(op.param1)
                        P.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(P)
                        invsend = 0
                        Ticket = random.choice(Bot).reissueGroupTicket(op.param1)
                        assist1.acceptGroupInvitationByTicket(op.param1, Ticket)
                        A = random.choice(Bot).getGroup(op.param1)
                        A.preventedJoinByTicket = False
                        random.choice(Bot).updateGroup(A)
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                msg.from_ = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType in [0,2]:
                            contact = assist.getContact(sender)
                            if text.lower() == 'help':
                                assist.sendText(receiver, vol)
                            elif text.lower() == 'respon':
                                assist.sendText(receiver, "Hadir... ")
                                assist1.sendText(receiver, "Hadir... ")
                            elif text.lower() == 'speed':
                                start = time.time()
                                assist.sendText(receiver, "Loading... ")
                                elapsed_time = time.time() - start
                                assist.sendText(receiver, "[Hasil Speed] \n%s" % (elapsed_time))
                            elif text.lower() == 'tagall':
                                group = assist.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    assist.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    assist.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    assist.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    assist.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    assist.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    assist.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    assist.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    assist.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    assist.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    assist.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    assist.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    assist.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    assist.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    assist.mention(receiver, nm5)             
                            elif text.lower() == 'masuk':
                                try:
                                    G = client.getGroup(receiver)
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    invsend = 0
                                    Ticket = client.reissueGroupTicket(receiver)
                                    assist.acceptGroupInvitationByTicket(receiver, Ticket)
                                    assist1.acceptGroupInvitationByTicket(receiver, Ticket)
                                    X = client.getGroup(receiver)
                                    X.preventedJoinByTicket = True
                                    client.updateGroup(X)
                                except Exception as axsd:
                                    print(axsd)
                            elif text.lower() == 'keluar':
                                assist.leaveGroup(receiver)
                                assist1.leaveGroup(receiver)
                            elif text.lower() == 'sider on':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                    client.sendText(receiver, "Cek sider on!")
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'sider off':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    assist.sendText(receiver, "Check reader off!")
                                else:
                                    assist.sendText(receiver, "Type sider on to get data siders")
                            elif text.lower() == ';':
                                restart_program()
                            elif text.lower().startswith("!"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in akedBOT:
                                        random.choice(Bot).kickoutFromGroup(receiver, [target])
                            elif text.lower().startswith("pkick"):
                                pset = text.split(":")
                                pk = text.replace(pset[0] + ":","")
                                if pk == "on":
                                    if receiver in protect["kick"]:
                                        assist.sendText(receiver, "Protect kick already On!")
                                    else:
                                        protect["kick"][receiver] = True
                                        assist.sendText(receiver, "Protect kick set On!")
                                if pk == "off":
                                    if receiver in protect["kick"]:
                                        del protect["kick"][receiver]
                                        assist.sendText(receiver, "Protect kick set Off!")
                                    else:
                                        assist.sendText(receiver, "Protect kick already Off!")
                except Exception as e:
                    assist.log("[SEND_MESSAGE] ERROR : " + str(e))
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = assist.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                assist.sendText(op.param1, 'Terbaca oleh: '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
