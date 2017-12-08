global users
global days
global weekend
global vardies
global num_days
global calendar_urls   

days    = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
days2Nums= {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
weekend = ["Saturday","Sunday"]
vardies = ["1","2","3"]
users   = ["orespan","hadem","konnos","canagnostou","sdelis","mikem","nobody"]
num_days= 7
owncloud_url    = "https://colab.noc.grnet.gr/remote.php/dav/calendars/"
support_vardies = "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/%ce%92%ce%ac%cf%81%ce%b4%ce%b9%ce%b5%cf%82support_shared_by_6fb185e4-c0ca-1034-9776-a916203cc14b/"
calendar_urls   ={"hadem":"https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/%ce%b4%ce%b9%ce%b1%ce%b8%ce%b5%cf%83%ce%b9%ce%bc%cf%8c%cf%84%ce%b7%cf%84%ce%b1hadem_shared_by_bbeca648-8558-1035-9abf-27b2d9334824/",
        "orespan"     : "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/availability_shared_by_9805809a-3873-1037-9772-cd5a8aea2f1e/",
        "mikem"       : "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/availability_shared_by_2aebc624-35fc-1036-9f74-b9a6f4f57df3/",
        "sdelis"      : "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/sdelis_shared_by_bbe5484e-8558-1035-9abe-27b2d9334824/",
        "canagnostou" : "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/canagnostou_availability_shared_by_bc3d0414-054d-1037-8d69-a58664e431f8/",
        "konnos"      : "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/konnosav/"
        }

default_events = {
        "nobody":[(0,"nobody 1"),(1,"nobody 1"),(2,"nobody 1"),(3,"nobody 1"),(4,"nobody 1")] ,
        "hadem":[(0,"hadem 1"),(1,"hadem 1 2 3"),(2,"hadem 1"),(3,"hadem 1 2 3"),(4,"hadem 1 2 3"),(5,"hadem"),(6,"hadem")] ,
        "orespan":[],
        "sdelis":[],
        "konnos":[],
        "mikem":[],
        "canagnostou":[]
}


# slot     -> 1,2,3,4,5,6,7,8,9,10,11,13,14,15,16
# user     -> User object
# vardia   -> 1,2 3
# usr_name -> mikem,hadem.konnos,sdelis,canagnostou,jstam
# availabilities -> [[konnos,mikem],[],[],[],[]] one sublist for each slot containing the name sof the callc_team thac can work at tha slot
# prog           -> a list of 16 elements each one representing one vardia at a specific daya

# assuming weekends have only vardia 2
