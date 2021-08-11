def hangman(a):
	print("Welcome To HangMan")
	t = list("_"*len(a))
	hang=['''
    \O/
     |
    / \     
    XXX    ''',''' 
     O          
    /|\       
    / \       
    XXX     ''','''
    
              |
     O        |  
    /|\       |
    / \       |
    XXX      =========''','''
   +------------+
              |
     O        |  
    /|\       |
    / \       |
    XXX      =========''','''
    +-------------+
     |         |
     O         |  
    /|\        |
    / \        |
    XXX      =========''','''
    +-------------+
     |         |
    (O)        |  
    /|\        |
    / \        |
    XXX       =========''','''
    +-------------+
      |         |
    \(O)/       |  
      |         |
     / \        |
                =========''','''
    +-------------+
     |          |
    (O)         |  
    |||         |
    / \         |
                ========'''                                                                        
    ]
	b = 0
	k = 0
	while True:
		x = input(f"Please Enter Your {b+1} Word: ")
		if x in a:
			for i in range(len(a)):
				if a[i] == x:
					t[i] = x
					k += 1
			print("".join(t))
		else:
			print(hang[b])
			b += 1
			print("Chance Left: ",len(hang)-b)
			
		if k == len(a):
			print("You win")
			break
		if b == len(hang):
			print("You Loose")
			break
hangman("Vikavvsh")