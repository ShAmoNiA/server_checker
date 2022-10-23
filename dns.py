import dns.resolver
import platform   
import subprocess  
import threading


def thread_run(item):
    answer = my_resolver.query(item)
    for rdata in answer:
        if ping(str(rdata)):
            print("valid IP : "+item + " = " +str(rdata))
        else:
            print("not response from : "+str(rdata)+"("+item+")")

def ping(host):

    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '2', host]
    return subprocess.call(command,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT) == 0

my_resolver = dns.resolver.Resolver()

list_server = ["us.tgate24.com","ca.tgate24.com","uk.tgate24.com","mx.tgate24.com",
"de.tgate24.com","nl.tgate24.com","se.tgate24.com","fr.tgate24.com","ie.tgate24.com",
"it.tgate24.com","ch.tgate24.com","ro.tgate24.com","kr.tgate24.com","br.tgate24.com",
"jp.tgate24.com","be.tgate24.com","at.tgate24.com","ar.tgate24.com","es.tgate24.com",
"my.tgate24.com","ae.tgate24.com","ir.tgate24.com","fi.tgate24.com","tr.tgate24.com",
"dk.tgate24.com","no.tgate24.com","ua.tgate24.com","in.tgate24.com","au.tgate24.com",
"sg.tgate24.com","gold.tgate24.com"]


dns_list = ['8.8.8.8','9.9.9.9','208.67.222.222','1.1.1.1','185.228.168.9','76.76.19.19']


for dns_server in dns_list : 
    print("start for : " + dns_server )
    hold = []
    hold.append(dns_list[0])
    my_resolver.nameservers = hold


    list_threads = []
    for i in range(len(list_server)):
        list_threads.append(threading.Thread(target=thread_run, args=(list_server[i],)))


    for member in list_threads:
        member.start()

    for member in list_threads:
        member.join()
