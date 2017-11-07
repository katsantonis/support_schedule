global users
global days
global weekend
global vardies
global num_days
	    
days    = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
days2Nums= {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
weekend = ["Saturday","Sunday"]
vardies = ["1","2","3"]
users   = ["orespan","hadem","konnos","jstam","canagnostou","sdelis","mikem","nobody"]
num_days= 7

# slot     -> 1,2,3,4,5,6,7,8,9,10,11,13,14,15,16
# user     -> User object
# vardia   -> 1,2 3
# usr_name -> mikem,hadem.konnos,sdelis,canagnostou,jstam
# availabilities -> [[konnos,mikem],[],[],[],[]] one sublist for each slot containing the name sof the callc_team thac can work at tha slot
# prog           -> a list of 16 elements each one representing one vardia at a specific daya

# assuming weekends have only vardia 2
